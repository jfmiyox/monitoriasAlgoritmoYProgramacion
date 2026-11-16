#!/usr/bin/env python3
"""Shared vector drawing utilities (Cairo + PIL) for monitoria_algoritmos_cpp diagrams."""

import math
import os
import cairo
from PIL import Image

# Unified color palette matching latex_common/estilo_monitoria.sty
WHITE = "#FFFFFF"
PAGE_BG = "#FFFFFF"
PANEL_BG = "#F8FAFC"
SUBTLE_BG = "#F1F5F9"
INK = "#0F172A"
INK_SEC = "#334155"
MUTED = "#64748B"
BORDER = "#CBD5E1"
BORDER_DARK = "#94A3B8"

NAVY = "#1E3A5F"
NAVY_SOFT = "#EEF2F7"
TEAL = "#0D9488"
TEAL_FILL = "#CCFBF1"
TEAL_SOFT = "#F0FDFA"
BLUE = "#2563EB"
BLUE_FILL = "#DBEAFE"
BLUE_SOFT = "#EFF6FF"
ORANGE = "#EA580C"
ORANGE_FILL = "#FFEDD5"
ORANGE_SOFT = "#FFF7ED"
RED = "#DC2626"
RED_FILL = "#FEE2E2"
RED_SOFT = "#FEF2F2"
GREEN = "#16A34A"
GREEN_FILL = "#DCFCE7"
GREEN_SOFT = "#F0FDF4"
PURPLE = "#7C3AED"
PURPLE_FILL = "#EDE9FE"
PURPLE_SOFT = "#F5F3FF"
AMBER = "#D97706"
AMBER_FILL = "#FEF3C7"
AMBER_SOFT = "#FFFBEB"


def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) / 255.0 for i in (0, 2, 4))


def set_color(ctx, h, alpha=1.0):
    r, g, b = hex_rgb(h)
    ctx.set_source_rgba(r, g, b, alpha)


def new_canvas(w, h, bg=PAGE_BG):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
    ctx = cairo.Context(surf)
    ctx.set_antialias(cairo.ANTIALIAS_BEST)
    set_color(ctx, bg)
    ctx.rectangle(0, 0, w, h)
    ctx.fill()
    return surf, ctx


def save_png(surf, path, dpi=300):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp.png"
    surf.write_to_png(tmp)
    im = Image.open(tmp).convert("RGBA")
    # Flatten on white for clean non-alpha PNG output
    bg = Image.new("RGB", im.size, (255, 255, 255))
    bg.paste(im, mask=im.split()[3])
    bg.save(path, format="PNG", dpi=(dpi, dpi), optimize=True)
    os.remove(tmp)


def set_font(ctx, family="Inter", size=20, bold=False, italic=False):
    slant = cairo.FONT_SLANT_ITALIC if italic else cairo.FONT_SLANT_NORMAL
    weight = cairo.FONT_WEIGHT_BOLD if bold else cairo.FONT_WEIGHT_NORMAL
    ctx.select_font_face(family, slant, weight)
    ctx.set_font_size(size)


def text_size(ctx, text, family="Inter", size=20, bold=False, italic=False):
    set_font(ctx, family, size, bold, italic)
    ext = ctx.text_extents(text)
    return ext.width, ext.height, ext


def draw_text(
    ctx,
    text,
    x,
    y,
    family="Inter",
    size=20,
    bold=False,
    italic=False,
    color=INK,
    align="left",
    valign="top",
):
    set_font(ctx, family, size, bold, italic)
    set_color(ctx, color)
    ext = ctx.text_extents(text)
    fe = ctx.font_extents()  # (ascent, descent, height, max_x_advance, max_y_advance)
    if align == "center":
        tx = x - ext.width / 2.0 - ext.x_bearing
    elif align == "right":
        tx = x - ext.width - ext.x_bearing
    else:
        tx = x
    if valign == "middle":
        ty = y + (fe[0] - fe[1]) / 2.0
    elif valign == "bottom":
        ty = y - fe[1]
    elif valign == "baseline":
        ty = y
    else:  # top
        ty = y + fe[0]
    ctx.move_to(tx, ty)
    ctx.show_text(text)
    return ext.width, fe[2]


def wrap_lines(ctx, text, max_w, family="Inter", size=20, bold=False, italic=False):
    set_font(ctx, family, size, bold, italic)
    paragraphs = text.split("\n")
    out = []
    for p in paragraphs:
        if p == "":
            out.append("")
            continue
        words = p.split(" ")
        cur = ""
        for w in words:
            cand = w if not cur else f"{cur} {w}"
            if ctx.text_extents(cand).width <= max_w:
                cur = cand
            else:
                if cur:
                    out.append(cur)
                cur = w
        if cur:
            out.append(cur)
    return out


def draw_wrapped(
    ctx,
    text,
    x,
    y,
    max_w,
    family="Inter",
    size=20,
    bold=False,
    italic=False,
    color=INK,
    line_mult=1.32,
    align="left",
    draw=True,
):
    lines = wrap_lines(ctx, text, max_w, family, size, bold, italic)
    set_font(ctx, family, size, bold, italic)
    line_h = size * line_mult
    total_h = len(lines) * line_h
    if draw:
        for i, line in enumerate(lines):
            ly = y + i * line_h
            cx = x if align == "left" else (x + max_w / 2.0 if align == "center" else x + max_w)
            draw_text(ctx, line, cx, ly, family, size, bold, italic, color, align=align, valign="top")
    return total_h, lines


def draw_multiline_centered(
    ctx,
    lines,
    cx,
    cy,
    family="Inter",
    size=20,
    bold=False,
    color=INK,
    line_mult=1.28,
):
    if isinstance(lines, str):
        lines = lines.split("\n")
    line_h = size * line_mult
    total_h = len(lines) * line_h
    start_y = cy - total_h / 2.0 + line_h / 2.0
    for i, line in enumerate(lines):
        draw_text(ctx, line, cx, start_y + i * line_h, family, size, bold, False, color, align="center", valign="middle")


def rounded_rect_path(ctx, x, y, w, h, r):
    r = min(r, w / 2.0, h / 2.0)
    ctx.new_sub_path()
    ctx.arc(x + w - r, y + r, r, -math.pi / 2, 0)
    ctx.arc(x + w - r, y + h - r, r, 0, math.pi / 2)
    ctx.arc(x + r, y + h - r, r, math.pi / 2, math.pi)
    ctx.arc(x + r, y + r, r, math.pi, 3 * math.pi / 2)
    ctx.close_path()


def rounded_rect(ctx, x, y, w, h, r=12, fill=None, stroke=None, stroke_w=2.5, shadow=False, dashed=False):
    if shadow:
        ctx.save()
        rounded_rect_path(ctx, x + 3, y + 5, w, h, r)
        set_color(ctx, "#0F172A", 0.08)
        ctx.fill()
        ctx.restore()
    if fill:
        rounded_rect_path(ctx, x, y, w, h, r)
        set_color(ctx, fill)
        ctx.fill()
    if stroke:
        ctx.save()
        rounded_rect_path(ctx, x, y, w, h, r)
        set_color(ctx, stroke)
        ctx.set_line_width(stroke_w)
        if dashed:
            ctx.set_dash([10, 7])
        ctx.stroke()
        ctx.restore()


def draw_header(ctx, W, title, subtitle, badge=None, accent=TEAL):
    # Top navy header banner with subtle rounded bottom corners or full crisp card
    bar_x, bar_y, bar_w, bar_h = 40, 32, W - 80, 118
    rounded_rect(ctx, bar_x, bar_y, bar_w, bar_h, r=16, fill=NAVY, shadow=True)
    # Left accent stripe
    ctx.save()
    rounded_rect_path(ctx, bar_x, bar_y, 14, bar_h, r=8)
    set_color(ctx, accent)
    ctx.fill()
    ctx.restore()
    # Title & subtitle
    draw_text(ctx, title, bar_x + 36, bar_y + 22, "Inter", 34, bold=True, color=WHITE)
    draw_text(ctx, subtitle, bar_x + 36, bar_y + 72, "Inter", 20, bold=False, color="#CBD5E1")
    if badge:
        bw = text_size(ctx, badge, "Inter", 18, bold=True)[0] + 34
        bx = bar_x + bar_w - bw - 26
        by = bar_y + (bar_h - 42) / 2.0
        rounded_rect(ctx, bx, by, bw, 42, r=21, fill=accent)
        draw_text(ctx, badge, bx + bw / 2.0, by + 21, "Inter", 18, bold=True, color=WHITE, align="center", valign="middle")
    return bar_y + bar_h


def draw_footer(ctx, W, H, text, badge=None):
    fy = H - 56
    set_color(ctx, BORDER)
    ctx.set_line_width(1.5)
    ctx.move_to(48, fy)
    ctx.line_to(W - 48, fy)
    ctx.stroke()
    draw_text(ctx, text, 52, fy + 16, "Inter", 17, bold=False, color=MUTED)
    if badge:
        draw_text(ctx, badge, W - 52, fy + 16, "Inter", 17, bold=True, color=NAVY, align="right")


# --- DFD Geometric Symbols (centered at cx, cy) ---

def _drop_shadow_path(ctx, path_fn, dx=3, dy=5):
    ctx.save()
    ctx.translate(dx, dy)
    path_fn()
    set_color(ctx, "#0F172A", 0.08)
    ctx.fill()
    ctx.restore()


def dfd_start_end(ctx, cx, cy, w, h, label, fill=TEAL_FILL, stroke=TEAL, text_color=NAVY, font_size=24, shadow=True):
    def p():
        rounded_rect_path(ctx, cx - w / 2, cy - h / 2, w, h, h / 2.0)

    if shadow:
        _drop_shadow_path(ctx, p)
    p()
    set_color(ctx, fill)
    ctx.fill()
    p()
    set_color(ctx, stroke)
    ctx.set_line_width(3.4)
    ctx.stroke()
    draw_multiline_centered(ctx, label, cx, cy, "Inter", font_size, bold=True, color=text_color)


def dfd_input(ctx, cx, cy, w, h, label, fill=BLUE_FILL, stroke=BLUE, text_color=INK, skew=22, font_size=22, mono=True, shadow=True):
    def p():
        x0, y0 = cx - w / 2, cy - h / 2
        ctx.new_path()
        ctx.move_to(x0 + skew, y0)
        ctx.line_to(x0 + w, y0)
        ctx.line_to(x0 + w - skew, y0 + h)
        ctx.line_to(x0, y0 + h)
        ctx.close_path()

    if shadow:
        _drop_shadow_path(ctx, p)
    p()
    set_color(ctx, fill)
    ctx.fill()
    p()
    set_color(ctx, stroke)
    ctx.set_line_width(3.2)
    ctx.stroke()
    fam = "DejaVu Sans Mono" if mono else "Inter"
    draw_multiline_centered(ctx, label, cx, cy, fam, font_size, bold=True, color=text_color)


def dfd_process(ctx, cx, cy, w, h, label, fill="#EFF6FF", stroke=NAVY, text_color=INK, font_size=22, mono=True, shadow=True):
    def p():
        rounded_rect_path(ctx, cx - w / 2, cy - h / 2, w, h, 10)

    if shadow:
        _drop_shadow_path(ctx, p)
    p()
    set_color(ctx, fill)
    ctx.fill()
    p()
    set_color(ctx, stroke)
    ctx.set_line_width(3.2)
    ctx.stroke()
    fam = "DejaVu Sans Mono" if mono else "Inter"
    draw_multiline_centered(ctx, label, cx, cy, fam, font_size, bold=True, color=text_color)


def dfd_decision(ctx, cx, cy, w, h, label, fill=ORANGE_FILL, stroke=ORANGE, text_color=INK, font_size=21, mono=True, shadow=True):
    def p():
        ctx.new_path()
        ctx.move_to(cx, cy - h / 2)
        ctx.line_to(cx + w / 2, cy)
        ctx.line_to(cx, cy + h / 2)
        ctx.line_to(cx - w / 2, cy)
        ctx.close_path()

    if shadow:
        _drop_shadow_path(ctx, p)
    p()
    set_color(ctx, fill)
    ctx.fill()
    p()
    set_color(ctx, stroke)
    ctx.set_line_width(3.4)
    ctx.stroke()
    fam = "DejaVu Sans Mono" if mono else "Inter"
    draw_multiline_centered(ctx, label, cx, cy, fam, font_size, bold=True, color=text_color)


def dfd_for_hex(ctx, cx, cy, w, h, label, fill=PURPLE_FILL, stroke=PURPLE, text_color=INK, point=26, font_size=21, mono=True, shadow=True):
    def p():
        x0, x1 = cx - w / 2, cx + w / 2
        y0, y1 = cy - h / 2, cy + h / 2
        ctx.new_path()
        ctx.move_to(x0 + point, y0)
        ctx.line_to(x1 - point, y0)
        ctx.line_to(x1, cy)
        ctx.line_to(x1 - point, y1)
        ctx.line_to(x0 + point, y1)
        ctx.line_to(x0, cy)
        ctx.close_path()

    if shadow:
        _drop_shadow_path(ctx, p)
    p()
    set_color(ctx, fill)
    ctx.fill()
    p()
    set_color(ctx, stroke)
    ctx.set_line_width(3.4)
    ctx.stroke()
    fam = "DejaVu Sans Mono" if mono else "Inter"
    draw_multiline_centered(ctx, label, cx, cy, fam, font_size, bold=True, color=text_color)


def dfd_output(ctx, cx, cy, w, h, label, fill=GREEN_FILL, stroke=GREEN, text_color=INK, font_size=21, mono=True, shadow=True):
    # Document / screen output with smooth S-wave bottom edge
    def p():
        x0, x1 = cx - w / 2, cx + w / 2
        y0 = cy - h / 2
        yb = cy + h / 2 - 8
        amp = 10
        ctx.new_path()
        ctx.move_to(x0, y0)
        ctx.line_to(x1, y0)
        ctx.line_to(x1, yb)
        ctx.curve_to(x1 - w * 0.25, yb - amp * 2, x0 + w * 0.25, yb + amp * 2, x0, yb + 3)
        ctx.close_path()

    if shadow:
        _drop_shadow_path(ctx, p)
    p()
    set_color(ctx, fill)
    ctx.fill()
    p()
    set_color(ctx, stroke)
    ctx.set_line_width(3.2)
    ctx.stroke()
    fam = "DejaVu Sans Mono" if mono else "Inter"
    draw_multiline_centered(ctx, label, cx, cy - 3, fam, font_size, bold=True, color=text_color)


def draw_arrow(ctx, pts, color=NAVY, width=3.2, head_len=14, head_w=9, dashed=False):
    if len(pts) < 2:
        return
    ctx.save()
    set_color(ctx, color)
    ctx.set_line_width(width)
    ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    if dashed:
        ctx.set_dash([9, 6])

    # Shorten final segment slightly so line tip enters cleanly behind arrowhead
    x1, y1 = pts[-2]
    x2, y2 = pts[-1]
    dx, dy = x2 - x1, y2 - y1
    dist = math.hypot(dx, dy)
    if dist > 1e-6:
        ux, uy = dx / dist, dy / dist
        end_x = x2 - ux * (head_len * 0.72)
        end_y = y2 - uy * (head_len * 0.72)
    else:
        ux, uy = 0, 1
        end_x, end_y = x2, y2

    ctx.new_path()
    ctx.move_to(pts[0][0], pts[0][1])
    for px, py in pts[1:-1]:
        ctx.line_to(px, py)
    ctx.line_to(end_x, end_y)
    ctx.stroke()

    # Solid arrowhead
    ctx.set_dash([])
    bx = x2 - ux * head_len
    by = y2 - uy * head_len
    px, py = -uy * (head_w / 2.0), ux * (head_w / 2.0)
    ctx.new_path()
    ctx.move_to(x2, y2)
    ctx.line_to(bx + px, by + py)
    ctx.line_to(bx - px, by - py)
    ctx.close_path()
    ctx.fill()
    ctx.restore()


def draw_pill(ctx, cx, cy, text, bg=GREEN, fg=WHITE, font_size=18, pad_x=14, pad_y=6, bold=True, mono=False, border=None):
    fam = "DejaVu Sans Mono" if mono else "Inter"
    lines = text.split("\n")
    widths = [text_size(ctx, ln, fam, font_size, bold=bold)[0] for ln in lines]
    tw = max(widths) if widths else 0
    line_h = font_size * 1.25
    pw = tw + pad_x * 2
    ph = (len(lines) * line_h if len(lines) > 1 else font_size) + pad_y * 2
    r = min(ph / 2.0, 18.0) if len(lines) > 1 else ph / 2.0
    rounded_rect(ctx, cx - pw / 2, cy - ph / 2, pw, ph, r=r, fill=bg, stroke=border, stroke_w=2.0)
    if len(lines) == 1:
        draw_text(ctx, text, cx, cy, fam, font_size, bold=bold, color=fg, align="center", valign="middle")
    else:
        draw_multiline_centered(ctx, lines, cx, cy, fam, font_size, bold=bold, color=fg, line_mult=1.25)
    return pw, ph


def draw_code_box(ctx, x, y, w, lines, font_size=17, pad_x=14, pad_y=10, bg=SUBTLE_BG, border=BORDER, fg=INK, line_mult=1.35):
    lh = font_size * line_mult
    h = pad_y * 2 + len(lines) * lh
    rounded_rect(ctx, x, y, w, h, r=8, fill=bg, stroke=border, stroke_w=1.8)
    for i, ln in enumerate(lines):
        draw_text(ctx, ln, x + pad_x, y + pad_y + i * lh, "DejaVu Sans Mono", font_size, bold=False, color=fg)
    return h


def draw_check_icon(ctx, cx, cy, r=12, bg=GREEN, fg=WHITE):
    ctx.save()
    set_color(ctx, bg)
    ctx.arc(cx, cy, r, 0, 2 * math.pi)
    ctx.fill()
    set_color(ctx, fg)
    ctx.set_line_width(2.8)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    ctx.move_to(cx - r * 0.45, cy + r * 0.05)
    ctx.line_to(cx - r * 0.1, cy + r * 0.38)
    ctx.line_to(cx + r * 0.48, cy - r * 0.35)
    ctx.stroke()
    ctx.restore()


def draw_cross_icon(ctx, cx, cy, r=12, bg=RED, fg=WHITE):
    ctx.save()
    set_color(ctx, bg)
    ctx.arc(cx, cy, r, 0, 2 * math.pi)
    ctx.fill()
    set_color(ctx, fg)
    ctx.set_line_width(2.8)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    d = r * 0.38
    ctx.move_to(cx - d, cy - d)
    ctx.line_to(cx + d, cy + d)
    ctx.move_to(cx + d, cy - d)
    ctx.line_to(cx - d, cy + d)
    ctx.stroke()
    ctx.restore()


def draw_warn_icon(ctx, cx, cy, r=14, bg=ORANGE, fg=WHITE):
    ctx.save()
    set_color(ctx, bg)
    ctx.new_path()
    ctx.move_to(cx, cy - r)
    ctx.line_to(cx + r * 0.95, cy + r * 0.8)
    ctx.line_to(cx - r * 0.95, cy + r * 0.8)
    ctx.close_path()
    ctx.fill()
    set_color(ctx, fg)
    ctx.set_line_width(2.6)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.move_to(cx, cy - r * 0.35)
    ctx.line_to(cx, cy + r * 0.25)
    ctx.stroke()
    ctx.arc(cx, cy + r * 0.52, 1.7, 0, 2 * math.pi)
    ctx.fill()
    ctx.restore()
