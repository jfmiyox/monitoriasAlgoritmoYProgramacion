# Módulo 08: Modularidad, Estrategia Anti-Pánico y Simulacros de Parcial

> **Duración estimada:** 3.0 horas (Sesión final de consolidación y preparación de exámenes)  
> **Prerrequisitos:** M00–M07 (Análisis EPS, DFD, PSeInt, Tipos/Operadores, Condicionales, Ciclos, Vectores Estáticos y Matrices Estáticas)  
> **Alcance estricto:** Funciones simples (`void` y con retorno), paso por valor vs. referencia básica (`&`), paso de vectores y matrices **estáticas** a funciones (`v[]` y `m[][MAX_C]`), SubProcesos/Funciones en PSeInt, estrategia de parcial y 2 simulacros completos con solucionario. **Cero punteros, cero memoria dinámica (`new`/`delete`), cero `std::vector`.**

---

## Mapa de Aprendizaje del Módulo

1. **Bloque 1 (1.0 h): Modularidad con Plastilina** — Funciones en C++ y SubProcesos en PSeInt.
2. **Bloque 2 (0.5 h): Estrategia "Anti-Pánico en Parciales"** — Lectura quirúrgica de enunciados, gestión de 90 minutos, checklist de 10 puntos y los 12 errores mortales.
3. **Bloque 3 (1.5 h): Simulacros Completos de Parcial** — Simulacro 1 (Corte 1) y Simulacro 2 (Corte Final) con rúbrica de 100 puntos, solucionario comentado, PSeInt, C++ compilable y pruebas de escritorio verificadas.

---

## 1. Modularidad: Funciones en C++ y SubProcesos en PSeInt

### 1.1 Explicado Para Tontos: ¿Por qué no meter todo en `main()`?

Imagina que abres un restaurante y **una sola persona** (llamémosla `main()`) toma los pedidos, pica la cebolla, asa la carne, lava los platos, cobra en la caja y barre el piso. Al principio, con 2 clientes, funciona. Cuando llegan 30 clientes (un problema largo de parcial), esa persona colapsa, quema la carne y mezcla las cuentas.

**Modularizar** es contratar especialistas:
- Uno se encarga solo de **leer y validar** (`leerEnteroEnRango`).
- Otro se encarga solo de **mostrar la tabla** (`mostrarInventario`).
- Otro se encarga solo de **buscar** (`buscarPorCodigo`).
- Y `main()` deja de hacer el trabajo sucio: ahora es el **director de orquesta** que llama a cada especialista en el orden correcto.

#### Ventajas inmediatas en un parcial:
1. **Menos errores:** Si falla el cálculo del promedio, sabes exactamente en qué función mirar (`calcularPromedio`), sin perderte en 150 líneas dentro de `main()`.
2. **Reutilización:** Si debes leer 3 datos validados entre 1 y 100, escribes una sola función `leerEnteroEnRango(...)` y la llamas 3 veces.
3. **Legibilidad:** El profesor lee tu `main()` como si fuera un resumen en español.

---

### 1.2 Anatomía de una Función en C++ vs. PSeInt

En C++, una función suele tener **dos partes** (si se declara arriba del `main` y se define abajo) o **una sola** (si se define completa arriba del `main`):

```
tipo_retorno nombreFuncion(tipo1 param1, tipo2 param2) {
    // instrucciones locales
    return resultado; // obligatorio salvo que tipo_retorno sea void
}
```

#### Equivalencia directa PSeInt $\leftrightarrow$ C++

| Tipo de módulo | En PSeInt (`SubProceso` / `Funcion`) | En C++ |
| :--- | :--- | :--- |
| **Sin retorno (acción)** | `SubProceso mostrarBanner()` ... `FinSubProceso` | `void mostrarBanner() { ... }` |
| **Con retorno simple** | `Funcion area <- calcArea(b, h)` ... `FinFuncion` | `double calcArea(double b, double h) { return b * h; }` |
| **Paso por valor (copia)** | `SubProceso f(x Por Valor)` *(por defecto en PSeInt)* | `void f(int x)` |
| **Paso por referencia (original)** | `SubProceso f(x Por Referencia)` | `void f(int &x)` |
| **Arreglo estático** | `SubProceso ver(v, n)` *(en PSeInt los arreglos pasan por ref.)* | `void ver(const int v[], int n)` |

> **Consejo de Monitoría:** En C++, si colocas el **prototipo** (la firma terminada en `;`) arriba de `main()` y el cuerpo completo debajo de `main()`, tu código queda ordenado de arriba hacia abajo: primero ves el índice de funciones, luego la lógica principal en `main()`, y después los detalles.

**Ejemplo ejecutable 1:** [`cpp/01_anatomia_funciones_void_retorno.cpp`](cpp/01_anatomia_funciones_void_retorno.cpp)
- Muestra `mostrarBanner()` (`void`), `calcularAreaRectangulo(double base, double altura)` (`double`), `esNumeroPar(int numero)` (`bool`) y `clasificarNota(double nota)` (`char`).
- En `esNumeroPar(numero)` puedes usarla directamente dentro de un `if (esNumeroPar(numero))`, porque la función devuelve `true` o `false`.

---

### 1.3 Paso por Valor vs. Paso por Referencia (`&`)

Esta es la duda que más puntos cuesta en los parciales finales. Vamos con la analogía definitiva:

- **Paso por VALOR (`int x`):** Le sacas una **fotocopia** a tu cédula y se la entregas a la función. Si la función raya la fotocopia (`x = x * 2;`), tu cédula original en `main()` **queda intacta**.
- **Paso por REFERENCIA (`int &x`):** Le entregas tu **cédula original** (un alias o apodo directo al mismo casillero en memoria RAM). Si la función la modifica (`x = x * 2;`), el cambio **sí afecta** a la variable original en `main()`.

#### ¿Cuándo usar cada uno?
1. **Usa paso por VALOR** cuando la función solo necesita leer el dato para calcular algo y devolver un único resultado (ej. `calcularArea(double base, double altura)`).
2. **Usa paso por REFERENCIA (`&`)** en estos 3 casos clásicos de parcial:
   - **Intercambiar dos variables:** `void intercambiar(int &a, int &b)`.
   - **Leer y validar un dato desde teclado dentro de una función:** `void leerEnteroEnRango(int &destino, int min, int max, const char mensaje[])`.
   - **Devolver 2 o más resultados al mismo tiempo:** por ejemplo `void obtenerMinMax(const int v[], int n, int &minimo, int &maximo)` o `encontrarPicoMaximo(..., int &pisoMax, int &diaMax)`.

> **OJO — Trampa Clásica de Parcial:**
> Si escribes `void intercambiar(int a, int b)` **sin el `&`**, compila sin errores, pero al terminar la función los valores en `main()` **NO se intercambiaron**. ¡Siempre verifica que el `&` esté tanto en el prototipo como en la definición!

**Ejemplo ejecutable 2:** [`cpp/02_valor_vs_referencia.cpp`](cpp/02_valor_vs_referencia.cpp)

---

### 1.4 Cómo Pasar un Vector Estático a una Función

En C++, un vector estático tiene capacidad física fija `MAX` definida por una constante (`const int MAX = 50;`), y un tamaño lógico `n` (cuántas casillas realmente estamos usando, `1 <= n <= MAX`).

Reglas de oro para pasar vectores a funciones:
1. **Firma si la función VA A MODIFICAR el vector** (como `leerVector`, `ordenarBurbuja`):
   ```cpp
   void leerVector(int v[], int n);
   ```
2. **Firma si la función SOLO VA A CONSULTAR el vector** (como `mostrarVector`, `calcularPromedio`, `buscarPosicion`):
   ```cpp
   void mostrarVector(const int v[], int n);
   ```
   Agregar `const` evita modificar el arreglo por accidente (por ejemplo, escribir `v[i] = 0` en lugar de `v[i] == 0`).
3. **Al llamar la función desde `main()`**, pasa **SOLO el nombre del arreglo (sin corchetes)** y el tamaño `n`:
   ```cpp
   leerVector(datos, n);      // CORRECTO
   mostrarVector(datos, n);   // CORRECTO
   ```
   **ERROR MORTAL:** escribir `mostrarVector(datos[n], n);` o `mostrarVector(datos[], n);`. `datos[n]` sería un único entero fuera de rango, ¡no el arreglo! Tampoco intentes retornar un arreglo local con `return v;` desde una función: en C++ básico, el `main()` crea el arreglo estático y se lo pasa a la función para que lo llene o consulte.
4. **Explicado con plastilina:** Los arreglos en C++ **NO se copian completos** al pasarlos a una función; la función trabaja directamente sobre los casilleros originales del `main()`, aunque no pongas `&`. Por eso **siempre** debes pasar también `int n` como segundo parámetro: el arreglo no recuerda cuántos elementos llenaste.

**Ejemplo ejecutable 3:** [`cpp/03_funciones_vector_estatico.cpp`](cpp/03_funciones_vector_estatico.cpp)

---

### 1.5 Cómo Pasar una Matriz Estática a una Función

En una matriz estática 2D:
```cpp
const int MAX_F = 10;
const int MAX_C = 10;
int mat[MAX_F][MAX_C];
```

**REGLA INQUEBRANTABLE DE C++:**
Al recibir una matriz estática como parámetro en una función, **el primer corchete puede quedar vacío `[]`, pero EL SEGUNDO CORCHETE `[MAX_C]` ES OBLIGATORIO**:

```cpp
void leerMatriz(int m[][MAX_C], int filas, int cols);
void mostrarMatriz(const int m[][MAX_C], int filas, int cols);
```

¿Por qué? Porque en memoria RAM la matriz se guarda fila tras fila. Para saltar de `m[0][0]` a `m[1][0]`, el compilador necesita saber cuántas columnas físicas (`MAX_C`) mide cada fila. Si escribes `int m[][]`, **no compila**.

Y recuerda:
- Declara `const int MAX_F` y `const int MAX_C` **arriba de los prototipos** (ámbito global de solo lectura) para que tanto las funciones como `main()` conozcan `MAX_C`.
- Pasa siempre `filas` y `cols` (tamaños lógicos reales usados por el usuario, validados entre `1` y `MAX_F` / `MAX_C`).
- Al llamar la función en `main()`: `mostrarMatriz(mat, f, c);` (solo el nombre `mat`, sin corchetes).

**Ejemplo ejecutable 4:** [`cpp/04_funciones_matriz_estatica.cpp`](cpp/04_funciones_matriz_estatica.cpp)

---

## 2. Estrategia "Anti-Pánico en Parciales"

Muchos estudiantes saben programar, pero reprueban un parcial porque leen rápido, entran en pánico y empiezan a escribir código antes de entender qué pide el problema. Aplica este protocolo militar:

### 2.1 Cómo Leer un Enunciado Largo (Los Primeros 8 Minutos SIN Teclado)

Lee el enunciado completo **dos veces**. En la segunda lectura, subraya o clasifica mentalmente en 4 cajones:

1. **ENTRADAS:** ¿Qué digita el usuario? ¿Qué tipo tiene (`int`, `double`, `char`)? ¿Cuál es su rango válido?
2. **REGLAS Y FÓRMULAS:** ¿Qué condiciones hay ("si supera...", "entre A y B inclusive", "descuento por categoría")? ¿En qué orden se aplican descuentos y recargos?
3. **REPETICIÓN:** ¿Se procesa un solo caso o muchos?
   - ¿Se sabe cuántos (`N` datos)? $\Rightarrow$ `for`.
   - ¿Termina con un valor especial ("hasta ingresar `-999` o `0`")? $\Rightarrow$ `while` con lectura previa + lectura al final del ciclo.
   - ¿Es un menú o validación que ocurre al menos una vez? $\Rightarrow$ `do-while`.
4. **SALIDAS EXACTAS:** ¿Qué pide imprimir exactamente el enunciado? (Promedio, conteos, posición 0-based o 1-based, formato decimal).

### 2.2 Reparto Inteligente de Tiempo (Parcial de 90 Minutos)

| Franja | Qué hacer | Meta |
| :--- | :--- | :--- |
| **Min 0 – 10** | Leer todo el parcial, elegir por cuál punto empezar (el más seguro primero) y armar tablas **EPS** en hoja borrador. | Cero código escrito aún; problema 100% entendido. |
| **Min 10 – 35** | Resolver el Punto 1 (o DFD + primer código) y probarlo con un caso manual. | Primeros 25–35 puntos asegurados. |
| **Min 35 – 75** | Resolver Puntos 2 y 3 dividiendo en funciones claras (si aplica) y compilando cada bloque pequeño en lugar de escribir 120 líneas de golpe. | Lógica completa compilando. |
| **Min 75 – 90** | **Prueba de escritorio** con caso normal, caso límite y caso inválido + revisar el Checklist de 10 puntos. | Eliminar errores silenciosos antes de entregar. |

---

### 2.3 Checklist de 10 Puntos Antes de Entregar

1. [ ] **Variables inicializadas:** ¿Todo contador y acumulador empieza en `0` (`int cont = 0; double suma = 0.0;`)?
2. [ ] **División real vs. entera:** ¿Evité `5 / 2` cuando quería `2.5` (usando `5.0 / 2` o `static_cast<double>(suma) / n`)?
3. [ ] **Condiciones de rango correctas:** ¿Escribí `10 <= x && x <= 20` y **NO** `10 <= x <= 20`?
4. [ ] **Igualdad vs. asignación:** ¿Puse `==` dentro de los `if`/`while` y `=` solo para asignar?
5. [ ] **Switch completo:** ¿Cada `case` tiene su `break;` y existe un `default:`?
6. [ ] **Ciclos que sí terminan:** ¿Dentro del `while` actualicé el contador o volví a leer el centinela?
7. [ ] **Arreglos estáticos seguros:** ¿Declaré `const int MAX = ...;` y validé `1 <= n && n <= MAX`? ¿Los índices van de `0` a `n - 1` (nunca `v[n]`)?
8. [ ] **Máximo y mínimo sin errores:** ¿Inicialicé `min` y `max` con el **primer dato válido** o `v[0]`, en lugar de asumir `min = 0`?
9. [ ] **Funciones bien conectadas:** ¿Las funciones que modifican variables escalares tienen `&`? ¿Las matrices tienen `[][MAX_C]`? ¿Toda función no-`void` tiene `return` en todos sus caminos?
10. [ ] **Prueba de escritorio ejecutada:** ¿Verifiqué a mano o ejecutando el programa que la salida coincide con lo calculado en papel?

---

### 2.4 Los 12 Errores Mortales en DFD, PSeInt y C++

| # | Error mortal | Qué pasa realmente | Antídoto rápido |
| :-: | :--- | :--- | :--- |
| 1 | `if (x = 5)` en lugar de `if (x == 5)` | Asigna `5` a `x` y el `if` siempre entra porque `5` es verdadero. | Lee en voz alta: `==` es "¿es igual a?". |
| 2 | `if (10 <= x <= 20)` | Se evalúa `(10 <= x)` dando `0` o `1`, y ambos son `<= 20` (siempre verdadero). | Usa siempre `10 <= x && x <= 20`. |
| 3 | `double p = suma / n;` con ambos `int` | C++ trunca los decimales antes de guardar en `p` (`7/2 = 3.0`). | `static_cast<double>(suma) / n`. |
| 4 | Olvidar `break;` en `switch` | Ejecuta el `case` correcto y sigue cayendo por los siguientes. | Escribe `break;` apenas abras cada `case`. |
| 5 | Confundir `Repetir...Hasta Que` con `do...while` | En PSeInt **termina** cuando es verdadero; en C++ **continúa** mientras es verdadero. | Al pasar a C++, **niega** la condición de PSeInt. |
| 6 | Mezclar `cin >>` y `getline(cin, s)` | `getline` lee el salto de línea `\n` pendiente y deja la cadena vacía. | Usa `cin.ignore();` antes de `getline`. |
| 7 | `int v[n];` (VLA) en C++ estándar | No es estándar en C++ ISO y falla si `n <= 0` o desborda la pila. | Usa `const int MAX = 100; int v[MAX];`. |
| 8 | Recorrer vector hasta `i <= n` | Accedes a `v[n]`, memoria basura fuera del arreglo. | Siempre `i < n` (índices `0` a `n - 1`). |
| 9 | En DFD: flechas sin dirección o ramas `Sí`/`No` sin etiquetar | Nadie sabe qué camino se toma cuando la condición es falsa. | Etiqueta siempre `Sí`/`V` y `No`/`F`, y une las ramas. |
| 10 | En PSeInt: usar índices `0` sin `Opción Base 0` o viceversa | Desfase de 1 casilla entre pseudocódigo y C++. | Aclara si PSeInt usa `1..n` y C++ `0..n-1`. |
| 11 | Olvidar `&` en `intercambiar(int a, int b)` | Modifica copias locales y no las variables del `main()`. | Si la función debe cambiar el argumento, pon `&`. |
| 12 | Escribir `void f(int m[][])` sin `MAX_C` | Error de compilación inmediato en C++. | Siempre `void f(int m[][MAX_C], int f, int c)`. |

---

## 3. SIMULACRO 1 (Corte 1 — 90 minutos, 100 puntos)

> **Temas evaluados:** Análisis EPS, DFD, tipos de datos, operadores (`/`, `%`), condicionales (`if/else`, `switch`) y ciclos (`while`, `for`, `do-while`) **sin arreglos**.

### 3.1 Enunciados y Rúbrica del Simulacro 1

#### Punto 1 (25 puntos — Sugerido: 25 min): Control de Peaje Vehicular
Construya el análisis EPS, la lógica (DFD/PSeInt) y el programa en C++ que liquide el pago de un vehículo en un peaje nacional:
- Categoría: `1` = Automóvil (`$12000`), `2` = Camioneta/Microbús (`$18500`), `3` = Camión pesado (base `$28000` para 2 ejes, más `$7500` por cada eje adicional; debe leer el número de ejes y validar que sea $\ge 2$). Si la categoría no está entre `1` y `3`, mostrar error y terminar.
- Preguntar si transita en hora pico (`S`/`N`): si es `'S'` o `'s'`, aplicar recargo del **15%** sobre la tarifa base.
- Preguntar si tiene Telepeaje/TAG (`S`/`N`): si es `'S'` o `'s'`, aplicar descuento del **10%** sobre el subtotal (tarifa base + recargo).
- Mostrar tarifa base, recargo, descuento y total a pagar con 2 decimales.

**Rúbrica P1 (25 pts):** Análisis EPS correcto (5 pts) + Validación de categoría y ejes $\ge 2$ (6 pts) + Cálculo exacto de recargo y descuento sobre subtotal (9 pts) + Prueba de escritorio completa (5 pts).

#### Punto 2 (35 puntos — Sugerido: 30 min): Parqueadero Inteligente
Un parqueadero cobra según el tipo de vehículo (`M` = Moto `$1800`/h, `C` = Carro `$3500`/h, `V` = Van `$5000`/h; aceptar mayúsculas y minúsculas mediante `switch-case`). Luego solicita el tiempo de estadía en minutos ($\ge 1$).
- Convierta los minutos a horas completas (`minutos / 60`) y minutos sobrantes (`minutos % 60`).
- Regla de cobro: si estuvo menos de 1 hora (`horasCompletas == 0`), se cobra mínimo **1 hora**. En otro caso, hay tolerancia de 15 minutos: si `minutosSobrantes > 15`, se cobra `horasCompletas + 1`; de lo contrario, `horasCompletas`.
- Si las horas cobradas son $\ge 6$, aplique **15% de descuento** por larga estadía.
- Si presenta tiquete de convenio comercial (`S`/`N`), reste **$2000** fijos al valor resultante (el total nunca puede ser negativo; si da $< 0$, dejar en `0.00`).

**Rúbrica P2 (35 pts):** `switch-case` con mayúsculas/minúsculas y `default` (8 pts) + Uso exacto de `/` y `%` + tolerancia de 15 min (12 pts) + Descuentos escalonados y piso en `$0` (10 pts) + Prueba de escritorio (5 pts).

#### Punto 3 (40 puntos — Sugerido: 35 min): Monitor de Temperaturas de Invernadero
Sin usar arreglos, lea lecturas de temperatura en grados Celsius hasta que el operador ingrese el centinela `-999`.
- El rango físico válido del sensor es de `-10.0` a `60.0` inclusive. Si una lectura (distinta de `-999`) está fuera de ese rango, mostrar aviso de lectura descartada y **no** contarla en las estadísticas.
- Calcule e imprima al finalizar: total de lecturas válidas, promedio térmico, temperatura mínima, temperatura máxima, cantidad de alertas por frío (`< 12.0` °C) y cantidad de alertas por calor (`> 32.0` °C).
- Si no hubo ninguna lectura válida antes de ingresar `-999`, informar `"No se registraron lecturas validas."` (sin dividir por cero).

**Rúbrica P3 (40 pts):** Ciclo `while` con lectura anticipada del centinela `-999` (10 pts) + Validación sin salir del ciclo ante dato fuera de rango (8 pts) + Inicialización correcta de min/max con el primer dato válido (10 pts) + Conteo de alertas y protección contra división por cero (7 pts) + Prueba de escritorio (5 pts).

---

### 3.2 Solucionario Comentado del Simulacro 1

#### Solución Punto 1: Peaje Vehicular (`cpp/05_simulacro1_p1_peaje.cpp`)

**1. Análisis EPS:**
- **Entradas:** `categoria` (`int`), `ejes` (`int`, solo si `categoria == 3`), `horaPico` (`char`), `tieneTag` (`char`).
- **Proceso:**
  1. Validar `1 <= categoria <= 3`.
  2. Asignar `tarifaBase`. Si `categoria == 3`, validar `ejes >= 2` y calcular `28000 + (ejes - 2) * 7500`.
  3. `recargoPico = (horaPico == 'S' || 's') ? tarifaBase * 0.15 : 0`.
  4. `subtotal = tarifaBase + recargoPico`.
  5. `descuentoTag = (tieneTag == 'S' || 's') ? subtotal * 0.10 : 0`.
  6. `totalPagar = subtotal - descuentoTag`.
- **Salidas:** `tarifaBase`, `recargoPico`, `descuentoTag`, `totalPagar`.

**2. Pseudocódigo PSeInt equivalente:**
```
Algoritmo PeajeNacional
    Definir categoria, ejes Como Entero
    Definir horaPico, tieneTag Como Caracter
    Definir tarifaBase, recargoPico, subtotal, descuentoTag, totalPagar Como Real
    Escribir "Ingrese categoria (1-3):"
    Leer categoria
    Si categoria < 1 O categoria > 3 Entonces
        Escribir "Error: categoria invalida."
    SiNo
        Si categoria = 1 Entonces
            tarifaBase <- 12000
        SiNo
            Si categoria = 2 Entonces
                tarifaBase <- 18500
            SiNo
                Escribir "Ingrese ejes (>=2):"
                Leer ejes
                Si ejes < 2 Entonces
                    Escribir "Error: minimo 2 ejes."
                SiNo
                    tarifaBase <- 28000 + (ejes - 2) * 7500
                FinSi
            FinSi
        FinSi
        Si categoria <> 3 O ejes >= 2 Entonces
            Escribir "Hora pico? (S/N):"
            Leer horaPico
            Escribir "Tiene TAG? (S/N):"
            Leer tieneTag
            recargoPico <- 0
            Si horaPico = "S" O horaPico = "s" Entonces
                recargoPico <- tarifaBase * 0.15
            FinSi
            subtotal <- tarifaBase + recargoPico
            descuentoTag <- 0
            Si tieneTag = "S" O tieneTag = "s" Entonces
                descuentoTag <- subtotal * 0.10
            FinSi
            totalPagar <- subtotal - descuentoTag
            Escribir "TOTAL A PAGAR: $", totalPagar
        FinSi
    FinSi
FinAlgoritmo
```

**3. Código C++ compilable:** Ver [`cpp/05_simulacro1_p1_peaje.cpp`](cpp/05_simulacro1_p1_peaje.cpp).

**4. Prueba de Escritorio (Entrada: `categoria=3`, `ejes=4`, `horaPico='S'`, `tieneTag='S'`):**

| Paso | `categoria` | `ejes` | `tarifaBase` | `horaPico` | `recargoPico` | `subtotal` | `tieneTag` | `descuentoTag` | `totalPagar` |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| 1 | `3` | — | `0.0` | `'N'` | `0.0` | — | `'N'` | `0.0` | — |
| 2 | `3` | `4` | `28000 + 2*7500 = 43000.00` | `'S'` | `43000 * 0.15 = 6450.00` | `49450.00` | `'S'` | `49450 * 0.10 = 4945.00` | **`44505.00`** |

---

#### Solución Punto 2: Parqueadero Inteligente (`cpp/06_simulacro1_p2_parqueadero.cpp`)

**1. Análisis EPS:**
- **Entradas:** `tipo` (`char`), `minutosTotales` (`int`), `tieneConvenio` (`char`).
- **Proceso:**
  1. `switch(tipo)` para determinar `tarifaHora` (`M/m`: 1800, `C/c`: 3500, `V/v`: 5000, otro: error).
  2. Validar `minutosTotales >= 1`.
  3. `horasCompletas = minutosTotales / 60`; `minutosSobrantes = minutosTotales % 60`.
  4. Si `horasCompletas == 0` $\Rightarrow$ `horasCobradas = 1`; si no, si `minutosSobrantes > 15` $\Rightarrow$ `horasCobradas = horasCompletas + 1`; si no, `horasCobradas = horasCompletas`.
  5. `subtotal = horasCobradas * tarifaHora`.
  6. Si `horasCobradas >= 6`, `descuentoEstadia = subtotal * 0.15`.
  7. Si convenio `'S'/'s'`, `descuentoConvenio = 2000`.
  8. `total = subtotal - descuentoEstadia - descuentoConvenio`; si `total < 0`, `total = 0`.
- **Salidas:** Tiempo real (`Xh Ym`), `horasCobradas`, `subtotal`, descuentos y `total`.

**2. Código C++ compilable:** Ver [`cpp/06_simulacro1_p2_parqueadero.cpp`](cpp/06_simulacro1_p2_parqueadero.cpp).

**3. Prueba de Escritorio (Entrada: `tipo='C'`, `minutosTotales=380`, `tieneConvenio='S'`):**

| Variable | Valor calculado | Explicación paso a paso |
| :--- | :--- | :--- |
| `tarifaHora` | `3500.00` | Entra al `case 'C':` |
| `horasCompletas` | `380 / 60 = 6` | División entera |
| `minutosSobrantes` | `380 % 60 = 20` | Residuo exacto en minutos |
| `horasCobradas` | `6 + 1 = 7` | Como `minutosSobrantes (20) > 15`, cobra 1 hora adicional |
| `subtotal` | `7 * 3500 = 24500.00` | Sin descuentos aún |
| `descuentoEstadia` | `24500 * 0.15 = 3675.00` | Aplica porque `horasCobradas (7) >= 6` |
| `descuentoConvenio` | `2000.00` | Convenio `'S'` |
| `total` | `24500 - 3675 - 2000 = 18825.00` | Resultado final impreso: **`$18825.00`** |

---

#### Solución Punto 3: Monitor de Invernadero (`cpp/07_simulacro1_p3_invernadero.cpp`)

**1. Análisis EPS y Decisión del Ciclo:**
- Como no sabemos cuántas lecturas ingresará el operador y termina al digitar `-999`, se elige **`while (temp != -999)`** con lectura previa (cebo) y lectura al final del ciclo.
- **Trampa evitada:** Si `tempMin` o `tempMax` se inicializan en `0.0` y todas las lecturas fueran `25.0, 30.0`, `tempMin` quedaría erróneamente en `0.0`. Por eso usamos `if (validas == 0) { tempMin = temp; tempMax = temp; }`.

**2. Código C++ compilable:** Ver [`cpp/07_simulacro1_p3_invernadero.cpp`](cpp/07_simulacro1_p3_invernadero.cpp).

**3. Prueba de Escritorio (Secuencia de entrada: `22.5`, `85.0`, `10.0`, `35.5`, `24.0`, `-999`):**

| Iteración | `temp` leída | ¿Válida `[-10, 60]`? | `validas` | `suma` | `tempMin` | `tempMax` | `alertasFrio` | `alertasCalor` |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Inicial | `22.5` (cebo) | — | `0` | `0.0` | `0.0` | `0.0` | `0` | `0` |
| 1 | `22.5` | Sí (1ª válida) | `1` | `22.5` | `22.5` | `22.5` | `0` | `0` |
| 2 | `85.0` | **No** (descartada) | `1` | `22.5` | `22.5` | `22.5` | `0` | `0` |
| 3 | `10.0` | Sí (`< 12.0`) | `2` | `32.5` | `10.0` | `22.5` | `1` | `0` |
| 4 | `35.5` | Sí (`> 32.0`) | `3` | `68.0` | `10.0` | `35.5` | `1` | `1` |
| 5 | `24.0` | Sí | `4` | `92.0` | `10.0` | `35.5` | `1` | `1` |
| Fin | `-999` | Sale del `while` | `4` | `92.0` | **`10.00`** | **`35.50`** | **`1`** | **`1`** |

Salida final verificada: `Promedio = 92.0 / 4 = 23.00 C`, `Min = 10.00 C`, `Max = 35.50 C`, `Alertas frio = 1`, `Alertas calor = 1`.

---

## 4. SIMULACRO 2 (Corte Final — 90 minutos, 100 puntos)

> **Temas evaluados:** Modularidad (`void`, retorno, `&`), ciclos anidados, vectores estáticos con capacidad fija `MAX` y matrices estáticas `[MAX_F][MAX_C]`. **Prohibido `std::vector`, punteros y memoria dinámica.**

### 4.1 Enunciados y Rúbrica del Simulacro 2

#### Punto 1 (25 puntos — Sugerido: 20 min): Analizador Numérico Modular
Desarrolle un programa modular en C++ que lea un rango `[inicio, fin]` validado (`1 <= inicio <= fin`) mediante una función con paso por referencia `leerRangoValido(int &inicio, int &fin)`. Luego implemente:
- `bool esPrimo(int n)`: devuelve `true` si `n` es primo (`n > 1` y sin divisores entre `2` y $\sqrt{n}$).
- `int sumaDivisoresPropios(int n)`: suma todos los divisores positivos de `n` menores que `n`.
- `bool esPerfecto(int n)`: devuelve `true` si `n > 1` y `sumaDivisoresPropios(n) == n` (ej. `6 = 1 + 2 + 3`).
- `void analizarRango(int inicio, int fin)`: recorre el rango e imprime cuáles son primos, cuántos hay, cuáles son perfectos y cuántos hay.

**Rúbrica P1 (25 pts):** Paso por referencia `&` en lectura validada (5 pts) + `esPrimo` correcto manejando `n = 1` (7 pts) + `sumaDivisoresPropios` y `esPerfecto` (8 pts) + `analizarRango` con conteo exacto y prueba de escritorio (5 pts).

#### Punto 2 (35 puntos — Sugerido: 35 min): Inventario de Tienda (Vectores Estáticos Paralelos)
Con capacidad máxima fija `const int MAX_PROD = 50;`, use tres vectores estáticos paralelos (`codigos[MAX_PROD]`, `stocks[MAX_PROD]`, `precios[MAX_PROD]`) y valide la cantidad lógica `n` (`1 <= n <= MAX_PROD`). Implemente funciones separadas para:
1. `cargarInventario`: leer código, stock ($\ge 0$) y precio ($> 0$).
2. `mostrarInventario`: imprimir la tabla alineada.
3. `indiceMasCaro`: devolver el índice del producto de mayor precio.
4. `contarStockCritico`: contar cuántos productos tienen `stock < umbral` (use umbral `5`).
5. `buscarPorCodigo`: búsqueda secuencial devolviendo índice o `-1`.
6. `ordenarPorPrecioDesc`: método Burbuja ordenando de mayor a menor precio **manteniendo sincronizados los tres vectores**.

**Rúbrica P2 (35 pts):** Vectores estáticos + validación `1..MAX_PROD` (6 pts) + `cargar` y `mostrar` (6 pts) + `indiceMasCaro` y `contarStockCritico` (7 pts) + `buscarPorCodigo` devolviendo `-1` si no está (6 pts) + Burbuja sincronizado en los 3 arreglos (10 pts).

#### Punto 3 (40 puntos — Sugerido: 35 min): Consumo Energético de Edificio (Matriz Estática)
Defina `const int MAX_P = 10;` y `const int MAX_D = 7;` y declare `double consumo[MAX_P][MAX_D]`. Valide `p` pisos (`1..MAX_P`) y `d` días (`1..MAX_D`). Implemente:
1. `leerConsumos(double m[][MAX_D], int pisos, int dias)` validando valores $\ge 0.0$.
2. `mostrarTabla(const double m[][MAX_D], int pisos, int dias)` con formato tabular limpio.
3. `totalPorPiso(const double m[][MAX_D], int piso, int dias)`: suma de una fila.
4. `promedioPorDia(const double m[][MAX_D], int pisos, int dia)`: promedio de una columna.
5. `encontrarPicoMaximo(const double m[][MAX_D], int pisos, int dias, int &pisoMax, int &diaMax)`: devuelve por referencia `&` las coordenadas del mayor consumo.
6. Si `p == d` (matriz cuadrada), invocar `sumarDiagonalPrincipal(const double m[][MAX_D], int n)`.

**Rúbrica P3 (40 pts):** Uso correcto de `[][MAX_D]` en todas las firmas (8 pts) + Lectura/impresión con recorridos válidos (8 pts) + Suma por fila y promedio por columna sin confundir índices `i`/`j` (10 pts) + Pico máximo con `&pisoMax, &diaMax` (9 pts) + Diagonal principal condicionada a `p == d` (5 pts).

---

### 4.2 Solucionario Comentado del Simulacro 2

#### Solución Punto 1: Primos y Perfectos (`cpp/08_simulacro2_p1_primos_perfectos.cpp`)

**Diseño Modular:**
- `leerRangoValido(int &inicio, int &fin)` modifica las dos variables del `main()` con `&`.
- `esPrimo(int n)` evita evaluar `n <= 1` retornando `false` temprano y prueba divisores `d` hasta `d * d <= n`.
- `esPerfecto(int n)` reutiliza `sumaDivisoresPropios(n)` (composición limpia de funciones!).

**Código C++ compilable:** Ver [`cpp/08_simulacro2_p1_primos_perfectos.cpp`](cpp/08_simulacro2_p1_primos_perfectos.cpp).

**Prueba de Escritorio (Entrada: `inicio=1`, `fin=30`):**
- `n = 1`: `esPrimo(1) -> false`, `esPerfecto(1) -> false`.
- `n = 2..30`: primos encontrados `2, 3, 5, 7, 11, 13, 17, 19, 23, 29` (`cantPrimos = 10`).
- `n = 6`: `sumaDivisoresPropios(6) = 1 + 2 + 3 = 6` $\Rightarrow$ **Perfecto**.
- `n = 28`: `sumaDivisoresPropios(28) = 1 + 2 + 4 + 7 + 14 = 28` $\Rightarrow$ **Perfecto**.
- Total perfectos = `2` (`6` y `28`).

---

#### Solución Punto 2: Inventario con Vectores Estáticos (`cpp/09_simulacro2_p2_inventario_vector.cpp`)

**Clave del diseño (Arreglos Paralelos):**
El índice `i` conecta los tres arreglos: el producto `i` tiene código `codigos[i]`, existencias `stocks[i]` y precio `precios[i]`. Por eso, cuando Burbuja intercambia `precios[j]` con `precios[j+1]`, **debe intercambiar también `codigos` y `stocks` en esas mismas posiciones**, o los precios quedarían asignados al código equivocado!

**Código C++ compilable:** Ver [`cpp/09_simulacro2_p2_inventario_vector.cpp`](cpp/09_simulacro2_p2_inventario_vector.cpp).

**Prueba de Escritorio (`n = 3`: `(101, 8, $4500)`, `(102, 2, $12000)`, `(103, 15, $3200)`, consultar `102`):**

| Operación | Resultado en memoria / pantalla |
| :--- | :--- |
| Estado inicial | `i=0: (101, 8, 4500.00)`, `i=1: (102, 2, 12000.00)`, `i=2: (103, 15, 3200.00)` |
| `indiceMasCaro` | Retorna `posMax = 1` $\Rightarrow$ Código `102`, Precio `$12000.00` |
| `contarStockCritico(5)` | Solo `stocks[1] = 2 < 5` $\Rightarrow$ retorna `1` |
| `buscarPorCodigo(102)` | Encuentra en `i = 1` $\Rightarrow$ Stock `2`, Precio `$12000.00` |
| `ordenarPorPrecioDesc` | Pasada 0 compara `4500 < 12000` (intercambia los 3) y luego `4500 < 3200` (no):<br>`[(102, 2, 12000.00), (101, 8, 4500.00), (103, 15, 3200.00)]` |

---

#### Solución Punto 3: Consumo Energético con Matriz Estática (`cpp/10_simulacro2_p3_consumo_matriz.cpp`)

**Clave del diseño (Filas vs. Columnas):**
- Para `totalPorPiso`: la fila `piso` queda fija y varía la columna `j` (`0..dias-1`).
- Para `promedioPorDia`: la columna `dia` queda fija y varía la fila `i` (`0..pisos-1`).
- Para `encontrarPicoMaximo`: inicializamos `pisoMax = 0; diaMax = 0;` y comparamos `m[i][j] > m[pisoMax][diaMax]`, devolviendo las coordenadas mediante `&pisoMax, &diaMax`.

**Código C++ compilable:** Ver [`cpp/10_simulacro2_p3_consumo_matriz.cpp`](cpp/10_simulacro2_p3_consumo_matriz.cpp).

**Prueba de Escritorio (`p = 2`, `d = 2`, matriz `[[10.5, 12.0], [8.5, 15.0]]`):**

| Métrica | Cálculo exacto | Salida verificada |
| :--- | :--- | :--- |
| `totalPorPiso(0)` | `10.5 + 12.0` | `22.50 kWh` (Piso 1) |
| `totalPorPiso(1)` | `8.5 + 15.0` | `23.50 kWh` (Piso 2) |
| `promedioPorDia(0)` | `(10.5 + 8.5) / 2` | `9.50 kWh` (Día 1) |
| `promedioPorDia(1)` | `(12.0 + 15.0) / 2` | `13.50 kWh` (Día 2) |
| `encontrarPicoMaximo` | Mayor valor `15.0` en `[1][1]` | `15.00 kWh (Piso 2, Dia 2)` |
| `sumarDiagonalPrincipal` | Como `p == d == 2`: `m[0][0] + m[1][1] = 10.5 + 15.0` | **`25.50 kWh`** |

---

## 5. Ejercicios Propuestos Express de Modularidad (Con Pistas y Solucionario)

### Ejercicio 1: Normalizar Dos Números en Orden Ascendente
Escriba una función `void ordenarPar(int &a, int &b)` que garantice que al terminar la llamada se cumpla `a <= b` (si `a > b`, debe intercambiarlos).
- **Pista del Monitor:** Reutiliza `intercambiar(a, b)` con paso por referencia `&`.
- **Solución:**
  ```cpp
  void ordenarPar(int &a, int &b) {
      if (a > b) {
          int temp = a;
          a = b;
          b = temp;
      }
  }
  ```

### Ejercicio 2: Contar Aprobados en un Vector Estático
Dado un vector `double notas[MAX]` con `n` notas válidas (`0.0` a `5.0`), escriba `int contarAprobados(const double notas[], int n, double minima)` que cuente cuántas notas son $\ge \text{minima}$.
- **Pista del Monitor:** Usa `const double notas[]` porque la función solo consulta el vector; nunca modifiques `notas[i]`.
- **Solución:**
  ```cpp
  int contarAprobados(const double notas[], int n, double minima) {
      int cont = 0;
      for (int i = 0; i < n; i++) {
          if (notas[i] >= minima) {
              cont++;
          }
      }
      return cont;
  }
  ```

### Ejercicio 3: Verificar Simetría de una Matriz Cuadrada Estática
Implemente `bool esSimetrica(const int m[][MAX_C], int n)` que retorne `true` si `m[i][j] == m[j][i]` para toda posición, y `false` apenas encuentre una pareja distinta.
- **Pista del Monitor:** Basta recorrer la triangular superior (`j = i + 1` hasta `n - 1`) para no comparar dos veces la misma pareja ni la diagonal consigo misma.
- **Solución:**
  ```cpp
  bool esSimetrica(const int m[][MAX_C], int n) {
      for (int i = 0; i < n; i++) {
          for (int j = i + 1; j < n; j++) {
              if (m[i][j] != m[j][i]) {
                  return false;
              }
          }
      }
      return true;
  }
  ```

### Ejercicio 4: Cazador de Errores de Parcial (Diagnóstico)
Encuentre los **3 errores mortales** en el siguiente fragmento antes de compilar:
```cpp
void leerMatriz(int m[][], int f, int c);
int main() {
    int n = 5;
    int vec[n];
    mostrar(vec[n], n);
}
```
- **Solución:** (1) `int m[][]` es inválido porque falta la segunda dimensión constante `[MAX_C]`; (2) `int vec[n];` usa un tamaño variable (VLA), debe usarse `const int MAX = ...; int vec[MAX];`; (3) `mostrar(vec[n], n)` pasa un entero fuera de rango en lugar del arreglo (`mostrar(vec, n)`).

---

## 6. Cierre del Curso de 30 Horas: Checklist de Dominio

Si puedes resolver los 2 simulacros anteriores sin consultar apuntes dentro de los 90 minutos asignados, dominas el ciclo completo de fundamentos de programación:
- **Análisis antes de código** (Método de los 5 Pasos + EPS).
- **Representación visual** (DFD limpio y sin flechas huérfanas).
- **Pseudocódigo estructurado** (PSeInt con sintaxis consistente).
- **Implementación robusta en C++17 básico** (tipos, condicionales, ciclos, vectores estáticos, matrices estáticas y funciones modulares).
