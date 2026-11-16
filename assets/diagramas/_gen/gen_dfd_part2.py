#!/usr/bin/env python3
"""Generates dfd_03_ciclo_mientras_centinela.png, dfd_04_ciclo_para_factorial.png, dfd_05_vector_estatico_busqueda.png."""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import draw_lib as dl

OUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def make_dfd_03():
    W, H = 2280, 1880
    surf, ctx = dl.new_canvas(W, H)
    dl.draw_header(
        ctx,
        W,
        "DFD Ciclo Mientras con Centinela: Sumar Compras",
        "Control por valor centinela (0 para terminar), contando artículos válidos y rechazando precios negativos",
        badge="MÓDULO M05 · CENTINELA",
        accent=dl.TEAL,
    )

    # Left main DFD container
    dl.rounded_rect(ctx, 44, 174, 1420, 1626, r=16, fill=dl.PANEL_BG, stroke=dl.BORDER, stroke_w=2.0)
    dl.draw_text(ctx, "Diagrama de Flujo (Mientras + Validación)", 754, 202, "Inter", 22, bold=True, color=dl.NAVY, align="center")

    cx = 790
    y_ini = 276
    y_init = 398
    y_read1 = 528
    y_join = 612
    y_cond1 = 720
    y_cond2 = 915
    y_body = 1090
    y_bus = 1200
    y_read2 = 1300
    y_out = 1545
    y_fin = 1715

    dl.dfd_start_end(ctx, cx, y_ini, 220, 66, "Inicio", font_size=23)
    dl.dfd_process(ctx, cx, y_init, 290, 84, "total <- 0\ncant <- 0", font_size=21, fill=dl.WHITE)
    dl.dfd_input(ctx, cx, y_read1, 300, 76, "Leer precio", font_size=21)

    # Callout badge for priming read
    dl.draw_pill(ctx, 1140, y_read1, "Lectura adelantada (0 = fin)", bg=dl.BLUE_FILL, fg=dl.BLUE, font_size=16, pad_x=14, pad_y=6, border=dl.BLUE)
    dl.set_color(ctx, dl.BLUE)
    ctx.set_line_width(2.0)
    ctx.set_dash([5, 4])
    ctx.move_to(cx + 150, y_read1)
    ctx.line_to(990, y_read1)
    ctx.stroke()
    ctx.set_dash([])

    dl.draw_arrow(ctx, [(cx, y_ini + 33), (cx, y_init - 42)], color=dl.NAVY, width=3.4)
    dl.draw_arrow(ctx, [(cx, y_init + 42), (cx, y_read1 - 38)], color=dl.NAVY, width=3.4)
    dl.draw_arrow(ctx, [(cx, y_read1 + 38), (cx, y_cond1 - 66)], color=dl.NAVY, width=3.4)

    # Loop return junction dot
    dl.set_color(ctx, dl.TEAL)
    ctx.arc(cx, y_join, 6.5, 0, 6.2832)
    ctx.fill()

    # Decision 1: Mientras precio != 0
    dl.dfd_decision(ctx, cx, y_cond1, 300, 132, "¿precio != 0?", font_size=22, fill=dl.TEAL_FILL, stroke=dl.TEAL)

    # Sí branch (down into loop body) -> inner validation
    dl.draw_arrow(ctx, [(cx, y_cond1 + 66), (cx, y_cond2 - 62)], color=dl.GREEN, width=3.4)
    dl.draw_pill(ctx, cx + 48, (y_cond1 + 66 + y_cond2 - 62) / 2, "Sí", bg=dl.GREEN, fg=dl.WHITE, font_size=17, pad_x=12, pad_y=4)

    dl.dfd_decision(ctx, cx, y_cond2, 280, 124, "¿precio < 0?", font_size=21, fill=dl.ORANGE_FILL, stroke=dl.ORANGE)

    lx = 475
    rx = 1090
    dl.dfd_output(ctx, lx, y_body, 360, 88, 'Escribir "Error:\nprecio negativo"', font_size=18, fill=dl.RED_FILL, stroke=dl.RED)
    dl.dfd_process(ctx, rx, y_body, 340, 92, "total <- total + precio\ncant <- cant + 1", font_size=19, fill=dl.WHITE, stroke=dl.NAVY)

    # Arrows inner decision -> branches
    dl.draw_arrow(ctx, [(cx - 140, y_cond2), (lx, y_cond2), (lx, y_body - 44)], color=dl.RED, width=3.2)
    dl.draw_pill(ctx, lx + 78, y_cond2, "Sí (Inválido)", bg=dl.RED, fg=dl.WHITE, font_size=15, pad_x=11, pad_y=4)

    dl.draw_arrow(ctx, [(cx + 140, y_cond2), (rx, y_cond2), (rx, y_body - 46)], color=dl.GREEN, width=3.2)
    dl.draw_pill(ctx, rx - 78, y_cond2, "No (Válido)", bg=dl.GREEN, fg=dl.WHITE, font_size=15, pad_x=11, pad_y=4)

    # Merge inner branches at y_bus -> Leer precio (actualización)
    dl.set_color(ctx, dl.NAVY)
    ctx.set_line_width(3.2)
    ctx.move_to(lx, y_body + 36)
    ctx.line_to(lx, y_bus)
    ctx.line_to(rx, y_bus)
    ctx.line_to(rx, y_body + 46)
    ctx.stroke()
    ctx.arc(cx, y_bus, 6.0, 0, 6.2832)
    ctx.fill()

    dl.draw_arrow(ctx, [(cx, y_bus), (cx, y_read2 - 38)], color=dl.NAVY, width=3.4)
    dl.dfd_input(ctx, cx, y_read2, 300, 76, "Leer precio", font_size=21)

    dl.draw_pill(ctx, 1140, y_read2, "Lectura de actualización", bg=dl.BLUE_FILL, fg=dl.BLUE, font_size=16, pad_x=14, pad_y=6, border=dl.BLUE)
    dl.set_color(ctx, dl.BLUE)
    ctx.set_line_width(2.0)
    ctx.set_dash([5, 4])
    ctx.move_to(cx + 150, y_read2)
    ctx.line_to(1002, y_read2)
    ctx.stroke()
    ctx.set_dash([])

    # Return loop on left side (x = 185)
    x_ret = 185
    dl.draw_arrow(ctx, [(cx, y_read2 + 38), (cx, y_read2 + 78), (x_ret, y_read2 + 78), (x_ret, y_join), (cx - 10, y_join)], color=dl.TEAL, width=3.8)
    dl.draw_pill(ctx, x_ret, 975, "Volver a\nevaluar\nMientras", bg=dl.TEAL, fg=dl.WHITE, font_size=15, pad_x=12, pad_y=8)

    # No exit branch on far right (x = 1380)
    x_exit = 1380
    dl.draw_arrow(ctx, [(cx + 150, y_cond1), (x_exit, y_cond1), (x_exit, 1445), (cx, 1445), (cx, y_out - 50)], color=dl.RED, width=3.6)
    dl.draw_pill(ctx, 1185, y_cond1, "No (Centinela = 0)", bg=dl.RED, fg=dl.WHITE, font_size=16, pad_x=14, pad_y=5)

    dl.dfd_output(ctx, cx, y_out, 590, 100, 'Escribir "Artículos: ", cant,\n" | Total: $", total', font_size=20)
    dl.draw_arrow(ctx, [(cx, y_out + 42), (cx, y_fin - 33)], color=dl.NAVY, width=3.4)
    dl.dfd_start_end(ctx, cx, y_fin, 220, 66, "Fin", font_size=23)

    # Right column: Rules + Trace + C++
    rx0 = 1496
    rw = 740

    # Card 1: Why sentinel?
    dl.rounded_rect(ctx, rx0, 174, rw, 286, r=16, fill=dl.WHITE, stroke=dl.BORDER_DARK, stroke_w=2.0, shadow=True)
    dl.draw_text(ctx, "1. Anatomía del Ciclo con Centinela", rx0 + 26, 200, "Inter", 22, bold=True, color=dl.NAVY)
    dl.draw_wrapped(
        ctx,
        "• Un centinela es un valor especial (aquí 0) que indica 'no hay más datos' y NO debe sumarse ni contarse.\n"
        "• Como no sabemos cuántos productos comprará el usuario (pueden ser 0, 3 o 50), usamos Mientras (while).\n"
        "• Regla obligatoria: lee una vez ANTES de entrar y otra vez al FINAL del ciclo.",
        rx0 + 26,
        244,
        rw - 52,
        "Inter",
        18.0,
        color=dl.INK_SEC,
        line_mult=1.36,
    )

    # Card 2: Trace table
    dl.rounded_rect(ctx, rx0, 488, rw, 610, r=16, fill=dl.WHITE, stroke=dl.BORDER_DARK, stroke_w=2.0, shadow=True)
    dl.draw_text(ctx, "2. Prueba de Escritorio (Entradas: 50, -10, 25, 0)", rx0 + 26, 514, "Inter", 21, bold=True, color=dl.NAVY)

    tx0, ty0 = rx0 + 24, 562
    cws = [108, 128, 95, 95, 266]
    hdrs = ["precio", "!= 0?", "cant", "total", "Acción / Pantalla"]
    rows_tr = [
        ["50", "Sí", "0→1", "0→50", "Válido: suma y cuenta"],
        ["-10", "Sí", "1", "50", "¡Negativo! Error (no suma)"],
        ["25", "Sí", "1→2", "50→75", "Válido: suma y cuenta"],
        ["0", "No", "2", "75", "Sale → Art: 2 | Total: $75"],
    ]
    dl.rounded_rect(ctx, tx0, ty0, sum(cws), 46, r=8, fill=dl.NAVY)
    px = tx0
    for h, w in zip(hdrs, cws):
        dl.draw_text(ctx, h, px + w / 2, ty0 + 23, "Inter", 16, bold=True, color=dl.WHITE, align="center", valign="middle")
        px += w
    for idx, r in enumerate(rows_tr):
        ry = ty0 + 46 + idx * 62
        bg_r = dl.RED_SOFT if idx == 1 else (dl.GREEN_SOFT if idx == 3 else (dl.PANEL_BG if idx % 2 else dl.WHITE))
        dl.rounded_rect(ctx, tx0, ry, sum(cws), 62, r=4, fill=bg_r, stroke=dl.BORDER, stroke_w=1.2)
        px = tx0
        for ci, (val, w) in enumerate(zip(r, cws)):
            fam = "Inter" if ci == 4 else "DejaVu Sans Mono"
            col = dl.RED if (idx == 1 and ci in (0, 4)) else (dl.GREEN if (idx == 3 and ci == 4) else dl.INK)
            dl.draw_text(ctx, val, px + w / 2, ry + 31, fam, 15.5, bold=(ci == 0 or idx == 3), color=col, align="center", valign="middle")
            px += w

    dl.rounded_rect(ctx, rx0 + 24, 882, rw - 48, 190, r=12, fill=dl.ORANGE_SOFT, stroke=dl.ORANGE, stroke_w=2.0)
    dl.draw_warn_icon(ctx, rx0 + 58, 922, r=13, bg=dl.ORANGE)
    dl.draw_text(ctx, "¿Qué pasa si el usuario ingresa 0 de inmediato?", rx0 + 84, 908, "Inter", 18.5, bold=True, color=dl.ORANGE)
    dl.draw_wrapped(
        ctx,
        "Como Mientras evalúa ANTES de entrar, 0 != 0 es Falso a la primera. No entra al ciclo, no falla y muestra correctamente: Artículos: 0 | Total: $0.",
        rx0 + 84,
        942,
        rw - 128,
        "Inter",
        17.5,
        color=dl.INK_SEC,
        line_mult=1.35,
    )

    # Card 3: Code C++
    dl.rounded_rect(ctx, rx0, 1126, rw, 674, r=16, fill=dl.WHITE, stroke=dl.BORDER_DARK, stroke_w=2.0, shadow=True)
    dl.draw_text(ctx, "3. Traducción directa a C++ Básico", rx0 + 26, 1152, "Inter", 22, bold=True, color=dl.NAVY)
    dl.draw_code_box(
        ctx,
        rx0 + 26,
        1198,
        rw - 52,
        [
            "double precio, total = 0;",
            "int cant = 0;",
            "",
            "cout << \"Precio (0 para terminar): \";",
            "cin >> precio;               // Lectura adelantada",
            "",
            "while (precio != 0) {",
            "  if (precio < 0) {",
            "    cout << \"Error: precio negativo\\n\";",
            "  } else {",
            "    total += precio;",
            "    cant++;",
            "  }",
            "  cout << \"Siguiente precio (0 fin): \";",
            "  cin >> precio;             // Actualización",
            "}",
            "cout << \"Artículos: \" << cant",
            "     << \" | Total: $\" << total << endl;",
        ],
        font_size=16.5,
        bg=dl.BLUE_SOFT,
        border="#BFDBFE",
        line_mult=1.38,
    )

    dl.draw_footer(ctx, W, H, "Curso de Algoritmos y Programación (30h) · Ciclo Mientras con Centinela", badge="dfd_03_ciclo_mientras_centinela.png")
    dl.save_png(surf, os.path.join(OUT_DIR, "dfd_03_ciclo_mientras_centinela.png"))


def make_dfd_04():
    W, H = 2240, 1740
    surf, ctx = dl.new_canvas(W, H)
    dl.draw_header(
        ctx,
        W,
        "DFD Ciclo Para: Factorial de un Número N (N!)",
        "Uso del hexágono Para (contador de 1 hasta N) con validación de negativos y acumulador multiplicativo",
        badge="MÓDULO M05 · CICLO PARA",
        accent=dl.PURPLE,
    )

    # Left DFD panel
    dl.rounded_rect(ctx, 44, 174, 1340, 1488, r=16, fill=dl.PANEL_BG, stroke=dl.BORDER, stroke_w=2.0)
    dl.draw_text(ctx, "Diagrama de Flujo (Hexágono Para)", 714, 202, "Inter", 22, bold=True, color=dl.NAVY, align="center")

    cx = 720
    y_ini = 276
    y_read = 392
    y_val = 540

    dl.dfd_start_end(ctx, cx, y_ini, 220, 66, "Inicio", font_size=23)
    dl.dfd_input(ctx, cx, y_read, 280, 76, "Leer N", font_size=22)
    dl.dfd_decision(ctx, cx, y_val, 260, 122, "¿N < 0?", font_size=22)

    dl.draw_arrow(ctx, [(cx, y_ini + 33), (cx, y_read - 38)], color=dl.NAVY, width=3.4)
    dl.draw_arrow(ctx, [(cx, y_read + 38), (cx, y_val - 61)], color=dl.NAVY, width=3.4)

    # Left branch (N < 0 -> Error)
    lx = 315
    y_err = 720
    dl.dfd_output(ctx, lx, y_err, 370, 92, 'Escribir "Error:\nN debe ser >= 0"', font_size=18.5, fill=dl.RED_FILL, stroke=dl.RED)
    dl.draw_arrow(ctx, [(cx - 130, y_val), (lx, y_val), (lx, y_err - 46)], color=dl.RED, width=3.4)
    dl.draw_pill(ctx, lx + 125, y_val, "Sí", bg=dl.RED, fg=dl.WHITE, font_size=17, pad_x=13, pad_y=5)

    # Right branch (N >= 0 -> Para loop)
    rx = 955
    y_fact = 700
    y_hex = 865
    y_body = 1045
    y_out = 1280
    y_bus = 1415
    y_fin = 1550

    dl.dfd_process(ctx, rx, y_fact, 260, 78, "fact <- 1", font_size=22, fill=dl.WHITE)
    dl.draw_arrow(ctx, [(cx + 130, y_val), (rx, y_val), (rx, y_fact - 39)], color=dl.GREEN, width=3.4)
    dl.draw_pill(ctx, (cx + 130 + rx) / 2, y_val, "No", bg=dl.GREEN, fg=dl.WHITE, font_size=17, pad_x=13, pad_y=5)

    dl.draw_arrow(ctx, [(rx, y_fact + 39), (rx, y_hex - 46)], color=dl.NAVY, width=3.4)

    # Hexagon Para
    dl.dfd_for_hex(ctx, rx, y_hex, 390, 92, "Para i <- 1 hasta N\ncon paso +1", font_size=19.5, point=28)

    # Body inside Para
    dl.draw_arrow(ctx, [(rx, y_hex + 46), (rx, y_body - 41)], color=dl.PURPLE, width=3.5)
    dl.draw_pill(ctx, rx + 62, (y_hex + 46 + y_body - 41) / 2, "Repite", bg=dl.PURPLE, fg=dl.WHITE, font_size=15, pad_x=11, pad_y=4)
    dl.dfd_process(ctx, rx, y_body, 300, 82, "fact <- fact * i", font_size=21, fill=dl.WHITE, stroke=dl.PURPLE)

    # Loop back arrow from bottom of fact <- fact * i around left to hexagon
    x_loop_l = 665
    dl.draw_arrow(ctx, [(rx, y_body + 41), (rx, y_body + 85), (x_loop_l, y_body + 85), (x_loop_l, y_hex), (rx - 195, y_hex)], color=dl.PURPLE, width=3.5)
    dl.draw_pill(ctx, x_loop_l, 965, "Siguiente i", bg=dl.PURPLE, fg=dl.WHITE, font_size=15, pad_x=11, pad_y=5)

    # Exit right from hexagon when i > N
    x_exit_r = 1285
    dl.draw_arrow(ctx, [(rx + 195, y_hex), (x_exit_r, y_hex), (x_exit_r, 1185), (rx, 1185), (rx, y_out - 46)], color=dl.GREEN, width=3.5)
    dl.draw_pill(ctx, 1220, y_hex - 28, "Sale (i > N)", bg=dl.GREEN, fg=dl.WHITE, font_size=15, pad_x=11, pad_y=4)

    dl.dfd_output(ctx, rx, y_out, 380, 92, 'Escribir N, "! = ", fact', font_size=21)

    # Merge bus to Fin
    dl.set_color(ctx, dl.NAVY)
    ctx.set_line_width(3.4)
    ctx.move_to(lx, y_err + 39)
    ctx.line_to(lx, y_bus)
    ctx.line_to(rx, y_bus)
    ctx.line_to(rx, y_out + 39)
    ctx.stroke()

    x_fin = 640
    ctx.arc(x_fin, y_bus, 6.0, 0, 6.2832)
    ctx.fill()
    dl.draw_arrow(ctx, [(x_fin, y_bus), (x_fin, y_fin - 33)], color=dl.NAVY, width=3.4)
    dl.dfd_start_end(ctx, x_fin, y_fin, 220, 66, "Fin", font_size=23)

    # Right column
    rx0 = 1416
    rw = 780

    # Card 1: Trace table for N=4
    dl.rounded_rect(ctx, rx0, 174, rw, 500, r=16, fill=dl.WHITE, stroke=dl.BORDER_DARK, stroke_w=2.0, shadow=True)
    dl.draw_text(ctx, "1. Prueba de Escritorio (Ejemplo: N = 4)", rx0 + 26, 200, "Inter", 22, bold=True, color=dl.NAVY)
    tx0, ty0 = rx0 + 26, 248
    cws = [110, 130, 220, 268]
    hdrs = ["i", "i <= 4?", "fact (nuevo)", "Estado"]
    rows_f = [
        ["—", "Inicio", "1", "Neutro multiplicativo"],
        ["1", "Sí", "1 * 1 = 1", "Iteración 1"],
        ["2", "Sí", "1 * 2 = 2", "Iteración 2"],
        ["3", "Sí", "2 * 3 = 6", "Iteración 3"],
        ["4", "Sí", "6 * 4 = 24", "Iteración 4"],
        ["5", "No", "24", "Sale → Imprime: 4! = 24"],
    ]
    dl.rounded_rect(ctx, tx0, ty0, sum(cws), 46, r=8, fill=dl.NAVY)
    px = tx0
    for h, w in zip(hdrs, cws):
        dl.draw_text(ctx, h, px + w / 2, ty0 + 23, "Inter", 16.5, bold=True, color=dl.WHITE, align="center", valign="middle")
        px += w
    for idx, r in enumerate(rows_f):
        ry = ty0 + 46 + idx * 52
        bg_r = dl.GREEN_SOFT if idx == 5 else (dl.PANEL_BG if idx % 2 else dl.WHITE)
        dl.rounded_rect(ctx, tx0, ry, sum(cws), 52, r=4, fill=bg_r, stroke=dl.BORDER, stroke_w=1.2)
        px = tx0
        for ci, (val, w) in enumerate(zip(r, cws)):
            fam = "Inter" if ci == 3 else "DejaVu Sans Mono"
            col = dl.GREEN if (idx == 5 and ci in (2, 3)) else dl.INK
            dl.draw_text(ctx, val, px + w / 2, ry + 26, fam, 16, bold=(idx == 5 or ci == 2), color=col, align="center", valign="middle")
            px += w

    dl.draw_text(ctx, "Caso especial: Si N = 0, el ciclo da 0 vueltas y sale directo: 0! = 1 ✓", rx0 + 26, 628, "Inter", 17.5, bold=True, color=dl.TEAL)

    # Card 2: Multiplier trap
    dl.rounded_rect(ctx, rx0, 702, rw, 232, r=16, fill=dl.ORANGE_SOFT, stroke=dl.ORANGE, stroke_w=2.2, shadow=True)
    dl.draw_warn_icon(ctx, rx0 + 60, 744, r=14, bg=dl.ORANGE)
    dl.draw_text(ctx, "2. Trampa Clásica: ¿En cuánto inicia el acumulador?", rx0 + 90, 730, "Inter", 20.5, bold=True, color=dl.ORANGE)
    dl.draw_wrapped(
        ctx,
        "• Suma acumulada: inicia en 0 (ej: suma <- 0) porque x + 0 = x.\n"
        "• Multiplicación / Factorial: SIEMPRE inicia en 1 (fact <- 1) porque x * 1 = x. ¡Si pones fact <- 0, todo producto dará 0!\n"
        "• En C++ usa long long para evitar desbordamiento desde N = 13.",
        rx0 + 30,
        776,
        rw - 60,
        "Inter",
        18.0,
        color=dl.INK_SEC,
        line_mult=1.38,
    )

    # Card 3: PSeInt & C++
    dl.rounded_rect(ctx, rx0, 962, rw, 700, r=16, fill=dl.WHITE, stroke=dl.BORDER_DARK, stroke_w=2.0, shadow=True)
    dl.draw_text(ctx, "3. Equivalencia PSeInt y C++", rx0 + 26, 988, "Inter", 22, bold=True, color=dl.NAVY)
    dl.draw_text(ctx, "PSeInt", rx0 + 26, 1034, "Inter", 17.5, bold=True, color=dl.TEAL)
    dl.draw_code_box(
        ctx,
        rx0 + 26,
        1064,
        rw - 52,
        [
            "Leer N;",
            "Si N < 0 Entonces",
            "  Escribir \"Error: N debe ser >= 0\";",
            "SiNo",
            "  fact <- 1;",
            "  Para i <- 1 Hasta N Con Paso 1 Hacer",
            "    fact <- fact * i;",
            "  FinPara",
            "  Escribir N, \"! = \", fact;",
            "FinSi",
        ],
        font_size=15.5,
        bg=dl.TEAL_SOFT,
        border="#99F6E4",
        line_mult=1.32,
    )
    dl.draw_text(ctx, "C++ Básico", rx0 + 26, 1344, "Inter", 17.5, bold=True, color=dl.BLUE)
    dl.draw_code_box(
        ctx,
        rx0 + 26,
        1374,
        rw - 52,
        [
            "int N; long long fact = 1;",
            "cin >> N;",
            "if (N < 0) cout << \"Error: N debe ser >= 0\";",
            "else {",
            "  for (int i = 1; i <= N; i++) fact *= i;",
            "  cout << N << \"! = \" << fact;",
            "}",
        ],
        font_size=15.5,
        bg=dl.BLUE_SOFT,
        border="#BFDBFE",
        line_mult=1.35,
    )

    dl.draw_footer(ctx, W, H, "Curso de Algoritmos y Programación (30h) · Ciclo Para (Contador Definido)", badge="dfd_04_ciclo_para_factorial.png")
    dl.save_png(surf, os.path.join(OUT_DIR, "dfd_04_ciclo_para_factorial.png"))


def make_dfd_05():
    W, H = 2500, 1860
    surf, ctx = dl.new_canvas(W, H)
    dl.draw_header(
        ctx,
        W,
        "DFD Vector Estático: Carga Validada y Búsqueda Secuencial",
        "Arreglo estático v[MAX] con tamaño lógico n (índices 0 .. n - 1) y bandera booleana de parada temprana",
        badge="MÓDULO M06 · VECTORES ESTÁTICOS",
        accent=dl.NAVY,
    )

    # Left Container: Phase 1
    p1_x, p1_y, p1_w, p1_h = 40, 174, 1140, 1598
    dl.rounded_rect(ctx, p1_x, p1_y, p1_w, p1_h, r=16, fill=dl.PANEL_BG, stroke=dl.BLUE, stroke_w=2.4)
    dl.rounded_rect(ctx, p1_x + 20, p1_y + 18, 620, 42, r=10, fill=dl.BLUE)
    dl.draw_text(ctx, "FASE 1 · Validar n y Cargar Vector v[MAX]", p1_x + 330, p1_y + 39, "Inter", 19, bold=True, color=dl.WHITE, align="center", valign="middle")

    cx1 = 710
    y_ini = 278
    y_max = 385
    y_rn = 500
    y_j1 = 582
    y_dec1 = 688
    y_for = 1135
    y_rv = 1310

    dl.dfd_start_end(ctx, cx1, y_ini, 210, 62, "Inicio", font_size=22)
    dl.dfd_process(ctx, cx1, y_max, 250, 70, "MAX <- 100", font_size=21, fill=dl.WHITE)
    dl.dfd_input(ctx, cx1, y_rn, 240, 72, "Leer n", font_size=21)
    dl.draw_arrow(ctx, [(cx1, y_ini + 31), (cx1, y_max - 35)], color=dl.NAVY, width=3.2)
    dl.draw_arrow(ctx, [(cx1, y_max + 35), (cx1, y_rn - 36)], color=dl.NAVY, width=3.2)
    dl.draw_arrow(ctx, [(cx1, y_rn + 36), (cx1, y_j1), (cx1, y_dec1 - 66)], color=dl.NAVY, width=3.2)

    dl.set_color(ctx, dl.ORANGE)
    ctx.arc(cx1, y_j1, 6, 0, 6.2832)
    ctx.fill()

    dl.dfd_decision(ctx, cx1, y_dec1, 330, 132, "¿n < 1 O\nn > MAX?", font_size=19.5)

    # Error loop on left of Phase 1
    lx1 = 300
    dl.dfd_output(ctx, lx1, 835, 310, 88, 'Escribir "Error:\n1 <= n <= ", MAX', font_size=17.5, fill=dl.RED_FILL, stroke=dl.RED)
    dl.dfd_input(ctx, lx1, 975, 240, 72, "Leer n", font_size=20)
    dl.draw_arrow(ctx, [(cx1 - 165, y_dec1), (lx1, y_dec1), (lx1, 791)], color=dl.RED, width=3.2)
    dl.draw_pill(ctx, 455, y_dec1, "Sí (Inválido)", bg=dl.RED, fg=dl.WHITE, font_size=15, pad_x=11, pad_y=4)
    dl.draw_arrow(ctx, [(lx1, 872), (lx1, 939)], color=dl.RED, width=3.2)
    # Loop back from Leer n -> y_j1
    dl.draw_arrow(ctx, [(lx1, 1011), (lx1, 1055), (92, 1055), (92, y_j1), (cx1 - 8, y_j1)], color=dl.ORANGE, width=3.2)

    # No -> Para cargar v[0..n-1]
    dl.draw_arrow(ctx, [(cx1, y_dec1 + 66), (cx1, y_for - 44)], color=dl.GREEN, width=3.4)
    dl.draw_pill(ctx, cx1 + 62, 900, "No (Válido)", bg=dl.GREEN, fg=dl.WHITE, font_size=16, pad_x=12, pad_y=5)

    dl.dfd_for_hex(ctx, cx1, y_for, 420, 88, "Para i <- 0 hasta n - 1\ncon paso +1", font_size=19, point=26)
    dl.draw_arrow(ctx, [(cx1, y_for + 44), (cx1, y_rv - 36)], color=dl.PURPLE, width=3.4)
    dl.dfd_input(ctx, cx1, y_rv, 260, 72, "Leer v[i]", font_size=21)

    # Return loop of Para
    dl.draw_arrow(ctx, [(cx1, y_rv + 36), (cx1, y_rv + 84), (420, y_rv + 84), (420, y_for), (cx1 - 210, y_for)], color=dl.PURPLE, width=3.4)
    dl.draw_pill(ctx, 420, 1225, "Sig. i", bg=dl.PURPLE, fg=dl.WHITE, font_size=15, pad_x=10, pad_y=4)

    # Static array memory reminder card inside bottom of Phase 1
    dl.rounded_rect(ctx, p1_x + 28, 1465, p1_w - 56, 280, r=14, fill=dl.WHITE, stroke=dl.NAVY, stroke_w=2.0, shadow=True)
    dl.draw_warn_icon(ctx, p1_x + 68, 1508, r=13, bg=dl.ORANGE)
    dl.draw_text(ctx, "Regla Estática Obligatoria (M06)", p1_x + 96, 1494, "Inter", 20, bold=True, color=dl.NAVY)
    dl.draw_wrapped(
        ctx,
        "• Capacidad física fija: const int MAX = 100; int v[MAX]; (¡NO usar int v[n] ni vector dinámico!).\n"
        "• Tamaño lógico: n es cuántos elementos realmente usará el usuario (validado 1 <= n <= MAX).\n"
        "• Índices válidos en C++: desde 0 hasta n - 1 (en PSeInt con Opcion Base 0, o de 1 hasta n).",
        p1_x + 56,
        1542,
        p1_w - 112,
        "Inter",
        18.0,
        color=dl.INK_SEC,
        line_mult=1.38,
    )

    # Right Container: Phase 2
    p2_x, p2_y, p2_w, p2_h = 1220, 174, 1240, 1598
    dl.rounded_rect(ctx, p2_x, p2_y, p2_w, p2_h, r=16, fill=dl.PANEL_BG, stroke=dl.TEAL, stroke_w=2.4)
    dl.rounded_rect(ctx, p2_x + 20, p2_y + 18, 660, 42, r=10, fill=dl.TEAL)
    dl.draw_text(ctx, "FASE 2 · Búsqueda Secuencial en v[0 .. n - 1]", p2_x + 350, p2_y + 39, "Inter", 19, bold=True, color=dl.WHITE, align="center", valign="middle")

    cx2 = 1830
    y_rk = 342
    y_init2 = 478
    y_j2 = 582
    y_while = 690
    y_eq = 900
    y_br = 1095
    y_bus2 = 1190
    y_res = 1350
    y_out2 = 1525
    y_fin = 1690

    # Bridge arrow from Phase 1 Para exit (cx1 + 210 = 920, y_for = 1135) -> Phase 2 top!
    dl.draw_arrow(
        ctx,
        [(cx1 + 210, y_for), (1120, y_for), (1120, 264), (cx2, 264), (cx2, y_rk - 37)],
        color=dl.TEAL,
        width=4.0,
    )
    dl.draw_pill(ctx, 1200, 264, "Carga lista → Buscar", bg=dl.TEAL, fg=dl.WHITE, font_size=16, pad_x=14, pad_y=6)

    dl.dfd_input(ctx, cx2, y_rk, 290, 74, "Leer clave", font_size=21)
    dl.dfd_process(ctx, cx2, y_init2, 360, 108, "encontrado <- Falso\npos <- -1\ni <- 0", font_size=19, fill=dl.WHITE)
    dl.draw_arrow(ctx, [(cx2, y_rk + 37), (cx2, y_init2 - 54)], color=dl.NAVY, width=3.2)
    dl.draw_arrow(ctx, [(cx2, y_init2 + 54), (cx2, y_while - 68)], color=dl.NAVY, width=3.2)

    dl.set_color(ctx, dl.TEAL)
    ctx.arc(cx2, y_j2, 6, 0, 6.2832)
    ctx.fill()

    dl.dfd_decision(ctx, cx2, y_while, 370, 136, "¿i < n Y\nNO encontrado?", font_size=19, fill=dl.TEAL_FILL, stroke=dl.TEAL)
    dl.draw_arrow(ctx, [(cx2, y_while + 68), (cx2, y_eq - 64)], color=dl.GREEN, width=3.4)
    dl.draw_pill(ctx, cx2 + 48, 792, "Sí", bg=dl.GREEN, fg=dl.WHITE, font_size=16, pad_x=12, pad_y=4)

    dl.dfd_decision(ctx, cx2, y_eq, 310, 128, "¿v[i] == clave?", font_size=20)

    lx2 = 1545
    rx2 = 2125
    dl.dfd_process(ctx, lx2, y_br, 330, 92, "encontrado <- Verdadero\npos <- i", font_size=18.5, fill=dl.GREEN_SOFT, stroke=dl.GREEN)
    dl.dfd_process(ctx, rx2, y_br, 240, 82, "i <- i + 1", font_size=20, fill=dl.WHITE)

    dl.draw_arrow(ctx, [(cx2 - 155, y_eq), (lx2, y_eq), (lx2, y_br - 46)], color=dl.GREEN, width=3.2)
    dl.draw_pill(ctx, lx2 + 78, y_eq, "Sí", bg=dl.GREEN, fg=dl.WHITE, font_size=16, pad_x=12, pad_y=4)

    dl.draw_arrow(ctx, [(cx2 + 155, y_eq), (rx2, y_eq), (rx2, y_br - 41)], color=dl.RED, width=3.2)
    dl.draw_pill(ctx, rx2 - 78, y_eq, "No", bg=dl.RED, fg=dl.WHITE, font_size=16, pad_x=12, pad_y=4)

    # Inner merge bus -> return loop on left of Phase 2 (x = 1285)
    dl.set_color(ctx, dl.NAVY)
    ctx.set_line_width(3.2)
    ctx.move_to(lx2, y_br + 46)
    ctx.line_to(lx2, y_bus2)
    ctx.line_to(rx2, y_bus2)
    ctx.line_to(rx2, y_br + 41)
    ctx.stroke()
    ctx.arc(cx2, y_bus2, 6, 0, 6.2832)
    ctx.fill()

    x_ret2 = 1285
    dl.draw_arrow(ctx, [(cx2, y_bus2), (cx2, y_bus2 + 44), (x_ret2, y_bus2 + 44), (x_ret2, y_j2), (cx2 - 8, y_j2)], color=dl.TEAL, width=3.4)
    dl.draw_pill(ctx, x_ret2, 920, "Repetir\nMientras", bg=dl.TEAL, fg=dl.WHITE, font_size=14.5, pad_x=10, pad_y=6)

    # Exit right from Mientras -> Result check
    x_exit2 = 2365
    dl.draw_arrow(ctx, [(cx2 + 185, y_while), (x_exit2, y_while), (x_exit2, 1255), (cx2, 1255), (cx2, y_res - 58)], color=dl.RED, width=3.4)
    dl.draw_pill(ctx, 2195, y_while, "No (Terminó)", bg=dl.RED, fg=dl.WHITE, font_size=16, pad_x=12, pad_y=5)

    dl.dfd_decision(ctx, cx2, y_res, 340, 116, "¿encontrado\n== Verdadero?", font_size=18.5)
    dl.dfd_output(ctx, lx2, y_out2, 390, 92, 'Escribir "Encontrado\nen índice: ", pos', font_size=18, fill=dl.GREEN_FILL, stroke=dl.GREEN)
    dl.dfd_output(ctx, rx2, y_out2, 370, 92, 'Escribir "No existe\nen el vector"', font_size=18, fill=dl.AMBER_FILL, stroke=dl.AMBER)

    dl.draw_arrow(ctx, [(cx2 - 170, y_res), (lx2, y_res), (lx2, y_out2 - 46)], color=dl.GREEN, width=3.2)
    dl.draw_pill(ctx, lx2 + 78, y_res, "Sí", bg=dl.GREEN, fg=dl.WHITE, font_size=16, pad_x=12, pad_y=4)

    dl.draw_arrow(ctx, [(cx2 + 170, y_res), (rx2, y_res), (rx2, y_out2 - 46)], color=dl.RED, width=3.2)
    dl.draw_pill(ctx, rx2 - 78, y_res, "No", bg=dl.RED, fg=dl.WHITE, font_size=16, pad_x=12, pad_y=4)

    # Merge to Fin
    y_bus_fin = 1608
    dl.set_color(ctx, dl.NAVY)
    ctx.set_line_width(3.2)
    ctx.move_to(lx2, y_out2 + 39)
    ctx.line_to(lx2, y_bus_fin)
    ctx.line_to(rx2, y_bus_fin)
    ctx.line_to(rx2, y_out2 + 39)
    ctx.stroke()
    ctx.arc(cx2, y_bus_fin, 6, 0, 6.2832)
    ctx.fill()

    dl.draw_arrow(ctx, [(cx2, y_bus_fin), (cx2, y_fin - 31)], color=dl.NAVY, width=3.4)
    dl.dfd_start_end(ctx, cx2, y_fin, 210, 62, "Fin", font_size=22)

    dl.draw_footer(ctx, W, H, "Curso de Algoritmos y Programación (30h) · Carga y Búsqueda Secuencial en Vector Estático", badge="dfd_05_vector_estatico_busqueda.png")
    dl.save_png(surf, os.path.join(OUT_DIR, "dfd_05_vector_estatico_busqueda.png"))


if __name__ == "__main__":
    make_dfd_03()
    make_dfd_04()
    make_dfd_05()
    print("Generated dfd_03, dfd_04, dfd_05 successfully.")
