# Documentación General del Proyecto

## Curso de Monitoría: Algoritmos y Programación — 30 Horas de Contenido Multimedia

> **Repositorio:** `git@github.com:jfmiyox/monitoriasAlgoritmoYProgramacion.git`
> **Rama principal:** `main` (commits `6b86c10` y `5b62c46`)
> **Autora del material / monitor:** Miyox
> **Última actualización de este documento:** 16 de noviembre de 2026

---

## Índice

1. [Qué es este proyecto](#1-qué-es-este-proyecto)
2. [Resumen ejecutivo en cifras](#2-resumen-ejecutivo-en-cifras)
3. [Origen y contexto](#3-origen-y-contexto)
4. [Filosofía pedagógica](#4-filosofía-pedagógica)
5. [Alcance técnico: qué sí y qué no](#5-alcance-técnico-qué-sí-y-qué-no)
6. [Estructura del repositorio](#6-estructura-del-repositorio)
7. [Los nueve módulos en detalle](#7-los-nueve-módulos-en-detalle)
8. [Material complementario](#8-material-complementario)
9. [El libro unificado](#9-el-libro-unificado)
10. [El portal web `index.html`](#10-el-portal-web-indexhtml)
11. [La hoja de estilo LaTeX](#11-la-hoja-de-estilo-latex)
12. [Inventario de código C++ y PSeInt](#12-inventario-de-código-c-y-pseint)
13. [El plan de 15 sesiones](#13-el-plan-de-15-sesiones)
14. [Cómo se verificó la calidad](#14-cómo-se-verificó-la-calidad)
15. [Cómo reproducir y editar el material](#15-cómo-reproducir-y-editar-el-material)
16. [Estado del repositorio y de Git](#16-estado-del-repositorio-y-de-git)
17. [Cómo usar el material en clase](#17-cómo-usar-el-material-en-clase)
18. [Cómo usar el material para estudiar](#18-cómo-usar-el-material-para-estudiar)
19. [Pendientes y próximos pasos](#19-pendientes-y-próximos-pasos)
20. [Glosario](#20-glosario)

---

## 1. Qué es este proyecto

Este repositorio es el **paquete completo de un curso de monitoría universitaria de 30.0 horas** sobre *Algoritmos y Programación*, dictado desde cero absoluto y terminando en **vectores y matrices estáticos en C++**.

No es un repositorio de apuntes sueltos: es un **sistema de material didáctico** con cuatro capas que se alimentan entre sí.

| Capa | Qué aporta | Formato |
| :--- | :--- | :--- |
| **Contenido teórico** | Explicaciones, analogías, trampas de parcial, pruebas de escritorio | LaTeX (`.tex`) y Markdown (`.md`) |
| **Contenido ejecutable** | Programas reales que compilan y corren | C++ (`.cpp`) y PSeInt (`.psc`) |
| **Contenido visual** | Diagramas de flujo, esquemas de memoria, ilustraciones, fichas | PNG y JPG de alta resolución |
| **Contenido de distribución** | Libro unificado de 300 páginas y portal web interactivo | PDF y HTML autocontenido |

La ruta de aprendizaje es siempre la misma y se repite en cada tema:

```
Lógica cotidiana  →  Diagrama de Flujo (DFD)  →  Pseudocódigo (PSeInt)  →  C++ básico
```

Esa progresión es el corazón del proyecto. La idea es que el estudiante nunca salte directo al compilador: primero entiende **qué entra, qué sale y qué pasos ocurren en el medio**, y solo después traduce esa idea a sintaxis.

---

## 2. Resumen ejecutivo en cifras

| Métrica | Valor |
| :--- | :--- |
| Duración total del curso | **30.0 horas exactas** |
| Sesiones | **15 sesiones de 2.0 horas** |
| Módulos | **9** (`M00` a `M08`) |
| Páginas de módulos | **293** |
| Páginas del libro unificado | **300** |
| Fichas resumen imprimibles | **4** (1 página cada una) |
| Ejercicios y problemas resueltos guiados | **61** + **2 simulacros de parcial** |
| Ejercicios propuestos con pista y solucionario | **102** |
| Programas C++ verificados | **57** |
| Programas PSeInt | **47** |
| Diagramas e ilustraciones | **11 diagramas maestros + 23 DFD + 3 ilustraciones** |
| Archivos rastreados por Git | **190** |
| Líneas de LaTeX escritas | **6.474** |
| Tamaño del historial de Git | **~45 MB** |

---

## 3. Origen y contexto

El material nace de una necesidad muy concreta de la monitoría: **la mayoría de los estudiantes que "se pierden" en C++ no tienen un problema de sintaxis, sino de análisis**. Escriben código rápido, el compilador les devuelve una lista de errores y concluyen que "la programación no es lo suyo", cuando en realidad nunca definieron qué datos entraban, qué debía salir ni en qué orden ocurrirían los pasos.

Por eso el curso está construido al revés de lo habitual:

1. No empieza en C++, empieza en **lógica cotidiana** (preparar un café, pedir un domicilio, sacar plata de un cajero).
2. Traduce esa lógica a un **lenguaje visual neutral** (DFD), que no tiene sintaxis que memorizar.
3. Pasa por **PSeInt en español**, donde las palabras del diagrama se vuelven código legible.
4. Solo al final llega a **C++**, mostrando que la sintaxis es "la ropa" y el algoritmo es "el cuerpo".

El público objetivo son estudiantes de primer semestre que:

- Nunca han programado.
- Vienen de un colegio con poca o nula formación en lógica.
- Sienten ansiedad frente al compilador y a los parciales.
- Necesitan material que puedan repasar solos, sin depender de la clase.

Todo el texto está redactado en **tono cercano**, con analogías explícitas, humor y un énfasis obsesivo en los errores que más puntos quitan en los exámenes.

---

## 4. Filosofía pedagógica

### 4.1 El tono "para tontos" / "con plastilina"

Cada concepto abstracto se presenta primero como algo físico y manipulable. El nombre de la caja en el PDF es literalmente **"Explicado Para Tontos"** o **"Con Plastilina"**. La intención no es infantilizar, sino **quitarle el miedo al tema**: si alguien puede explicar una matriz como un edificio de apartamentos con pisos y puertas, entonces puede programarla.

Ejemplos reales del material:

- Un **algoritmo** es una receta de cocina ejecutada por un genio literal que hace exactamente lo que le dices, ni más ni menos.
- Una **variable en RAM** es una caja con nombre, tamaño y tipo; si no la inicializas, la caja trae basura.
- Un **vector estático** es una fila de casilleros numerados desde `0`, donde el casillero `n` **no existe** (porque el último válido es `n - 1`).
- Una **matriz estática** es un edificio con filas y columnas: `mat[fila][columna]`.
- Un **ciclo** es un bucle de una montaña rusa: necesitas saber dónde empieza, cuándo se repite y cómo se sale.

### 4.2 El Método de los 5 Pasos

Es el esqueleto de análisis que se repite en todo el curso antes de escribir una sola línea de código:

1. **Leer y subrayar** los verbos de acción y los datos del enunciado.
2. **Construir la tabla EPS**: Entradas → Proceso → Salidas.
3. **Elegir las herramientas** (¿hay decisión?, ¿hay repetición?, ¿hay arreglo?).
4. **Hacer la prueba de escritorio** en papel con 2 o 3 casos pequeños.
5. **Traducir** a DFD, a PSeInt y finalmente a C++.

La ficha `Ficha_03_Metodo_5_Pasos_Analizar_Problemas.pdf` resume este método en una sola página para tenerlo al lado durante un parcial.

### 4.3 La prueba de escritorio

Casi todos los problemas resueltos incluyen una **tabla de seguimiento** donde se simula el programa a mano: columnas para cada variable, fila por cada iteración o paso. El estudiante aprende a predecir la salida **antes** de ejecutar el programa, que es exactamente la habilidad que se evalúa en un parcial escrito.

### 4.4 Las cajas de color

La hoja de estilo LaTeX define siete cajas semánticas que el estudiante aprende a reconocer:

| Caja | Color predominante | Uso |
| :--- | :--- | :--- |
| `paratontos` | Azul | Explicación con analogías cotidianas |
| `consejo` | Turquesa | Recomendaciones del monitor |
| `peligro` | Rojo | "OJO: trampa clásica de parcial" |
| `analisis` | Morado | Tabla EPS y descomposición del problema |
| `pruebaescritorio` | Verde | Simulación paso a paso en papel |
| `ejercicio` | Naranja | Enunciado de práctica |
| `solucion` | Gris claro | Solucionario comentado |

La instrucción de estudio es simple: si un concepto suena abstracto, leer primero la caja azul; la noche antes del parcial, repasar solo las cajas rojas.

### 4.5 La estrategia anti-pánico

El módulo `M08` cierra el curso con una metodología explícita para enfrentar un parcial de 90 minutos:

- Los primeros **8 minutos sin teclado**, solo leyendo y subrayando.
- Reparto de tiempo por puntaje (minuto por punto, aproximadamente).
- Checklist de **10 puntos** antes de entregar.
- Catálogo de los **12 errores mortales** en DFD, PSeInt y C++.
- Dos **simulacros completos** cronometrados con rúbrica de 100 puntos.

---

## 5. Alcance técnico: qué sí y qué no

El curso mantiene una frontera técnica estricta para no mezclar temas de semestres posteriores. Esto está documentado en el `README.md` y respetado en los nueve módulos.

| Sí hace parte del curso | Fuera de alcance (prohibido en este curso) |
| :--- | :--- |
| Análisis con el Método de los 5 Pasos y tabla EPS | Memoria dinámica (`new`, `delete`, `malloc`, `calloc`, `free`) |
| DFD con simbología estándar y pruebas de escritorio | Contenedores dinámicos de la STL (`std::vector`, `list`, `map`) |
| PSeInt en español (`Algoritmo`, `Definir`, `Si`, `Segun`, `Mientras`, `Repetir`, `Para`, `Dimension`, `SubProceso`) | Arreglos de longitud variable no estándar (VLA, `int v[n];`) |
| C++ básico con `<iostream>`, `<iomanip>`, `<cmath>`, `<string>` | Punteros (`*`, `->`) y aritmética de direcciones |
| Estructuras de control (`if`, `else if`, `switch`, `while`, `do-while`, `for`) | Programación orientada a objetos (`class`, herencia, polimorfismo) |
| Vectores y matrices **estáticos** con capacidad fija | Estructuras avanzadas (listas enlazadas, árboles, grafos) |
| Funciones simples, paso por valor, referencia básica (`&`) y paso de arreglos estáticos | Recursividad avanzada y archivos binarios complejos |

**Regla de oro de los arreglos en este curso:** siempre se reserva capacidad fija conocida en tiempo de compilación y se acompaña de una variable `n` validada.

```cpp
const int MAX = 100;
int notas[MAX];
int n;
// Validación obligatoria antes de usar el arreglo:
// 1 <= n && n <= MAX
```

Consecuencias directas de esta regla:

- Los índices válidos de C++ van de `0` a `n - 1`; escribir `v[n]` es un error de parcial.
- En PSeInt los índices por defecto van de `1` a `n`, de modo que toda traducción exige un ajuste mental.
- Las funciones reciben el arreglo junto con su tamaño: `void mostrar(const int v[], int n)`.
- Las matrices se pasan indicando la dimensión de columnas: `void mostrar(int m[][MAX_C], int f, int c)`.

---

## 6. Estructura del repositorio

```text
monitoriasAlgoritmoYProgramacion/
├── README.md                                   # Mapa maestro del curso
├── DOCUMENTACION_DEL_PROYECTO.md               # Este documento
├── LIBRO_COMPLETO_MONITORIA_30H.tex            # Fuente LaTeX del libro unificado
├── LIBRO_COMPLETO_MONITORIA_30H.pdf            # Libro de 300 páginas (17 MB)
├── index.html                                  # Portal web autocontenido (2.267 líneas)
├── .gitignore
├── latex_common/
│   └── estilo_monitoria.sty                    # Hoja de estilo compartida
├── assets/
│   ├── diagramas/
│   │   ├── dfd_00_simbolos_oficiales.png
│   │   ├── dfd_01_suma_promedio.png
│   │   ├── dfd_02_mayor_tres_numeros.png
│   │   ├── dfd_03_ciclo_mientras_centinela.png
│   │   ├── dfd_04_ciclo_para_factorial.png
│   │   ├── dfd_05_vector_estatico_busqueda.png
│   │   ├── mem_01_variables_ram.png
│   │   ├── mem_02_puente_ciclos.png
│   │   ├── mem_03_vector_estatico_1d.png
│   │   ├── mem_04_matriz_estatica_2d.png
│   │   ├── met_01_cinco_pasos_analisis.png
│   │   └── _gen/                               # Scripts Python que generan los diagramas
│   │       ├── draw_lib.py
│   │       ├── gen_dfd_part1.py
│   │       ├── gen_dfd_part2.py
│   │       └── gen_mem_met.py
│   └── ilustraciones/
│       ├── ilus_01_algoritmo_receta.jpg
│       ├── ilus_02_variables_ram.jpg
│       └── ilus_03_puente_dfd_pseint_cpp.jpg
├── fichas_resumen/
│   ├── Ficha_01_Simbolos_DFD.{tex,pdf,png}
│   ├── Ficha_02_Traductor_DFD_PSeInt_CPP.{tex,pdf,png}
│   ├── Ficha_03_Metodo_5_Pasos_Analizar_Problemas.{tex,pdf,png}
│   └── Ficha_04_Patrones_Vectores_y_Matrices_Estaticos.{tex,pdf,png}
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

Cada módulo sigue el mismo patrón de artefactos:

```text
MXX_Nombre_Del_Modulo/
├── MXX_Nombre_Del_Modulo.md     # Versión Markdown del módulo
├── MXX_Nombre_Del_Modulo.tex    # Fuente LaTeX (la versión "oficial")
├── MXX_Nombre_Del_Modulo.pdf    # PDF compilado listo para imprimir
├── cpp/                         # Programas C++ del módulo (cuando aplica)
├── pseint/                      # Programas PSeInt (.psc) del módulo (cuando aplica)
└── dfd/                         # Diagramas de flujo del módulo (cuando aplica)
```

El Markdown existe como copia de lectura rápida y para que el contenido sea indexable por herramientas como editores o asistentes; el LaTeX es la fuente que produce los PDF.

---

## 7. Los nueve módulos en detalle

### Tabla resumen

| Módulo | Duración | Páginas | Eje pedagógico | Resueltos | Propuestos |
| :--- | :---: | :---: | :--- | :---: | :---: |
| **M00** Algoritmos Para Tontos | 2.5 h | 14 | Perder el miedo, pensar antes de teclear | 4 | 8 |
| **M01** Lógica y DFD | 3.0 h | 15 | Símbolos, reglas y prueba de escritorio | 6 | 10 |
| **M02** PSeInt y Puente a C++ | 3.0 h | 20 | Traducción DFD ↔ PSeInt ↔ C++ | 6 | 10 |
| **M03** Tipos de Datos y Operadores | 3.0 h | 29 | Memoria, tipos, aritmética y casting | 7 | 12 |
| **M04** Condicionales | 3.5 h | 54 | Lógica booleana, `if`, `switch` | 8 | 14 |
| **M05** Ciclos y Bucles | 4.0 h | 59 | `for`, `while`, `do-while`, centinelas | 10 | 16 |
| **M06** Vectores Estáticos | 4.0 h | 35 | Patrones de arreglos 1D y Burbuja | 8 | 14 |
| **M07** Matrices Estáticas | 4.0 h | 36 | Recorridos 2D, diagonales, simetría | 8 | 14 |
| **M08** Modularidad y Simulacros | 3.0 h | 31 | Funciones, anti-pánico, 2 simulacros | 4 + 2 simulacros | 4 |
| **Total** | **30.0 h** | **293** | | **61 + 2** | **102** |

---

### M00 — Algoritmos Para Tontos (2.5 h)

**Objetivo:** que el estudiante entienda qué es un algoritmo y aprenda a analizar un enunciado antes de escribir código.

Contenido:

1. Qué es un algoritmo, contado con la analogía del "genio literal".
2. Cinco analogías completas: café con leche, domicilio de hamburguesa, cajero automático, mueble LEGO y maleta según el clima.
3. El modelo **EPS** (Entradas–Proceso–Salidas) y el diccionario de palabras clave de los enunciados.
4. El Método de los 5 Pasos del monitor.
5. El método aplicado a cuatro problemas completos (pizza entre amigos, cine con decisión, nota ponderada, tiempo de viaje).
6. Los cinco errores clásicos de principiante.
7. Ocho ejercicios propuestos de lógica pura (sin código) y su solucionario.

Este módulo no incluye C++ a propósito: se puede dictar con tablero y papel.

---

### M01 — Lógica y Diagramas de Flujo (3.0 h)

**Objetivo:** representar un algoritmo de forma visual, universal y verificable.

Contenido:

1. Qué es un DFD y por qué existe.
2. Todos los símbolos oficiales: óvalo de inicio/fin, paralelogramo de lectura, rectángulo de proceso, rombo de decisión, salida.
3. Las **7 reglas de oro** de un DFD limpio (un solo inicio y fin, flechas con sentido, rombos etiquetados, convergencia, inicializar antes del ciclo, entre otras).
4. Cómo hacer una prueba de escritorio sobre un DFD.
5. Seis problemas resueltos paso a paso en DFD.
6. Diez ejercicios propuestos con pistas y solucionario.

Artefactos: carpeta `dfd/` con seis diagramas en PNG:

- promedio de notas
- área y perímetro de una cancha
- salario neto con descuento del 8 %
- aprueba o reprueba materia
- descuento en papelería
- mayor de dos números

---

### M02 — PSeInt y el Puente hacia C++ (3.0 h)

**Objetivo:** convertir el diagrama en código sin perder la lógica en el camino.

Contenido:

1. Por qué PSeInt antes de C++.
2. Instalación y configuración de PSeInt (incluida la recomendación de usar perfil estricto para forzar la declaración de variables).
3. **Tabla maestra de traducción** DFD ↔ PSeInt ↔ C++.
4. Anatomía de un programa C++ línea por línea: `#include`, `using namespace std;`, `int main()`, `return 0;`.
5. Traducción de errores de compilación al español (el "traductor de errores").
6. Seis ejemplos completos, cada uno con su versión `.psc` y su versión `.cpp`:

| Ejemplo | PSeInt | C++ |
| :--- | :--- | :--- |
| Saludo y suma | `01_saludo_y_suma.psc` | `01_saludo_y_suma.cpp` |
| Promedio de notas | `02_promedio_notas.psc` | `02_promedio_notas.cpp` |
| Rectángulo / terreno | `03_rectangulo_terreno.psc` | `03_rectangulo_terreno.cpp` |
| Conversión de temperatura | `04_conversion_temperatura.psc` | `04_conversion_temperatura.cpp` |
| Factura de cafetería | `05_factura_cafeteria.psc` | `05_factura_cafeteria.cpp` |
| Salario semanal | `06_salario_semanal.psc` | `06_salario_semanal.cpp` |

7. Diez ejercicios propuestos de traducción y depuración, con solucionario.

---

### M03 — Tipos de Datos y Operadores (3.0 h)

**Objetivo:** entender que una variable es una caja en memoria con nombre, tamaño y tipo.

Contenido:

1. La memoria RAM explicada con cajas y una ilustración propia.
2. Tipos fundamentales en PSeInt y C++: `int`, `float`, `double`, `char`, `bool`, `string`.
3. La diferencia entre `cin >>` y `getline()` y por qué hace falta `cin.ignore()`.
4. Constantes con `const` y la prohibición de los "números mágicos".
5. Operadores aritméticos y asignación compuesta.
6. **División entera vs. división real**: `5 / 2` da `2` en C++ y `2.5` en PSeInt.
7. El operador módulo (`%` / `MOD`) y sus usos típicos.
8. Precedencia de operadores y traducción de fórmulas matemáticas.
9. Casting básico.
10. Siete problemas resueltos y doce propuestos, todos con versión `.psc` y `.cpp`.

Los siete resueltos cubren casos muy reconocibles en parciales: desglose de billetes, conversión de segundos, promedio ponderado con `getline`, física básica (MRUV y energía cinética), IMC con casting, factura con IVA y extracción de dígitos.

---

### M04 — Estructuras Condicionales (3.5 h)

**Objetivo:** tomar decisiones correctas y saber traducir un enunciado a condiciones booleanas.

Contenido:

1. Qué es una decisión en programación.
2. Lógica booleana y tablas de verdad con `&&`, `||` y `!`.
3. **La trampa mortal de los rangos**: `10 <= x <= 20` no significa lo que parece en C++.
4. Las cinco estructuras condicionales en DFD, PSeInt y C++: `if`, `if-else`, escalera `else-if`, `if` anidados y `switch-case`.
5. Diccionario traductor de enunciados de parcial ("si el cliente es socio y compra más de…").
6. Ocho problemas resueltos: portero numérico, filtro de beca, podio de atletas, factura escalonada de energía, cajero con `switch`, tienda con `switch` de `char`, clasificación de triángulos y año bisiesto.
7. Catorce ejercicios propuestos con pista y solucionario.

Artefactos: nueve diagramas de flujo propios del módulo y ocho pares `.psc` / `.cpp`.

---

### M05 — Ciclos y Bucles (4.0 h)

**Objetivo:** dominar la repetición sin usar arreglos todavía.

Contenido:

1. Qué es un ciclo y los tres ingredientes obligatorios: inicialización, condición y actualización.
2. Los tres ciclos frente a frente en DFD, PSeInt y C++.
3. Guía de cuándo usar `for`, `while` o `do-while`.
4. **La trampa mortal de parcial:** `Repetir...Hasta Que` en PSeInt termina cuando la condición es verdadera; `do...while` en C++ continúa mientras sea verdadera. Hay que negar la condición al traducir.
5. Los seis errores clásicos de parcial.
6. Caja de herramientas sin arreglos: contadores, acumuladores, banderas, máximo y mínimo, centinelas, ciclos anidados.
7. Diez problemas resueltos y dieciséis propuestos con solucionario.

Es el módulo más extenso en texto (59 páginas y 1.593 líneas de LaTeX), porque es donde más estudiantes se pierden.

---

### M06 — Vectores Estáticos (4.0 h)

**Objetivo:** manejar arreglos de una dimensión con capacidad fija y los patrones que se repiten en todos los parciales.

Contenido:

1. Qué es un vector estático y la analogía de los casilleros.
2. La regla de oro: `const int MAX` y validación de `n`.
3. Declaración, inicialización y trampas clásicas.
4. Lectura y escritura con `for`.
5. Los **ocho patrones maestros obligatorios**: suma y promedio, conteo, máximo y mínimo con posición, búsqueda secuencial, invertir, rotar, insertar y eliminar.
6. Ordenamiento **Burbuja** paso a paso, con trazas de las iteraciones.
7. Ocho problemas resueltos completos y catorce propuestos.

Cada problema resuelto incluye EPS, versión PSeInt, versión C++ y prueba de escritorio.

---

### M07 — Matrices Estáticas (4.0 h)

**Objetivo:** extender todo lo aprendido a dos dimensiones.

Contenido:

1. Qué es una matriz estática: el edificio de filas y columnas.
2. Declaración e inicialización con `MAX_F` y `MAX_C`.
3. Recorrido por filas vs. recorrido por columnas y por qué el orden importa.
4. Patrones maestros: suma por fila, suma por columna, máximo con coordenadas, diagonales (`i == j` y `i + j == n - 1`), triangular superior e inferior, simetría y transpuesta.
5. Casos reales: notas de varios estudiantes en varias materias, ventas por sucursal, ocupación de un cine.
6. Ocho resueltos completos y catorce propuestos.

---

### M08 — Modularidad, Anti-Pánico y Simulacros (3.0 h)

**Objetivo:** cerrar el curso con funciones y con la preparación real para el parcial.

Contenido:

1. **Modularidad:** por qué no meter todo en `main()`, anatomía de una función en C++ vs. un `SubProceso` en PSeInt, paso por valor vs. paso por referencia (`&`), y cómo pasar vectores y matrices estáticas a funciones.
2. **Estrategia anti-pánico:**
   - cómo leer un enunciado largo en los primeros 8 minutos sin teclado,
   - reparto del tiempo en un parcial de 90 minutos,
   - checklist de 10 puntos antes de entregar,
   - los 12 errores mortales en DFD, PSeInt y C++.
3. **Simulacro 1 (Corte 1, 90 minutos, 100 puntos):**
   - control de peaje vehicular (25 pts),
   - parqueadero inteligente (35 pts),
   - monitor de temperaturas de invernadero (40 pts).
4. **Simulacro 2 (Corte Final, 90 minutos, 100 puntos):**
   - analizador numérico modular (25 pts),
   - inventario de tienda con vectores paralelos y Burbuja sincronizado (35 pts),
   - consumo energético de un edificio con matriz estática (40 pts).
5. Cuatro ejercicios express de modularidad con pistas y solucionario.
6. Checklist final de dominio del curso.

Cada punto de cada simulacro trae **rúbrica desglosada por criterio**, de modo que el estudiante puede autoevaluarse y el monitor puede calificar sin improvisar.

---

## 8. Material complementario

### 8.1 Las cuatro fichas resumen

Son hojas de una sola página pensadas para imprimir o tener abiertas en el celular mientras se resuelve un taller.

| Ficha | Contenido |
| :--- | :--- |
| **Ficha 01 — Símbolos y reglas de DFD** | Todos los símbolos oficiales, las reglas de oro y una lista de verificación para revisar un diagrama antes de entregarlo |
| **Ficha 02 — Traductor DFD ↔ PSeInt ↔ C++** | Tabla de equivalencias y las cinco trampas de traducción: ciclo invertido, índices 1 vs. 0, división entera, rangos encadenados e igualdad |
| **Ficha 03 — Método de los 5 Pasos y anti-pánico** | El método resumido, traducción de frases típicas de parcial a estructuras de control y checklist de examen |
| **Ficha 04 — Patrones de vectores y matrices** | Declaración estática obligatoria, firmas de funciones para pasar arreglos y matrices, y los patrones que siempre aparecen |

Cada ficha está en tres formatos: `.tex` (editable), `.pdf` (imprimible) y `.png` (para compartir por chat o proyectar).

### 8.2 Diagramas maestros

Once diagramas de alta resolución en `assets/diagramas/`:

| Archivo | Qué muestra |
| :--- | :--- |
| `dfd_00_simbolos_oficiales.png` | Lámina única con toda la simbología DFD |
| `dfd_01_suma_promedio.png` | DFD secuencial clásico |
| `dfd_02_mayor_tres_numeros.png` | Anidamiento de decisiones |
| `dfd_03_ciclo_mientras_centinela.png` | Ciclo con valor centinela |
| `dfd_04_ciclo_para_factorial.png` | Ciclo `Para` con acumulador |
| `dfd_05_vector_estatico_busqueda.png` | Recorrido de vector con búsqueda |
| `mem_01_variables_ram.png` | Variables como cajas en memoria |
| `mem_02_puente_ciclos.png` | Equivalencia entre los tres ciclos |
| `mem_03_vector_estatico_1d.png` | Índices, capacidad y casilleros |
| `mem_04_matriz_estatica_2d.png` | Filas, columnas y coordenadas |
| `met_01_cinco_pasos_analisis.png` | El Método de los 5 Pasos en una imagen |

Los diagramas no son capturas de pantalla: se generan con **scripts Python** propios que usan Cairo y PIL (`assets/diagramas/_gen/`). Eso permite regenerarlos o modificarlos sin volver a dibujarlos a mano.

### 8.3 Ilustraciones conceptuales

Tres ilustraciones en `assets/ilustraciones/`:

- `ilus_01_algoritmo_receta.jpg`: el algoritmo como receta.
- `ilus_02_variables_ram.jpg`: las variables como cajas en RAM.
- `ilus_03_puente_dfd_pseint_cpp.jpg`: el puente entre DFD, PSeInt y C++.

Se usan como portada de sección y como disparador visual al inicio de cada sesión.

### 8.4 Diagramas por módulo

Además de los maestros, hay diagramas específicos dentro de los módulos:

- `M01/dfd/`: 6 diagramas.
- `M04/dfd/`: 9 diagramas.
- `M05/dfd/`: 8 diagramas.

---

## 9. El libro unificado

`LIBRO_COMPLETO_MONITORIA_30H.pdf` es la compilación de todo el curso en un solo documento de **300 páginas**, pensado para imprimir como cuaderno o para distribuir como archivo único.

Cómo está armado (`LIBRO_COMPLETO_MONITORIA_30H.tex`):

1. Portada con la ilustración del puente DFD → PSeInt → C++.
2. Índice general con marcadores de PDF.
3. Los nueve módulos insertados como PDF completos mediante `\includepdf`.
4. Las cuatro fichas resumen al final, también insertadas como PDF.

Detalle técnico: el libro **no recompila** el contenido de cada módulo, sino que **inserta los PDF ya compilados**. La consecuencia práctica es importante:

- Para cambiar el libro hay que recompilar primero el módulo afectado y después el libro.
- Los módulos conservan exactamente el mismo diseño que tienen por separado.
- El libro pesa ~17 MB porque contiene todas las imágenes a resolución de impresión.

---

## 10. El portal web `index.html`

Es un archivo único de 2.267 líneas, sin dependencias externas ni conexión a internet: se abre haciendo doble clic y funciona. Todo el CSS y el JavaScript están embebidos.

Secciones:

| Sección | Función |
| :--- | :--- |
| **Inicio / hero** | Presentación del curso, sus cifras y la ruta de aprendizaje |
| **Buscador rápido** | Búsqueda con filtros por tipo: ejercicio, patrón, trampa, consejo o simulacro |
| **Módulos** | Tarjetas de M00 a M08 con filtro por etapa: fundamentos, control o estructuras |
| **Fichas** | Acceso directo a las cuatro fichas en PDF y PNG |
| **Galería** | Visor con lightbox para diagramas, DFD, ilustraciones y fichas |
| **Ruta de 30 horas** | Checklist interactivo de las 15 sesiones de 2 horas |

Características destacables:

- El **checklist de sesiones** guarda el progreso del estudiante en el navegador.
- El **lightbox** permite ver cualquier diagrama a pantalla completa sin salir de la página.
- El **buscador** indexa los recursos por etiqueta semántica, no solo por nombre de archivo.
- La paleta visual es la misma del material impreso (azul marino, turquesa, naranja, rojo y verde), de modo que el estudiante reconoce los mismos códigos de color en pantalla y en papel.

---

## 11. La hoja de estilo LaTeX

`latex_common/estilo_monitoria.sty` es el archivo que le da identidad visual a todo el curso y garantiza que los nueve módulos se vean como un mismo producto.

Decisiones técnicas y su por qué:

| Decisión | Motivo |
| :--- | :--- |
| **XeLaTeX** con `fontspec` | Soporte nativo de UTF-8 para tildes, `ñ`, `→`, `≤` y símbolos de C++ |
| Fuente **Inter** para texto y **DejaVu Sans Mono** para código | Inter es muy legible en pantalla; DejaVu Mono distingue bien `l`, `1` e `I` |
| `babel` con `es-tabla,es-noshorthands` | Cambia "Cuadro" por "Tabla" y evita conflictos con `<<`, `>>` y `->` de C++ |
| Paleta de 13 colores con nombre semántico | Coherencia entre PDF, portal web y fichas |
| Siete `tcolorbox` semánticas | Cada tipo de contenido se reconoce por color |
| `listings` configurado para C++ y PSeInt | Resaltado de sintaxis legible, con comentarios en gris |
| Opción `ficha` del paquete | Reutiliza el mismo estilo con márgenes reducidos para las hojas de una página |
| `microtype` | Mejor justificación y menos ríos de espacio |

La existencia de este archivo es lo que permite que un cambio de color o de tipografía se propague a todo el curso recompilando, en lugar de editar nueve documentos a mano.

---

## 12. Inventario de código C++ y PSeInt

### 12.1 Distribución

| Módulo | `.cpp` | `.psc` |
| :--- | :---: | :---: |
| M02 PSeInt y puente a C++ | 6 | 6 |
| M03 Tipos de datos | 7 | 7 |
| M04 Condicionales | 8 | 8 |
| M05 Ciclos | 10 | 10 |
| M06 Vectores | 8 | 8 |
| M07 Matrices | 8 | 8 |
| M08 Modularidad | 10 | — |
| **Total** | **57** | **47** |

Los `.cpp` de `M08` no tienen pareja en PSeInt porque el módulo se centra en funciones de C++ y en los simulacros.

### 12.2 Estándar de los programas C++

Todos los programas están escritos en C++ estándar, sin extensiones, y se verificaron con:

```bash
g++ -std=c++17 -Wall -Wextra -Werror -fsyntax-only archivo.cpp
```

Es decir: **compilan sin una sola advertencia** bajo `-Wall -Wextra -Werror`. Esto no es un detalle cosmético; significa que el material no enseña vicios como variables sin usar, comparaciones entre tipos distintos o funciones sin retorno.

Convenciones que se mantienen en todo el código:

- `#include` explícitos y en orden.
- `using namespace std;` solo en programas de nivel básico, con la advertencia correspondiente.
- Nombres de variables en español y descriptivos (`promedio`, `notaFinal`, `contadorAprobados`).
- Comentarios que explican el **porqué**, no el qué.
- `const int MAX` en lugar de números mágicos.
- Validación de entrada con ciclos cuando el dato lo requiere.

### 12.3 Estándar de los programas PSeInt

Los `.psc` usan la sintaxis en español y están pensados para abrirse directamente en PSeInt:

- `Algoritmo` / `FinAlgoritmo`
- `Definir ... Como Entero/Real/Caracter/Logico`
- `Leer`, `Escribir`, `Si ... Entonces`, `Segun ... De Otro Modo`
- `Mientras`, `Repetir ... Hasta Que`, `Para`
- `Dimension` para arreglos

Se recomienda configurar PSeInt en **perfil estricto** para que exija declarar variables, igual que C++.

---

## 13. El plan de 15 sesiones

El curso se dicta en 15 encuentros de 2 horas. El reparto de horas es exacto y suma 30.0:

| Módulo | Horas | Sesiones que lo cubren |
| :--- | :---: | :--- |
| M00 | 2.5 h | S01 (2.0 h) + S02 (0.5 h) |
| M01 | 3.0 h | S02 (1.5 h) + S03 (1.5 h) |
| M02 | 3.0 h | S03 (0.5 h) + S04 (2.0 h) + S05 (0.5 h) |
| M03 | 3.0 h | S05 (1.5 h) + S06 (1.5 h) |
| M04 | 3.5 h | S06 (0.5 h) + S07 (2.0 h) + S08 (1.0 h) |
| M05 | 4.0 h | S08 (1.0 h) + S09 (2.0 h) + S10 (1.0 h) |
| M06 | 4.0 h | S10 (1.0 h) + S11 (2.0 h) + S12 (1.0 h) |
| M07 | 4.0 h | S12 (1.0 h) + S13 (2.0 h) + S14 (1.0 h) |
| M08 | 3.0 h | S14 (1.0 h) + S15 (2.0 h) |
| **Total** | **30.0 h** | **15 × 2.0 h** |

Ritmo estándar de cada sesión de 120 minutos:

| Minutos | Fase |
| :---: | :--- |
| 00–15 | Enganche: pregunta, reto o error provocado |
| 15–55 | Explicación visual: DFD → PSeInt → C++ |
| 55–95 | Práctica guiada en tablero y en vivo |
| 95–110 | Errores típicos que cazar |
| 110–120 | Cierre y tarea |

**Nota sobre el archivo del plan:** el documento original `PLAN_30_HORAS.md`, con el guion minuto a minuto de las 15 sesiones, se retiró del repositorio en el commit `5b62c46` (*"chore: eliminar plan interno de trabajo"*). Se puede recuperar en cualquier momento desde el historial:

```bash
git show 5b62c46~1:PLAN_30_HORAS.md > PLAN_30_HORAS.md
```

El cronograma resumido sigue disponible en el `README.md` y en el checklist interactivo del portal web.

---

## 14. Cómo se verificó la calidad

El material no se entregó "a ojo". Estos son los controles aplicados:

| Control | Herramienta | Resultado |
| :--- | :--- | :--- |
| Compilación limpia de los 57 programas C++ | `g++ -std=c++17 -Wall -Wextra -Werror` | Sin errores ni advertencias |
| Conteo de páginas de cada PDF | `pdfinfo` | 293 páginas de módulos + 4 fichas + 300 del libro |
| Coherencia de horas | Suma manual y en tablas | 2.5 + 3 + 3 + 3 + 3.5 + 4 + 4 + 4 + 3 = 30.0 |
| Coherencia de diseño | Hoja de estilo única compartida | Los nueve módulos usan la misma paleta y tipografía |
| Enlaces del portal | Script de verificación de rutas | 99 rutas referenciadas, 0 faltantes |
| Autocontención del portal | Búsqueda de URLs externas | Ninguna: funciona sin internet |
| Ejercicios con solucionario | Revisión módulo por módulo | 102 propuestos, todos con solución |
| Rúbricas de simulacro | Suma de puntajes | Cada simulacro suma exactamente 100 puntos |

El conteo de páginas por módulo es:

| Módulo | Páginas |
| :--- | :---: |
| M00 | 14 |
| M01 | 15 |
| M02 | 20 |
| M03 | 29 |
| M04 | 54 |
| M05 | 59 |
| M06 | 35 |
| M07 | 36 |
| M08 | 31 |
| Fichas | 4 |
| **Subtotal** | **297** |
| Libro (con portada e índice) | **300** |

---

## 15. Cómo reproducir y editar el material

### 15.1 Compilar un módulo

```bash
cd modulos/M05_Ciclos_y_Bucles
xelatex -interaction=nonstopmode M05_Ciclos_y_Bucles.tex
xelatex -interaction=nonstopmode M05_Ciclos_y_Bucles.tex
```

Se compila dos veces porque la primera pasada genera el índice y los contadores internos, y la segunda los resuelve. Requisitos: TeX Live con `xelatex`, `fontspec`, `tcolorbox`, `listings`, `tikz` y las fuentes **Inter** y **DejaVu Sans Mono**.

### 15.2 Recompilar las fichas

```bash
cd fichas_resumen
xelatex -interaction=nonstopmode Ficha_01_Simbolos_DFD.tex
```

La opción que activa los márgenes reducidos ya está declarada dentro de cada ficha.

### 15.3 Reconstruir el libro completo

Primero recompilar todos los módulos y las fichas, y después:

```bash
xelatex -interaction=nonstopmode LIBRO_COMPLETO_MONITORIA_30H.tex
```

El libro inserta los PDF ya compilados, así que no hay que tocar su `.tex` salvo que cambie el orden o se agregue una sección.

### 15.4 Compilar y ejecutar un programa C++

```bash
g++ -std=c++17 -Wall -Wextra archivo.cpp -o programa
./programa
```

En Windows con Dev-C++ o Code::Blocks: abrir el `.cpp`, verificar que el estándar sea C++11 o C++17 y presionar compilar y ejecutar.

### 15.5 Regenerar los diagramas

Los diagramas maestros se generan con Python:

```bash
cd assets/diagramas/_gen
python3 gen_dfd_part1.py
python3 gen_dfd_part2.py
python3 gen_mem_met.py
```

Requieren Cairo y Pillow. `draw_lib.py` contiene las utilidades de dibujo vectorial compartidas: cajas, flechas, rombos, texto y exportación a PNG.

### 15.6 Abrir el portal

No requiere servidor:

```bash
xdg-open index.html   # Linux
open index.html       # macOS
start index.html      # Windows
```

---

## 16. Estado del repositorio y de Git

| Dato | Valor |
| :--- | :--- |
| Remoto | `git@github.com:jfmiyox/monitoriasAlgoritmoYProgramacion.git` |
| Autenticación | SSH |
| Rama | `main`, rastrea `origin/main` |
| Commits | `6b86c10` (material completo) y `5b62c46` (eliminación del plan interno) |
| Archivos rastreados | 190 |
| Tamaño del historial | ~45 MB |
| Archivo más pesado | `LIBRO_COMPLETO_MONITORIA_30H.pdf` (~17 MB) |

Archivos y carpetas excluidos por `.gitignore`:

- Temporales de LaTeX: `.aux`, `.log`, `.toc`, `.out`, `.fls`, `.fdb_latexmk`, `.synctex.gz`, `.nav`, `.snm`, `.vrb`.
- Binarios de C++: `.o`, `.obj`, `.exe`, `a.out`.
- Python: `__pycache__/`, `.py[cod]`.
- Editores y sistema: `.vscode/`, `.idea/`, `.DS_Store`, `Thumbs.db`, `*~`.
- Configuraciones locales de agentes: `.agents/`, `.opencode/`, `.gemini/`, `.claude/`, `.codex/`, `AGENTS.md`, `GEMINI.md`, `CLAUDE.md`, `opencode.jsonc`.

Nota sobre el historial: el mensaje del primer commit se reescribió para cambiar "curso completo de monitoria 30h" por **"30 horas de contenido multimedia"**. Los hashes cambiaron en ese momento (`55334a2` → `6b86c10`) y se hizo `--force-with-lease`, que solo reemplaza el remoto si nadie más ha subido cambios.

---

## 17. Cómo usar el material en clase

Para el monitor o docente:

1. **Planificar con el cronograma de 15 sesiones.** Cada encuentro tiene un eje claro y una duración exacta; no hay que decidir qué dictar el día anterior.
2. **Proyectar primero la idea, después el código.** Abrir siempre con la analogía del módulo, pasar al DFD, luego a PSeInt, hacer la prueba de escritorio con el grupo y solo al final mostrar C++.
3. **Usar las cajas rojas como guion de errores.** Cada "OJO: trampa clásica de parcial" es una oportunidad de provocar el error en vivo y dejar que los estudiantes lo detecten.
4. **Imprimir o compartir las fichas.** Son el material de apoyo natural durante talleres y parciales.
5. **Cerrar con M08.** Los dos simulacros cronometrados y la rúbrica permiten llegar al examen oficial con el formato ya ensayado.

Sugerencia de dinámica por sesión:

- **Enganche (15 min):** una pregunta incómoda o un código roto para diagnosticar.
- **Explicación (40 min):** tablero + PDF proyectado + ilustración.
- **Práctica (40 min):** resolver un problema nuevo entre todos, sin copiar del solucionario.
- **Errores (15 min):** cazar en vivo los errores del módulo.
- **Cierre (10 min):** recapitular y asignar tarea del banco de ejercicios.

---

## 18. Cómo usar el material para estudiar

Para el estudiante:

1. **No saltarse M00 y M01.** Casi todos los bloqueos posteriores vienen de no saber analizar, no de no saber sintaxis.
2. **Aplicar la regla de los 3 borradores** antes de abrir el compilador: tabla EPS en papel, DFD o esbozo en PSeInt, y prueba de escritorio con 2 o 3 datos pequeños.
3. **Leer por colores:** azul para entender, verde para verificar, rojo para no perder puntos.
4. **Modificar los programas.** Abrir los `.cpp` de cada módulo, cambiar entradas y predecir qué pasará antes de ejecutar.
5. **Autoevaluarse con los simulacros.** Cronometrar 90 minutos, resolver sin mirar el solucionario y calificar con la rúbrica.
6. **Usar las fichas como filtro final.** Si puedes explicar cada punto de la ficha sin mirar el cuaderno, estás listo para el parcial.

Ruta mínima de repaso antes de un parcial:

```
Ficha 03 (método y anti-pánico)
  → Ficha 01 (si el parcial pide DFD)
  → Ficha 02 (si pide traducción)
  → Ficha 04 (si pide arreglos)
  → Simulacro correspondiente
```

---

## 19. Pendientes y próximos pasos

Cosas que quedan abiertas y que conviene atender:

1. **El `README.md` todavía enlaza a `PLAN_30_HORAS.md`**, que se eliminó del repositorio. Hay dos opciones: restaurar el archivo o actualizar los enlaces del README al cronograma del portal web.
2. **Los nombres de archivo conservan "MONITORIA"**: `LIBRO_COMPLETO_MONITORIA_30H.*` y `latex_common/estilo_monitoria.sty`. Si el curso se va a presentar como "contenido multimedia", habría que renombrarlos y actualizar las referencias.
3. **No hay licencia explícita.** Si el material va a circular fuera de la universidad, conviene agregar un archivo `LICENSE`.
4. **El libro y los módulos se compilan a mano.** Un `Makefile` o un script `build.sh` ahorraría errores cuando se edite más de un módulo.
5. **Los `.png` de las fichas se generan aparte de los PDF.** Conviene documentar o automatizar ese paso.
6. **No hay pruebas automáticas del portal.** Un script que verifique que todas las rutas del `index.html` existen evitaría enlaces rotos al mover archivos.

---

## 20. Glosario

| Término | Significado en este proyecto |
| :--- | :--- |
| **Algoritmo** | Secuencia finita, ordenada y sin ambigüedad de pasos para resolver un problema |
| **DFD** | Diagrama de Flujo de Datos: representación visual de un algoritmo con símbolos estándar |
| **PSeInt** | Intérprete de pseudocódigo en español usado como paso intermedio antes de C++ |
| **EPS** | Entradas, Proceso y Salidas: tabla de análisis previa a cualquier código |
| **Prueba de escritorio** | Simulación manual de un algoritmo con datos concretos, anotando el valor de cada variable |
| **Vector estático** | Arreglo de una dimensión con capacidad fija definida en compilación |
| **Matriz estática** | Arreglo de dos dimensiones con capacidad fija definida en compilación |
| **VLA** | Arreglo de longitud variable no estándar (`int v[n];`), prohibido en este curso |
| **Centinela** | Valor especial que marca el final de una secuencia de datos |
| **Burbuja** | Algoritmo de ordenamiento que intercambia vecinos hasta que el arreglo queda ordenado |
| **Rúbrica** | Desglose de puntos por criterio usado para calificar un simulacro |
| **Ficha** | Hoja de una página con lo esencial de un tema, para repaso rápido |

---

### Cierre

En conjunto, el repositorio contiene un curso completo y autoconsistente: **30 horas de contenido multimedia** repartidas en nueve módulos, con teoría, diagramas, pseudocódigo, código C++ verificado, ejercicios, solucionarios, dos simulacros de parcial, cuatro fichas imprimibles, un libro de 300 páginas y un portal web que funciona sin internet.

La idea central que atraviesa todo el material es sencilla: **programar es pensar con orden antes de escribir**. El DFD, PSeInt y C++ son solo tres formas de decir lo mismo; el curso enseña a pensarlo primero.
