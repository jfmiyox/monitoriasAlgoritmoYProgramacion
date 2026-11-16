# Módulo 07: Matrices Estáticas (Arreglos Bidimensionales)

> **Duración estimada:** 4.0 horas (2 sesiones de 2 horas)  
> **Ruta:** DFD $\rightarrow$ PSeInt $\rightarrow$ C++ Básico (Estático)  
> **Prerrequisitos:** M05 (Ciclos anidados), M06 (Vectores estáticos)

---

## 1. Explicado Para Tontos: ¿Qué es una Matriz Estática?

Si un **vector** es una fila de casilleros en un solo pasillo, una **matriz estática** (arreglo bidimensional) es un **edificio de apartamentos o una hoja de cálculo de Excel**:

* Tiene **filas horizontales** (como los pisos del edificio, numerados desde la **fila `0`** hasta `f - 1` en C++).
* Tiene **columnas verticales** (como los apartamentos por piso, numerados desde la **columna `0`** hasta `c - 1` en C++).
* Cada celda se identifica con **dos coordenadas exactas**: `matriz[fila][columna]`. Primero el piso (`fila`), luego la puerta (`columna`).
* La capacidad del edificio se construye **fija desde el inicio** (`MAX_F` filas por `MAX_C` columnas, o un tamaño literal fijo como una sala de cine `5x6`). Aunque hoy solo ocupemos `f` filas y `c` columnas, el terreno reservado en la memoria RAM siempre es fijo y estático.

---

## 2. Declaración Estática e Inicialización

### 2.1 Las dos formas válidas en este curso

#### Forma A: Tamaño fijo literal (cuando las dimensiones nunca cambian)
```cpp
char cine[5][6];        // 5 filas (0..4) x 6 columnas (0..5) = 30 sillas
int tablero[3][3];      // Tablero fijo de triqui 3x3
```

#### Forma B: Capacidad máxima con constantes + dimensiones lógicas `f` y `c`
```cpp
const int MAX_F = 20;
const int MAX_C = 20;
int mat[MAX_F][MAX_C];  // Reserva 20x20 = 400 enteros estaticos en RAM
int f, c;               // Cuantas filas y columnas usaremos hoy

do {
    cout << "Filas (1 a " << MAX_F << "): ";
    cin >> f;
} while (f < 1 || f > MAX_F);

do {
    cout << "Columnas (1 a " << MAX_C << "): ";
    cin >> c;
} while (c < 1 || c > MAX_C);
```

> **⚠️ ¿Por qué NO hacemos `int m[f][c];` ni `vector<vector<int>>` en este curso?**
> 1. **`int m[f][c];` es un VLA no estándar:** C++ estándar prohíbe arreglos cuyo tamaño dependa de variables en tiempo de ejecución. Además, en matrices el riesgo es **cuadrático**: si el usuario digita `10000 x 10000`, desbordas de inmediato la memoria de pila (*stack overflow*).
> 2. **Matrices dinámicas (`new` o `vector<vector<...>>`):** Requieren punteros dobles o contenedores de la STL que corresponden a cursos posteriores. En Fundamentos de Programación dominamos primero la lógica bidimensional con memoria estática segura y validada (`MAX_F`, `MAX_C`).

### 2.2 Inicialización y Trampas Clásicas
```cpp
int m1[2][3] = {
    {10, 20, 30},   // Fila 0
    {40, 50, 60}    // Fila 1
};
int m2[4][4] = {0}; // Todas las 16 celdas quedan en 0!
```

> **🔥 OJO — Trampas Clásicas en Matrices:**
> 1. **Orden de índices `[fila][columna]`:** Jamás intercambies `mat[i][j]` por `mat[j][i]` sin querer. En una matriz rectangular `2x5`, `mat[4][1]` se sale de las 2 filas y corrompe la memoria.
> 2. **PSeInt vs C++:** En **PSeInt** declaras `Dimension mat[20, 20];` (con coma `,` y usando índices de `1` a `f` y `1` a `c` por defecto). En **C++** declaras `int mat[20][20];` (con doble corchete `[][ ]` y usando índices `0` a `f-1` y `0` a `c-1`).
> 3. **Olvidar reiniciar el acumulador:** Al sumar por filas o por columnas, si declaras `sumaFila = 0` **afuera** de ambos `for`, acumularás la suma de todas las filas anteriores en lugar de cada fila individual.

---

## 3. Recorrido por Filas vs Recorrido por Columnas

Necesitas **dos ciclos `for` anidados**: uno fija una dimensión y el otro barre la otra. El orden define cómo caminas por la tabla:

### 3.1 Recorrido por Filas (`for i` afuera $\rightarrow$ `for j` adentro)
Visitas toda la fila `0` de izquierda a derecha, luego toda la fila `1`, etc.
```cpp
for (int i = 0; i < f; i++) {          // Fija la fila i
    for (int j = 0; j < c; j++) {      // Recorre todas las columnas j
        cout << mat[i][j] << " ";
    }
    cout << "\n";                      // Salto de linea al terminar cada fila
}
```
**¿Cuándo usarlo?** Para leer e imprimir la matriz como tabla, calcular totales/promedios **por estudiante** (si cada fila es un estudiante) o **por tienda**.

### 3.2 Recorrido por Columnas (`for j` afuera $\rightarrow$ `for i` adentro)
Visitas toda la columna `0` de arriba hacia abajo, luego toda la columna `1`, etc.
```cpp
for (int j = 0; j < c; j++) {          // Fija la columna j
    double sumaCol = 0.0;              // Reinicia al cambiar de columna!
    for (int i = 0; i < f; i++) {      // Recorre todas las filas i
        sumaCol += mat[i][j];
    }
    cout << "Suma columna " << j << ": " << sumaCol << "\n";
}
```
**¿Cuándo usarlo?** Para calcular totales/promedios **por materia** (si cada columna es una materia) o **por mes** en una matriz de ventas.

---

## 4. Patrones Maestros de Matrices Estáticas

### Patrón 1: Suma Total y Promedio General
```cpp
double suma = 0.0;
for (int i = 0; i < f; i++) {
    for (int j = 0; j < c; j++) {
        suma += mat[i][j];
    }
}
double promedio = suma / (f * c);
```

### Patrón 2: Suma y Promedio por Fila / por Columna
* **Por fila:** `for i` afuera, `double sumaFila = 0;` dentro del `for i`, `for j` adentro.
* **Por columna:** `for j` afuera, `double sumaCol = 0;` dentro del `for j`, `for i` adentro.

### Patrón 3: Mayor y Menor con Coordenadas `(fila, col)`
```cpp
int mayor = mat[0][0], filaMay = 0, colMay = 0;
for (int i = 0; i < f; i++) {
    for (int j = 0; j < c; j++) {
        if (mat[i][j] > mayor) {
            mayor = mat[i][j];
            filaMay = i;
            colMay = j;
        }
    }
}
```

### Patrón 4: Matriz Cuadrada (`f == c = n`) — Diagonales, Triangulares y Simetría

Para una matriz cuadrada de orden `n = 4` (índices `0, 1, 2, 3`):

| Zona de la matriz | Condición matemática (C++ Base 0) | Condición en PSeInt (Base 1) | Coordenadas en `4x4` (Base 0) |
| :--- | :--- | :--- | :--- |
| **Diagonal Principal** | `i == j` | `i = j` | `(0,0), (1,1), (2,2), (3,3)` |
| **Diagonal Secundaria** | `i + j == n - 1` | `i + j = n + 1` | `(0,3), (1,2), (2,1), (3,0)` |
| **Triangular Superior** (estricta) | `i < j` (con diagonal: `i <= j`) | `i < j` | `(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)` |
| **Triangular Inferior** (estricta) | `i > j` (con diagonal: `i >= j`) | `i > j` | `(1,0), (2,0), (2,1), (3,0), (3,1), (3,2)` |

* **Recorrer una diagonal en $O(n)$ (un solo `for`, mucho más limpio):**
  ```cpp
  for (int i = 0; i < n; i++) {
      sumaDiagP += mat[i][i];            // Principal
      sumaDiagS += mat[i][n - 1 - i];    // Secundaria
  }
  ```
* **Simetría (`mat[i][j] == mat[j][i]`):** Solo comparas el triángulo superior contra el inferior (`j = i + 1` hasta `n - 1`):
  ```cpp
  bool simetrica = true;
  for (int i = 0; i < n && simetrica; i++) {
      for (int j = i + 1; j < n; j++) {
          if (mat[i][j] != mat[j][i]) { simetrica = false; break; }
      }
  }
  ```

### Patrón 5: Matriz Transpuesta (`T[j][i] = A[i][j]`)
Convierte una matriz `A` de `f x c` en una matriz `T` de `c x f` intercambiando filas por columnas:
```cpp
for (int i = 0; i < f; i++) {
    for (int j = 0; j < c; j++) {
        T[j][i] = A[i][j];
    }
}
```

---

## 5. Ocho Problemas Resueltos Completos (EPS + PSeInt + C++ + Prueba de Escritorio)

---

### Problema 1: Boletín de Notas (`N` Estudiantes $\times$ `M` Materias)
**Enunciado:** Un colegio registra las notas (`0.0..5.0`) de `f` estudiantes (`MAX_EST = 30`) en `c` materias (`MAX_MAT = 10`). Calcular el promedio de cada estudiante (por filas), el promedio de cada materia (por columnas) y la nota más alta del salón con sus coordenadas `(estudiante, materia)`.

#### Análisis EPS
* **Entradas:** `f`, `c`, `notas[30][10]`.
* **Proceso:** Lectura validada por filas. Acumular por filas para promedio de estudiante; acumular por columnas para promedio de materia; buscar máximo guardando `(filaMayor, colMayor)`.
* **Salidas:** Lista de promedios por estudiante, por materia y nota máxima con coordenadas.

#### PSeInt (`pseint/m07_p01_boletin_notas.psc`) y C++ (`cpp/m07_p01_boletin_notas.cpp`)
```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const int MAX_EST = 30, MAX_MAT = 10;
    double notas[MAX_EST][MAX_MAT];
    int f, c;

    do { cin >> f; } while (f < 1 || f > MAX_EST);
    do { cin >> c; } while (c < 1 || c > MAX_MAT);

    for (int i = 0; i < f; i++) {
        for (int j = 0; j < c; j++) {
            do { cin >> notas[i][j]; } while (notas[i][j] < 0.0 || notas[i][j] > 5.0);
        }
    }

    cout << fixed << setprecision(2);
    for (int i = 0; i < f; i++) {
        double sumaEst = 0.0;
        for (int j = 0; j < c; j++) sumaEst += notas[i][j];
        cout << "Estudiante " << i << ": " << (sumaEst / c) << "\n";
    }

    for (int j = 0; j < c; j++) {
        double sumaMat = 0.0;
        for (int i = 0; i < f; i++) sumaMat += notas[i][j];
        cout << "Materia " << j << ": " << (sumaMat / f) << "\n";
    }

    double mayor = notas[0][0];
    int filaMayor = 0, colMayor = 0;
    for (int i = 0; i < f; i++) {
        for (int j = 0; j < c; j++) {
            if (notas[i][j] > mayor) {
                mayor = notas[i][j]; filaMayor = i; colMayor = j;
            }
        }
    }
    cout << "Mejor nota: " << mayor << " en (" << filaMayor << ", " << colMayor << ")\n";
    return 0;
}
```

#### Prueba de Escritorio (`2` estudiantes $\times$ `3` materias)
Tabla `notas`:
* Fila 0 (Est 0): `[4.0, 3.5, 5.0]` $\rightarrow$ suma `12.5` $\rightarrow$ prom `4.17`.
* Fila 1 (Est 1): `[2.5, 4.5, 3.0]` $\rightarrow$ suma `10.0` $\rightarrow$ prom `3.33`.
* Columnas (Materias): Mat 0: `(4.0+2.5)/2 = 3.25`; Mat 1: `(3.5+4.5)/2 = 4.00`; Mat 2: `(5.0+3.0)/2 = 4.00`.
* Mayor global: `5.00` en `(estudiante=0, materia=2)`.

---

### Problema 2: Ventas por Tienda y Mes
**Enunciado:** Una empresa con `t` tiendas (`MAX_T = 15`) registra sus ventas durante `m` meses (`MAX_M = 12`). Calcular el total global, la tienda con mayor venta acumulada (por filas) y el mes con menor venta acumulada (por columnas).

#### Análisis EPS
* **Entradas:** `t`, `m`, `ventas[15][12]`.
* **Proceso:** Recorrido por filas acumulando `sumaTienda` y `totalGlobal` para detectar `mejorTienda`; luego recorrido por columnas acumulando `sumaMes` para detectar `peorMes`.
* **Salidas:** Totales por tienda, por mes, `totalGlobal`, `mejorTienda`, `peorMes`.

*(Archivos completos: `pseint/m07_p02_ventas_tiendas_meses.psc` y `cpp/m07_p02_ventas_tiendas_meses.cpp`).*

#### Prueba de Escritorio (`2` tiendas $\times$ `3` meses: Fila 0 `[100, 200, 150]`, Fila 1 `[300, 250, 100]`)
* Tienda 0: `450.00`; Tienda 1: `650.00` $\rightarrow$ **Tienda líder: 1 ($650.00)**.
* Mes 0: `400.00`; Mes 1: `450.00`; Mes 2: `250.00` $\rightarrow$ **Mes menor venta: 2 ($250.00)**.
* **Total global:** `$1100.00`.

---

### Problema 3: Reserva de Sillas de Cine `5x6` (Tamaño Fijo Literal)
**Enunciado:** Modelar una sala de cine fija `char sala[5][6]` donde todas las sillas comienzan libres (`'L'`). Menú repetitivo: (1) Ver mapa, (2) Reservar silla `(f, c)` validando coordenadas y que no esté ocupada (`'X'`), (3) Estadísticas (ocupadas, libres y porcentaje), (0) Salir.

#### Análisis EPS
* **Entradas:** `opcion`, coordenadas `f` (`0..4`) y `c` (`0..5`).
* **Proceso:** Inicializar matriz `5x6` con `'L'`. Validar rango `0 <= f < 5` y `0 <= c < 6`; si `sala[f][c] == 'L'`, cambiar a `'X'`.
* **Salidas:** Mapa formateado de la sala y estadísticas.

#### C++ (`cpp/m07_p03_reserva_cine_5x6.cpp`) — *(PSeInt en `pseint/m07_p03_reserva_cine_5x6.psc`)*
```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const int FILAS = 5, COLS = 6;
    char sala[5][6];
    for (int i = 0; i < FILAS; i++)
        for (int j = 0; j < COLS; j++)
            sala[i][j] = 'L';

    int opcion;
    do {
        cout << "\n1.Mapa  2.Reservar  3.Estadisticas  0.Salir: ";
        if (!(cin >> opcion)) break;

        if (opcion == 1) {
            for (int i = 0; i < FILAS; i++) {
                for (int j = 0; j < COLS; j++) cout << sala[i][j] << " ";
                cout << "\n";
            }
        } else if (opcion == 2) {
            int f, c;
            cin >> f >> c;
            if (f < 0 || f >= FILAS || c < 0 || c >= COLS) {
                cout << "Coordenada fuera de rango.\n";
            } else if (sala[f][c] == 'X') {
                cout << "Silla ocupada.\n";
            } else {
                sala[f][c] = 'X';
                cout << "Reservada (" << f << ", " << c << ").\n";
            }
        } else if (opcion == 3) {
            int ocupadas = 0;
            for (int i = 0; i < FILAS; i++)
                for (int j = 0; j < COLS; j++)
                    if (sala[i][j] == 'X') ocupadas++;
            cout << "Ocupadas: " << ocupadas << " | Libres: " << (30 - ocupadas) << "\n";
        }
    } while (opcion != 0);
    return 0;
}
```

#### Prueba de Escritorio
* Reservar `(1, 2)` $\rightarrow$ `sala[1][2] = 'X'`.
* Estadísticas: `Ocupadas = 1`, `Libres = 29`, `Porcentaje = (1 / 30.0) * 100 = 3.3%`.
* Intentar reservar `(1, 2)` de nuevo $\rightarrow$ rechaza por estar ocupada.

---

### Problema 4: Diagonales y Triangulares en Matriz Cuadrada `N x N`
**Enunciado:** Leer una matriz cuadrada `N x N` (`MAX = 15`). Mostrar y sumar la diagonal principal (`i == j`), la diagonal secundaria (`i + j == n - 1`), la suma de los elementos estrictamente encima de la diagonal principal (`i < j`) y estrictamente debajo (`i > j`).

#### Análisis EPS
* **Entradas:** `n` (`1..15`), `mat[15][15]`.
* **Proceso:** Barrer `i = 0..n-1` para ambas diagonales; doble bucle `i, j` clasificando `i < j` (triangular superior) e `i > j` (triangular inferior).
* **Salidas:** Elementos y sumas de las cuatro zonas.

*(Archivos completos: `pseint/m07_p04_diagonales_y_triangulares.psc` y `cpp/m07_p04_diagonales_y_triangulares.cpp`).*

#### Prueba de Escritorio (`N = 3`, matriz `[[1,2,3],[4,5,6],[7,8,9]]`)
* Diagonal principal (`i == j`): `1, 5, 9` $\rightarrow$ suma `15`.
* Diagonal secundaria (`i + j == 2`): `3, 5, 7` $\rightarrow$ suma `15`.
* Triangular superior (`i < j`): `2, 3, 6` $\rightarrow$ suma `11`.
* Triangular inferior (`i > j`): `4, 7, 8` $\rightarrow$ suma `19`.

---

### Problema 5: Matriz Transpuesta y Verificación de Simetría
**Enunciado:** Dada una matriz `A` de `F x C` (`MAX_F = 15, MAX_C = 15`), generar su transpuesta `T` de `C x F`. Además, si es cuadrada (`F == C`), verificar si es simétrica (`A[i][j] == A[j][i]`).

#### Análisis EPS
* **Entradas:** `f`, `c`, `A[15][15]`.
* **Proceso:** Asignar `T[j][i] = A[i][j]`. Si `f == c`, recorrer `i = 0..f-1` y `j = i+1..c-1` verificando igualdad con bandera `esSimetrica`.
* **Salidas:** Matriz `T` y diagnóstico de simetría.

*(Archivos completos: `pseint/m07_p05_transpuesta_y_simetria.psc` y `cpp/m07_p05_transpuesta_y_simetria.cpp`).*

#### Prueba de Escritorio (`A = [[1,2,3],[2,4,5],[3,5,6]]`)
* `T` queda idéntica a `A`.
* Comparaciones de simetría: `(0,1)==(1,0)` (`2==2`), `(0,2)==(2,0)` (`3==3`), `(1,2)==(2,1)` (`5==5`) $\rightarrow$ `esSimetrica = true`.

---

### Problema 6: Verificador de Cuadrado Mágico `N x N`
**Enunciado:** Leer una matriz cuadrada `N x N` (`MAX = 10`) y verificar si es un **Cuadrado Mágico** (todas sus filas, todas sus columnas y ambas diagonales suman exactamente lo mismo).

#### Análisis EPS
* **Entradas:** `n`, `mat[10][10]`.
* **Proceso:** Calcular `sumaObjetivo` con la fila `0`. Validar cada fila `i`, cada columna `j`, diagonal principal `diagP` y secundaria `diagS` usando bandera `bool esMagico = true`.
* **Salidas:** Si es cuadrado mágico (con su constante mágica) o si no lo es.

#### C++ (`cpp/m07_p06_cuadrado_magico.cpp`) — *(PSeInt en `pseint/m07_p06_cuadrado_magico.psc`)*
```cpp
#include <iostream>
using namespace std;

int main() {
    const int MAX = 10;
    int mat[MAX][MAX], n;
    do { cin >> n; } while (n < 1 || n > MAX);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> mat[i][j];

    int sumaObjetivo = 0;
    for (int j = 0; j < n; j++) sumaObjetivo += mat[0][j];

    bool esMagico = true;
    for (int i = 0; i < n && esMagico; i++) {
        int sFila = 0;
        for (int j = 0; j < n; j++) sFila += mat[i][j];
        if (sFila != sumaObjetivo) esMagico = false;
    }
    for (int j = 0; j < n && esMagico; j++) {
        int sCol = 0;
        for (int i = 0; i < n; i++) sCol += mat[i][j];
        if (sCol != sumaObjetivo) esMagico = false;
    }
    if (esMagico) {
        int dP = 0, dS = 0;
        for (int i = 0; i < n; i++) {
            dP += mat[i][i];
            dS += mat[i][n - 1 - i];
        }
        if (dP != sumaObjetivo || dS != sumaObjetivo) esMagico = false;
    }
    cout << (esMagico ? "ES Cuadrado Magico\n" : "NO es Cuadrado Magico\n");
    return 0;
}
```

#### Prueba de Escritorio (Cuadrado de Lo Shu `[[8,1,6],[3,5,7],[4,9,2]]`)
* `sumaObjetivo = 8 + 1 + 6 = 15`.
* Filas: `15, 15, 15`. Columnas: `8+3+4=15`, `1+5+9=15`, `6+7+2=15`.
* Diagonales: `8+5+2=15`, `6+5+4=15`. $\rightarrow$ **ES Cuadrado Mágico (constante 15)**.

---

### Problema 7: Búsqueda de Coordenadas e Intercambio de Filas
**Enunciado:** Dada una matriz `F x C` (`MAX_F = 20, MAX_C = 20`): (a) Buscar todas las apariciones de un valor `objetivo` imprimiendo `(fila, col)`, y (b) Encontrar la fila que contiene al menor elemento global e intercambiar toda esa fila con la fila `0`.

#### Análisis EPS
* **Entradas:** `f`, `c`, `mat[20][20]`, `objetivo`.
* **Proceso:** Recorrido exhaustivo contando coincidencias; segundo recorrido hallando `(filaMenor, colMenor)`; si `filaMenor != 0`, recorrer `j = 0..c-1` intercambiando `mat[0][j]` con `mat[filaMenor][j]`.
* **Salidas:** Coordenadas halladas y matriz modificada.

*(Archivos completos: `pseint/m07_p07_busqueda_e_intercambio_filas.psc` y `cpp/m07_p07_busqueda_e_intercambio_filas.cpp`).*

#### Prueba de Escritorio (`2x3`: `[[9, 5, 7], [5, 1, 8]]`, `objetivo = 5`)
* Coordenadas de `5`: `(0, 1)` y `(1, 0)` (total `2`).
* Menor global: `1` en `(1, 1)` $\rightarrow$ `filaMenor = 1`.
* Intercambia fila `0` con fila `1`: resultado `[[5, 1, 8], [9, 5, 7]]`.

---

### Problema 8: Multiplicación de Matrices Estáticas (`A * B`)
**Enunciado:** Dadas dos matrices estáticas `A` (`f1 x c1`) y `B` (`f2 x c2`) con capacidad `MAX = 15`, validar si son multiplicables (`c1 == f2`). Si lo son, calcular `R = A * B` (`f1 x c2`) usando el triple ciclo anidado (`i, j, k`).

#### Análisis EPS
* **Entradas:** `f1, c1, f2, c2`, matrices `A[15][15]`, `B[15][15]`.
* **Proceso:** Si `c1 != f2`, mostrar error y terminar. Si `c1 == f2`, para cada celda `(i, j)` de `R`, acumular `R[i][j] = sum_{k=0}^{c1-1} A[i][k] * B[k][j]`.
* **Salidas:** Matriz `R` de `f1 x c2`.

#### C++ (`cpp/m07_p08_multiplicacion_matrices.cpp`) — *(PSeInt en `pseint/m07_p08_multiplicacion_matrices.psc`)*
```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const int MAX = 15;
    int A[MAX][MAX], B[MAX][MAX], R[MAX][MAX] = {0};
    int f1, c1, f2, c2;

    do { cin >> f1 >> c1; } while (f1 < 1 || f1 > MAX || c1 < 1 || c1 > MAX);
    do { cin >> f2 >> c2; } while (f2 < 1 || f2 > MAX || c2 < 1 || c2 > MAX);

    if (c1 != f2) {
        cout << "No multiplicables: c1 != f2.\n";
        return 0;
    }

    for (int i = 0; i < f1; i++)
        for (int j = 0; j < c1; j++) cin >> A[i][j];

    for (int i = 0; i < f2; i++)
        for (int j = 0; j < c2; j++) cin >> B[i][j];

    for (int i = 0; i < f1; i++) {
        for (int j = 0; j < c2; j++) {
            int suma = 0;
            for (int k = 0; k < c1; k++) {
                suma += A[i][k] * B[k][j];
            }
            R[i][j] = suma;
        }
    }

    for (int i = 0; i < f1; i++) {
        for (int j = 0; j < c2; j++) cout << setw(6) << R[i][j];
        cout << "\n";
    }
    return 0;
}
```

#### Prueba de Escritorio (`A(2x3) = [[1,2,3],[4,5,6]]`, `B(3x2) = [[7,8],[9,10],[11,12]]`)
* `R[0][0] = 1*7 + 2*9 + 3*11 = 7 + 18 + 33 = 58`
* `R[0][1] = 1*8 + 2*10 + 3*12 = 8 + 20 + 36 = 64`
* `R[1][0] = 4*7 + 5*9 + 6*11 = 28 + 45 + 66 = 139`
* `R[1][1] = 4*8 + 5*10 + 6*12 = 32 + 50 + 72 = 154`

---

## 6. Catorce Ejercicios Propuestos (con Pistas)

> **Regla:** Solo matrices estáticas (`const int MAX_F = ..., MAX_C = ...; tipo mat[MAX_F][MAX_C];` o tamaño literal fijo). Valida `f` y `c`.

1. **[Básico] Suma de dos matrices `A + B`:** Lee `f`, `c` (`MAX = 20`) y dos matrices `A` y `B` de igual tamaño. Construye `C[i][j] = A[i][j] + B[i][j]`.  
   *Pista:* Un doble `for` calcula cada celda sumando los mismos índices `i, j`.
2. **[Básico] Conteo de pares, impares y ceros en matriz:** Lee una matriz `F x C` (`MAX = 15`) de enteros y cuenta cuántos son ceros, cuántos pares no nulos y cuántos impares.  
   *Pista:* Evalúa `mat[i][j] == 0` **antes** que `mat[i][j] % 2 == 0` para no contar el `0` como par no nulo.
3. **[Básico] Matriz identidad `N x N`:** Dado `N` (`1..15`), llena automáticamente una matriz con `1` en la diagonal principal (`i == j`) y `0` en el resto, e imprímela.  
   *Pista:* Puedes usar operador condicional o `if (i == j) m[i][j] = 1; else m[i][j] = 0;`.
4. **[Básico] Suma del borde (marco) de una matriz:** Dada una matriz `F x C` (`MAX = 20`), suma únicamente las celdas ubicadas en el perímetro exterior (primera fila, última fila, primera columna, última columna, ¡sin sumar dos veces las esquinas!).  
   *Pista:* Usa un único `if (i == 0 || i == f - 1 || j == 0 || j == c - 1)` dentro del doble `for`.
5. **[Intermedio] Máximo por cada fila y mínimo por cada columna:** Lee una matriz `F x C` (`MAX = 15`). Imprime el máximo de cada fila en un vector `maxFila[MAX]` y el mínimo de cada columna en `minCol[MAX]`.  
   *Pista:* Inicializa `maxFila[i] = mat[i][0]` dentro del `for i`, y `minCol[j] = mat[0][j]` dentro del `for j`.
6. **[Intermedio] Matriz de temperaturas semanales (7 días $\times$ 3 jornadas):** Declara `double temp[7][3];` (Mañana, Tarde, Noche). Lee las 21 temperaturas y determina qué día tuvo el promedio más alto y en qué jornada hizo más frío en toda la semana.  
   *Pista:* El día es la fila (`0..6`) y la jornada la columna (`0..2`).
7. **[Intermedio] Verificar matriz diagonal y triangular superior:** Dada `N x N` (`MAX = 12`), verifica con banderas booleanas si es **matriz diagonal** (todos los elementos con `i != j` valen `0`) y si es **triangular superior** (todos los de debajo `i > j` valen `0`).  
   *Pista:* Arranca ambas banderas en `true` y cámbialas a `false` apenas encuentres un valor `!= 0` en la zona prohibida.
8. **[Intermedio] Ordenar cada fila de una matriz:** Dada `F x C` (`MAX = 20`), ordena ascendentemente los elementos dentro de cada fila independiente usando Burbuja.  
   *Pista:* Fija la fila `i` afuera y ejecuta Burbuja sobre `mat[i][j]` vs `mat[i][j + 1]`.
9. **[Intermedio] Sumar las dos diagonales sin repetir el centro:** Dada una matriz `N x N` (`MAX = 15`), suma los elementos de ambas diagonales; si `N` es impar, el elemento central `mat[n/2][n/2]` debe sumarse **una sola vez**.  
   *Pista:* Suma ambas diagonales y al final, si `n % 2 != 0`, resta `mat[n / 2][n / 2]`.
10. **[Intermedio] Rotar matriz cuadrada `90°` en sentido horario:** Dada `A` de `N x N` (`MAX = 12`), guarda en `R[MAX][MAX]` la matriz rotada 90 grados a la derecha.  
    *Pista:* La fila `i` de `A` pasa a ser la columna `n - 1 - i` de `R`: `R[j][n - 1 - i] = A[i][j]`.
11. **[Reto] Punto de silla (*Saddle Point*):** En una matriz `F x C` (`MAX = 15`), un elemento `mat[i][j]` es punto de silla si es el **menor de su fila `i`** y al mismo tiempo el **mayor de su columna `j`**. Imprime todas las coordenadas que lo cumplan (o indica si no hay).  
    *Pista:* Para cada fila `i`, halla primero el valor mínimo de la fila `minF` y luego revisa si las celdas de esa fila que igualan `minF` son también máximas en su columna.
12. **[Reto] Recorrido en espiral:** Dada una matriz `F x C` (`MAX = 15`), imprime sus elementos en orden espiral horario (borde superior $\rightarrow$ borde derecho $\rightarrow$ borde inferior $\rightarrow$ borde izquierdo $\rightarrow$ hacia adentro).  
    *Pista:* Usa cuatro límites: `top = 0, bottom = f - 1, left = 0, right = c - 1` en un `while (top <= bottom && left <= right)`.
13. **[Reto] Tablero de Buscaminas (conteo de minas vecinas):** Dada una matriz fija `char mapa[5][5]` con `'*'` (mina) y `'.'` (vacío), genera una matriz de enteros `conteo[5][5]` donde cada celda vacía indique cuántas minas hay en sus hasta 8 celdas vecinas.  
    *Pista:* Para cada `(i, j)`, recorre `di = -1..1` y `dj = -1..1`, validando `ni >= 0 && ni < 5 && nj >= 0 && nj < 5` antes de leer `mapa[ni][nj]`.
14. **[Parcial] Reserva de vuelos (matriz `6x4` + estadísticas por fila/clase):** Simula un avión de `6` filas y `4` sillas por fila (`char avion[6][4]` inicializada en `'D'` disponible). Las filas `0..1` son Primera Clase (`$500`) y `2..5` Económica (`$200`). Permite reservar una silla `(f, c)`, cancelar reserva, mostrar el mapa y calcular el recaudo total actual.  
    *Pista:* Al calcular el recaudo, multiplica por `500` si `i <= 1` y por `200` si `i >= 2` cada vez que `avion[i][j] == 'O'`.

---

## 7. Solucionario Paso a Paso de los 14 Ejercicios

### Solución 1: Suma de dos matrices `A + B`
```cpp
const int MAX = 20;
int A[MAX][MAX], B[MAX][MAX], C[MAX][MAX], f, c;
do { cin >> f >> c; } while (f < 1 || f > MAX || c < 1 || c > MAX);
for (int i = 0; i < f; i++) for (int j = 0; j < c; j++) cin >> A[i][j];
for (int i = 0; i < f; i++) for (int j = 0; j < c; j++) cin >> B[i][j];
for (int i = 0; i < f; i++) {
    for (int j = 0; j < c; j++) {
        C[i][j] = A[i][j] + B[i][j];
        cout << C[i][j] << " ";
    }
    cout << "\n";
}
```
* *Prueba rápida:* `[[1,2],[3,4]] + [[5,6],[7,8]]` $\rightarrow$ `[[6,8],[10,12]]`.

### Solución 2: Conteo de pares, impares y ceros
```cpp
const int MAX = 15;
int m[MAX][MAX], f, c, ceros = 0, pares = 0, impares = 0;
do { cin >> f >> c; } while (f < 1 || f > MAX || c < 1 || c > MAX);
for (int i = 0; i < f; i++) {
    for (int j = 0; j < c; j++) {
        cin >> m[i][j];
        if (m[i][j] == 0) ceros++;
        else if (m[i][j] % 2 == 0) pares++;
        else impares++;
    }
}
cout << "Ceros: " << ceros << " | Pares: " << pares << " | Impares: " << impares << "\n";
```
* *Prueba rápida:* `[[0, 2], [-3, 4]]` $\rightarrow$ `Ceros: 1 | Pares: 2 | Impares: 1`.

### Solución 3: Matriz identidad `N x N`
```cpp
const int MAX = 15;
int id[MAX][MAX], n;
do { cin >> n; } while (n < 1 || n > MAX);
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        id[i][j] = (i == j) ? 1 : 0;
        cout << id[i][j] << " ";
    }
    cout << "\n";
}
```
* *Prueba rápida:* `n=3` $\rightarrow$ `1 0 0` / `0 1 0` / `0 0 1`.

### Solución 4: Suma del borde (marco)
```cpp
const int MAX = 20;
int m[MAX][MAX], f, c, sumaBorde = 0;
do { cin >> f >> c; } while (f < 1 || f > MAX || c < 1 || c > MAX);
for (int i = 0; i < f; i++) {
    for (int j = 0; j < c; j++) {
        cin >> m[i][j];
        if (i == 0 || i == f - 1 || j == 0 || j == c - 1) sumaBorde += m[i][j];
    }
}
cout << "Suma del borde: " << sumaBorde << "\n";
```
* *Prueba rápida:* `3x3` del `1` al `9`: suma todo excepto el centro (`5`) $\rightarrow$ `45 - 5 = 40`.

### Solución 5: Máximo por fila y mínimo por columna
```cpp
const int MAX = 15;
int m[MAX][MAX], maxFila[MAX], minCol[MAX], f, c;
do { cin >> f >> c; } while (f < 1 || f > MAX || c < 1 || c > MAX);
for (int i = 0; i < f; i++) for (int j = 0; j < c; j++) cin >> m[i][j];

for (int i = 0; i < f; i++) {
    maxFila[i] = m[i][0];
    for (int j = 1; j < c; j++) if (m[i][j] > maxFila[i]) maxFila[i] = m[i][j];
    cout << "Max fila " << i << ": " << maxFila[i] << "\n";
}
for (int j = 0; j < c; j++) {
    minCol[j] = m[0][j];
    for (int i = 1; i < f; i++) if (m[i][j] < minCol[j]) minCol[j] = m[i][j];
    cout << "Min col " << j << ": " << minCol[j] << "\n";
}
```
* *Prueba rápida:* `[[3,8],[5,2]]` $\rightarrow$ `maxFila=[8, 5]`, `minCol=[3, 2]`.

### Solución 6: Temperaturas semanales (`7x3`)
```cpp
double temp[7][3];
for (int i = 0; i < 7; i++) for (int j = 0; j < 3; j++) cin >> temp[i][j];

double maxProm = -1e9;
int diaMasCaluroso = 0;
for (int i = 0; i < 7; i++) {
    double s = temp[i][0] + temp[i][1] + temp[i][2];
    double prom = s / 3.0;
    if (prom > maxProm) { maxProm = prom; diaMasCaluroso = i; }
}
double minTemp = temp[0][0];
int jorFria = 0;
for (int i = 0; i < 7; i++) {
    for (int j = 0; j < 3; j++) {
        if (temp[i][j] < minTemp) { minTemp = temp[i][j]; jorFria = j; }
    }
}
cout << "Dia promedio mas alto (0..6): " << diaMasCaluroso
     << " | Jornada mas fria (0=M,1=T,2=N): " << jorFria << " (" << minTemp << ")\n";
```
* *Prueba rápida:* Si la columna `0` tiene `10.0` y las demás `>15.0`, reporta jornada `0` (`10.0`).

### Solución 7: Verificar matriz diagonal y triangular superior
```cpp
const int MAX = 12;
int m[MAX][MAX], n;
do { cin >> n; } while (n < 1 || n > MAX);
for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) cin >> m[i][j];

bool esDiagonal = true, esTriangSup = true;
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        if (i != j && m[i][j] != 0) esDiagonal = false;
        if (i > j && m[i][j] != 0) esTriangSup = false;
    }
}
cout << "Diagonal: " << (esDiagonal ? "SI" : "NO")
     << " | Triangular superior: " << (esTriangSup ? "SI" : "NO") << "\n";
```
* *Prueba rápida:* `[[2,5],[0,3]]` $\rightarrow$ `Diagonal: NO`, `Triangular superior: SI`.

### Solución 8: Ordenar cada fila de la matriz
```cpp
const int MAX = 20;
int m[MAX][MAX], f, c;
do { cin >> f >> c; } while (f < 1 || f > MAX || c < 1 || c > MAX);
for (int i = 0; i < f; i++) for (int j = 0; j < c; j++) cin >> m[i][j];

for (int i = 0; i < f; i++) {
    for (int p = 0; p < c - 1; p++) {
        for (int j = 0; j < c - 1 - p; j++) {
            if (m[i][j] > m[i][j + 1]) {
                int aux = m[i][j];
                m[i][j] = m[i][j + 1];
                m[i][j + 1] = aux;
            }
        }
    }
}
for (int i = 0; i < f; i++) {
    for (int j = 0; j < c; j++) cout << m[i][j] << " ";
    cout << "\n";
}
```
* *Prueba rápida:* `[[9,2,5],[8,1,4]]` $\rightarrow$ `[[2,5,9],[1,4,8]]`.

### Solución 9: Sumar ambas diagonales sin repetir el centro
```cpp
const int MAX = 15;
int m[MAX][MAX], n, suma = 0;
do { cin >> n; } while (n < 1 || n > MAX);
for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) cin >> m[i][j];

for (int i = 0; i < n; i++) {
    suma += m[i][i] + m[i][n - 1 - i];
}
if (n % 2 != 0) suma -= m[n / 2][n / 2];
cout << "Suma total de diagonales: " << suma << "\n";
```
* *Prueba rápida:* `3x3` del `1` al `9`: `(1+5+9) + (3+5+7) - 5 = 25`.

### Solución 10: Rotar matriz cuadrada `90°` horario
```cpp
const int MAX = 12;
int A[MAX][MAX], R[MAX][MAX], n;
do { cin >> n; } while (n < 1 || n > MAX);
for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) cin >> A[i][j];

for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        R[j][n - 1 - i] = A[i][j];
    }
}
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) cout << R[i][j] << " ";
    cout << "\n";
}
```
* *Prueba rápida:* `[[1,2],[3,4]]` $\rightarrow$ `[[3,1],[4,2]]`.

### Solución 11: Punto de silla (*Saddle Point*)
```cpp
const int MAX = 15;
int m[MAX][MAX], f, c;
do { cin >> f >> c; } while (f < 1 || f > MAX || c < 1 || c > MAX);
for (int i = 0; i < f; i++) for (int j = 0; j < c; j++) cin >> m[i][j];

bool haySilla = false;
for (int i = 0; i < f; i++) {
    int minF = m[i][0];
    for (int j = 1; j < c; j++) if (m[i][j] < minF) minF = m[i][j];

    for (int j = 0; j < c; j++) {
        if (m[i][j] == minF) {
            bool esMaxCol = true;
            for (int k = 0; k < f; k++) {
                if (m[k][j] > m[i][j]) { esMaxCol = false; break; }
            }
            if (esMaxCol) {
                cout << "Punto de silla en (" << i << ", " << j << ") = " << m[i][j] << "\n";
                haySilla = true;
            }
        }
    }
}
if (!haySilla) cout << "No existe punto de silla.\n";
```
* *Prueba rápida:* `[[1,2,3],[4,5,6],[7,8,9]]` $\rightarrow$ `(2,0) = 7` es el menor de la fila 2 y el mayor de la columna 0.

### Solución 12: Recorrido en espiral
```cpp
const int MAX = 15;
int m[MAX][MAX], f, c;
do { cin >> f >> c; } while (f < 1 || f > MAX || c < 1 || c > MAX);
for (int i = 0; i < f; i++) for (int j = 0; j < c; j++) cin >> m[i][j];

int top = 0, bottom = f - 1, left = 0, right = c - 1;
while (top <= bottom && left <= right) {
    for (int j = left; j <= right; j++) cout << m[top][j] << " ";
    top++;
    for (int i = top; i <= bottom; i++) cout << m[i][right] << " ";
    right--;
    if (top <= bottom) {
        for (int j = right; j >= left; j--) cout << m[bottom][j] << " ";
        bottom--;
    }
    if (left <= right) {
        for (int i = bottom; i >= top; i--) cout << m[i][left] << " ";
        left++;
    }
}
cout << "\n";
```
* *Prueba rápida:* `3x3` del `1` al `9` $\rightarrow$ `1 2 3 6 9 8 7 4 5`.

### Solución 13: Conteo de minas vecinas (`5x5`)
```cpp
char mapa[5][5];
int conteo[5][5] = {0};
for (int i = 0; i < 5; i++) for (int j = 0; j < 5; j++) cin >> mapa[i][j];

for (int i = 0; i < 5; i++) {
    for (int j = 0; j < 5; j++) {
        if (mapa[i][j] == '*') {
            conteo[i][j] = -1; // Marca de mina
        } else {
            int minas = 0;
            for (int di = -1; di <= 1; di++) {
                for (int dj = -1; dj <= 1; dj++) {
                    int ni = i + di, nj = j + dj;
                    if (ni >= 0 && ni < 5 && nj >= 0 && nj < 5 && mapa[ni][nj] == '*') {
                        minas++;
                    }
                }
            }
            conteo[i][j] = minas;
        }
    }
}
for (int i = 0; i < 5; i++) {
    for (int j = 0; j < 5; j++) {
        if (conteo[i][j] == -1) cout << "* ";
        else cout << conteo[i][j] << " ";
    }
    cout << "\n";
}
```
* *Prueba rápida:* Si `(0,0)` es `'*'`, las celdas vecinas `(0,1)`, `(1,0)` y `(1,1)` reciben `1`.

### Solución 14: Reserva de vuelos (`6x4`) con recaudo
```cpp
char avion[6][4];
for (int i = 0; i < 6; i++) for (int j = 0; j < 4; j++) avion[i][j] = 'D';

int op;
do {
    cout << "1.Reservar  2.Cancelar  3.Mapa y Recaudo  0.Salir: ";
    if (!(cin >> op)) break;
    if (op == 1 || op == 2) {
        int f, c;
        cin >> f >> c;
        if (f >= 0 && f < 6 && c >= 0 && c < 4) {
            if (op == 1 && avion[f][c] == 'D') { avion[f][c] = 'O'; cout << "Reservada.\n"; }
            else if (op == 2 && avion[f][c] == 'O') { avion[f][c] = 'D'; cout << "Cancelada.\n"; }
            else cout << "Operacion no valida para el estado actual.\n";
        }
    } else if (op == 3) {
        int recaudo = 0;
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 4; j++) {
                cout << avion[i][j] << " ";
                if (avion[i][j] == 'O') recaudo += (i <= 1 ? 500 : 200);
            }
            cout << "\n";
        }
        cout << "Recaudo total: $" << recaudo << "\n";
    }
} while (op != 0);
```
* *Prueba rápida:* Reservar `(0,1)` (Primera Clase `$500`) y `(4,2)` (Económica `$200`) $\rightarrow$ Recaudo `$700`.
