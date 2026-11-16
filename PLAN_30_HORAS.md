# Plan Maestro de Monitoría — 30.0 Horas (15 Sesiones de 2 Horas)

> **Curso:** Algoritmos y Programación (DFD $\rightarrow$ PSeInt $\rightarrow$ C++ Básico hasta Vectores y Matrices Estáticos)  
> **Duración total:** **30.0 horas exactas** = 15 sesiones presenciales/virtuales de 120 minutos (2.0 h cada una)  
> **Frontera técnica:** C++ básico (`<iostream>`, `<iomanip>`, `<cmath>`, `<string>`), arreglos y matrices **estáticos** con capacidad fija definida (`const int MAX = ...`). **Sin** memoria dinámica, punteros, `std::vector`, VLA ni POO.

---

## 1. Matriz de Horas: Módulos vs. Sesiones (Suma Exacta = 30.0 h)

### 1.1 Distribución por Módulo (`M00`–`M08`)

| Código | Módulo | Horas Totales | Sesiones que lo cubren |
| :---: | :--- | :---: | :--- |
| **M00** | `M00_Algoritmos_Para_Tontos` | **2.5 h** | S01 (2.0 h) + S02 (0.5 h) |
| **M01** | `M01_Logica_y_DFD` | **3.0 h** | S02 (1.5 h) + S03 (1.5 h) |
| **M02** | `M02_PSeInt_y_Puente_CPP` | **3.0 h** | S03 (0.5 h) + S04 (2.0 h) + S05 (0.5 h) |
| **M03** | `M03_Tipos_Datos_y_Operadores` | **3.0 h** | S05 (1.5 h) + S06 (1.5 h) |
| **M04** | `M04_Condicionales` | **3.5 h** | S06 (0.5 h) + S07 (2.0 h) + S08 (1.0 h) |
| **M05** | `M05_Ciclos_y_Bucles` | **4.0 h** | S08 (1.0 h) + S09 (2.0 h) + S10 (1.0 h) |
| **M06** | `M06_Vectores_Estaticos` | **4.0 h** | S10 (1.0 h) + S11 (2.0 h) + S12 (1.0 h) |
| **M07** | `M07_Matrices_Estaticas` | **4.0 h** | S12 (1.0 h) + S13 (2.0 h) + S14 (1.0 h) |
| **M08** | `M08_Modularidad_Parciales_y_Solucionario` | **3.0 h** | S14 (1.0 h) + S15 (2.0 h) |
| **TOTAL** | **9 Módulos Completos** | **30.0 h** | **15 sesiones × 2.0 h = 30.0 h** |

### 1.2 Cronograma Rápido de las 15 Sesiones

| Sesión | Duración | Bloque Temático y Distribución Exacta |
| :---: | :---: | :--- |
| **S01** | 2.0 h | **M00 (2.0 h):** Perder el miedo, analogías cotidianas, lógica secuencial y Método de los 5 Pasos (EPS) |
| **S02** | 2.0 h | **M00 (0.5 h) + M01 (1.5 h):** Cierre de análisis EPS + Símbolos oficiales de DFD y primeros diagramas secuenciales |
| **S03** | 2.0 h | **M01 (1.5 h) + M02 (0.5 h):** Decisiones en DFD, prueba de escritorio en papel + Bienvenida a PSeInt |
| **S04** | 2.0 h | **M02 (2.0 h):** Puente DFD $\rightarrow$ PSeInt $\rightarrow$ C++ básico, anatomía de `main()` y lectura de errores |
| **S05** | 2.0 h | **M02 (0.5 h) + M03 (1.5 h):** Cierre de ejercicios duales + Memoria RAM "para tontos" (`int`, `double`, `char`, `bool`, `string`, `cin.ignore()`) |
| **S06** | 2.0 h | **M03 (1.5 h) + M04 (0.5 h):** Aritmética (`/` entera vs real, `%`, casting) + Introducción a lógica booleana (`&&`, `||`, `!`) |
| **S07** | 2.0 h | **M04 (2.0 h):** `if`, `if-else`, escalera `else-if`, trampa `10 <= x && x <= 20` y diccionario traductor de enunciados |
| **S08** | 2.0 h | **M04 (1.0 h) + M05 (1.0 h):** `if` anidados y `switch-case` + Primeros ciclos (`while` / `Mientras` con contadores y centinela) |
| **S09** | 2.0 h | **M05 (2.0 h):** `for`, `while`, `do-while`, trampa `Repetir...Hasta Que` vs `do-while`, banderas y máx/mín sin arreglos |
| **S10** | 2.0 h | **M05 (1.0 h) + M06 (1.0 h):** Ciclos anidados + Bienvenida a Vectores Estáticos (`const int MAX`, índices `0..n-1`) |
| **S11** | 2.0 h | **M06 (2.0 h):** Patrones maestros en vectores estáticos (búsqueda secuencial, invertir, rotar, insertar y eliminar con `MAX`) |
| **S12** | 2.0 h | **M06 (1.0 h) + M07 (1.0 h):** Ordenamiento Burbuja paso a paso + Bienvenida a Matrices Estáticas (`mat[MAX_F][MAX_C]`) |
| **S13** | 2.0 h | **M07 (2.0 h):** Recorridos por filas vs columnas, coordenadas máx/mín y matrices cuadradas (diagonales, simetría, transpuesta) |
| **S14** | 2.0 h | **M07 (1.0 h) + M08 (1.0 h):** Casos reales 2D (notas, ventas, cine) + Funciones/SubProcesos pasando vectores y matrices estáticos |
| **S15** | 2.0 h | **M08 (2.0 h):** Estrategia Anti-Pánico en Parciales, Simulacro Corte 1 y Corte Final, checklist de 10 puntos y cierre |

---

## 2. Guion Minuto a Minuto para el Monitor (15 Sesiones)

> **Ritmo estándar de cada sesión (120 min):**  
> `00–15` Enganche $\rightarrow$ `15–55` Explicación visual (`DFD -> PSeInt -> C++`) $\rightarrow$ `55–95` Práctica guiada $\rightarrow$ `95–110` Errores típicos a cazar $\rightarrow$ `110–120` Cierre y tarea.

---

### Sesión 1 (2.0 h) — Perdiendo el miedo: pensar como computadora y Método de los 5 Pasos
- **Cobertura:** `M00_Algoritmos_Para_Tontos` (2.0 h de 2.5 h).
- **Material de apoyo:** `M00_Algoritmos_Para_Tontos.pdf`, `assets/ilustraciones/ilus_01_algoritmo_receta.jpg`, `fichas_resumen/Ficha_03_*`.

| Minutos | Fase | Guion del Monitor |
| :---: | :--- | :--- |
| **00–15** | **Enganche** | Pide a dos voluntarios que te den instrucciones literales para "preparar un sándwich" o "lavarse los dientes". Ejecuta literalmente lo que digan (ej. si dicen "pon el queso sobre el pan" sin abrir el paquete, apoya el paquete cerrado). Remata: *"La computadora no es inteligente: es obediente al extremo"*. |
| **15–55** | **Explicación** | Proyecta `ilus_01_algoritmo_receta.jpg`. Explica qué es un **algoritmo** (entrada $\rightarrow$ transformación finita y ordenada $\rightarrow$ salida). Introduce el **Método de los 5 Pasos**: (1) Leer y subrayar verbos/datos, (2) Tabla **EPS** (Entradas–Proceso–Salidas), (3) Elegir herramientas, (4) Prueba de escritorio en papel, (5) Traducir a DFD/código. |
| **55–95** | **Práctica guiada** | Resuelve en tablero 2 problemas de `M00` sin tocar código todavía (ej. calcular nota definitiva con porcentajes y repartir propina entre amigos). Haz que los estudiantes llenen primero la columna **Salidas** antes de **Entradas** para que descubran qué falta pedir. |
| **95–110** | **Errores típicos** | Caza el error clásico #1: *"inventarse datos que el enunciado no da"* o *"empezar a escribir código antes de saber qué fórmula usar"*. Muestra cómo un enunciado con "ruido" (nombres de personajes, historias largas) se reduce a 3 líneas EPS. |
| **110–120** | **Cierre y tarea** | Recapitula los 5 pasos en voz alta. **Tarea:** resolver en cuaderno la tabla EPS y secuencia lógica de los ejercicios 1 a 4 de `M00`. |

---

### Sesión 2 (2.0 h) — Cierre EPS y los Símbolos Oficiales de DFD
- **Cobertura:** `M00` (0.5 h cierre $\rightarrow$ **2.5 h**) + `M01_Logica_y_DFD` (1.5 h de 3.0 h).
- **Material de apoyo:** `M00`, `M01_Logica_y_DFD.pdf`, diagramas de `assets/diagramas/`, `fichas_resumen/Ficha_01_*`.

| Minutos | Fase | Guion del Monitor |
| :---: | :--- | :--- |
| **00–15** | **Enganche** | Revisa rápidamente 2 tablas EPS de la tarea. Lanza el reto: *"¿Cómo explicarle este algoritmo a un compañero en otro país sin usar ni español ni C++?"* $\rightarrow$ introduce la necesidad de un mapa visual universal: el **DFD**. |
| **15–55** | **Explicación** | Cierra `M00` (30 min: último ejemplo completo con los 5 pasos). Pasa a `M01`: presenta la lámina de **símbolos oficiales DFD** (Óvalo Inicio/Fin, Paralelogramo/Trapecio Lectura, Rectángulo Proceso/Asignación `<-`, Rombo Decisión `Sí/No`, Cono/Documento Salida). Enseña las 4 reglas de oro del DFD limpio (un Inicio, un Fin, flechas con dirección clara, nunca cruzar líneas sin necesidad). |
| **55–95** | **Práctica guiada** | Dibuja en tablero paso a paso el DFD de **suma y promedio de 3 notas** y el de **conversión de temperatura o área de triángulo**. Pasa de inmediato a una primera **decisión simple** (¿aprobó si `prom >= 3.0`?) mostrando las dos ramas del rombo. |
| **95–110** | **Errores típicos** | Caza los 3 errores mortales en DFD de parcial: (1) dejar ramas del rombo sueltas sin volver al flujo o sin cerrar, (2) poner `=` en vez de `<-` o `Escribir` dentro de un rectángulo, (3) olvidar la lectura antes de usar la variable en la fórmula. |
| **110–120** | **Cierre y tarea** | Entrega o proyecta la `Ficha_01` de símbolos DFD. **Tarea:** dibujar en hoja cuadriculada los ejercicios 1 a 4 de `M01` (secuenciales y decisión simple). |

---

### Sesión 3 (2.0 h) — Decisiones en DFD, Prueba de Escritorio y Bienvenida a PSeInt
- **Cobertura:** `M01` (1.5 h cierre $\rightarrow$ **3.0 h**) + `M02_PSeInt_y_Puente_CPP` (0.5 h de 3.0 h).
- **Material de apoyo:** `M01`, `M02`, diagramas DFD de mayor de 3 números, `ilus_03_puente_dfd_pseint_cpp.jpg`.

| Minutos | Fase | Guion del Monitor |
| :---: | :--- | :--- |
| **00–15** | **Enganche** | Muestra en pantalla un DFD deliberadamente desordenado (con un cálculo antes de leer los datos y una rama sin salida). Reta al grupo a encontrar los 3 bugs en 3 minutos usando solo el dedo sobre la flecha. |
| **15–55** | **Explicación** | Resuelve el clásico **"Mayor de tres números A, B, C"** en DFD mostrando cómo se anidan los rombos y cómo se hace la **prueba de escritorio en papel** (tabla con columnas `A | B | C | Salida`) probando 3 casos: mayor al inicio, al medio y al final. |
| **55–95** | **Práctica guiada** | En los últimos 30 min del bloque práctico, abre **PSeInt** en vivo. Proyecta `ilus_03_puente_dfd_pseint_cpp.jpg` y traduce el mismo DFD del promedio y del mayor de dos números a `Algoritmo ... Definir ... Leer ... Si ... FinSi ... FinAlgoritmo`. Ejecuta paso a paso en PSeInt mostrando cómo la flecha verde recorre las líneas igual que el DFD. |
| **95–110** | **Errores típicos** | Advierte sobre configurar PSeInt en **perfil Estricto** (o declarar siempre con `Definir x Como Entero/Real;`), porque si se acostumbran a no declarar variables, luego sufrirán en C++. |
| **110–120** | **Cierre y tarea** | **Tarea:** completar ejercicios 5 a 10 de `M01` con su prueba de escritorio en papel, e instalar/probar PSeInt ejecutando el primer ejemplo de `M02/pseint/`. |

---

### Sesión 4 (2.0 h) — El Puente DFD $\rightarrow$ PSeInt $\rightarrow$ C++ Básico
- **Cobertura:** `M02_PSeInt_y_Puente_CPP` (2.0 h; acumulado M02 = 2.5 h de 3.0 h).
- **Material de apoyo:** `M02_PSeInt_y_Puente_CPP.pdf`, `fichas_resumen/Ficha_02_*`, ejemplos duales en `M02/pseint/` y `M02/cpp/`.

| Minutos | Fase | Guion del Monitor |
| :---: | :--- | :--- |
| **00–15** | **Enganche** | Compara dos pantallas lado a lado: un `.psc` de PSeInt y un `.cpp` básico que hacen exactamente lo mismo. Pregunta: *"¿Qué cambió de fondo y qué cambió solo de ropa?"* (El algoritmo es idéntico; solo cambia la "ropa" de la sintaxis). |
| **15–55** | **Explicación** | Usa la **Tabla Maestra de Traducción** (`Ficha_02`). Disecciona la anatomía mínima de C++ (`#include <iostream>`, `using namespace std;`, `int main() { ... return 0; }`). Explica `cout <<` (flechas saliendo hacia la pantalla) y `cin >>` (flechas entrando hacia la caja variable) con regla nemotécnica visual. |
| **55–95** | **Práctica guiada** | Toma 3 programas `.psc` de `M02` (saludo personalizado, cálculo de salario básico y área/perímetro) y tradúcelos línea por línea a `.cpp` frente al grupo. Compila con `g++` o Dev-C++ y ejecuta pruebas con consola real. |
| **95–110** | **Errores típicos** | Sección estrella: **"Traductor de errores de C++ al español"**. Provoca intencionalmente 5 errores en vivo: olvidar `;`, escribir `cout >>` al revés, no cerrar `"`, usar variable sin declarar, y escribir `Return 0;` con mayúscula. Enséñales a leer el **número de línea** del error. |
| **110–120** | **Cierre y tarea** | **Tarea:** traducir 4 ejercicios de `M02` desde `.psc` a `.cpp`, compilarlos localmente y anotar al menos un error que hayan corregido. |

---

### Sesión 5 (2.0 h) — Memoria RAM "Para Tontos" y Tipos de Datos
- **Cobertura:** `M02` (0.5 h cierre $\rightarrow$ **3.0 h**) + `M03_Tipos_Datos_y_Operadores` (1.5 h de 3.0 h).
- **Material de apoyo:** `M02`, `M03`, `assets/ilustraciones/ilus_02_variables_ram.jpg`, esquema de memoria RAM de `assets/diagramas/`.

| Minutos | Fase | Guion del Monitor |
| :---: | :--- | :--- |
| **00–15** | **Enganche** | Cierra dudas rápidas de compilación de `M02`. Saca una caja de zapatos, una taza, un frasco pequeño y un post-it: *"¿Guardarías sopa en un sobre de carta?"* $\rightarrow$ introducción a los tipos de datos. |
| **15–55** | **Explicación** | Proyecta `ilus_02_variables_ram.jpg`. Explica **qué es una variable en RAM** (nombre, tipo/tamaño, valor y basura inicial si no se inicializa). Presenta `int`, `float`, `double`, `char` (comillas simples `'A'`), `bool`, `string` (comillas dobles `"Ana"`) y constantes `const`. Dedica 10 minutos especiales a `cin >>` vs `getline(cin, nombre)` y por qué hace falta `cin.ignore()` después de leer un número! |
| **55–95** | **Práctica guiada** | Construye en vivo un programa de ficha de estudiante / factura simple en `M03/pseint/` y `M03/cpp/` que mezcle edad (`int`), promedio (`double`), inicial/género (`char`), becado (`bool`) y nombre completo con espacios (`getline` + `cin.ignore()`). |
| **95–110** | **Errores típicos** | Caza en vivo: (1) usar `int` para una nota `3.8` y ver cómo se trunca a `3`, (2) saltar la lectura de `getline` por olvidar `cin.ignore()`, (3) confundir `'5'` (`char`) con `5` (`int`). |
| **110–120** | **Cierre y tarea** | **Tarea:** ejercicios 1 a 5 de `M03` (elección de tipos y lectura mixta con `getline`). |

---

### Sesión 6 (2.0 h) — Aritmética sin Trampas y Primeros Operadores Lógicos
- **Cobertura:** `M03` (1.5 h cierre $\rightarrow$ **3.0 h**) + `M04_Condicionales` (0.5 h de 3.5 h).
- **Material de apoyo:** `M03/cpp/` (desglose de billetes, horas/min/seg, IMC, dígitos), `M04`.

| Minutos | Fase | Guion del Monitor |
| :---: | :--- | :--- |
| **00–15** | **Enganche** | Pregunta al salón: *"¿Cuánto da `5 / 2` en C++? ¿Y `5.0 / 2`? ¿Y `17 % 5`?"*. Deja que apuesten antes de ejecutarlo en pantalla para fijar la sorpresa visualmente. |
| **15–55** | **Explicación** | Explica la **división entera vs división real**, la magia del operador módulo `%` (residuo, útil para par/impar, múltiplos, extraer último dígito `n % 10`, partir segundos en horas/min/seg, desglosar billetes), **precedencia** (paréntesis obligatorios en promedios `(a+b+c)/3.0`) y **casting simple** `(double)a / b`. En los últimos 15 min inicia `M04` con tablas de verdad cotidianas (`&&` Y, `||` O, `!` NO). |
| **55–95** | **Práctica guiada** | Resuelve 2 problemas clásicos de parcial de `M03`: (1) **Desglose de un monto en billetes** usando `/` y `%`, (2) **Invertir o sumar dígitos de un número de 3 cifras** con su prueba de escritorio en papel paso a paso. |
| **95–110** | **Errores típicos** | Caza: escribir `double p = (a + b) / 2;` con dos enteros (el resultado ya perdió decimales antes de guardarse en `p`), olvidar paréntesis en fórmulas de física/promedio, e intentar usar `%` con `double`. |
| **110–120** | **Cierre y tarea** | **Tarea:** ejercicios 6 a 12 de `M03` (IMC, factura IVA, conversión de segundos) y leer la sección de tablas de verdad de `M04`. |

---

### Sesión 7 (2.0 h) — Condicionales sin Enredos y Traductor de Enunciados
- **Cobertura:** `M04_Condicionales` (2.0 h; acumulado M04 = 2.5 h de 3.5 h).
- **Material de apoyo:** `M04_Condicionales.pdf`, DFDs de `M04/dfd/`, ejemplos de `M04/pseint/` y `M04/cpp/`.

| Minutos | Fase | Guion del Monitor |
| :---: | :--- | :--- |
| **00–15** | **Enganche** | Escribe en rojo en el tablero: `if (10 <= x <= 20)`. Prueba `x = 50` en C++ frente al grupo y muestra que entra al `if` como si fuera verdadero. Explícales que esa sola línea ha tumbado más parciales que cualquier otra. |
| **15–55** | **Explicación** | Muestra por qué `10 <= x <= 20` evalúa `(10 <= 50)` $\rightarrow$ `1` (true) y luego `1 <= 20` $\rightarrow$ `true`! Enseña la forma correcta: `10 <= x && x <= 20`. Repasa `if` simple, `if-else` y **escalera `else-if`** (rangos excluyentes de notas/descuentos). Presenta el **Diccionario Traductor de Enunciados**: *"al menos"* (`>=`), *"supera"* (`>`), *"a lo sumo"* (`<=`), *"entre A y B inclusive"*, *"múltiplo de k"* (`x % k == 0`). |
| **55–95** | **Práctica guiada** | Resuelve 2 problemas completos (`DFD -> EPS -> PSeInt -> C++ -> Prueba de escritorio`): (1) **Clasificador de IMC o escala de notas con descuentos**, (2) **Año bisiesto o tipo de triángulo** (validando primero existencia del triángulo antes de clasificarlo). |
| **95–110** | **Errores típicos** | Caza: poner `;` después del `if (cond);`, confundir asignación `=` con comparación `==` dentro del `if`, y duplicar condiciones en `else if` (ej. probar `>= 3.0` después de no haber atrapado `>= 4.0`, olvidando el orden descendente). |
| **110–120** | **Cierre y tarea** | **Tarea:** ejercicios 1 a 8 de `M04` con tabla EPS y prueba de escritorio de al menos 3 casos borde (límite inferior, límite exacto, límite superior). |

---

### Sesión 8 (2.0 h) — `if` Anidados, `switch-case` y Bienvenida a Ciclos (`while`)
- **Cobertura:** `M04` (1.0 h cierre $\rightarrow$ **3.5 h**) + `M05_Ciclos_y_Bucles` (1.0 h de 4.0 h).
- **Material de apoyo:** `M04`, `M05_Ciclos_y_Bucles.pdf`, DFD de ciclo `Mientras` con centinela.

| Minutos | Fase | Guion del Monitor |
| :---: | :--- | :--- |
| **00–15** | **Enganche** | Pregunta: *"¿Qué pasa si quiero un menú de 4 opciones (1. Sumar, 2. Restar, 3. Multiplicar, 4. Dividir)?"* y luego: *"¿Y si quiero que el usuario pueda repetir cálculos 50 veces sin reiniciar el programa?"*. |
| **15–55** | **Explicación** | **Primera mitad (`M04`, 45 min):** cierra `M04` con `if` anidados vs operadores lógicos y **`switch-case`** (`break` obligatorio y `default`, mostrando qué ocurre cuando se omite `break` — efecto cascada). **Segunda mitad (`M05`, 15 min inicio):** introduce el concepto de **ciclo** con el DFD de `Mientras` y los roles de **contador** (`cont = cont + 1`) y **acumulador** (`suma = suma + valor`). |
| **55–95** | **Práctica guiada** | Implementa primero la calculadora/menú con `switch-case` (validando división entre cero). Luego resuelve el **DFD + PSeInt + C++** del **ciclo `while` con centinela** (sumar precios de compras hasta ingresar `0`, contando productos y rechazando precios negativos), haciendo la prueba de escritorio fila por fila. |
| **95–110** | **Errores típicos** | Caza: (1) olvidar `break` en `switch`, (2) usar `switch` con `double` o rangos (`case x > 5:` no existe en C++), (3) **bucle infinito** por olvidar actualizar la variable de control antes de cerrar el `while`, (4) olvidar inicializar `suma = 0` y `cont = 0`. |
| **110–120** | **Cierre y tarea** | **Tarea:** ejercicios 9 a 14 de `M04` y ejercicios 1 a 4 de `M05` (ciclo `while` con contador y centinela). |

---

### Sesión 9 (2.0 h) — Los 3 Ciclos (`for`, `while`, `do-while`) y Patrones sin Arreglos
- **Cobertura:** `M05_Ciclos_y_Bucles` (2.0 h; acumulado M05 = 3.0 h de 4.0 h).
- **Material de apoyo:** `M05`, diagrama comparativo `while` vs `do-while` vs `for` de `assets/diagramas/`, `M05/pseint/` y `M05/cpp/`.

| Minutos | Fase | Guion del Monitor |
| :---: | :--- | :--- |
| **00–15** | **Enganche** | Pon en pantalla un bucle `Repetir ... Hasta Que opcion = 0` de PSeInt junto a un `do { ... } while (opcion == 0);` mal traducido. Pregunta por qué en C++ se detuvo en la primera vuelta: **¡destapa la trampa mortal de condiciones opuestas!** |
| **15–55** | **Explicación** | Presenta la **Guía Para Tontos de Cuándo Usar Cada Ciclo**: (1) Sé cuántas vueltas dar $\rightarrow$ `for` / `Para`; (2) Depende de condición o centinela (puede dar 0 vueltas) $\rightarrow$ `while` / `Mientras`; (3) Menú o validación que debe ejecutarse al menos 1 vez $\rightarrow$ `do-while` / `Repetir...Hasta Que` (recordando invertir la condición entre PSeInt y C++!). Explica también **banderas `bool`** y cómo hallar **máximo y mínimo sin arreglos** (leyendo el primero aparte o inicializando con el primer dato válido). |
| **55–95** | **Práctica guiada** | Resuelve 2 problemas completos con prueba de escritorio: (1) **Factorial / Suma de serie con `for`** (cuidando `suma` en `0` vs `prod` en `1`), (2) **Lectura de `N` temperaturas para hallar promedio, máximo, mínimo y bandera de alerta** usando solo variables simples (sin arreglos). |
| **95–110** | **Errores típicos** | Caza: inicializar `mayor = 0` cuando todos los datos son negativos (error fatal: da `0` aunque nadie ingresó `0`), poner `;` tras el `for (...)`, e invertir mal `Hasta Que (x >= 1 Y x <= 5)` al pasarlo a `while (x < 1 || x > 5)`. |
| **110–120** | **Cierre y tarea** | **Tarea:** ejercicios 5 a 11 de `M05` (validación con `do-while`, series con `for`, máximo/mínimo sin arreglos). |

---

### Sesión 10 (2.0 h) — Ciclos Anidados y Bienvenida a Vectores Estáticos
- **Cobertura:** `M05` (1.0 h cierre $\rightarrow$ **4.0 h**) + `M06_Vectores_Estaticos` (1.0 h de 4.0 h).
- **Material de apoyo:** `M05`, `M06_Vectores_Estaticos.pdf`, diagrama de vector estático 1D en RAM de `assets/diagramas/`.

| Minutos | Fase | Guion del Monitor |
| :---: | :--- | :--- |
| **00–15** | **Enganche** | Dibuja un reloj analógico (horero y minutero) o un edificio de pisos y apartamentos: *"¿Cómo avanza el minutero mientras el horario espera en una misma hora?"* $\rightarrow$ **ciclos anidados**. Luego pregunta: *"Si un profesor pide guardar las 40 notas para mostrar cuáles superaron el promedio después de calcularlo, ¿me sirven 40 variables sueltas?"*. |
| **15–55** | **Explicación** | **Primera hora (`M05`, 60 min):** resuelve tablas de multiplicar, triángulo de asteriscos y verificación de número primo con ciclos anidados (haciendo tabla de prueba de escritorio con columnas `i | j | salida`). **Segunda hora (`M06`, 60 min — 30 min aquí + 30 en práctica):** analogía de **"casilleros fijos numerados desde 0"**. Explica por qué usamos `const int MAX = 100; int vec[MAX]; int n;` y por qué **NO** usamos `int vec[n];` (VLA no estándar) ni `std::vector`. Resalta la diferencia de índices: `0..n-1` en C++ vs `1..n` por defecto en PSeInt. |
| **55–95** | **Práctica guiada** | Escribe paso a paso el primer vector estático (`const int MAX = 50; double notas[MAX];`): validar `1 <= n && n <= MAX` con `do-while`, cargar los `n` datos con `for`, calcular el promedio y **recorrer por segunda vez** el vector para contar e imprimir qué notas superaron el promedio (demostrando por qué aquí sí hacía falta el arreglo). |
| **95–110** | **Errores típicos** | Caza: (1) acceder a `notas[n]` o escribir `i <= n` en el `for` (desbordamiento de arreglo!), (2) olvidar validar que `n <= MAX`, (3) imprimir `cout << notas;` esperando ver todo el vector (en C++ imprime una dirección hexadecimal). |
| **110–120** | **Cierre y tarea** | **Tarea:** terminar ejercicios 12 a 16 de `M05` (primos, Fibonacci, menú) y ejercicios 1 a 4 de `M06` (carga, promedio y conteo con condición). |

---

### Sesión 11 (2.0 h) — Patrones Maestros en Vectores Estáticos
- **Cobertura:** `M06_Vectores_Estaticos` (2.0 h; acumulado M06 = 3.0 h de 4.0 h).
- **Material de apoyo:** `M06`, `fichas_resumen/Ficha_04_*`, DFD de carga y búsqueda secuencial, `M06/pseint/` y `M06/cpp/`.

| Minutos | Fase | Guion del Monitor |
| :---: | :--- | :--- |
| **00–15** | **Enganche** | Dibuja en el tablero un vector de 6 casilleros `[14, 8, 25, 3, 19, 11]` y reta a los estudiantes a explicar en voz alta *sin código* cómo harían para: (1) encontrar el `25`, (2) voltear el arreglo al revés, (3) borrar el `8` sin dejar un hueco vacío. |
| **15–55** | **Explicación** | Recorre los **patrones maestros 1D**: (1) **Mayor/Menor guardando su índice/posición** (`posMayor = 0`), (2) **Búsqueda secuencial con bandera `bool encontrado = false`** (y detención temprana), (3) **Invertir arreglo in-place** intercambiando `i` con `n - 1 - i` hasta `n / 2`, (4) **Rotar izquierda/derecha** usando variable auxiliar `aux`, (5) **Insertar y eliminar** en un arreglo de capacidad `MAX` corriendo elementos y actualizando `n` (cuidando no pasar de `MAX` ni bajar de `0`). |
| **55–95** | **Práctica guiada** | Implementa en vivo en PSeInt y C++ un programa con **búsqueda secuencial + eliminación lógica/desplazamiento** sobre un vector estático `int codigos[MAX]`, trazando en el tablero las flechas de desplazamiento (`v[i] = v[i + 1]`) para que entiendan por qué el ciclo va hacia adelante al eliminar y hacia atrás al insertar. |
| **95–110** | **Errores típicos** | Caza: (1) intercambiar `a = b; b = a;` sin variable temporal `aux` (sobrescribe y pierde el valor), (2) al invertir el arreglo, recorrer `i` desde `0` hasta `n - 1` (lo voltea dos veces y lo deja igual!), (3) en búsqueda secuencial, poner `else { cout << "No está"; }` DENTRO del `for` (imprime "No está" en cada casillero que no coincide). |
| **110–120** | **Cierre y tarea** | Entrega `Ficha_04` (Patrones de Vectores y Matrices Estáticos). **Tarea:** ejercicios 5 a 11 de `M06`. |

---

### Sesión 12 (2.0 h) — Ordenamiento Burbuja y Bienvenida a Matrices Estáticas (2D)
- **Cobertura:** `M06` (1.0 h cierre $\rightarrow$ **4.0 h**) + `M07_Matrices_Estaticas` (1.0 h de 4.0 h).
- **Material de apoyo:** `M06`, `M07_Matrices_Estaticas.pdf`, diagrama 2D de matriz estática `m[4][4]` de `assets/diagramas/`.

| Minutos | Fase | Guion del Monitor |
| :---: | :--- | :--- |
| **00–15** | **Enganche** | Simula el **Ordenamiento Burbuja** en vivo con 5 tarjetas numeradas en las manos de 5 estudiantes frente al salón: que comparen de a pares y el mayor "flote" hacia la derecha en cada pasada. |
| **15–55** | **Explicación** | **Primera hora (`M06`, 60 min):** pasa las 5 tarjetas a la prueba de escritorio visual de **Burbuja** (`for` externo de pasadas `0..n-2`, `for` interno `0..n-2-p`, intercambio con `aux`) y codifícalo en `.psc` y `.cpp`. **Segunda hora (`M07`, 60 min):** presenta la matriz estática con la analogía de **"edificio de pisos y apartamentos / hoja de cálculo"** (`const int MAX_F = 20, MAX_C = 20; int mat[MAX_F][MAX_C];`). Explica índices `[fila][columna]` empezando en `0` y la diferencia entre **recorrido por filas** (`for i -> for j`) y **recorrido por columnas** (`for j -> for i`). |
| **55–95** | **Práctica guiada** | Carga y muestra una matriz estática de `f x c` (validando `1 <= f <= MAX_F` y `1 <= c <= MAX_C`) impresa en formato tabular limpio con `setw`, y calcula la **suma por cada fila** y la **suma por cada columna**. |
| **95–110** | **Errores típicos** | Caza: (1) en Burbuja, escribir `j < n` y acceder a `v[j + 1]` (desbordamiento en el último elemento!), (2) invertir índices `mat[j][i]` cuando se quería `mat[i][j]` en matrices no cuadradas (causa lectura fuera de rango), (3) olvidar reiniciar `sumaFila = 0` dentro del ciclo externo antes de empezar la siguiente fila. |
| **110–120** | **Cierre y tarea** | **Tarea:** completar ejercicios 12 a 14 de `M06` (Burbuja y variantes) y ejercicios 1 a 4 de `M07` (lectura, impresión y sumas por fila/columna). |

---

### Sesión 13 (2.0 h) — Matrices Cuadradas, Diagonales y Coordenadas
- **Cobertura:** `M07_Matrices_Estaticas` (2.0 h; acumulado M07 = 3.0 h de 4.0 h).
- **Material de apoyo:** `M07`, diagrama 2D de diagonales de `assets/diagramas/`, `M07/pseint/` y `M07/cpp/`.

| Minutos | Fase | Guion del Monitor |
| :---: | :--- | :--- |
| **00–15** | **Enganche** | Dibuja una cuadrícula `4 x 4` en el tablero con coordenadas `(0,0)...(3,3)` escritas dentro de cada celda. Pide que pinten con un color las celdas donde `i == j` y con otro color aquellas donde `i + j == n - 1`: los estudiantes descubren la **ecuación de ambas diagonales** visualmente antes de ver código. |
| **15–55** | **Explicación** | Explica los patrones clave en 2D: (1) **Mayor/Menor con coordenadas** (`filaMay`, `colMay`), (2) **Matriz cuadrada** (`n x n`): diagonal principal (`i == j`), diagonal secundaria (`i + j == n - 1`), triangular superior (`i < j` o `i <= j`), triangular inferior (`i > j`), (3) **Matriz simétrica** (`mat[i][j] == mat[j][i]` usando bandera), (4) **Transpuesta** (`trans[j][i] = mat[i][j]`). |
| **55–95** | **Práctica guiada** | Resuelve paso a paso un problema integrador de matriz cuadrada estática (`MAX = 10`): leer `n x n`, verificar si es **simétrica** con bandera y construir/mostrar su **transpuesta** + suma de ambas diagonales (resaltando el caso impar donde el elemento central se cruza en ambas!). |
| **95–110** | **Errores típicos** | Caza: (1) en simetría, hacer `return` o imprimir `"Es simétrica"` dentro del primer par igual (basta un solo par distinto para que NO sea simétrica!), (2) escribir `i + j == n` en vez de `i + j == n - 1` en C++ base 0, (3) intentar calcular la transpuesta in-place con dos ciclos completos `0..n-1` (¡la vuelve a dejar igual!). |
| **110–120** | **Cierre y tarea** | **Tarea:** ejercicios 5 a 10 de `M07` (diagonales, simetría, transpuesta y búsqueda de mayor con coordenadas). |

---

### Sesión 14 (2.0 h) — Casos Reales 2D y Modularidad con Arreglos Estáticos
- **Cobertura:** `M07` (1.0 h cierre $\rightarrow$ **4.0 h**) + `M08_Modularidad_Parciales_y_Solucionario` (1.0 h de 3.0 h).
- **Material de apoyo:** `M07`, `M08_Modularidad_Parciales_y_Solucionario.pdf`, `M07/cpp/`, `M08/cpp/`.

| Minutos | Fase | Guion del Monitor |
| :---: | :--- | :--- |
| **00–15** | **Enganche** | Muestra el caso real de una **sala de cine 5×6** (`'L'` libre / `'O'` ocupada) o un **boletín de N estudiantes × M materias**. Pregunta: *"Si este programa ya tiene 120 líneas dentro de `main()`, ¿cómo lo dividimos en piezas pequeñas sin enredarnos?"*. |
| **15–55** | **Explicación** | **Primera hora (`M07`, 60 min):** resuelve uno de los casos reales de `M07` (ventas por tienda/mes o reserva de sillas de cine 5×6 con validación de coordenadas). **Segunda hora (`M08`, 60 min):** introduce **funciones en C++** y **SubProcesos en PSeInt**: funciones `void` vs funciones con `return`, **paso por valor vs paso por referencia `&`** (ejemplo clásico `intercambiar(int &a, int &b)`), y la regla exacta para pasar arreglos estáticos: `void mostrarVec(int v[], int n)` y `void mostrarMat(int m[][MAX_C], int f, int c)` (explicando por qué `MAX_C` debe ir fijo en los corchetes de la matriz!). |
| **55–95** | **Práctica guiada** | Toma el menú de gestión de un vector estático (leer, mostrar, promedio, buscar mayor) y refactorízalo en vivo en `M08/cpp/` dividiéndolo en 4 funciones limpias llamadas desde `main()`. |
| **95–110** | **Errores típicos** | Caza: (1) declarar `void leerMat(int m[][], ...)` dejando vacío el segundo corchete en C++ (error de compilación!), (2) olvidar `&` en una función de intercambio o lectura de `n` y preguntarse por qué en `main` no cambió el valor, (3) intentar retornar un arreglo estático local con `return v;`. |
| **110–120** | **Cierre y tarea** | **Tarea:** terminar ejercicios 11 a 14 de `M07` y repasar `Ficha_01` a `Ficha_04` para el simulacro de parcial de la sesión final. |

---

### Sesión 15 (2.0 h) — Estrategia Anti-Pánico, Simulacros de Parcial y Cierre
- **Cobertura:** `M08_Modularidad_Parciales_y_Solucionario` (2.0 h cierre $\rightarrow$ **3.0 h**; curso completo = **30.0 h**).
- **Material de apoyo:** `M08` (Simulacro 1, Simulacro 2, Checklist de 10 puntos y rúbrica), `fichas_resumen/`.

| Minutos | Fase | Guion del Monitor |
| :---: | :--- | :--- |
| **00–15** | **Enganche** | Presenta la **Estrategia Anti-Pánico en Parciales**: qué hacer en los primeros 5 minutos cuando te entregan un enunciado largo (subrayar sustantivos/verbos, armar EPS en la esquina de la hoja, decidir estructuras antes de escribir una sola línea). |
| **15–55** | **Explicación y Simulacro Exprés** | Aplica una mini-ronda cronometrada usando puntos reales del **Simulacro 1 (Corte 1)** y del **Simulacro 2 (Corte Final: ciclos anidados + vector estático + matriz estática)** de `M08`. Los estudiantes arman en 25 min la tabla EPS + estructura del punto integrador mientras el monitor pasea revisando planteamientos. |
| **55–95** | **Práctica guiada** | Resuelve y califica en vivo en el tablero usando la **rúbrica de puntuación** de `M08`: construye la solución compilable en C++ paso a paso, ejecuta la prueba de escritorio sobre un caso límite y muestra dónde se pierden o ganan puntos parciales (validaciones, nombres claros, cierre de llaves, inicialización). |
| **95–110** | **Checklist final** | Repasa el **Checklist de 10 puntos antes de entregar un parcial** (¿inicialicé acumuladores?, ¿validé división por cero?, ¿`&&` en rangos?, ¿`break` en `switch`?, ¿índices `0..n-1`?, ¿`MAX` fijo y `n <= MAX`?, ¿hice prueba de escritorio con al menos 1 caso normal y 1 borde?). |
| **110–120** | **Cierre del curso** | Entrega el mapa completo del repositorio (`LIBRO_COMPLETO_MONITORIA_30H.pdf` e `index.html`) y asigna como práctica autónoma cronometrar completos el **Simulacro 1 (90 min)** y **Simulacro 2 (90 min)** de `M08` antes del examen oficial. |

---

## 3. Verificación Rápida de Consistencia de Horas

- **Suma por sesiones:** `15 sesiones × 2.0 horas = 30.0 horas`.
- **Suma por módulos:** `2.5 (M00) + 3.0 (M01) + 3.0 (M02) + 3.0 (M03) + 3.5 (M04) + 4.0 (M05) + 4.0 (M06) + 4.0 (M07) + 3.0 (M08) = 30.0 horas`.
- **Diferencia:** `0.0 horas`.
