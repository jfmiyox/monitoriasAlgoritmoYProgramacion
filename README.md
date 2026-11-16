# Curso de Monitoría: Algoritmos y Programación (30 Horas)

> **Ruta de aprendizaje progresiva y sin miedo:**  
> **Lógica cotidiana $\rightarrow$ Diagramas de Flujo (DFD) $\rightarrow$ Pseudocódigo (PSeInt) $\rightarrow$ C++ Básico (hasta Vectores y Matrices Estáticos)**

Este repositorio contiene el material maestro completo de una monitoría universitaria de **30.0 horas** diseñada para estudiantes que empiezan desde cero (o sienten que "la programación no es lo suyo"). Todo está redactado con tono cercano, analogías cotidianas (*"explicado con plastilina"*), énfasis constante en **cómo analizar e interpretar problemas antes de escribir código**, pruebas de escritorio paso a paso y un banco amplio de ejercicios con solucionario explicado.

---

## 1. Alcance Técnico del Curso (Qué SÍ y Qué NO)

Para evitar confusiones en clase y en parciales, este curso mantiene fronteras estrictas y coherentes con un primer semestre de Algoritmos y Programación:

| Sí hace parte del curso | Fuera de alcance (prohibido en este curso) |
| :--- | :--- |
| Análisis de enunciados con el **Método de los 5 Pasos (EPS)** | Memoria dinámica (`new`, `delete`, `malloc`, `calloc`, `free`) |
| **DFD** (simbología estándar, decisiones, ciclos y pruebas de escritorio) | Contenedores dinámicos de la STL (`std::vector`, `list`, `map`) |
| **PSeInt** en español (`Algoritmo`, `Definir`, `Si`, `Segun`, `Mientras`, `Repetir`, `Para`, `Dimension`, `SubProceso`) | Arreglos de longitud variable no estándar (**VLA**, como `int v[n];`) |
| **C++ básico** con `<iostream>`, `<iomanip>`, `<cmath>`, `<string>` (`cin`, `cout`, `getline`) | Punteros (`*`, `->`), aritmética de direcciones |
| Estructuras de control (`if`, `else if`, `switch`, `while`, `do-while`, `for`) | Programación Orientada a Objetos (`class`, herencia, polimorfismo) |
| **Vectores estáticos** y **matrices estáticas** con capacidad fija definida (`const int MAX = ...; int v[MAX];`) | Estructuras de datos avanzadas (listas enlazadas, árboles, grafos) |
| Funciones simples (`void`, retorno, paso por valor, referencia básica `&` y paso de arreglos estáticos) | Recursividad avanzada y archivos binarios complejos |

> **Regla de oro de los arreglos en este curso:** Siempre reservamos capacidad fija conocida en tiempo de compilación (ej. `const int MAX = 100; int notas[MAX];`) junto con una variable entera `n` validada (`1 <= n && n <= MAX`) que indica cuántos casilleros están realmente en uso.

---

## 2. Mapa Maestro de Módulos (30.0 Horas Exactas)

| Módulo | Carpeta | Duración | Eje Pedagógico y Contenido Principal |
| :--- | :--- | :---: | :--- |
| **M00** | [`modulos/M00_Algoritmos_Para_Tontos/`](modulos/M00_Algoritmos_Para_Tontos/) | **2.5 h** | Perder el miedo a programar. Analogías cotidianas, cómo piensa una computadora, qué es un algoritmo, **Método de los 5 Pasos** y análisis **EPS** (Entradas–Proceso–Salidas). 8 ejercicios de lógica con solucionario. |
| **M01** | [`modulos/M01_Logica_y_DFD/`](modulos/M01_Logica_y_DFD/) | **3.0 h** | Símbolos oficiales de **DFD**, reglas de oro para diagramas limpios, flujo secuencial y decisiones simples/dobles, y **prueba de escritorio en papel**. 6 DFDs resueltos + 10 ejercicios con pistas y solucionario. |
| **M02** | [`modulos/M02_PSeInt_y_Puente_CPP/`](modulos/M02_PSeInt_y_Puente_CPP/) | **3.0 h** | Uso de **PSeInt**, tabla de traducción **DFD $\leftrightarrow$ PSeInt $\leftrightarrow$ C++**, anatomía de un programa en C++, compilación y diccionario de errores comunes del compilador al español. 6 ejemplos duales (`.psc` + `.cpp`) + 10 ejercicios. |
| **M03** | [`modulos/M03_Tipos_Datos_y_Operadores/`](modulos/M03_Tipos_Datos_y_Operadores/) | **3.0 h** | La memoria RAM "para tontos". `int`, `float`, `double`, `char`, `bool`, `string` (`cin` vs `getline` + `cin.ignore()`), `const`, división entera vs real (`5/2` vs `5.0/2`), módulo `%`, precedencia y casting simple. 7 resueltos + 12 propuestos. |
| **M04** | [`modulos/M04_Condicionales/`](modulos/M04_Condicionales/) | **3.5 h** | Lógica booleana (`&&`, `||`, `!`), trampa clásica `10 <= x <= 20`, `if`, `if-else`, escalera `else-if`, `if` anidados, `switch-case` (`break` y `default`) y **diccionario traductor de enunciados de parcial**. 8 resueltos + 14 propuestos. |
| **M05** | [`modulos/M05_Ciclos_y_Bucles/`](modulos/M05_Ciclos_y_Bucles/) | **4.0 h** | Cuándo usar `for`, `while` o `do-while`. Trampa mortal: `Repetir...Hasta Que` (PSeInt) vs `do...while` (C++). Contadores, acumuladores, banderas, máx/mín sin arreglos, centinelas y ciclos anidados. 10 resueltos + 16 propuestos. |
| **M06** | [`modulos/M06_Vectores_Estaticos/`](modulos/M06_Vectores_Estaticos/) | **4.0 h** | Analogía de casilleros fijos desde índice `0`. Declaración estática (`const int MAX`), índices `0..n-1` (C++) vs `1..n` (PSeInt), suma, promedio, conteo, máx/mín con posición, búsqueda secuencial, invertir, rotar, insertar/eliminar y **Burbuja** paso a paso. 8 resueltos + 14 propuestos. |
| **M07** | [`modulos/M07_Matrices_Estaticas/`](modulos/M07_Matrices_Estaticas/) | **4.0 h** | Analogía de edificio / hoja de cálculo fija (`mat[MAX_F][MAX_C]`). Recorrido por filas vs por columnas, sumas por fila/columna, mayor/menor con coordenadas, diagonales (`i == j`, `i + j == n - 1`), triangulares, simetría, transpuesta y casos reales (notas, ventas, cine). 8 resueltos + 14 propuestos. |
| **M08** | [`modulos/M08_Modularidad_Parciales_y_Solucionario/`](modulos/M08_Modularidad_Parciales_y_Solucionario/) | **3.0 h** | Funciones simples (`void`, retorno, valor vs referencia `&`), paso de vectores y matrices estáticas a funciones, **Estrategia Anti-Pánico en Parciales**, checklist de 10 puntos y **2 simulacros completos de parcial** (Corte 1 y Corte Final) con rúbrica y solucionario. |
| **Total** | **9 módulos (M00–M08)** | **30.0 h** | **15 sesiones de 2.0 horas cada una (`PLAN_30_HORAS.md`)** |

---

## 3. Estructura del Repositorio

```text
monitoria_algoritmos_cpp/
├── README.md                          # Este mapa maestro del curso
├── PLAN_30_HORAS.md                   # Guion minuto a minuto para las 15 sesiones (30.0 h)
├── LIBRO_COMPLETO_MONITORIA_30H.pdf   # Libro unificado de todo el curso (M00..M08)
├── index.html                         # Portal web local interactivo y buscador de recursos
├── latex_common/
│   └── estilo_monitoria.sty           # Hoja de estilo LaTeX (XeLaTeX, cajas, PSeInt/C++)
├── assets/
│   ├── diagramas/                     # Diagramas DFD y esquemas de memoria (>=200 DPI)
│   └── ilustraciones/                 # Ilustraciones conceptuales (receta, RAM, 3 puentes)
├── fichas_resumen/                    # 4 fichas imprimibles de consulta rápida (PDF + PNG)
│   ├── Ficha_01_Simbolos_DFD.*
│   ├── Ficha_02_Traductor_DFD_PSeInt_CPP.*
│   ├── Ficha_03_Metodo_5_Pasos_Analizar_Problemas.*
│   └── Ficha_04_Patrones_Vectores_y_Matrices_Estaticos.*
└── modulos/
    ├── M00_Algoritmos_Para_Tontos/
    ├── M01_Logica_y_DFD/
    ├── M02_PSeInt_y_Puente_CPP/
    ├── M03_Tipos_Datos_y_Operadores/
    ├── M04_Condicionales/
    ├── M05_Ciclos_y_Bucles/
    ├── M06_Vectores_Estaticos/
    ├── M07_Matrices_Estaticas/
    └── M08_Modularidad_Parciales_y_Solucionario/
```

Dentro de los módulos aplicables encontrarás además subcarpetas organizadas por artefacto:
- `dfd/`: diagramas de flujo específicos del módulo.
- `pseint/`: archivos `.psc` listos para abrir y ejecutar en **PSeInt**.
- `cpp/`: programas `.cpp` reales verificados sin advertencias bajo `g++ -std=c++17 -Wall -Wextra -Werror`.

---

## 4. Cómo Usar Este Material

### Para el Monitor (Docente / Tutor)
1. **Planifica cada encuentro con [`PLAN_30_HORAS.md`](PLAN_30_HORAS.md):** cada sesión de 2 horas tiene un guion minuto a minuto con enganche, explicación visual, práctica guiada, trampas clásicas que cazar en vivo y tarea.
2. **Proyecta primero la idea, luego el código:** inicia siempre en tablero con la analogía del módulo (cajas en `paratontos` e imágenes de `assets/`), pasa por **DFD** y **PSeInt**, haz la **prueba de escritorio** con los estudiantes y solo entonces traduce a **C++**.
3. **Imprime o comparte las `fichas_resumen/`:** son hojas de referencia de 1–2 páginas ideales para que los estudiantes las tengan al lado mientras resuelven talleres.
4. **Cierra el corte con `M08`:** usa los dos simulacros cronometrados (90 min cada uno) y la rúbrica paso a paso antes de los parciales oficiales.

### Para el Estudiante
1. **Lee sin saltarte el módulo `M00` y `M01`:** casi todos los bloqueos en C++ no son problemas de sintaxis sino de no saber qué datos entran, qué debe salir y en qué orden ocurren los pasos.
2. **Regla de los 3 borradores:** antes de abrir el compilador en un ejercicio nuevo, escribe en papel tu tabla **EPS**, dibuja el **DFD** (o esbozo en **PSeInt**) y haz una **prueba de escritorio** con 2 o 3 datos pequeños.
3. **Usa las cajas de colores como guía de estudio:**
   - **Explicado Para Tontos / Con Plastilina:** léela primero si un concepto te suena abstracto.
   - **OJO: Trampa Clásica de Parcial:** repásala la noche anterior a tu examen (ahí están los errores que más puntos quitan).
   - **Prueba de Escritorio Paso a Paso:** síguela línea por línea con lápiz y papel hasta predecir la salida sin mirar el resultado.
4. **Experimenta modificando los `.cpp`:** descarga o abre los ejemplos de cada carpeta `cpp/`, compílalos y cambia valores de entrada para observar qué ocurre.

---

## 5. Compilación y Verificación Local

### Compilar cualquier ejemplo en C++ (Linux / macOS / Windows con MinGW)
```bash
g++ -std=c++17 -Wall -Wextra archivo.cpp -o programa
./programa
```

> Si estás en Windows con Dev-C++ o Code::Blocks, abre el archivo `.cpp`, presiona **Compilar y Ejecutar (`F11` o `F9`)** y verifica que el compilador esté configurado con estándar C++11 o C++17.

### Recompilar los PDFs con XeLaTeX (opcional, para editar notas)
Los módulos comparten la hoja de estilo [`latex_common/estilo_monitoria.sty`](latex_common/estilo_monitoria.sty) (fuentes `Inter` y `DejaVu Sans Mono`, soporte UTF-8 para español, C++ y PSeInt):

```bash
cd modulos/M03_Tipos_Datos_y_Operadores
xelatex -interaction=nonstopmode M03_Tipos_Datos_y_Operadores.tex
xelatex -interaction=nonstopmode M03_Tipos_Datos_y_Operadores.tex
```

Para abrir el portal visual completo del curso, abre [`index.html`](index.html) en tu navegador web.
