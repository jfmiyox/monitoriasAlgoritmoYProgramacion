#!/usr/bin/env python3
"""Generates dfd_00_simbolos_oficiales.png, dfd_01_suma_promedio.png, dfd_02_mayor_tres_numeros.png."""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import draw_lib as dl

OUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def make_dfd_00():
    W, H = 2400, 1820
    surf, ctx = dl.new_canvas(W, H)
    dl.draw_header(
        ctx,
        W,
        "Símbolos Oficiales de Diagramas de Flujo (DFD)",
        "Guía de formas geométricas estándar, función y traducción directa a PSeInt y C++",
        badge="MÓDULO M01 · GUÍA DFD",
        accent=dl.TEAL,
    )

    tx, ty = 40, 174
    cols = [
        ("Símbolo DFD", 330),
        ("Nombre y Forma", 330),
        ("¿Para qué sirve?", 660),
        ("Equivalencia en PSeInt", 490),
        ("Equivalencia en C++", 510),
    ]
    total_w = sum(c[1] for c in cols)  # 2320
    hdr_h = 64
    row_h = 204
    rows_n = 7
    table_h = hdr_h + rows_n * row_h

    # Outer table card
    dl.rounded_rect(ctx, tx, ty, total_w, table_h, r=14, fill=dl.WHITE, stroke=dl.BORDER_DARK, stroke_w=2.2, shadow=True)

    # Header row
    dl.rounded_rect(ctx, tx, ty, total_w, hdr_h, r=14, fill=dl.NAVY_SOFT)
    # Square bottom corners of header
    dl.set_color(ctx, dl.NAVY_SOFT)
    ctx.rectangle(tx, ty + hdr_h - 14, total_w, 14)
    ctx.fill()

    cx_col = tx
    for idx, (cname, cw) in enumerate(cols):
        dl.draw_text(ctx, cname, cx_col + cw / 2, ty + hdr_h / 2, "Inter", 20, bold=True, color=dl.NAVY, align="center", valign="middle")
        if idx > 0:
            dl.set_color(ctx, dl.BORDER)
            ctx.set_line_width(1.6)
            ctx.move_to(cx_col, ty)
            ctx.line_to(cx_col, ty + table_h)
            ctx.stroke()
        cx_col += cw

    # Horizontal header divider
    dl.set_color(ctx, dl.BORDER_DARK)
    ctx.set_line_width(2.0)
    ctx.move_to(tx, ty + hdr_h)
    ctx.line_to(tx + total_w, ty + hdr_h)
    ctx.stroke()

    def draw_sym_inicio(cx, cy):
        dl.dfd_start_end(ctx, cx, cy, 210, 68, "Inicio / Fin", font_size=21, shadow=False)

    def draw_sym_leer(cx, cy):
        dl.dfd_input(ctx, cx, cy, 224, 72, "Leer x", font_size=20, shadow=False)

    def draw_sym_proc(cx, cy):
        dl.dfd_process(ctx, cx, cy, 224, 72, "x <- a + b", font_size=19, shadow=False)

    def draw_sym_dec(cx, cy):
        dl.dfd_decision(ctx, cx, cy - 8, 178, 86, "¿a > b?", font_size=18, shadow=False)
        # Sí left-down, No right-down
        dl.draw_arrow(ctx, [(cx - 89, cy - 8), (cx - 122, cy - 8), (cx - 122, cy + 56)], color=dl.GREEN, width=2.8, head_len=11, head_w=7)
        dl.draw_arrow(ctx, [(cx + 89, cy - 8), (cx + 122, cy - 8), (cx + 122, cy + 56)], color=dl.RED, width=2.8, head_len=11, head_w=7)
        dl.draw_pill(ctx, cx - 105, cy - 32, "Sí", bg=dl.GREEN, fg=dl.WHITE, font_size=14, pad_x=8, pad_y=3)
        dl.draw_pill(ctx, cx + 105, cy - 32, "No", bg=dl.RED, fg=dl.WHITE, font_size=14, pad_x=8, pad_y=3)

    def draw_sym_while(cx, cy):
        # Return arrow coming into top of diamond from left
        dl.draw_arrow(ctx, [(cx - 108, cy + 58), (cx - 108, cy - 68), (cx + 12, cy - 68), (cx + 12, cy - 54)], color=dl.TEAL, width=2.6, head_len=10, head_w=7)
        dl.dfd_decision(ctx, cx + 12, cy - 12, 166, 78, "¿cond?", font_size=18, fill=dl.TEAL_FILL, stroke=dl.TEAL, shadow=False)
        # Sí downward into mini body -> loop back left
        dl.draw_arrow(ctx, [(cx + 12, cy + 27), (cx + 12, cy + 44)], color=dl.GREEN, width=2.6, head_len=9, head_w=6)
        dl.dfd_process(ctx, cx + 12, cy + 62, 118, 34, "Cuerpo", font_size=15, mono=False, fill=dl.SUBTLE_BG, stroke=dl.NAVY, shadow=False)
        dl.set_color(ctx, dl.TEAL)
        ctx.set_line_width(2.6)
        ctx.move_to(cx - 47, cy + 62)
        ctx.line_to(cx - 108, cy + 62)
        ctx.line_to(cx - 108, cy + 56)
        ctx.stroke()
        # No exit right
        dl.draw_arrow(ctx, [(cx + 95, cy - 12), (cx + 142, cy - 12)], color=dl.RED, width=2.6, head_len=10, head_w=7)
        dl.draw_pill(ctx, cx + 38, cy + 33, "Sí", bg=dl.GREEN, fg=dl.WHITE, font_size=13, pad_x=6, pad_y=2)
        dl.draw_pill(ctx, cx + 120, cy - 34, "No", bg=dl.RED, fg=dl.WHITE, font_size=13, pad_x=6, pad_y=2)

    def draw_sym_for(cx, cy):
        dl.dfd_for_hex(ctx, cx + 10, cy - 22, 206, 62, "i <- 1 .. N", font_size=17, point=20, shadow=False)
        # Down to body
        dl.draw_arrow(ctx, [(cx + 10, cy + 9), (cx + 10, cy + 32)], color=dl.PURPLE, width=2.6, head_len=9, head_w=6)
        dl.dfd_process(ctx, cx + 10, cy + 52, 134, 36, "Cuerpo", font_size=15, mono=False, fill=dl.SUBTLE_BG, stroke=dl.NAVY, shadow=False)
        # Loop back left into hexagon
        dl.draw_arrow(ctx, [(cx - 57, cy + 52), (cx - 115, cy + 52), (cx - 115, cy - 22), (cx - 93, cy - 22)], color=dl.PURPLE, width=2.6, head_len=10, head_w=7)
        # Exit right
        dl.draw_arrow(ctx, [(cx + 113, cy - 22), (cx + 146, cy - 22)], color=dl.NAVY, width=2.6, head_len=10, head_w=7)

    def draw_sym_out(cx, cy):
        dl.dfd_output(ctx, cx, cy, 224, 78, "Escribir x", font_size=19, shadow=False)

    data = [
        (
            draw_sym_inicio,
            "Inicio / Fin",
            "Óvalo o Cápsula",
            dl.TEAL,
            "Marca de forma obligatoria dónde comienza y dónde termina todo algoritmo o diagrama de flujo.",
            ["Algoritmo MiPrograma", "  ...", "FinAlgoritmo"],
            ["int main() {", "  ...", "  return 0;", "}"],
        ),
        (
            draw_sym_leer,
            "Lectura (Entrada)",
            "Paralelogramo",
            dl.BLUE,
            "Pide datos al usuario por teclado y los guarda inmediatamente dentro de una o más variables.",
            ["Leer edad", "Leer n1, n2"],
            ["cin >> edad;", "cin >> n1 >> n2;"],
        ),
        (
            draw_sym_proc,
            "Asignación / Proceso",
            "Rectángulo",
            dl.NAVY,
            "Ejecuta cálculos matemáticos, inicializa variables o actualiza el contenido de una variable en RAM.",
            ["suma <- a + b", "cont <- cont + 1"],
            ["suma = a + b;", "cont = cont + 1;"],
        ),
        (
            draw_sym_dec,
            "Decisión Sí / No",
            "Rombo",
            dl.ORANGE,
            "Evalúa una condición lógica (V o F). Bifurca el flujo por el camino Sí (verdadero) o No (falso).",
            ["Si a > b Entonces", "  ...", "SiNo", "  ...", "FinSi"],
            ["if (a > b) {", "  ...", "} else {", "  ...", "}"],
        ),
        (
            draw_sym_while,
            "Ciclo Mientras",
            "Rombo + Retorno",
            dl.TEAL,
            "Repite un bloque mientras la condición sea verdadera. Evalúa ANTES de entrar (puede ejecutar 0 veces).",
            ["Mientras cond Hacer", "  ...", "FinMientras"],
            ["while (cond) {", "  ...", "}"],
        ),
        (
            draw_sym_for,
            "Ciclo Para",
            "Hexágono + Retorno",
            dl.PURPLE,
            "Ciclo controlado por contador (inicio, fin y paso). Ideal cuando sabes cuántas veces repetir.",
            ["Para i<-1 Hasta N Hacer", "  ...", "FinPara"],
            ["for (int i=1; i<=N; i++) {", "  ...", "}"],
        ),
        (
            draw_sym_out,
            "Salida en Pantalla",
            "Pantalla / Documento",
            dl.GREEN,
            "Muestra resultados, mensajes o valores de variables al usuario en la consola o pantalla.",
            ["Escribir \"Total: \", tot"],
            ["cout << \"Total: \" << tot;"],
        ),
    ]

    for r_idx, (draw_fn, title, shape_sub, accent, desc, ps_lines, cpp_lines) in enumerate(data):
        ry = ty + hdr_h + r_idx * row_h
        if r_idx % 2 == 1:
            dl.set_color(ctx, dl.PANEL_BG)
            ctx.rectangle(tx + 2, ry + 1, total_w - 4, row_h - 2)
            ctx.fill()
        if r_idx > 0:
            dl.set_color(ctx, dl.BORDER)
            ctx.set_line_width(1.5)
            ctx.move_to(tx, ry)
            ctx.line_to(tx + total_w, ry)
            ctx.stroke()

        # Col 1: Symbol
        c1_x = tx
        draw_fn(c1_x + cols[0][1] / 2, ry + row_h / 2)

        # Col 2: Name + shape badge
        c2_x = c1_x + cols[0][1]
        dl.draw_text(ctx, title, c2_x + 24, ry + 64, "Inter", 23, bold=True, color=dl.NAVY)
        dl.draw_pill(ctx, c2_x + 24 + dl.text_size(ctx, shape_sub, "Inter", 16, bold=True)[0] / 2 + 14, ry + 124, shape_sub, bg=dl.NAVY_SOFT, fg=accent, font_size=16, pad_x=14, pad_y=6, border=accent)

        # Col 3: Purpose
        c3_x = c2_x + cols[1][1]
        _, lines = dl.draw_wrapped(ctx, desc, c3_x + 24, ry + 56, cols[2][1] - 48, "Inter", 19.5, color=dl.INK_SEC, line_mult=1.35, draw=False)
        text_h = len(lines) * 19.5 * 1.35
        dl.draw_wrapped(ctx, desc, c3_x + 24, ry + (row_h - text_h) / 2, cols[2][1] - 48, "Inter", 19.5, color=dl.INK_SEC, line_mult=1.35, draw=True)

        # Col 4: PSeInt code box
        c4_x = c3_x + cols[2][1]
        box_w4 = cols[3][1] - 40
        lh4 = 17.5 * 1.38
        bh4 = 20 + len(ps_lines) * lh4
        dl.draw_code_box(ctx, c4_x + 20, ry + (row_h - bh4) / 2, box_w4, ps_lines, font_size=17.5, pad_x=16, pad_y=10, bg=dl.TEAL_SOFT, border="#99F6E4", fg=dl.INK, line_mult=1.38)

        # Col 5: C++ code box
        c5_x = c4_x + cols[3][1]
        box_w5 = cols[4][1] - 40
        bh5 = 20 + len(cpp_lines) * lh4
        dl.draw_code_box(ctx, c5_x + 20, ry + (row_h - bh5) / 2, box_w5, cpp_lines, font_size=17.5, pad_x=16, pad_y=10, bg=dl.BLUE_SOFT, border="#BFDBFE", fg=dl.INK, line_mult=1.38)

    # Golden rule banner
    gy = ty + table_h + 22
    dl.rounded_rect(ctx, 40, gy, W - 80, 62, r=12, fill=dl.AMBER_SOFT, stroke=dl.AMBER, stroke_w=2.2)
    dl.draw_warn_icon(ctx, 76, gy + 31, r=14, bg=dl.AMBER, fg=dl.WHITE)
    dl.draw_text(
        ctx,
        "Reglas de Oro DFD: 1) Un único Inicio.  2) Flujo claro con flechas (sin flechas sueltas ni cruces).  3) Todo camino llega a Fin.",
        106,
        gy + 31,
        "Inter",
        19,
        bold=True,
        color=dl.NAVY,
        valign="middle",
    )

    dl.draw_footer(ctx, W, H, "Curso de Algoritmos y Programación (30h) · De la lógica al C++ estático", badge="dfd_00_simbolos_oficiales.png")
    dl.save_png(surf, os.path.join(OUT_DIR, "dfd_00_simbolos_oficiales.png"))


def make_dfd_01():
    W, H = 2000, 1480
    surf, ctx = dl.new_canvas(W, H)
    dl.draw_header(
        ctx,
        W,
        "DFD Secuencial: Suma y Promedio de 3 Notas",
        "Flujo lineal clásico sin bifurcaciones: Entrada → Proceso aritmético → Salida",
        badge="MÓDULO M01 · EJEMPLO 1",
        accent=dl.BLUE,
    )

    # Left panel container for clean DFD
    dl.rounded_rect(ctx, 44, 178, 960, 1210, r=16, fill=dl.PANEL_BG, stroke=dl.BORDER, stroke_w=2.0)
    dl.draw_text(ctx, "Diagrama de Flujo (DFD)", 524, 210, "Inter", 23, bold=True, color=dl.NAVY, align="center")

    cx = 524
    # Nodes
    y_ini = 295
    y_read = 475
    y_proc = 685
    y_out = 905
    y_fin = 1110

    dl.dfd_start_end(ctx, cx, y_ini, 230, 72, "Inicio", font_size=24)
    dl.dfd_input(ctx, cx, y_read, 410, 90, "Leer n1, n2, n3", font_size=22)
    dl.dfd_process(ctx, cx, y_proc, 510, 98, "prom <- (n1 + n2 + n3) / 3", font_size=22)
    dl.dfd_output(ctx, cx, y_out, 440, 102, 'Escribir "Promedio: ", prom', font_size=21)
    dl.dfd_start_end(ctx, cx, y_fin, 230, 72, "Fin", font_size=24)

    # Arrows
    dl.draw_arrow(ctx, [(cx, y_ini + 36), (cx, y_read - 45)], color=dl.NAVY, width=3.5)
    dl.draw_arrow(ctx, [(cx, y_read + 45), (cx, y_proc - 49)], color=dl.NAVY, width=3.5)
    dl.draw_arrow(ctx, [(cx, y_proc + 49), (cx, y_out - 51)], color=dl.NAVY, width=3.5)
    dl.draw_arrow(ctx, [(cx, y_out + 44), (cx, y_fin - 36)], color=dl.NAVY, width=3.5)

    # EPS badges connected lightly to shapes
    dl.draw_pill(ctx, 160, y_read, "ENTRADA", bg=dl.BLUE, fg=dl.WHITE, font_size=16, pad_x=14, pad_y=6)
    dl.draw_pill(ctx, 160, y_proc, "PROCESO", bg=dl.NAVY, fg=dl.WHITE, font_size=16, pad_x=14, pad_y=6)
    dl.draw_pill(ctx, 160, y_out, "SALIDA", bg=dl.GREEN, fg=dl.WHITE, font_size=16, pad_x=14, pad_y=6)

    # Subtle explanatory note inside bottom of left panel
    dl.rounded_rect(ctx, 84, 1200, 880, 150, r=12, fill=dl.WHITE, stroke=dl.BORDER, stroke_w=1.8)
    dl.draw_check_icon(ctx, 120, 1245, r=13, bg=dl.TEAL)
    dl.draw_text(ctx, "Lectura de la flecha  <-  (asignación):", 148, 1232, "Inter", 20, bold=True, color=dl.NAVY)
    dl.draw_wrapped(
        ctx,
        "Primero se calcula la expresión de la derecha (n1 + n2 + n3) / 3 y ese resultado se guarda en la variable prom. Los paréntesis son obligatorios: sin ellos, solo dividiría n3 entre 3.",
        148,
        1268,
        790,
        "Inter",
        18.5,
        color=dl.INK_SEC,
    )

    # Right column cards
    rx = 1040
    rw = 916

    # Card 1: EPS Breakdown
    dl.rounded_rect(ctx, rx, 178, rw, 300, r=16, fill=dl.WHITE, stroke=dl.BORDER_DARK, stroke_w=2.0, shadow=True)
    dl.draw_text(ctx, "1. Análisis EPS del Problema", rx + 28, 206, "Inter", 23, bold=True, color=dl.NAVY)
    eps_items = [
        ("Entradas:", "n1, n2, n3 (las tres calificaciones ingresadas por teclado)", dl.BLUE_FILL, dl.BLUE),
        ("Proceso:", "Sumar las tres notas y dividir el total entre 3 → prom", dl.NAVY_SOFT, dl.NAVY),
        ("Salida:", "Mostrar en pantalla el promedio calculado prom", dl.GREEN_FILL, dl.GREEN),
    ]
    ey = 258
    for tag, desc, bg, fg in eps_items:
        dl.rounded_rect(ctx, rx + 28, ey, 140, 44, r=8, fill=bg, stroke=fg, stroke_w=1.8)
        dl.draw_text(ctx, tag, rx + 98, ey + 22, "Inter", 18, bold=True, color=fg, align="center", valign="middle")
        dl.draw_wrapped(ctx, desc, rx + 186, ey + 9, rw - 214, "Inter", 19, color=dl.INK_SEC)
        ey += 70

    # Card 2: Prueba de escritorio
    dl.rounded_rect(ctx, rx, 506, rw, 300, r=16, fill=dl.WHITE, stroke=dl.BORDER_DARK, stroke_w=2.0, shadow=True)
    dl.draw_text(ctx, "2. Prueba de Escritorio (Seguimiento en Papel)", rx + 28, 534, "Inter", 23, bold=True, color=dl.NAVY)

    # Mini table
    tx0, ty0 = rx + 28, 588
    cw_t = [150, 150, 150, 190, 220]
    headers_t = ["n1", "n2", "n3", "prom", "Pantalla"]
    vals_t = [
        ["3.5", "4.5", "4.0", "4.0", "Promedio: 4.0"],
        ["5.0", "2.0", "3.5", "3.5", "Promedio: 3.5"],
    ]
    dl.rounded_rect(ctx, tx0, ty0, sum(cw_t), 48, r=8, fill=dl.NAVY)
    px = tx0
    for htxt, wcol in zip(headers_t, cw_t):
        dl.draw_text(ctx, htxt, px + wcol / 2, ty0 + 24, "DejaVu Sans Mono", 18, bold=True, color=dl.WHITE, align="center", valign="middle")
        px += wcol
    for r_i, row in enumerate(vals_t):
        ry0 = ty0 + 48 + r_i * 54
        dl.rounded_rect(ctx, tx0, ry0, sum(cw_t), 54, r=4, fill=dl.PANEL_BG if r_i % 2 else dl.WHITE, stroke=dl.BORDER, stroke_w=1.4)
        px = tx0
        for c_i, (val, wcol) in enumerate(zip(row, cw_t)):
            col_txt = dl.GREEN if c_i == 4 else (dl.NAVY if c_i == 3 else dl.INK)
            dl.draw_text(ctx, val, px + wcol / 2, ry0 + 27, "DejaVu Sans Mono", 18, bold=(c_i >= 3), color=col_txt, align="center", valign="middle")
            px += wcol
    dl.draw_text(ctx, "Comprobación: (3.5 + 4.5 + 4.0) / 3 = 12.0 / 3 = 4.0  ✓", rx + 28, 760, "Inter", 18.5, bold=True, color=dl.TEAL)

    # Card 3: PSeInt & C++ + Trap warning
    dl.rounded_rect(ctx, rx, 834, rw, 554, r=16, fill=dl.WHITE, stroke=dl.BORDER_DARK, stroke_w=2.0, shadow=True)
    dl.draw_text(ctx, "3. Traducción directa a PSeInt y C++", rx + 28, 862, "Inter", 23, bold=True, color=dl.NAVY)

    dl.draw_text(ctx, "PSeInt (Español)", rx + 28, 912, "Inter", 18, bold=True, color=dl.TEAL)
    dl.draw_code_box(
        ctx,
        rx + 28,
        942,
        420,
        [
            "Algoritmo Promedio3",
            "  Definir n1, n2, n3 Como Real;",
            "  Definir prom Como Real;",
            "  Escribir \"Ingrese 3 notas:\";",
            "  Leer n1, n2, n3;",
            "  prom <- (n1 + n2 + n3) / 3;",
            "  Escribir \"Promedio: \", prom;",
            "FinAlgoritmo",
        ],
        font_size=15.0,
        bg=dl.TEAL_SOFT,
        border="#99F6E4",
    )

    dl.draw_text(ctx, "C++ Básico", rx + 470, 912, "Inter", 18, bold=True, color=dl.BLUE)
    dl.draw_code_box(
        ctx,
        rx + 470,
        942,
        418,
        [
            "#include <iostream>",
            "using namespace std;",
            "int main() {",
            "  double n1, n2, n3, prom;",
            "  cin >> n1 >> n2 >> n3;",
            "  prom = (n1 + n2 + n3) / 3.0;",
            "  cout << \"Promedio: \" << prom;",
            "  return 0;",
            "}",
        ],
        font_size=15.0,
        bg=dl.BLUE_SOFT,
        border="#BFDBFE",
    )

    # Warning box at bottom of Card 3
    dl.rounded_rect(ctx, rx + 28, 1244, rw - 56, 118, r=12, fill=dl.ORANGE_SOFT, stroke=dl.ORANGE, stroke_w=2.2)
    dl.draw_warn_icon(ctx, rx + 64, 1284, r=14, bg=dl.ORANGE, fg=dl.WHITE)
    dl.draw_text(ctx, "¡OJO CON LA TRAMPA EN C++!", rx + 92, 1268, "Inter", 19, bold=True, color=dl.ORANGE)
    dl.draw_wrapped(
        ctx,
        "Si n1, n2, n3 fueran int y escribes (n1+n2+n3)/3, C++ trunca los decimales (ej: 10/3 da 3). Usa variables double y divide por 3.0.",
        rx + 92,
        1298,
        rw - 140,
        "Inter",
        17.5,
        color=dl.INK_SEC,
    )

    dl.draw_footer(ctx, W, H, "Curso de Algoritmos y Programación (30h) · Estructura Secuencial", badge="dfd_01_suma_promedio.png")
    dl.save_png(surf, os.path.join(OUT_DIR, "dfd_01_suma_promedio.png"))


def make_dfd_02():
    W, H = 2400, 1740
    surf, ctx = dl.new_canvas(W, H)
    dl.draw_header(
        ctx,
        W,
        "DFD Decisiones Anidadas: Mayor de Tres Números (A, B, C)",
        "Árbol completo de decisiones Sí / No usando >= para manejar correctamente posibles empates",
        badge="MÓDULO M01 · M04",
        accent=dl.ORANGE,
    )

    # Main background card
    dl.rounded_rect(ctx, 40, 172, W - 80, 1486, r=16, fill=dl.PANEL_BG, stroke=dl.BORDER, stroke_w=2.0)

    cx = 1200
    y_ini = 236
    y_read = 374
    y_d1 = 550

    dl.dfd_start_end(ctx, cx, y_ini, 230, 68, "Inicio", font_size=24)
    dl.dfd_input(ctx, cx, y_read, 340, 82, "Leer A, B, C", font_size=22)
    dl.dfd_decision(ctx, cx, y_d1, 280, 134, "¿A >= B?", font_size=23)

    dl.draw_arrow(ctx, [(cx, y_ini + 34), (cx, y_read - 41)], color=dl.NAVY, width=3.5)
    dl.draw_arrow(ctx, [(cx, y_read + 41), (cx, y_d1 - 67)], color=dl.NAVY, width=3.5)

    # Level 2 decisions
    lx, rx = 620, 1780
    y_d2 = 790
    dl.dfd_decision(ctx, lx, y_d2, 280, 134, "¿A >= C?", font_size=23)
    dl.dfd_decision(ctx, rx, y_d2, 280, 134, "¿B >= C?", font_size=23)

    # Arrows D1 -> D2
    dl.draw_arrow(ctx, [(cx - 140, y_d1), (lx, y_d1), (lx, y_d2 - 67)], color=dl.GREEN, width=3.5)
    dl.draw_arrow(ctx, [(cx + 140, y_d1), (rx, y_d1), (rx, y_d2 - 67)], color=dl.RED, width=3.5)
    dl.draw_pill(ctx, (cx - 140 + lx) / 2, y_d1, "Sí", bg=dl.GREEN, fg=dl.WHITE, font_size=19, pad_x=16, pad_y=6)
    dl.draw_pill(ctx, (cx + 140 + rx) / 2, y_d1, "No", bg=dl.RED, fg=dl.WHITE, font_size=19, pad_x=16, pad_y=6)

    # Level 3 assignments
    xs_leaf = [350, 890, 1510, 2050]
    labels_leaf = ["mayor <- A", "mayor <- C", "mayor <- B", "mayor <- C"]
    y_leaf = 1045

    for x_pos, lbl in zip(xs_leaf, labels_leaf):
        dl.dfd_process(ctx, x_pos, y_leaf, 250, 82, lbl, font_size=22, fill=dl.WHITE, stroke=dl.NAVY)

    # Arrows D2_left -> leaf 0 & 1
    dl.draw_arrow(ctx, [(lx - 140, y_d2), (xs_leaf[0], y_d2), (xs_leaf[0], y_leaf - 41)], color=dl.GREEN, width=3.5)
    dl.draw_arrow(ctx, [(lx + 140, y_d2), (xs_leaf[1], y_d2), (xs_leaf[1], y_leaf - 41)], color=dl.RED, width=3.5)
    dl.draw_pill(ctx, xs_leaf[0] + 62, y_d2, "Sí", bg=dl.GREEN, fg=dl.WHITE, font_size=18, pad_x=14, pad_y=5)
    dl.draw_pill(ctx, xs_leaf[1] - 62, y_d2, "No", bg=dl.RED, fg=dl.WHITE, font_size=18, pad_x=14, pad_y=5)

    # Arrows D2_right -> leaf 2 & 3
    dl.draw_arrow(ctx, [(rx - 140, y_d2), (xs_leaf[2], y_d2), (xs_leaf[2], y_leaf - 41)], color=dl.GREEN, width=3.5)
    dl.draw_arrow(ctx, [(rx + 140, y_d2), (xs_leaf[3], y_d2), (xs_leaf[3], y_leaf - 41)], color=dl.RED, width=3.5)
    dl.draw_pill(ctx, xs_leaf[2] + 62, y_d2, "Sí", bg=dl.GREEN, fg=dl.WHITE, font_size=18, pad_x=14, pad_y=5)
    dl.draw_pill(ctx, xs_leaf[3] - 62, y_d2, "No", bg=dl.RED, fg=dl.WHITE, font_size=18, pad_x=14, pad_y=5)

    # Collector bus at y_bus = 1190
    y_bus = 1190
    dl.set_color(ctx, dl.NAVY)
    ctx.set_line_width(3.5)
    ctx.move_to(xs_leaf[0], y_bus)
    ctx.line_to(xs_leaf[3], y_bus)
    ctx.stroke()

    for xp in xs_leaf:
        ctx.move_to(xp, y_leaf + 41)
        ctx.line_to(xp, y_bus)
        ctx.stroke()
        ctx.arc(xp, y_bus, 6.5, 0, 6.2832)
        ctx.fill()

    y_out = 1325
    y_fin = 1495
    dl.draw_arrow(ctx, [(cx, y_bus), (cx, y_out - 50)], color=dl.NAVY, width=3.5)
    dl.dfd_output(ctx, cx, y_out, 470, 100, 'Escribir "El mayor es: ", mayor', font_size=21)
    dl.draw_arrow(ctx, [(cx, y_out + 43), (cx, y_fin - 34)], color=dl.NAVY, width=3.5)
    dl.dfd_start_end(ctx, cx, y_fin, 230, 68, "Fin", font_size=24)

    # Bottom corner pedagogical cards (never touch central flow)
    # Left card: Why >= instead of >
    dl.rounded_rect(ctx, 80, 1280, 740, 260, r=14, fill=dl.WHITE, stroke=dl.ORANGE, stroke_w=2.0, shadow=True)
    dl.draw_warn_icon(ctx, 118, 1320, r=13, bg=dl.ORANGE)
    dl.draw_text(ctx, "Detalle Clave de Parcial: ¿Por qué >= y no >?", 146, 1306, "Inter", 20, bold=True, color=dl.NAVY)
    dl.draw_wrapped(
        ctx,
        "• Si A = 8, B = 8 y C = 5, hay empate en el mayor (8).\n• Con >= entra por A >= B (Sí) y luego A >= C (Sí) → mayor = 8.\n• Todos los 4 caminos asignan siempre un valor válido a mayor y convergen antes de imprimir.",
        106,
        1352,
        690,
        "Inter",
        18.5,
        color=dl.INK_SEC,
        line_mult=1.38,
    )

    # Right card: Quick trace example
    dl.rounded_rect(ctx, 1580, 1280, 740, 260, r=14, fill=dl.WHITE, stroke=dl.TEAL, stroke_w=2.0, shadow=True)
    dl.draw_check_icon(ctx, 1618, 1320, r=13, bg=dl.TEAL)
    dl.draw_text(ctx, "Prueba de Escritorio Rápida: A = 7, B = 12, C = 9", 1646, 1306, "Inter", 20, bold=True, color=dl.NAVY)
    dl.draw_wrapped(
        ctx,
        "1. ¿7 >= 12?  → Falso (No, rama derecha).\n2. ¿12 >= 9? → Verdadero (Sí, rama izquierda).\n3. Se ejecuta mayor <- B (mayor = 12).\n4. Sale: \"El mayor es: 12\" y termina en Fin.",
        1606,
        1352,
        690,
        "Inter",
        18.5,
        color=dl.INK_SEC,
        line_mult=1.38,
    )

    dl.draw_footer(ctx, W, H, "Curso de Algoritmos y Programación (30h) · Condicionales Anidados", badge="dfd_02_mayor_tres_numeros.png")
    dl.save_png(surf, os.path.join(OUT_DIR, "dfd_02_mayor_tres_numeros.png"))


if __name__ == "__main__":
    make_dfd_00()
    make_dfd_01()
    make_dfd_02()
    print("Generated dfd_00, dfd_01, dfd_02 successfully.")
