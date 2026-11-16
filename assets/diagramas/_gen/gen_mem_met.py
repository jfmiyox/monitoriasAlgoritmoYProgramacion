#!/usr/bin/env python3
"""Generates mem_01_variables_ram.png, mem_02_puente_ciclos.png, mem_03_vector_estatico_1d.png, mem_04_matriz_estatica_2d.png, met_01_cinco_pasos_analisis.png."""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import draw_lib as dl

OUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def make_mem_01():
    W, H = 2400, 1680
    surf, ctx = dl.new_canvas(W, H)
    dl.draw_header(
        ctx,
        W,
        'Memoria RAM "Para Tontos": Cajas de Tipos de Datos',
        "Cada variable reserva una caja con nombre, tipo, tamaño aproximado y un único valor a la vez",
        badge="MÓDULO M02 · M03 · RAM",
        accent=dl.BLUE,
    )

    cards = [
        {
            "tipo": "int",
            "pseint": "PSeInt: Entero",
            "size": "~4 bytes",
            "color": dl.BLUE,
            "fill": dl.BLUE_SOFT,
            "addr": "0x100",
            "var": "edad",
            "val": "19",
            "decl": "int edad = 19;",
            "valid": "-42, 0, 19, 2025 (números enteros SIN parte decimal).",
            "err": "int x = 3.9; → C++ trunca el .9 y guarda 3 (¡no redondea!).",
        },
        {
            "tipo": "double",
            "pseint": "PSeInt: Real",
            "size": "~8 bytes",
            "color": dl.TEAL,
            "fill": dl.TEAL_SOFT,
            "addr": "0x104",
            "var": "nota",
            "val": "4.75",
            "decl": "double nota = 4.75;",
            "valid": "3.1416, -0.5, 4.75, 4.0 (números reales con decimales).",
            "err": "double r = 5 / 2; → guarda 2.0 (división entera). ¡Usa 5.0 / 2!",
        },
        {
            "tipo": "char",
            "pseint": "PSeInt: Carácter",
            "size": "1 byte",
            "color": dl.PURPLE,
            "fill": dl.PURPLE_SOFT,
            "addr": "0x10C",
            "var": "grupo",
            "val": "'A'",
            "decl": "char grupo = 'A';",
            "valid": "'A', 'z', '7', '@' (EXACTAMENTE 1 símbolo entre comillas simples).",
            "err": 'Usar comillas dobles "A" o meter 2 letras (\'AB\') produce error.',
        },
        {
            "tipo": "bool",
            "pseint": "PSeInt: Lógico",
            "size": "1 byte",
            "color": dl.ORANGE,
            "fill": dl.ORANGE_SOFT,
            "addr": "0x10D",
            "var": "aprobo",
            "val": "true (1)",
            "decl": "bool aprobo = true;",
            "valid": "true (1) o false (0) (en PSeInt: Verdadero o Falso).",
            "err": 'Escribir "true" con comillas (es texto) o confundir = con == en if.',
        },
        {
            "tipo": "string",
            "pseint": "PSeInt: Cadena",
            "size": "Variable (objeto)",
            "color": dl.NAVY,
            "fill": dl.NAVY_SOFT,
            "addr": "0x110",
            "var": "nombre",
            "val": '"Ana Sofía"',
            "decl": 'string nombre = "Ana Sofía";',
            "valid": '"Hola", "Ana Sofía", "" (texto de 0 o más caracteres, comillas dobles).',
            "err": "cin >> nombre; corta en el primer espacio. Usa getline() + cin.ignore().",
        },
    ]

    cw, ch = 1136, 444
    xs = [44, 1220]
    ys = [178, 646, 1114]

    for idx, c in enumerate(cards):
        col_i = idx % 2
        row_i = idx // 2
        x, y = xs[col_i], ys[row_i]
        accent = c["color"]

        dl.rounded_rect(ctx, x, y, cw, ch, r=16, fill=dl.WHITE, stroke=accent, stroke_w=2.4, shadow=True)
        # Card top header band
        dl.rounded_rect(ctx, x, y, cw, 64, r=16, fill=c["fill"])
        dl.set_color(ctx, c["fill"])
        ctx.rectangle(x + 2, y + 48, cw - 4, 16)
        ctx.fill()
        dl.set_color(ctx, accent)
        ctx.set_line_width(2.0)
        ctx.move_to(x, y + 64)
        ctx.line_to(x + cw, y + 64)
        ctx.stroke()

        dl.draw_text(ctx, c["tipo"], x + 28, y + 32, "DejaVu Sans Mono", 28, bold=True, color=accent, valign="middle")
        dl.draw_text(ctx, f"·  {c['pseint']}", x + 150, y + 32, "Inter", 19, bold=True, color=dl.INK_SEC, valign="middle")
        dl.draw_pill(ctx, x + cw - 110, y + 32, c["size"], bg=accent, fg=dl.WHITE, font_size=16, pad_x=14, pad_y=6)

        # Left inside card: RAM locker box
        bx, by, bw, bh = x + 28, y + 92, 330, 324
        dl.rounded_rect(ctx, bx, by, bw, bh, r=14, fill=dl.PANEL_BG, stroke=dl.BORDER, stroke_w=1.8)
        dl.draw_text(ctx, f"Dir. RAM: {c['addr']}", bx + bw / 2, by + 26, "DejaVu Sans Mono", 15, color=dl.MUTED, align="center")

        # Locker 3D-feel box
        lx, ly, lw, lh = bx + 30, by + 72, bw - 60, 146
        dl.rounded_rect(ctx, lx + 8, ly + 8, lw, lh, r=12, fill=c["fill"], stroke=accent, stroke_w=1.5)
        dl.rounded_rect(ctx, lx, ly, lw, lh, r=12, fill=dl.WHITE, stroke=accent, stroke_w=3.2)
        # Variable label tab on top of box
        dl.draw_pill(ctx, lx + lw / 2, ly, c["var"], bg=accent, fg=dl.WHITE, font_size=18, pad_x=18, pad_y=5, mono=True)
        # Value inside box
        vsize = 28 if len(c["val"]) <= 10 else 22
        dl.draw_text(ctx, c["val"], lx + lw / 2, ly + lh / 2 + 6, "DejaVu Sans Mono", vsize, bold=True, color=dl.INK, align="center", valign="middle")

        # Code declaration strip below locker
        dl.draw_code_box(ctx, bx + 18, by + 246, bw - 36, [c["decl"]], font_size=15.5, pad_x=12, pad_y=10, bg=c["fill"], border=accent)

        # Right inside card: Valid + Common Error
        rx = x + 382
        rw = cw - 410

        dl.rounded_rect(ctx, rx, y + 92, rw, 148, r=12, fill=dl.GREEN_SOFT, stroke="#86EFAC", stroke_w=1.8)
        dl.draw_check_icon(ctx, rx + 28, y + 122, r=12, bg=dl.GREEN)
        dl.draw_text(ctx, "Ejemplos válidos:", rx + 50, y + 111, "Inter", 18.5, bold=True, color=dl.GREEN)
        dl.draw_wrapped(ctx, c["valid"], rx + 22, y + 148, rw - 44, "Inter", 18, color=dl.INK_SEC, line_mult=1.34)

        dl.rounded_rect(ctx, rx, y + 258, rw, 158, r=12, fill=dl.RED_SOFT, stroke="#FCA5A5", stroke_w=1.8)
        dl.draw_cross_icon(ctx, rx + 28, y + 288, r=12, bg=dl.RED)
        dl.draw_text(ctx, "Error común de principiante:", rx + 50, y + 277, "Inter", 18.5, bold=True, color=dl.RED)
        dl.draw_wrapped(ctx, c["err"], rx + 22, y + 314, rw - 44, "Inter", 18, color=dl.INK_SEC, line_mult=1.34)

    # 6th Card: Golden Rules of RAM
    x6, y6 = xs[1], ys[2]
    dl.rounded_rect(ctx, x6, y6, cw, ch, r=16, fill=dl.AMBER_SOFT, stroke=dl.AMBER, stroke_w=2.4, shadow=True)
    dl.rounded_rect(ctx, x6, y6, cw, 64, r=16, fill=dl.AMBER_FILL)
    dl.set_color(ctx, dl.AMBER_FILL)
    ctx.rectangle(x6 + 2, y6 + 48, cw - 4, 16)
    ctx.fill()
    dl.set_color(ctx, dl.AMBER)
    ctx.set_line_width(2.0)
    ctx.move_to(x6, y6 + 64)
    ctx.line_to(x6 + cw, y6 + 64)
    ctx.stroke()

    dl.draw_warn_icon(ctx, x6 + 38, y6 + 32, r=14, bg=dl.AMBER)
    dl.draw_text(ctx, "3 Reglas de Oro de la Memoria RAM", x6 + 68, y6 + 32, "Inter", 22, bold=True, color=dl.NAVY, valign="middle")

    rules = [
        ("1. Sin inicializar = Basura:", "int x; deja [ ??? ] con basura aleatoria. ¡Siempre inicializa (int x = 0;) antes de leer o sumar!", "[ ??? ]", dl.RED),
        ("2. Sobrescritura:", "Si haces x = 10; y luego x = 25; el 10 se borra para siempre. Una caja solo guarda 1 valor a la vez.", "10  →  25", dl.BLUE),
        ("3. Constantes (const):", "const int MAX = 100; crea una caja con candado: su valor nunca puede cambiar durante la ejecución.", "MAX = 100", dl.TEAL),
    ]
    ry = y6 + 88
    for r_title, r_desc, box_txt, col in rules:
        dl.rounded_rect(ctx, x6 + 24, ry, cw - 48, 102, r=12, fill=dl.WHITE, stroke=dl.BORDER, stroke_w=1.6)
        dl.rounded_rect(ctx, x6 + 40, ry + 18, 165, 66, r=10, fill=dl.PANEL_BG, stroke=col, stroke_w=2.4)
        dl.draw_text(ctx, box_txt, x6 + 122.5, ry + 51, "DejaVu Sans Mono", 19, bold=True, color=col, align="center", valign="middle")
        dl.draw_text(ctx, r_title, x6 + 228, ry + 16, "Inter", 18.5, bold=True, color=dl.NAVY)
        dl.draw_wrapped(ctx, r_desc, x6 + 228, ry + 46, cw - 290, "Inter", 17.5, color=dl.INK_SEC, line_mult=1.28)
        ry += 114

    dl.draw_footer(ctx, W, H, "Curso de Algoritmos y Programación (30h) · Fundamentos de Variables y Tipos de Datos", badge="mem_01_variables_ram.png")
    dl.save_png(surf, os.path.join(OUT_DIR, "mem_01_variables_ram.png"))


def make_mem_02():
    W, H = 2400, 1820
    surf, ctx = dl.new_canvas(W, H)
    dl.draw_header(
        ctx,
        W,
        "Puente Comparativo de Ciclos: while vs do-while vs for",
        "Guía visual de elección y advertencia crítica sobre la condición invertida entre PSeInt y C++",
        badge="MÓDULO M05 · PUENTE CICLOS",
        accent=dl.ORANGE,
    )

    cols = [
        {
            "title": "while  /  Mientras",
            "badge": "0 o más repeticiones",
            "sub": "Primero pregunta, luego actúa",
            "color": dl.TEAL,
            "fill": dl.TEAL_SOFT,
            "when": "No sabes cuántas veces repetirá: depende de un centinela (ej: 0 para salir) o una condición previa.",
            "ps": ["Mientras x <> 0 Hacer", "  suma <- suma + x;", "  Leer x;", "FinMientras"],
            "cpp": ["while (x != 0) {", "  suma += x;", "  cin >> x;", "}"],
            "kind": "while",
        },
        {
            "title": "do-while  /  Repetir",
            "badge": "Al menos 1 repetición",
            "sub": "Primero actúa, al final pregunta",
            "color": dl.ORANGE,
            "fill": dl.ORANGE_SOFT,
            "when": "Menús interactivos y validación de datos donde el bloque debe ejecutarse mínimo 1 vez antes de comprobar.",
            "ps": ["Repetir", "  Leer nota;", "Hasta Que nota>=0 Y nota<=5"],
            "cpp": ["do {", "  cin >> nota;", "} while (nota<0 || nota>5);"],
            "kind": "dowhile",
        },
        {
            "title": "for  /  Para",
            "badge": "N repeticiones conocidas",
            "sub": "Contador automático en 1 línea",
            "color": dl.PURPLE,
            "fill": dl.PURPLE_SOFT,
            "when": "Sabes exactamente cuántas veces iterar (inicio, límite, paso): sumas de 1..N, tablas y recorrer vectores/matrices.",
            "ps": ["Para i <- 0 Hasta n-1 Con Paso 1", "  Escribir v[i];", "FinPara"],
            "cpp": ["for (int i = 0; i < n; i++) {", "  cout << v[i];", "}"],
            "kind": "for",
        },
    ]

    cw = 746
    gap = 41
    top_y = 174
    top_h = 885

    for idx, c in enumerate(cols):
        x = 40 + idx * (cw + gap)
        accent = c["color"]
        dl.rounded_rect(ctx, x, top_y, cw, top_h, r=16, fill=dl.WHITE, stroke=accent, stroke_w=2.5, shadow=True)
        dl.rounded_rect(ctx, x, top_y, cw, 96, r=16, fill=c["fill"])
        dl.set_color(ctx, c["fill"])
        ctx.rectangle(x + 2, top_y + 76, cw - 4, 20)
        ctx.fill()
        dl.set_color(ctx, accent)
        ctx.set_line_width(2.0)
        ctx.move_to(x, top_y + 96)
        ctx.line_to(x + cw, top_y + 96)
        ctx.stroke()

        dl.draw_text(ctx, c["title"], x + cw / 2, top_y + 26, "DejaVu Sans Mono", 23, bold=True, color=accent, align="center")
        dl.draw_pill(ctx, x + cw / 2, top_y + 70, c["badge"], bg=accent, fg=dl.WHITE, font_size=15.5, pad_x=14, pad_y=4)

        dl.draw_text(ctx, c["sub"], x + cw / 2, top_y + 118, "Inter", 19, bold=True, color=dl.NAVY, align="center")

        # Mini flowchart diagram box inside each column
        fx, fy, fw, fh = x + 30, top_y + 154, cw - 60, 232
        dl.rounded_rect(ctx, fx, fy, fw, fh, r=12, fill=dl.PANEL_BG, stroke=dl.BORDER, stroke_w=1.6)
        mcx = fx + fw / 2 - 20

        if c["kind"] == "while":
            dl.draw_arrow(ctx, [(mcx, fy + 10), (mcx, fy + 26)], color=dl.NAVY, width=2.6, head_len=9, head_w=6)
            dl.dfd_decision(ctx, mcx, fy + 64, 190, 72, "¿Condición?", font_size=16, fill=dl.TEAL_FILL, stroke=dl.TEAL, shadow=False)
            dl.draw_arrow(ctx, [(mcx, fy + 100), (mcx, fy + 144)], color=dl.GREEN, width=2.6, head_len=9, head_w=6)
            dl.draw_pill(ctx, mcx + 34, fy + 120, "V", bg=dl.GREEN, fg=dl.WHITE, font_size=13, pad_x=7, pad_y=2)
            dl.dfd_process(ctx, mcx, fy + 174, 180, 52, "Cuerpo", font_size=16, mono=False, fill=dl.WHITE, stroke=dl.NAVY, shadow=False)
            dl.draw_arrow(ctx, [(mcx - 90, fy + 174), (mcx - 160, fy + 174), (mcx - 160, fy + 22), (mcx - 6, fy + 22)], color=dl.TEAL, width=2.6, head_len=9, head_w=6)
            dl.draw_arrow(ctx, [(mcx + 95, fy + 64), (mcx + 185, fy + 64)], color=dl.RED, width=2.6, head_len=9, head_w=6)
            dl.draw_pill(ctx, mcx + 135, fy + 42, "F (Sale)", bg=dl.RED, fg=dl.WHITE, font_size=13, pad_x=8, pad_y=2)

        elif c["kind"] == "dowhile":
            dl.draw_arrow(ctx, [(mcx, fy + 10), (mcx, fy + 28)], color=dl.NAVY, width=2.6, head_len=9, head_w=6)
            dl.dfd_process(ctx, mcx, fy + 58, 190, 52, "Cuerpo (1ra vez)", font_size=15.5, mono=False, fill=dl.WHITE, stroke=dl.NAVY, shadow=False)
            dl.draw_arrow(ctx, [(mcx, fy + 84), (mcx, fy + 114)], color=dl.NAVY, width=2.6, head_len=9, head_w=6)
            dl.dfd_decision(ctx, mcx, fy + 154, 196, 76, "¿Condición?", font_size=16, fill=dl.ORANGE_FILL, stroke=dl.ORANGE, shadow=False)
            dl.draw_arrow(ctx, [(mcx - 98, fy + 154), (mcx - 165, fy + 154), (mcx - 165, fy + 20), (mcx - 6, fy + 20)], color=dl.ORANGE, width=2.6, head_len=9, head_w=6)
            dl.draw_pill(ctx, mcx - 165, fy + 88, "Repite", bg=dl.ORANGE, fg=dl.WHITE, font_size=12.5, pad_x=7, pad_y=2)
            dl.draw_arrow(ctx, [(mcx + 98, fy + 154), (mcx + 190, fy + 154)], color=dl.RED, width=2.6, head_len=9, head_w=6)
            dl.draw_pill(ctx, mcx + 145, fy + 130, "Sale", bg=dl.NAVY, fg=dl.WHITE, font_size=13, pad_x=8, pad_y=2)

        else:  # for
            dl.dfd_for_hex(ctx, mcx, fy + 56, 226, 62, "i <- ini .. fin", font_size=15.5, point=20, shadow=False)
            dl.draw_arrow(ctx, [(mcx, fy + 87), (mcx, fy + 126)], color=dl.PURPLE, width=2.6, head_len=9, head_w=6)
            dl.dfd_process(ctx, mcx, fy + 156, 180, 52, "Cuerpo", font_size=16, mono=False, fill=dl.WHITE, stroke=dl.PURPLE, shadow=False)
            dl.draw_arrow(ctx, [(mcx - 90, fy + 156), (mcx - 160, fy + 156), (mcx - 160, fy + 56), (mcx - 113, fy + 56)], color=dl.PURPLE, width=2.6, head_len=9, head_w=6)
            dl.draw_pill(ctx, mcx - 160, fy + 106, "i++", bg=dl.PURPLE, fg=dl.WHITE, font_size=13, pad_x=8, pad_y=2)
            dl.draw_arrow(ctx, [(mcx + 113, fy + 56), (mcx + 195, fy + 56)], color=dl.GREEN, width=2.6, head_len=9, head_w=6)
            dl.draw_pill(ctx, mcx + 155, fy + 34, "Sale", bg=dl.GREEN, fg=dl.WHITE, font_size=13, pad_x=8, pad_y=2)

        # When to use
        dl.draw_text(ctx, "¿Cuándo usarlo?", x + 30, top_y + 404, "Inter", 18, bold=True, color=dl.NAVY)
        dl.draw_wrapped(ctx, c["when"], x + 30, top_y + 434, cw - 60, "Inter", 17.5, color=dl.INK_SEC, line_mult=1.32)

        # PSeInt snippet
        dl.draw_text(ctx, "PSeInt", x + 30, top_y + 542, "Inter", 16.5, bold=True, color=dl.TEAL)
        dl.draw_code_box(ctx, x + 30, top_y + 568, cw - 60, c["ps"], font_size=15.0, pad_x=14, pad_y=10, bg=dl.TEAL_SOFT, border="#99F6E4", line_mult=1.32)

        # C++ snippet
        dl.draw_text(ctx, "C++ Básico", x + 30, top_y + 706, "Inter", 16.5, bold=True, color=dl.BLUE)
        dl.draw_code_box(ctx, x + 30, top_y + 732, cw - 60, c["cpp"], font_size=15.0, pad_x=14, pad_y=10, bg=dl.BLUE_SOFT, border="#BFDBFE", line_mult=1.32)

    # Bottom Band: THE FATAL TRAP
    by = 1090
    bh = 640
    dl.rounded_rect(ctx, 40, by, W - 80, bh, r=18, fill=dl.RED_SOFT, stroke=dl.RED, stroke_w=3.0, shadow=True)
    dl.rounded_rect(ctx, 40, by, W - 80, 68, r=18, fill=dl.RED)
    dl.set_color(ctx, dl.RED)
    ctx.rectangle(40, by + 48, W - 80, 20)
    ctx.fill()

    dl.draw_warn_icon(ctx, 84, by + 34, r=15, bg=dl.WHITE, fg=dl.RED)
    dl.draw_text(ctx, "¡TRAMPA MORTAL DE PARCIAL! Condición Invertida entre PSeInt y C++", 116, by + 34, "Inter", 24, bold=True, color=dl.WHITE, valign="middle")

    # Left comparison card: PSeInt Repetir...Hasta Que
    lx, ly, lw, lh = 76, by + 94, 980, 514
    dl.rounded_rect(ctx, lx, ly, lw, lh, r=14, fill=dl.WHITE, stroke=dl.TEAL, stroke_w=2.4)
    dl.draw_text(ctx, "PSeInt:  Repetir ... Hasta Que (cond)", lx + lw / 2, ly + 32, "DejaVu Sans Mono", 22, bold=True, color=dl.TEAL, align="center")
    dl.draw_pill(ctx, lx + lw / 2, ly + 86, "TERMINA cuando la condición es VERDADERA", bg=dl.TEAL, fg=dl.WHITE, font_size=18, pad_x=22, pad_y=8)
    dl.draw_text(ctx, "Mientras sea FALSA, el ciclo sigue repitiendo. (Regla: 'Repite HASTA lograr lo válido')", lx + lw / 2, ly + 136, "Inter", 17.5, bold=True, color=dl.INK_SEC, align="center")

    dl.draw_text(ctx, "Ejemplo: Validar una nota entre 0.0 y 5.0", lx + 30, ly + 180, "Inter", 18, bold=True, color=dl.NAVY)
    dl.draw_code_box(
        ctx,
        lx + 30,
        ly + 214,
        lw - 60,
        [
            "Repetir",
            '  Escribir "Ingrese nota (0 a 5):";',
            "  Leer nota;",
            "Hasta Que (nota >= 0 Y nota <= 5)",
        ],
        font_size=17.5,
        bg=dl.TEAL_SOFT,
        border="#99F6E4",
    )
    dl.rounded_rect(ctx, lx + 30, ly + 382, lw - 60, 106, r=10, fill=dl.GREEN_SOFT, stroke=dl.GREEN, stroke_w=1.8)
    dl.draw_wrapped(
        ctx,
        "• Si ingresas 4.2 → (4.2 >= 0 Y 4.2 <= 5) es VERDADERO → ¡SALE del ciclo!\n"
        "• Si ingresas 7.0 → es FALSO → Vuelve a pedir la nota.",
        lx + 50,
        ly + 402,
        lw - 100,
        "Inter",
        17.5,
        color=dl.INK,
        line_mult=1.35,
    )

    # Center VS / Inverted circle
    vcx, vcy = W / 2, ly + lh / 2
    dl.set_color(ctx, dl.RED)
    ctx.arc(vcx, vcy, 48, 0, 6.2832)
    ctx.fill()
    dl.set_color(ctx, dl.WHITE)
    ctx.set_line_width(4.0)
    ctx.arc(vcx, vcy, 48, 0, 6.2832)
    ctx.stroke()
    dl.draw_text(ctx, "≠", vcx, vcy - 2, "Inter", 46, bold=True, color=dl.WHITE, align="center", valign="middle")
    dl.draw_pill(ctx, vcx, vcy + 78, "¡CONDICIÓN\nOPUESTA!", bg=dl.NAVY, fg=dl.WHITE, font_size=15, pad_x=14, pad_y=6)

    # Right comparison card: C++ do...while
    rx = W - 76 - lw
    dl.rounded_rect(ctx, rx, ly, lw, lh, r=14, fill=dl.WHITE, stroke=dl.RED, stroke_w=2.4)
    dl.draw_text(ctx, "C++:  do { ... } while (cond);", rx + lw / 2, ly + 32, "DejaVu Sans Mono", 22, bold=True, color=dl.RED, align="center")
    dl.draw_pill(ctx, rx + lw / 2, ly + 86, "CONTINÚA mientras la condición es VERDADERA", bg=dl.RED, fg=dl.WHITE, font_size=18, pad_x=22, pad_y=8)
    dl.draw_text(ctx, "Termina cuando se vuelve FALSA. ¡OJO: lleva punto y coma (;) al final de while(...)!", rx + lw / 2, ly + 136, "Inter", 17.5, bold=True, color=dl.INK_SEC, align="center")

    dl.draw_text(ctx, "Ejemplo: Validar una nota entre 0.0 y 5.0", rx + 30, ly + 180, "Inter", 18, bold=True, color=dl.NAVY)
    dl.draw_code_box(
        ctx,
        rx + 30,
        ly + 214,
        lw - 60,
        [
            "do {",
            '  cout << "Ingrese nota (0 a 5): ";',
            "  cin >> nota;",
            "} while (nota < 0 || nota > 5);",
        ],
        font_size=17.5,
        bg=dl.RED_SOFT,
        border="#FCA5A5",
    )
    dl.rounded_rect(ctx, rx + 30, ly + 382, lw - 60, 106, r=10, fill=dl.ORANGE_SOFT, stroke=dl.ORANGE, stroke_w=1.8)
    dl.draw_wrapped(
        ctx,
        "• Si ingresas 7.0 → (7.0 < 0 || 7.0 > 5) es VERDADERO → ¡REPITE el ciclo!\n"
        "• Si ingresas 4.2 → es FALSO → Termina y continúa el programa.",
        rx + 50,
        ly + 402,
        lw - 100,
        "Inter",
        17.5,
        color=dl.INK,
        line_mult=1.35,
    )

    dl.draw_footer(ctx, W, H, "Curso de Algoritmos y Programación (30h) · Estructuras Repetitivas", badge="mem_02_puente_ciclos.png")
    dl.save_png(surf, os.path.join(OUT_DIR, "mem_02_puente_ciclos.png"))


def make_mem_03():
    W, H = 2400, 1560
    surf, ctx = dl.new_canvas(W, H)
    dl.draw_header(
        ctx,
        W,
        "Vector Estático 1D en Memoria RAM: int notas[8]",
        "Capacidad física fija (MAX = 8) y tamaño lógico (n = 5 usados) · Índices contiguos desde 0",
        badge="MÓDULO M06 · ARREGLO ESTÁTICO",
        accent=dl.RED,
    )

    # Top Declaration + Static Clarification Banner
    dl.rounded_rect(ctx, 44, 174, 1340, 84, r=12, fill=dl.BLUE_SOFT, stroke=dl.BLUE, stroke_w=2.0)
    dl.draw_text(
        ctx,
        "const int MAX = 8;   int notas[MAX] = {85, 92, 74, 60, 88};   int n = 5;",
        714,
        216,
        "DejaVu Sans Mono",
        21,
        bold=True,
        color=dl.NAVY,
        align="center",
        valign="middle",
    )

    dl.rounded_rect(ctx, 1408, 174, 948, 84, r=12, fill=dl.NAVY, stroke=dl.TEAL, stroke_w=2.4)
    dl.draw_text(
        ctx,
        "TAMAÑO DEFINIDO, NO DINÁMICO",
        1882,
        204,
        "Inter",
        21,
        bold=True,
        color=dl.TEAL_FILL,
        align="center",
        valign="middle",
    )
    dl.draw_text(
        ctx,
        "Los 8 casilleros se reservan fijos al iniciar el programa",
        1882,
        236,
        "Inter",
        16.5,
        color=dl.WHITE,
        align="center",
        valign="middle",
    )

    # Main RAM Tape Card
    dl.rounded_rect(ctx, 44, 286, W - 88, 690, r=16, fill=dl.PANEL_BG, stroke=dl.BORDER_DARK, stroke_w=2.0, shadow=True)
    dl.draw_text(ctx, "Mapa Contiguo en Memoria RAM (cada int ocupa 4 bytes consecutivos)", 80, 314, "Inter", 21, bold=True, color=dl.NAVY)

    # Cells 0..7 + Ghost 8
    x0 = 76
    cell_w = 200
    cell_h = 176
    cy = 440
    vals = ["85", "92", "74", "60", "88", "? basura", "? basura", "? basura"]
    addrs = ["0x200", "0x204", "0x208", "0x20C", "0x210", "0x214", "0x218", "0x21C"]

    for i in range(8):
        cx = x0 + i * cell_w
        used = i < 5
        fill = dl.BLUE_FILL if used else "#E2E8F0"
        stroke = dl.BLUE if used else dl.BORDER_DARK
        # Index header above cell
        dl.draw_text(ctx, f"notas[{i}]", cx + cell_w / 2, cy - 42, "DejaVu Sans Mono", 19, bold=True, color=dl.NAVY if used else dl.MUTED, align="center")
        dl.draw_text(ctx, f"índice {i}", cx + cell_w / 2, cy - 18, "Inter", 14.5, bold=used, color=dl.BLUE if used else dl.MUTED, align="center")

        # Cell rectangle
        if used:
            dl.rounded_rect(ctx, cx + 3, cy + 6, cell_w - 6, cell_h, r=10, fill=fill, stroke=stroke, stroke_w=3.0)
            dl.draw_text(ctx, vals[i], cx + cell_w / 2, cy + cell_h / 2 - 6, "DejaVu Sans Mono", 34, bold=True, color=dl.INK, align="center", valign="middle")
            dl.draw_pill(ctx, cx + cell_w / 2, cy + cell_h - 22, "USADO", bg=dl.GREEN, fg=dl.WHITE, font_size=13, pad_x=10, pad_y=3)
        else:
            dl.rounded_rect(ctx, cx + 3, cy + 6, cell_w - 6, cell_h, r=10, fill=fill, stroke=stroke, stroke_w=2.4, dashed=True)
            dl.draw_text(ctx, "???", cx + cell_w / 2, cy + cell_h / 2 - 22, "DejaVu Sans Mono", 28, bold=True, color=dl.MUTED, align="center", valign="middle")
            dl.draw_text(ctx, "basura RAM", cx + cell_w / 2, cy + cell_h / 2 + 16, "Inter", 15, color=dl.MUTED, align="center", valign="middle")
            dl.draw_pill(ctx, cx + cell_w / 2, cy + cell_h - 22, "LIBRE", bg=dl.BORDER_DARK, fg=dl.WHITE, font_size=13, pad_x=10, pad_y=3)

        # RAM address below cell
        dl.draw_text(ctx, addrs[i], cx + cell_w / 2, cy + cell_h + 26, "DejaVu Sans Mono", 15.5, color=dl.INK_SEC, align="center")

    # Ghost out-of-bounds cell [8]
    gx = x0 + 8 * cell_w + 56
    gw = 216
    dl.draw_text(ctx, "notas[8]", gx + gw / 2, cy - 42, "DejaVu Sans Mono", 19, bold=True, color=dl.RED, align="center")
    dl.draw_text(ctx, "¡NO EXISTE!", gx + gw / 2, cy - 18, "Inter", 15, bold=True, color=dl.RED, align="center")
    dl.rounded_rect(ctx, gx, cy + 6, gw, cell_h, r=10, fill=dl.RED_FILL, stroke=dl.RED, stroke_w=3.2, dashed=True)
    dl.draw_cross_icon(ctx, gx + gw / 2, cy + 56, r=18, bg=dl.RED)
    dl.draw_multiline_centered(ctx, "FUERA DE\nRANGO", gx + gw / 2, cy + 126, "Inter", 18, bold=True, color=dl.RED)

    dl.draw_text(ctx, "0x220 (ajeno)", gx + gw / 2, cy + cell_h + 26, "DejaVu Sans Mono", 15, bold=True, color=dl.RED, align="center")

    # Red callout box to the right of ghost cell
    rx_w = 350
    rx_x = gx + gw + 26
    dl.rounded_rect(ctx, rx_x, cy - 26, rx_w, 250, r=12, fill=dl.RED_SOFT, stroke=dl.RED, stroke_w=2.4)
    dl.draw_warn_icon(ctx, rx_x + 34, cy + 10, r=14, bg=dl.RED)
    dl.draw_text(ctx, "¡ERROR MORTAL!", rx_x + 58, cy - 4, "Inter", 19, bold=True, color=dl.RED)
    dl.draw_wrapped(
        ctx,
        "En C++, acceder a notas[8] (o notas[MAX]) NO da error de compilación, pero lee o corrompe memoria ajena (Comportamiento Indefinido / Crash).\n\nÚltimo índice válido: MAX - 1 = 7.",
        rx_x + 20,
        cy + 34,
        rx_w - 40,
        "Inter",
        16.5,
        color=dl.INK_SEC,
        line_mult=1.30,
    )

    # Dimension Bracket 1: Logical size n = 5 (0..4)
    b1_x1, b1_x2, b1_y = x0 + 8, x0 + 5 * cell_w - 8, 690
    dl.set_color(ctx, dl.TEAL)
    ctx.set_line_width(3.2)
    ctx.move_to(b1_x1, b1_y)
    ctx.line_to(b1_x1, b1_y + 22)
    ctx.line_to(b1_x2, b1_y + 22)
    ctx.line_to(b1_x2, b1_y)
    ctx.stroke()
    dl.draw_pill(
        ctx,
        (b1_x1 + b1_x2) / 2,
        b1_y + 52,
        "Tamaño lógico usado: n = 5  (índices 0 .. n - 1  →  for (int i = 0; i < n; i++))",
        bg=dl.TEAL,
        fg=dl.WHITE,
        font_size=17,
        pad_x=18,
        pad_y=6,
    )

    # Dimension Bracket 2: Physical capacity MAX = 8 (0..7)
    b2_x1, b2_x2, b2_y = x0 + 8, x0 + 8 * cell_w - 8, 800
    dl.set_color(ctx, dl.NAVY)
    ctx.set_line_width(3.2)
    ctx.move_to(b2_x1, b2_y)
    ctx.line_to(b2_x1, b2_y + 22)
    ctx.line_to(b2_x2, b2_y + 22)
    ctx.line_to(b2_x2, b2_y)
    ctx.stroke()
    dl.draw_pill(
        ctx,
        (b2_x1 + b2_x2) / 2,
        b2_y + 52,
        "Capacidad física fija definida: MAX = 8  (índices físicos posibles: 0 .. MAX - 1 = 7)",
        bg=dl.NAVY,
        fg=dl.WHITE,
        font_size=17,
        pad_x=18,
        pad_y=6,
    )

    # Bottom 2 comparison cards
    by = 1006
    bh = 468
    lw = 1136

    # Left card: PSeInt vs C++ indexing trap
    dl.rounded_rect(ctx, 44, by, lw, bh, r=16, fill=dl.WHITE, stroke=dl.ORANGE, stroke_w=2.4, shadow=True)
    dl.draw_warn_icon(ctx, 84, by + 40, r=14, bg=dl.ORANGE)
    dl.draw_text(ctx, "Trampa de Parcial: Índices en PSeInt vs C++", 114, by + 26, "Inter", 22, bold=True, color=dl.NAVY)
    dl.draw_wrapped(
        ctx,
        "• En PSeInt (por defecto), los arreglos empiezan en índice 1 hasta n.\n"
        "• En C++, los arreglos SIEMPRE empiezan en índice 0 hasta n - 1.",
        74,
        by + 74,
        lw - 60,
        "Inter",
        18.5,
        color=dl.INK_SEC,
        line_mult=1.35,
    )
    dl.draw_code_box(
        ctx,
        74,
        by + 168,
        lw - 60,
        [
            "// Acceso en C++ (base 0):",
            "notas[0]     // Primer elemento (85)",
            "notas[n - 1] // Último elemento usado (88)",
            "notas[n]     // ¡ERROR! Ahí hay basura (o fuera de rango si n==MAX)",
        ],
        font_size=16.5,
        bg=dl.ORANGE_SOFT,
        border="#FDBA74",
        line_mult=1.42,
    )
    dl.draw_text(ctx, "Tip: En PSeInt puedes activar 'Opcion Base 0' o ajustar índices al traducir a C++.", 74, by + 414, "Inter", 17.5, bold=True, color=dl.TEAL)

    # Right card: Static vs Prohibited Dynamic
    rx = 1220
    dl.rounded_rect(ctx, rx, by, lw, bh, r=16, fill=dl.WHITE, stroke=dl.NAVY, stroke_w=2.4, shadow=True)
    dl.draw_text(ctx, "¿Por qué Vector Estático y NO Dinámico?", rx + 30, by + 26, "Inter", 22, bold=True, color=dl.NAVY)

    dl.rounded_rect(ctx, rx + 30, by + 80, lw - 60, 165, r=12, fill=dl.GREEN_SOFT, stroke=dl.GREEN, stroke_w=2.0)
    dl.draw_check_icon(ctx, rx + 60, by + 112, r=13, bg=dl.GREEN)
    dl.draw_text(ctx, "ESTÁTICO (Correcto en el curso):", rx + 86, by + 98, "Inter", 19, bold=True, color=dl.GREEN)
    dl.draw_code_box(
        ctx,
        rx + 50,
        by + 136,
        lw - 100,
        [
            "const int MAX = 100;   // Capacidad fija en compilación",
            "int notas[MAX];",
            "do { cin >> n; } while (n < 1 || n > MAX);",
        ],
        font_size=15.5,
        bg=dl.WHITE,
        border="#86EFAC",
    )

    dl.rounded_rect(ctx, rx + 30, by + 266, lw - 60, 174, r=12, fill=dl.RED_SOFT, stroke=dl.RED, stroke_w=2.0)
    dl.draw_cross_icon(ctx, rx + 60, by + 298, r=13, bg=dl.RED)
    dl.draw_text(ctx, "PROHIBIDO en este curso (VLA / Memoria Dinámica):", rx + 86, by + 284, "Inter", 19, bold=True, color=dl.RED)
    dl.draw_wrapped(
        ctx,
        "• NO usar int notas[n]; con n variable (VLA no estándar en C++).\n"
        "• NO usar std::vector, new[], malloc ni punteros.\n"
        "• Si necesitas guardar hasta 100 datos, declaras MAX = 100 y validas n.",
        rx + 52,
        by + 324,
        lw - 104,
        "Inter",
        17.5,
        color=dl.INK_SEC,
        line_mult=1.35,
    )

    dl.draw_footer(ctx, W, H, "Curso de Algoritmos y Programación (30h) · Vectores Estáticos (Tamaño Definido)", badge="mem_03_vector_estatico_1d.png")
    dl.save_png(surf, os.path.join(OUT_DIR, "mem_03_vector_estatico_1d.png"))


def make_mem_04():
    W, H = 2400, 1660
    surf, ctx = dl.new_canvas(W, H)
    dl.draw_header(
        ctx,
        W,
        "Matriz Estática 2D en Memoria: int m[4][4]",
        "Coordenadas m[fila][columna] (0..n-1), fila i, columna j, diagonal principal y secundaria",
        badge="MÓDULO M07 · MATRICES ESTÁTICAS",
        accent=dl.TEAL,
    )

    # Left main grid container
    lx, ly, lw, lh = 44, 174, 1220, 1400
    dl.rounded_rect(ctx, lx, ly, lw, lh, r=16, fill=dl.PANEL_BG, stroke=dl.BORDER_DARK, stroke_w=2.0, shadow=True)

    # Code strip
    dl.rounded_rect(ctx, lx + 28, ly + 22, lw - 56, 62, r=10, fill=dl.WHITE, stroke=dl.NAVY, stroke_w=2.0)
    dl.draw_text(
        ctx,
        "const int N = 4;   int m[N][N];   // Tamaño fijo: 4 filas × 4 columnas",
        lx + lw / 2,
        ly + 53,
        "DejaVu Sans Mono",
        19,
        bold=True,
        color=dl.NAVY,
        align="center",
        valign="middle",
    )

    # Grid geometry
    n = 4
    cw, ch = 204, 176
    gx0 = lx + 210
    gy0 = ly + 190
    vals = [
        [12, 18, 25, 31],
        [40, 55, 62, 74],
        [81, 19, 33, 47],
        [90, 27, 64, 88],
    ]

    # Column labels across top
    dl.draw_text(ctx, "Columnas  (segundo índice j) →", gx0 + (n * cw) / 2, gy0 - 82, "Inter", 18, bold=True, color=dl.PURPLE, align="center")
    for j in range(n):
        col_c = dl.PURPLE if j == 2 else dl.NAVY
        dl.draw_pill(ctx, gx0 + j * cw + cw / 2, gy0 - 38, f"j = {j}", bg=dl.PURPLE_FILL if j == 2 else dl.NAVY_SOFT, fg=col_c, font_size=18, pad_x=18, pad_y=5, mono=True, border=col_c if j == 2 else None)

    # Row labels down left
    for i in range(n):
        row_c = dl.BLUE if i == 1 else dl.NAVY
        dl.draw_pill(ctx, gx0 - 68, gy0 + i * ch + ch / 2, f"i = {i}", bg=dl.BLUE_FILL if i == 1 else dl.NAVY_SOFT, fg=row_c, font_size=18, pad_x=16, pad_y=6, mono=True, border=row_c if i == 1 else None)

    dl.draw_text(ctx, "Filas (i)", gx0 - 68, gy0 - 38, "Inter", 17.5, bold=True, color=dl.BLUE, align="center", valign="middle")

    # Draw 4x4 cells
    for i in range(n):
        for j in range(n):
            cx = gx0 + j * cw
            cy = gy0 + i * ch
            is_diag_p = i == j
            is_diag_s = i + j == n - 1
            if is_diag_p:
                fill, stroke, sw = dl.TEAL_FILL, dl.TEAL, 3.2
            elif is_diag_s:
                fill, stroke, sw = dl.ORANGE_FILL, dl.ORANGE, 3.2
            else:
                fill, stroke, sw = dl.WHITE, dl.BORDER_DARK, 1.8

            dl.rounded_rect(ctx, cx + 6, cy + 6, cw - 12, ch - 12, r=10, fill=fill, stroke=stroke, stroke_w=sw)
            # Coordinate badge
            dl.draw_text(ctx, f"m[{i}][{j}]", cx + 18, cy + 16, "DejaVu Sans Mono", 16, bold=True, color=stroke if (is_diag_p or is_diag_s) else dl.MUTED)
            # Value
            dl.draw_text(ctx, str(vals[i][j]), cx + cw / 2, cy + ch / 2 + 6, "DejaVu Sans Mono", 34, bold=True, color=dl.INK, align="center", valign="middle")
            # Diagonal pill tag
            if is_diag_p:
                dl.draw_pill(ctx, cx + cw / 2, cy + ch - 24, "Diag. Principal", bg=dl.TEAL, fg=dl.WHITE, font_size=12.5, pad_x=10, pad_y=2)
            elif is_diag_s:
                dl.draw_pill(ctx, cx + cw / 2, cy + ch - 24, "Diag. Secundaria", bg=dl.ORANGE, fg=dl.WHITE, font_size=12.5, pad_x=10, pad_y=2)

    # Translucent outer highlights for Row i=1 (Blue) and Column j=2 (Purple)
    # Row i = 1 frame
    dl.rounded_rect(ctx, gx0 - 4, gy0 + 1 * ch - 4, n * cw + 8, ch + 8, r=14, fill=None, stroke=dl.BLUE, stroke_w=4.2, dashed=True)
    dl.draw_pill(ctx, gx0 + n * cw + 80, gy0 + 1 * ch + ch / 2, "FILA i = 1", bg=dl.BLUE, fg=dl.WHITE, font_size=15, pad_x=14, pad_y=6)
    dl.draw_arrow(ctx, [(gx0 + n * cw + 24, gy0 + 1 * ch + ch / 2), (gx0 + n * cw + 6, gy0 + 1 * ch + ch / 2)], color=dl.BLUE, width=3.0, head_len=10, head_w=7)

    # Column j = 2 frame
    dl.rounded_rect(ctx, gx0 + 2 * cw - 4, gy0 - 4, cw + 8, n * ch + 8, r=14, fill=None, stroke=dl.PURPLE, stroke_w=4.2, dashed=True)
    dl.draw_pill(ctx, gx0 + 2 * cw + cw / 2, gy0 + n * ch + 22, "COLUMNA j = 2", bg=dl.PURPLE, fg=dl.WHITE, font_size=15, pad_x=14, pad_y=5)

    # Bottom summary inside Left Container
    sum_y = gy0 + n * ch + 52
    dl.rounded_rect(ctx, lx + 28, sum_y, lw - 56, 390, r=14, fill=dl.WHITE, stroke=dl.BORDER, stroke_w=1.8)
    dl.draw_text(ctx, "Anatomía del Acceso y Regla Estática", lx + 54, sum_y + 24, "Inter", 20, bold=True, color=dl.NAVY)
    dl.draw_wrapped(
        ctx,
        "• Primer índice [i] = FILA (horizontal: arriba hacia abajo, de 0 a F - 1).\n"
        "• Segundo índice [j] = COLUMNA (vertical: izquierda a derecha, de 0 a C - 1).\n"
        "• En matrices rectangulares: const int MAX_F = 20, MAX_C = 20; int mat[MAX_F][MAX_C];\n"
        "• Recorrido completo estándar (por filas):",
        lx + 54,
        sum_y + 62,
        lw - 108,
        "Inter",
        18,
        color=dl.INK_SEC,
        line_mult=1.38,
    )
    dl.draw_code_box(
        ctx,
        lx + 54,
        sum_y + 230,
        lw - 108,
        [
            "for (int i = 0; i < F; i++) {          // Fija una fila i",
            "  for (int j = 0; j < C; j++) {        // Recorre todas sus columnas j",
            "    cout << m[i][j] << \" \";",
            "  }",
            "  cout << endl;",
            "}",
        ],
        font_size=15.5,
        bg=dl.NAVY_SOFT,
        border=dl.BORDER_DARK,
        line_mult=1.28,
    )

    # Right Section: 4 Pattern Cards with mini 4x4 grids
    rx = 1296
    rw = 1060
    card_h = 332
    patterns = [
        {
            "title": "1. Fila i fija (ej: Fila i = 1)",
            "color": dl.BLUE,
            "fill": dl.BLUE_FILL,
            "cond": lambda r, c: r == 1,
            "code": ["// Suma de la fila i:", "for (int j = 0; j < C; j++) {", "  suma += m[i][j];", "}"],
            "use": "Promedio de un estudiante o ventas de una tienda.",
        },
        {
            "title": "2. Columna j fija (ej: Columna j = 2)",
            "color": dl.PURPLE,
            "fill": dl.PURPLE_FILL,
            "cond": lambda r, c: c == 2,
            "code": ["// Suma de la columna j:", "for (int i = 0; i < F; i++) {", "  suma += m[i][j];", "}"],
            "use": "Promedio de una materia o total vendido en un mes.",
        },
        {
            "title": "3. Diagonal Principal (i == j)",
            "color": dl.TEAL,
            "fill": dl.TEAL_FILL,
            "cond": lambda r, c: r == c,
            "code": ["// Solo 1 ciclo (matriz cuadrada n×n):", "for (int i = 0; i < n; i++) {", "  suma += m[i][i]; // (0,0),(1,1),(2,2),(3,3)", "}"],
            "use": "Traza de una matriz o verificación de identidad.",
        },
        {
            "title": "4. Diagonal Secundaria (i + j == n - 1)",
            "color": dl.ORANGE,
            "fill": dl.ORANGE_FILL,
            "cond": lambda r, c: r + c == 3,
            "code": ["// Con n = 4, j = n - 1 - i:", "for (int i = 0; i < n; i++) {", "  suma += m[i][n - 1 - i]; // (0,3)..(3,0)", "}"],
            "use": "Suma inversa de esquinas; solo si filas == columnas.",
        },
    ]

    for idx, p in enumerate(patterns):
        cy = ly + idx * (card_h + 24)
        col = p["color"]
        dl.rounded_rect(ctx, rx, cy, rw, card_h, r=16, fill=dl.WHITE, stroke=col, stroke_w=2.4, shadow=True)
        # Left mini 4x4 thumbnail
        mx0, my0, ms = rx + 28, cy + 54, 56
        dl.draw_text(ctx, p["title"], rx + 28, cy + 16, "Inter", 20, bold=True, color=col)
        for r in range(4):
            for c in range(4):
                active = p["cond"](r, c)
                dl.rounded_rect(
                    ctx,
                    mx0 + c * ms + 2,
                    my0 + r * ms + 2,
                    ms - 4,
                    ms - 4,
                    r=5,
                    fill=p["fill"] if active else dl.PANEL_BG,
                    stroke=col if active else dl.BORDER,
                    stroke_w=2.2 if active else 1.2,
                )
                dl.draw_text(
                    ctx,
                    f"{r},{c}",
                    mx0 + c * ms + ms / 2,
                    my0 + r * ms + ms / 2,
                    "DejaVu Sans Mono",
                    13.5,
                    bold=active,
                    color=col if active else dl.MUTED,
                    align="center",
                    valign="middle",
                )

        # Right side code + use case
        cx_r = rx + 290
        cw_r = rw - 318
        dl.draw_code_box(ctx, cx_r, cy + 56, cw_r, p["code"], font_size=16, pad_x=14, pad_y=10, bg=dl.SUBTLE_BG, border=col, line_mult=1.35)
        dl.draw_text(ctx, f"Uso típico: {p['use']}", cx_r, cy + 258, "Inter", 17.5, bold=True, color=dl.INK_SEC)

    dl.draw_footer(ctx, W, H, "Curso de Algoritmos y Programación (30h) · Matrices Estáticas 2D", badge="mem_04_matriz_estatica_2d.png")
    dl.save_png(surf, os.path.join(OUT_DIR, "mem_04_matriz_estatica_2d.png"))


def make_met_01():
    W, H = 2300, 1940
    surf, ctx = dl.new_canvas(W, H)
    dl.draw_header(
        ctx,
        W,
        "Método de los 5 Pasos del Monitor para Analizar Problemas",
        "Flujograma anti-bloqueo: piensa y valida en papel ANTES de tocar el teclado",
        badge="MÓDULO M00 · METODOLOGÍA",
        accent=dl.GREEN,
    )

    steps = [
        {
            "num": "1",
            "title": "Leer y Subrayar Verbos / Datos",
            "color": dl.NAVY,
            "fill": dl.NAVY_SOFT,
            "desc": "Lee el enunciado completo 2 veces. Identifica los datos que te entregan (sustantivos/números) y las acciones o reglas que exigen (verbos y palabras clave).",
            "widget": "step1",
        },
        {
            "num": "2",
            "title": "Construir la Tabla EPS (Entradas – Proceso – Salidas)",
            "color": dl.BLUE,
            "fill": dl.BLUE_SOFT,
            "desc": "Separa con claridad qué necesita pedir el programa al usuario, qué fórmulas o validaciones transforma en memoria y qué resultado exacto debe mostrar.",
            "widget": "step2",
        },
        {
            "num": "3",
            "title": "Elegir las Estructuras de Control y Datos",
            "color": dl.TEAL,
            "fill": dl.TEAL_SOFT,
            "desc": "Traduce las palabras clave del enunciado a piezas algorítmicas antes de escribir código.",
            "widget": "step3",
        },
        {
            "num": "4",
            "title": "Prueba de Escritorio en Papel",
            "color": dl.ORANGE,
            "fill": dl.ORANGE_SOFT,
            "desc": "Simula paso a paso tu lógica con un ejemplo normal y casos límite (0, negativos, empates). Si funciona en papel, funcionará en código.",
            "widget": "step4",
        },
        {
            "num": "5",
            "title": "Traducir a DFD → PSeInt → C++",
            "color": dl.GREEN,
            "fill": dl.GREEN_SOFT,
            "desc": "Solo ahora pasa tu solución verificada a bloques visuales (DFD), pseudocódigo en español (PSeInt) y C++ compilado con g++, comprobando los mismos casos del Paso 4.",
            "widget": "step5",
        },
    ]

    sx = 56
    sw = W - 112
    step_h = 268
    gap = 46
    y_cur = 176

    for idx, st in enumerate(steps):
        col = st["color"]
        dl.rounded_rect(ctx, sx, y_cur, sw, step_h, r=16, fill=dl.WHITE, stroke=col, stroke_w=2.6, shadow=True)
        # Left colored number ribbon
        dl.rounded_rect(ctx, sx, y_cur, 118, step_h, r=16, fill=col)
        dl.set_color(ctx, col)
        ctx.rectangle(sx + 90, y_cur, 28, step_h)
        ctx.fill()
        # Circle badge inside ribbon
        dl.set_color(ctx, dl.WHITE, 0.2)
        ctx.arc(sx + 59, y_cur + step_h / 2, 38, 0, 6.2832)
        ctx.fill()
        dl.draw_text(ctx, st["num"], sx + 59, y_cur + step_h / 2 + 2, "Inter", 44, bold=True, color=dl.WHITE, align="center", valign="middle")

        # Title + description on middle-left
        tx = sx + 148
        tw_text = 860
        dl.draw_text(ctx, st["title"], tx, y_cur + 24, "Inter", 23, bold=True, color=col)
        dl.draw_wrapped(ctx, st["desc"], tx, y_cur + 64, tw_text, "Inter", 18.5, color=dl.INK_SEC, line_mult=1.35)

        # Right-side visual widget
        wx = tx + tw_text + 36
        ww = sx + sw - wx - 26
        wy = y_cur + 22
        wh = step_h - 44
        dl.rounded_rect(ctx, wx, wy, ww, wh, r=12, fill=st["fill"], stroke=col, stroke_w=1.8)

        if st["widget"] == "step1":
            dl.draw_text(ctx, "Ejemplo de lectura activa:", wx + 22, wy + 18, "Inter", 17, bold=True, color=dl.NAVY)
            dl.draw_wrapped(
                ctx,
                'Enunciado: "Leer precios hasta ingresar 0, sumar el total y contar cuántos superan $50."',
                wx + 22,
                wy + 48,
                ww - 44,
                "Inter",
                17.5,
                color=dl.INK,
            )
            dl.draw_pill(ctx, wx + 180, wy + 132, "hasta ingresar 0 → Centinela", bg=dl.TEAL, fg=dl.WHITE, font_size=14.5, pad_x=12, pad_y=5)
            dl.draw_pill(ctx, wx + 490, wy + 132, "sumar → Acumulador", bg=dl.BLUE, fg=dl.WHITE, font_size=14.5, pad_x=12, pad_y=5)
            dl.draw_pill(ctx, wx + 805, wy + 132, "superan $50 → Condición > 50", bg=dl.ORANGE, fg=dl.WHITE, font_size=14.5, pad_x=12, pad_y=5)
            dl.draw_text(ctx, "Regla: Cada verbo suele convertirse en una acción o estructura.", wx + 22, wy + 182, "Inter", 16.5, bold=True, color=dl.MUTED)

        elif st["widget"] == "step2":
            dl.draw_text(ctx, "Plantilla EPS (3 preguntas obligatorias):", wx + 22, wy + 16, "Inter", 17, bold=True, color=dl.BLUE)
            cw3 = (ww - 56) / 3
            eps_cols = [
                ("ENTRADAS", "¿Qué datos pide\nel teclado?", "precio (double)", dl.BLUE),
                ("PROCESO", "¿Qué calcula y\nvalida?", "total += precio\nsi >50 → cont++", dl.NAVY),
                ("SALIDAS", "¿Qué muestra al\nfinal?", "total, cont", dl.GREEN),
            ]
            for ci, (eh, eq, ex_t, ecol) in enumerate(eps_cols):
                ex0 = wx + 18 + ci * (cw3 + 10)
                dl.rounded_rect(ctx, ex0, wy + 52, cw3, 152, r=10, fill=dl.WHITE, stroke=ecol, stroke_w=1.8)
                dl.draw_text(ctx, eh, ex0 + cw3 / 2, wy + 68, "Inter", 16, bold=True, color=ecol, align="center")
                dl.draw_multiline_centered(ctx, eq, ex0 + cw3 / 2, wy + 108, "Inter", 15, color=dl.MUTED)
                dl.draw_multiline_centered(ctx, ex_t, ex0 + cw3 / 2, wy + 166, "DejaVu Sans Mono", 14.5, bold=True, color=dl.INK)

        elif st["widget"] == "step3":
            dl.draw_text(ctx, "Mapa de decisión rápida:", wx + 22, wy + 16, "Inter", 17, bold=True, color=dl.TEAL)
            chips = [
                ("¿Condición / Rango?", "Si / if-else / switch", dl.ORANGE),
                ("¿N veces fijas?", "Para / for", dl.PURPLE),
                ("¿Hasta centinela?", "Mientras / while", dl.TEAL),
                ("¿Menú / Validar ≥1 vez?", "Repetir / do-while", dl.RED),
                ("¿Lista de tamaño fijo?", "Vector v[MAX] o m[F][C]", dl.NAVY),
            ]
            # 2 rows of pills
            px_positions = [(wx + 195, wy + 82), (wx + 530, wy + 82), (wx + 860, wy + 82), (wx + 275, wy + 158), (wx + 715, wy + 158)]
            for (q, ans, c_col), (px, py) in zip(chips, px_positions):
                dl.rounded_rect(ctx, px - 150, py - 30, 300, 62, r=10, fill=dl.WHITE, stroke=c_col, stroke_w=1.8)
                dl.draw_text(ctx, q, px, py - 11, "Inter", 14.5, bold=True, color=dl.MUTED, align="center", valign="middle")
                dl.draw_text(ctx, ans, px, py + 14, "DejaVu Sans Mono", 15.5, bold=True, color=c_col, align="center", valign="middle")

        elif st["widget"] == "step4":
            dl.draw_text(ctx, "Mini Prueba de Escritorio (Entradas: 60, 30, 0):", wx + 22, wy + 16, "Inter", 17, bold=True, color=dl.ORANGE)
            tx0, ty0 = wx + 22, wy + 48
            cws4 = [140, 140, 140, 140, ww - 604]
            hdr4 = ["precio", "total", "cont", "> 50?", "Observación"]
            rows4 = [
                ["60", "0→60", "0→1", "Sí", "Suma y cuenta"],
                ["30", "60→90", "1", "No", "Solo suma"],
                ["0", "90", "1", "Fin", "Imprime 90 y 1"],
            ]
            dl.rounded_rect(ctx, tx0, ty0, sum(cws4), 38, r=6, fill=dl.NAVY)
            px = tx0
            for h, w in zip(hdr4, cws4):
                dl.draw_text(ctx, h, px + w / 2, ty0 + 19, "Inter", 15, bold=True, color=dl.WHITE, align="center", valign="middle")
                px += w
            for ri, r in enumerate(rows4):
                ry = ty0 + 38 + ri * 40
                dl.rounded_rect(ctx, tx0, ry, sum(cws4), 40, r=4, fill=dl.GREEN_SOFT if ri == 2 else dl.WHITE, stroke=dl.BORDER, stroke_w=1.0)
                px = tx0
                for ci, (v, w) in enumerate(zip(r, cws4)):
                    dl.draw_text(ctx, v, px + w / 2, ry + 20, "DejaVu Sans Mono" if ci < 4 else "Inter", 15, bold=(ri == 2), color=dl.INK, align="center", valign="middle")
                    px += w

        elif st["widget"] == "step5":
            dl.draw_text(ctx, "La escalera limpia de implementación:", wx + 22, wy + 18, "Inter", 17, bold=True, color=dl.GREEN)
            stages = [
                ("1. DFD", "Flujo visual\nsin sintaxis", dl.BLUE),
                ("2. PSeInt", "Pseudocódigo\nen español", dl.TEAL),
                ("3. C++ (g++)", "Compilar y probar\ncasos del Paso 4", dl.GREEN),
            ]
            bw5 = 270
            bx0 = wx + 26
            for si, (st_t, st_s, st_c) in enumerate(stages):
                bx = bx0 + si * (bw5 + 68)
                dl.rounded_rect(ctx, bx, wy + 60, bw5, 130, r=12, fill=dl.WHITE, stroke=st_c, stroke_w=2.4)
                dl.draw_text(ctx, st_t, bx + bw5 / 2, wy + 90, "Inter", 20, bold=True, color=st_c, align="center", valign="middle")
                dl.draw_multiline_centered(ctx, st_s, bx + bw5 / 2, wy + 144, "Inter", 16.5, color=dl.INK_SEC)
                if si < 2:
                    dl.draw_arrow(ctx, [(bx + bw5 + 8, wy + 125), (bx + bw5 + 60, wy + 125)], color=dl.NAVY, width=4.0, head_len=14, head_w=10)

        # Flow arrow between steps
        if idx < len(steps) - 1:
            dl.draw_arrow(ctx, [(W / 2, y_cur + step_h + 4), (W / 2, y_cur + step_h + gap - 4)], color=dl.NAVY, width=4.5, head_len=15, head_w=11)

        y_cur += step_h + gap

    # Bottom Alert Rule
    ay = 1758
    dl.rounded_rect(ctx, 56, ay, W - 112, 92, r=14, fill=dl.RED_SOFT, stroke=dl.RED, stroke_w=2.6)
    dl.draw_warn_icon(ctx, 102, ay + 46, r=17, bg=dl.RED)
    dl.draw_text(
        ctx,
        "Error #1 del Principiante: Empezar a escribir #include <iostream> sin hacer los Pasos 1 al 4.",
        136,
        ay + 30,
        "Inter",
        21,
        bold=True,
        color=dl.RED,
        valign="middle",
    )
    dl.draw_text(
        ctx,
        "10 minutos de análisis y prueba de escritorio en papel ahorran 2 horas de errores y frustración en el compilador.",
        136,
        ay + 64,
        "Inter",
        18.5,
        color=dl.INK_SEC,
        valign="middle",
    )

    dl.draw_footer(ctx, W, H, "Curso de Algoritmos y Programación (30h) · Metodología de Análisis de Problemas", badge="met_01_cinco_pasos_analisis.png")
    dl.save_png(surf, os.path.join(OUT_DIR, "met_01_cinco_pasos_analisis.png"))


if __name__ == "__main__":
    make_mem_01()
    make_mem_02()
    make_mem_03()
    make_mem_04()
    make_met_01()
    print("Generated mem_01..mem_04 and met_01 successfully.")
