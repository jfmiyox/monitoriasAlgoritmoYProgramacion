# Módulo 06: Vectores Estáticos (Arreglos Unidimensionales)

> **Duración estimada:** 4.0 horas (2 sesiones de 2 horas)  
> **Ruta:** DFD $\rightarrow$ PSeInt $\rightarrow$ C++ Básico (Estático)  
> **Prerrequisitos:** M03 (Tipos de datos), M04 (Condicionales), M05 (Ciclos `for`, `while`, `do-while`)

---

## 1. Explicado Para Tontos: ¿Qué es un Vector Estático?

Imagina un **pasillo de la universidad con 100 casilleros metálicos atornillados a la pared**, numerados desde el **0 hasta el 99**.

* El **edificio** construyó exactamente **100 casilleros físicos** (`MAX = 100`). No puedes derribar la pared para agregar un casillero 101 ni encoger la pared para que queden solo 5 casilleros físicos. Esa capacidad física fija se llama **tamaño estático**.
* Hoy llegaron apenas **5 estudiantes** (`n = 5`) a guardar sus cuadernos. Usan los casilleros **0, 1, 2, 3 y 4**.
* ¿Qué pasa con los casilleros **5 al 99**? Siguen existiendo físicamente en la memoria RAM, pero **no los estás usando hoy** (tienen "basura" o ceros si los limpiaste al inicio).
* Todos los casilleros del mismo bloque guardan **cosas del mismo tipo** (si es un bloque para notas `double`, cada casillero guarda un `double`; si es para códigos `int`, cada casillero guarda un `int`).

En programación, un **vector estático** (también llamado *arreglo unidimensional*) es exactamente eso: **una fila contigua de casilleros del mismo tipo en memoria RAM, con una capacidad fija definida desde antes de ejecutar el programa, a los que accedes usando un número entero llamado índice.**

---

## 2. Regla de Oro del Curso: ¡Solo Espacio Definido!

En este curso trabajamos **exclusivamente con arreglos estáticos de espacio definido**. Hay dos formas válidas de declararlos en C++:

### Forma A: Tamaño fijo literal (cuando siempre son exactamente esos elementos)
```cpp
int notas[5];              // Exactamente 5 casilleros: indices 0, 1, 2, 3, 4
double temperaturas[7];    // 7 dias de la semana: indices 0..6
```

### Forma B: Capacidad máxima fija (`const int MAX`) + tamaño lógico `n` (la más usada en parciales)
```cpp
const int MAX = 100;       // Capacidad fisica maxima (constante)
int vec[MAX];              // Reserva 100 casilleros fijos en memoria
int n;                     // Tamano logico: cuantos casilleros usaremos hoy

do {
    cout << "Cuantos datos ingresara (1 a " << MAX << "): ";
    cin >> n;
} while (n < 1 || n > MAX);
```

> **⚠️ ¿Por qué NO hacemos `int v[n];` ni vectores dinámicos (`std::vector`, `new`) en este curso?**
> 1. **Estándar oficial de C++:** Escribir `int v[n];` cuando `n` es una variable se llama *VLA (Variable Length Array)*. **NO es parte del estándar ISO C++** (es una extensión tolerada por algunos compiladores como GCC, pero rechazada por Visual Studio / MSVC y con el flag `-Wvla`). En muchos parciales o jueces en línea te anulan el punto por usarlo.
> 2. **Peligro de colapso en memoria:** Si el usuario digita `n = -5` o `n = 100000000`, `int v[n];` intenta reservar memoria inválida o desborda la pila (*stack overflow*), haciendo que el programa explote sin aviso.
> 3. **Disciplina de memoria y validación:** Usar `const int MAX = 100;` + validar `1 <= n && n <= MAX` garantiza que el compilador conozca exactamente cuánta memoria necesita desde el primer instante y te obliga a programar con seguridad. Los arreglos dinámicos, punteros y `std::vector` los verás en cursos posteriores (Estructuras de Datos / POO).

---

## 3. Declaración, Inicialización y Trampas Clásicas

### 3.1 Inicialización en C++
```cpp
int a[5] = {10, 20, 30, 40, 50}; // Todos inicializados explicitamente
int b[5] = {10, 20};             // b[0]=10, b[1]=20, el resto (b[2..4]) queda en 0
int c[5] = {0};                  // Todos en 0 (muy util para contadores/acumuladores!)
int d[5] = {};                   // Todos en 0 en C++11 o superior
int e[]  = {4, 8, 15, 16};       // El compilador deduce tamano fijo 4 (sigue siendo estatico!)
```

> **🔥 OJO — Trampa Clásica #1: Índices `0 .. n-1` en C++ vs `1 .. n` en PSeInt**
> * En **C++**, el primer casillero **SIEMPRE** es el **0** y el último casillero usado es **`n - 1`**. Si tienes `n = 5` datos, los índices válidos son `0, 1, 2, 3, 4`.
> * En **PSeInt** (configuración por defecto), los índices van de **1 hasta `n`**: `1, 2, 3, 4, 5` (a menos que actives *"Utilizar índices en arreglos y cadenas en base 0"* en *Configurar $\rightarrow$ Opciones del Lenguaje*).
> * Además, en PSeInt `Dimension vec[100]` suele exigir un **número literal** dentro de los corchetes en el perfil estricto, por eso declaramos `Dimension vec[100];` y guardamos `MAX <- 100;` para las validaciones.

> **🚨 OJO — Trampa Clásica #2: El desbordamiento silencioso (`vec[n]` y `vec[-1]`)**
> Supón que tienes `int vec[5];` y escribes un ciclo mal hecho:
> ```cpp
> for (int i = 0; i <= 5; i++) {   // ERROR MORTAL: <= en lugar de <
>     cin >> vec[i];               // Cuando i == 5, escribe FUERA del arreglo!
> }
> ```
> C++ **NO te detiene ni te muestra un mensaje bonito de error** cuando accedes a `vec[5]` o `vec[-1]`. Simplemente sobrescribe otra variable vecina en tu memoria RAM o provoca un cierre inesperado (*Segmentation fault*).  
> **Regla de oro:** Si el tamaño lógico es `n`, la condición del `for` en C++ casi siempre es `i < n` (NUNCA `i <= n`), y siempre valida cualquier índice `pos` con `0 <= pos && pos < n`.

---

## 4. Lectura y Escritura con `for`

El compañero inseparable del vector estático es el ciclo **`for`** (`Para` en PSeInt), porque sabemos exactamente cuántas posiciones queremos recorrer (`n`).

| Operación | PSeInt (Base 1 por defecto) | C++ (Base 0 obligatorio) |
| :--- | :--- | :--- |
| Declarar capacidad 100 | `Dimension v[100];` | `const int MAX = 100; int v[MAX];` |
| Leer `n` elementos | `Para i <- 1 Hasta n Hacer`<br>&nbsp;&nbsp;`Leer v[i];`<br>`FinPara` | `for (int i = 0; i < n; i++) {`<br>&nbsp;&nbsp;`cin >> v[i];`<br>`}` |
| Mostrar `n` elementos | `Para i <- 1 Hasta n Hacer`<br>&nbsp;&nbsp;`Escribir v[i];`<br>`FinPara` | `for (int i = 0; i < n; i++) {`<br>&nbsp;&nbsp;`cout << v[i] << " ";`<br>`}` |

---

## 5. Los 8 Patrones Maestros Obligatorios

Casi todos los ejercicios de parcial sobre vectores estáticos se resuelven combinando estos **8 bloques fundamentales**:

### Patrón 1: Suma y Promedio
```cpp
double suma = 0.0;
for (int i = 0; i < n; i++) {
    suma += vec[i];
}
double promedio = suma / n; // Si vec es int, usa static_cast<double>(suma) / n
```
*Consejo de monitoría:* Si `suma` fuera `int` y `n` es `int`, `suma / n` hace división entera en C++ (`7 / 2 == 3`). Declara `suma` como `double` o usa `static_cast<double>(suma) / n`.

### Patrón 2: Contar con Condición
```cpp
int aprobados = 0;
for (int i = 0; i < n; i++) {
    if (notas[i] >= 3.0) {
        aprobados++;
    }
}
```

### Patrón 3: Mayor y Menor con su Posición
```cpp
int mayor = vec[0]; // NO inicializar en 0! Podrian ser todos negativos
int posMayor = 0;
for (int i = 1; i < n; i++) {
    if (vec[i] > mayor) {
        mayor = vec[i];
        posMayor = i;
    }
}
```
*¿Por qué NO `mayor = 0`?* Si el vector es `{-10, -4, -20}`, inicializar `mayor = 0` diría falsamente que el mayor es `0`, que ni siquiera está en el arreglo. Siempre arranca asumiendo que el primer elemento (`vec[0]`, índice `0`) es el campeón temporal.

### Patrón 4: Búsqueda Secuencial con Bandera
```cpp
bool encontrado = false;
int pos = -1;
for (int i = 0; i < n; i++) {
    if (vec[i] == buscado) {
        encontrado = true;
        pos = i;
        break; // Detiene el ciclo apenas lo halla
    }
}
```
*Consejo de parcial:* Nunca imprimas `"No encontrado"` **dentro** del `for` en un `else`, porque lo imprimiría por cada casillero distinto al buscado. Evalúa la bandera `encontrado` **después** de que termine el ciclo.

### Patrón 5: Invertir un Arreglo *In-Place* (sin otro arreglo)
Para invertir `{10, 20, 30, 40, 50}`, intercambias el primero con el último (`0` con `4`), el segundo con el penúltimo (`1` con `3`), y te detienes en la **mitad** (`i < n / 2`). Si siguieras hasta `n`, lo volverías a des-invertir.
```cpp
for (int i = 0; i < n / 2; i++) {
    int aux = vec[i];
    vec[i] = vec[n - 1 - i];
    vec[n - 1 - i] = aux;
}
```

### Patrón 6: Rotar a la Izquierda y a la Derecha
* **Rotar 1 paso a la izquierda** (`[A, B, C, D]` $\rightarrow$ `[B, C, D, A]`):
  1. Guardar `aux = vec[0]`.
  2. Correr de izquierda a derecha: `for (int i = 0; i < n - 1; i++) vec[i] = vec[i + 1];`
  3. Poner `vec[n - 1] = aux`.
* **Rotar 1 paso a la derecha** (`[A, B, C, D]` $\rightarrow$ `[D, A, B, C]`):
  1. Guardar `aux = vec[n - 1]`.
  2. Correr de derecha a izquierda: `for (int i = n - 1; i > 0; i--) vec[i] = vec[i - 1];`
  3. Poner `vec[0] = aux`.
* Si piden rotar `k` posiciones, primero calculas `pasos = k % n` (rotar `n` veces deja el arreglo igual) y repites el proceso `pasos` veces.

### Patrón 7: Insertar y Eliminar en Vector Estático de Capacidad `MAX`
* **Insertar `valor` en `pos` (`0 <= pos <= n`)**:
  1. Verificar que haya espacio (`n < MAX`).
  2. Abrir hueco desplazando **hacia la derecha** desde `n` hasta `pos + 1`:
     ```cpp
     for (int i = n; i > pos; i--) {
         vec[i] = vec[i - 1];
     }
     vec[pos] = valor;
     n++;
     ```
* **Eliminar el elemento en `pos` (`0 <= pos < n`)**:
  1. Verificar que no esté vacío (`n > 0`).
  2. Tapar el hueco desplazando **hacia la izquierda** desde `pos` hasta `n - 2`:
     ```cpp
     for (int i = pos; i < n - 1; i++) {
         vec[i] = vec[i + 1];
     }
     n--;
     ```

### Patrón 8: Ordenamiento Burbuja (*Bubble Sort*) con Prueba de Escritorio Visual
Consiste en hacer pasadas comparando parejas vecinas `vec[j]` y `vec[j + 1]`. Si están al revés (`vec[j] > vec[j + 1]`), se intercambian. En cada pasada, el número más grande "flota como una burbuja" hasta su posición definitiva al final.

```cpp
for (int pasada = 0; pasada < n - 1; pasada++) {
    bool huboCambio = false;
    for (int j = 0; j < n - 1 - pasada; j++) {
        if (vec[j] > vec[j + 1]) {
            int aux = vec[j];
            vec[j] = vec[j + 1];
            vec[j + 1] = aux;
            huboCambio = true;
        }
    }
    if (!huboCambio) break; // Ya quedo ordenado antes de tiempo
}
```

**Prueba de escritorio visual para `vec = [40, 10, 50, 20, 30]` (`n = 5`):**

| Pasada | Comparaciones `j` (`vec[j]` vs `vec[j+1]`) | Estado resultante tras pasada | Elemento fijo al final |
| :---: | :--- | :--- | :---: |
| **Inicio** | — | `[40, 10, 50, 20, 30]` | — |
| **1** | `(40,10)→swap`, `(40,50)→ok`, `(50,20)→swap`, `(50,30)→swap` | `[10, 40, 20, 30, 50]` | `50` fijo |
| **2** | `(10,40)→ok`, `(40,20)→swap`, `(40,30)→swap` | `[10, 20, 30, 40, 50]` | `40, 50` fijos |
| **3** | `(10,20)→ok`, `(20,30)→ok` (`huboCambio = false`) | `[10, 20, 30, 40, 50]` | ¡Termina por bandera! |

---

## 6. Ocho Problemas Resueltos Completos (EPS + PSeInt + C++ + Prueba de Escritorio)

---

### Problema 1: Registro y Estadísticas de Notas de un Grupo
**Enunciado:** Un docente desea registrar las notas (de `0.0` a `5.0`) de `n` estudiantes en un arreglo estático de capacidad máxima `MAX = 50`. Calcular e imprimir el promedio general, la mayor y la menor nota con el índice del estudiante que la obtuvo, y la cantidad de aprobados (`nota >= 3.0`).

#### Análisis EPS
* **Entradas:** Cantidad `n` (`1 <= n <= 50`), arreglo `notas[50]` con `n` valores reales en `[0.0, 5.0]`.
* **Proceso:** Validar `n` y cada nota. Acumular suma, contar `>= 3.0`, actualizar `mayor`/`posMayor` y `menor`/`posMenor` comparando desde `notas[0]`. Dividir `suma / n`.
* **Salidas:** `promedio`, `mayor` (`posMayor`), `menor` (`posMenor`), `aprobados`.

#### PSeInt (`pseint/m06_p01_notas_estadisticas.psc`)
```psc
Algoritmo NotasEstadisticas
    Definir MAX, n, i, aprobados, posMayor, posMenor Como Entero;
    Definir suma, promedio, mayor, menor Como Real;
    Dimension notas[50];
    MAX <- 50;

    Repetir
        Escribir "Ingrese cantidad de estudiantes (1 a ", MAX, "): ";
        Leer n;
    Hasta Que n >= 1 Y n <= MAX

    Para i <- 1 Hasta n Con Paso 1 Hacer
        Repetir
            Escribir "Nota del estudiante [", i, "] (0.0 a 5.0): ";
            Leer notas[i];
        Hasta Que notas[i] >= 0 Y notas[i] <= 5
    FinPara

    suma <- 0; aprobados <- 0;
    mayor <- notas[1]; menor <- notas[1];
    posMayor <- 1; posMenor <- 1;

    Para i <- 1 Hasta n Con Paso 1 Hacer
        suma <- suma + notas[i];
        Si notas[i] >= 3.0 Entonces aprobados <- aprobados + 1; FinSi
        Si notas[i] > mayor Entonces mayor <- notas[i]; posMayor <- i; FinSi
        Si notas[i] < menor Entonces menor <- notas[i]; posMenor <- i; FinSi
    FinPara

    promedio <- suma / n;
    Escribir "Promedio general: ", promedio;
    Escribir "Mayor nota: ", mayor, " (posicion ", posMayor, ")";
    Escribir "Menor nota: ", menor, " (posicion ", posMenor, ")";
    Escribir "Aprobados: ", aprobados, " de ", n;
FinAlgoritmo
```

#### C++ (`cpp/m06_p01_notas_estadisticas.cpp`)
```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const int MAX = 50;
    double notas[MAX];
    int n;

    do {
        cout << "Ingrese cantidad de estudiantes (1 a " << MAX << "): ";
        cin >> n;
    } while (n < 1 || n > MAX);

    for (int i = 0; i < n; i++) {
        do {
            cout << "Nota del estudiante [" << i << "] (0.0 a 5.0): ";
            cin >> notas[i];
        } while (notas[i] < 0.0 || notas[i] > 5.0);
    }

    double suma = 0.0;
    int aprobados = 0;
    double mayor = notas[0], menor = notas[0];
    int posMayor = 0, posMenor = 0;

    for (int i = 0; i < n; i++) {
        suma += notas[i];
        if (notas[i] >= 3.0) aprobados++;
        if (notas[i] > mayor) { mayor = notas[i]; posMayor = i; }
        if (notas[i] < menor) { menor = notas[i]; posMenor = i; }
    }

    cout << fixed << setprecision(2);
    cout << "Promedio general: " << (suma / n) << "\n";
    cout << "Mayor nota: " << mayor << " (indice " << posMayor << ")\n";
    cout << "Menor nota: " << menor << " (indice " << posMenor << ")\n";
    cout << "Aprobados (>= 3.0): " << aprobados << " de " << n << "\n";
    return 0;
}
```

#### Prueba de Escritorio (`n = 4`, `notas = {2.5, 4.8, 3.0, 1.9}`)
| `i` | `notas[i]` | `suma` | `aprobados` | `mayor` (`posMayor`) | `menor` (`posMenor`) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Init | — | `0.0` | `0` | `2.5 (0)` | `2.5 (0)` |
| `0` | `2.5` | `2.5` | `0` | `2.5 (0)` | `2.5 (0)` |
| `1` | `4.8` | `7.3` | `1` | `4.8 (1)` | `2.5 (0)` |
| `2` | `3.0` | `10.3` | `2` | `4.8 (1)` | `2.5 (0)` |
| `3` | `1.9` | `12.2` | `2` | `4.8 (1)` | `1.9 (3)` |

*Salida final:* Promedio `3.05`, Mayor `4.80 (indice 1)`, Menor `1.90 (indice 3)`, Aprobados `2 de 4`.

---

### Problema 2: Inventario de Papelería (Vectores Paralelos + Búsqueda Secuencial)
**Enunciado:** Una papelería almacena hasta `MAX = 40` productos en dos vectores paralelos: `codigos[MAX]` y `precios[MAX]`. Leer `n` productos y luego un `codigoBuscado`. Indicar con una bandera booleana si existe, mostrando su índice y precio.

#### Análisis EPS
* **Entradas:** `n`, `codigos[40]`, `precios[40]`, `codigoBuscado`.
* **Proceso:** Recorrer `0 .. n-1`. Si `codigos[i] == codigoBuscado`, marcar `encontrado = true`, guardar `pos = i` y salir con `break`.
* **Salidas:** Índice y precio si `encontrado == true`; mensaje de no existencia en caso contrario.

#### PSeInt (`pseint/m06_p02_busqueda_inventario.psc`)
```psc
Algoritmo BusquedaInventario
    Definir MAX, n, i, codigoBuscado, pos Como Entero;
    Definir encontrado Como Logico;
    Dimension codigos[40]; Dimension precios[40];
    MAX <- 40;

    Repetir
        Escribir "Cantidad de productos (1 a ", MAX, "): ";
        Leer n;
    Hasta Que n >= 1 Y n <= MAX

    Para i <- 1 Hasta n Con Paso 1 Hacer
        Escribir "Producto #", i, " - Codigo: "; Leer codigos[i];
        Escribir "Producto #", i, " - Precio: "; Leer precios[i];
    FinPara

    Escribir "Ingrese el codigo del producto a buscar: ";
    Leer codigoBuscado;

    encontrado <- Falso; pos <- -1; i <- 1;
    Mientras i <= n Y NO encontrado Hacer
        Si codigos[i] = codigoBuscado Entonces
            encontrado <- Verdadero; pos <- i;
        SiNo
            i <- i + 1;
        FinSi
    FinMientras

    Si encontrado Entonces
        Escribir "Producto ENCONTRADO en posicion ", pos, " | Precio: $", precios[pos];
    SiNo
        Escribir "El codigo ", codigoBuscado, " NO existe en el inventario.";
    FinSi
FinAlgoritmo
```

#### C++ (`cpp/m06_p02_busqueda_inventario.cpp`)
```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const int MAX = 40;
    int codigos[MAX];
    double precios[MAX];
    int n;

    do {
        cout << "Cantidad de productos a registrar (1 a " << MAX << "): ";
        cin >> n;
    } while (n < 1 || n > MAX);

    for (int i = 0; i < n; i++) {
        cout << "Producto #" << (i + 1) << " (indice " << i << ") - Codigo entero: ";
        cin >> codigos[i];
        cout << "Producto #" << (i + 1) << " (indice " << i << ") - Precio: ";
        cin >> precios[i];
    }

    int codigoBuscado;
    cout << "\nIngrese el codigo del producto a buscar: ";
    cin >> codigoBuscado;

    bool encontrado = false;
    int pos = -1;
    for (int i = 0; i < n; i++) {
        if (codigos[i] == codigoBuscado) {
            encontrado = true;
            pos = i;
            break;
        }
    }

    cout << fixed << setprecision(2);
    if (encontrado) {
        cout << "Producto ENCONTRADO en el indice " << pos
             << " | Precio: $" << precios[pos] << "\n";
    } else {
        cout << "El codigo " << codigoBuscado << " NO existe en el inventario.\n";
    }
    return 0;
}
```

#### Prueba de Escritorio (`n = 3`, `codigos = {101, 102, 103}`, `precios = {2500, 4200, 1800}`, `codigoBuscado = 102`)
| `i` | `codigos[i]` | `codigos[i] == 102` | `encontrado` | `pos` | Acción |
| :---: | :---: | :---: | :---: | :---: | :--- |
| Init | — | — | `false` | `-1` | Inicia búsqueda |
| `0` | `101` | `false` | `false` | `-1` | Continúa |
| `1` | `102` | `true` | `true` | `1` | `break` (termina ciclo) |

*Salida:* `Producto ENCONTRADO en el indice 1 | Precio: $4200.00`.

---

### Problema 3: Verificar Capicúa e Invertir Arreglo *In-Place*
**Enunciado:** Leer un vector estático `vec[50]` de `n` enteros. Primero verificar si el arreglo es capicúa (se lee igual de izquierda a derecha que de derecha a izquierda). Luego invertirlo sobre el mismo vector usando intercambios con `aux`.

#### Análisis EPS
* **Entradas:** `n`, `vec[50]`.
* **Proceso:** Comparar `vec[i]` con `vec[n - 1 - i]` para `i = 0 .. n/2 - 1`. Luego intercambiar esas mismas parejas sobre `vec`.
* **Salidas:** Mensaje indicando si es capicúa y el vector invertido.

#### PSeInt (`pseint/m06_p03_invertir_capicua.psc`) y C++ (`cpp/m06_p03_invertir_capicua.cpp`)
*(Código fuente completo en `pseint/m06_p03_invertir_capicua.psc` y `cpp/m06_p03_invertir_capicua.cpp`).*
```cpp
#include <iostream>
using namespace std;

int main() {
    const int MAX = 50;
    int vec[MAX];
    int n;

    do {
        cout << "Cantidad de elementos (1 a " << MAX << "): ";
        cin >> n;
    } while (n < 1 || n > MAX);

    for (int i = 0; i < n; i++) {
        cout << "vec[" << i << "] = ";
        cin >> vec[i];
    }

    bool esCapicua = true;
    for (int i = 0; i < n / 2; i++) {
        if (vec[i] != vec[n - 1 - i]) {
            esCapicua = false;
            break;
        }
    }

    cout << (esCapicua ? "El arreglo ES capicua.\n" : "El arreglo NO es capicua.\n");

    for (int i = 0; i < n / 2; i++) {
        int aux = vec[i];
        vec[i] = vec[n - 1 - i];
        vec[n - 1 - i] = aux;
    }

    cout << "Arreglo invertido: [ ";
    for (int i = 0; i < n; i++) cout << vec[i] << " ";
    cout << "]\n";
    return 0;
}
```

#### Prueba de Escritorio (`n = 5`, `vec = {10, 20, 30, 20, 10}`)
* `n / 2` es `2` (`i = 0` y `i = 1`).
* `i = 0`: compara `vec[0]` (`10`) con `vec[4]` (`10`) $\rightarrow$ iguales.
* `i = 1`: compara `vec[1]` (`20`) con `vec[3]` (`20`) $\rightarrow$ iguales.
* `esCapicua = true`. Al invertir intercambia `(0,4)` y `(1,3)`, dejando `[10, 20, 30, 20, 10]`.
* Con `vec = {1, 2, 3, 4}` (`n = 4`): `i = 0` compara `1 != 4` $\rightarrow$ `esCapicua = false`; al invertir: `(0,3)` $\rightarrow$ `[4, 2, 3, 1]`, `(1,2)` $\rightarrow$ `[4, 3, 2, 1]`.

---

### Problema 4: Rotación Circular de Turnos (`k` Posiciones)
**Enunciado:** Dado un arreglo de `n` turnos (`MAX = 30`), rotarlo `k` posiciones a la izquierda (`1`) o a la derecha (`2`) según indique el usuario. Optimizar usando `pasos = k % n`.

#### Análisis EPS
* **Entradas:** `n`, `turnos[30]`, `direccion` (`1` ó `2`), `k >= 0`.
* **Proceso:** Calcular `pasos = k % n`. Repetir `pasos` veces la rotación de 1 posición en la dirección elegida.
* **Salidas:** Vector antes y después de la rotación.

#### C++ (`cpp/m06_p04_rotar_turnos.cpp`) — *(PSeInt equivalente en `pseint/m06_p04_rotar_turnos.psc`)*
```cpp
#include <iostream>
using namespace std;

int main() {
    const int MAX = 30;
    int turnos[MAX];
    int n;

    do {
        cout << "Cantidad de turnos (1 a " << MAX << "): ";
        cin >> n;
    } while (n < 1 || n > MAX);

    for (int i = 0; i < n; i++) cin >> turnos[i];

    int direccion, k;
    do { cout << "1=Izquierda, 2=Derecha: "; cin >> direccion; } while (direccion != 1 && direccion != 2);
    do { cout << "Posiciones k (>= 0): "; cin >> k; } while (k < 0);

    int pasos = k % n;
    if (direccion == 1) {
        for (int p = 0; p < pasos; p++) {
            int primero = turnos[0];
            for (int i = 0; i < n - 1; i++) turnos[i] = turnos[i + 1];
            turnos[n - 1] = primero;
        }
    } else {
        for (int p = 0; p < pasos; p++) {
            int ultimo = turnos[n - 1];
            for (int i = n - 1; i > 0; i--) turnos[i] = turnos[i - 1];
            turnos[0] = ultimo;
        }
    }

    cout << "Despues: [ ";
    for (int i = 0; i < n; i++) cout << turnos[i] << " ";
    cout << "]\n";
    return 0;
}
```

#### Prueba de Escritorio (`turnos = {1, 2, 3, 4, 5}`, `direccion = 2` (Derecha), `k = 7`)
* `pasos = 7 % 5 = 2` (rotar 7 veces en 5 elementos equivale a rotar 2 veces).
* Paso `p = 0`: `ultimo = 5`, desplaza `{1,2,3,4}` a `1..4`, pone `5` en `0` $\rightarrow$ `[5, 1, 2, 3, 4]`.
* Paso `p = 1`: `ultimo = 4`, desplaza `{5,1,2,3}` a `1..4`, pone `4` en `0` $\rightarrow$ `[4, 5, 1, 2, 3]`.

---

### Problema 5: Gestor de Lista Estática (Insertar y Eliminar con `MAX = 10`)
**Enunciado:** Administrar una lista de códigos en un arreglo estático con capacidad `MAX = 10` y tamaño lógico `n`. Ofrecer un menú para: (1) Mostrar lista y ocupación, (2) Insertar un valor en índice `pos`, (3) Eliminar el elemento en `pos`, (0) Salir.

#### Análisis EPS
* **Entradas:** `n` inicial (`0..10`), elementos iniciales, `opcion`, y según el caso `pos` y `valor`.
* **Proceso:** Para insertar validar `n < MAX` y `0 <= pos <= n`, desplazar hacia la derecha e incrementar `n`. Para eliminar validar `n > 0` y `0 <= pos < n`, desplazar hacia la izquierda y decrementar `n`.
* **Salidas:** Mensajes de confirmación/error y estado de la lista.

#### C++ (`cpp/m06_p05_insertar_eliminar.cpp`) — *(PSeInt en `pseint/m06_p05_insertar_eliminar.psc`)*
```cpp
#include <iostream>
using namespace std;

int main() {
    const int MAX = 10;
    int lista[MAX] = {0};
    int n;

    do {
        cout << "Cantidad inicial (0 a " << MAX << "): ";
        cin >> n;
    } while (n < 0 || n > MAX);

    for (int i = 0; i < n; i++) cin >> lista[i];

    int opcion;
    do {
        cout << "\n1.Mostrar  2.Insertar  3.Eliminar  0.Salir (" << n << "/" << MAX << "): ";
        if (!(cin >> opcion)) break;

        if (opcion == 1) {
            for (int i = 0; i < n; i++) cout << lista[i] << " ";
            cout << "\n";
        } else if (opcion == 2) {
            if (n == MAX) {
                cout << "Arreglo lleno (MAX=" << MAX << ").\n";
            } else {
                int pos, valor;
                cin >> pos >> valor;
                if (pos >= 0 && pos <= n) {
                    for (int i = n; i > pos; i--) lista[i] = lista[i - 1];
                    lista[pos] = valor;
                    n++;
                }
            }
        } else if (opcion == 3) {
            if (n > 0) {
                int pos;
                cin >> pos;
                if (pos >= 0 && pos < n) {
                    for (int i = pos; i < n - 1; i++) lista[i] = lista[i + 1];
                    n--;
                }
            }
        }
    } while (opcion != 0);
    return 0;
}
```

#### Prueba de Escritorio (`lista = [10, 20, 30]`, `n = 3`)
1. Insertar `99` en `pos = 1`: `i=3: lista[3]=30`, `i=2: lista[2]=20`, `lista[1]=99`, `n=4` $\rightarrow$ `[10, 99, 20, 30]`.
2. Eliminar `pos = 2`: `i=2: lista[2]=lista[3]` (`30`), `n=3` $\rightarrow$ `[10, 99, 30]`. *(En `lista[3]` queda `30` como basura inactiva fuera de `0..n-1`).*

---

### Problema 6: Ordenamiento Burbuja Paso a Paso
**Enunciado:** Leer `n` puntajes (`MAX = 30`), ordenarlos ascendentemente mediante Ordenamiento Burbuja optimizado con bandera `huboCambio`, e imprimir el estado del vector al terminar cada pasada.

#### Análisis EPS
* **Entradas:** `n`, `puntajes[30]`.
* **Proceso:** Bucle externo `pasada` (`0 .. n-2`), bucle interno `j` (`0 .. n-2-pasada`) intercambiando adyacentes desordenados y activando `huboCambio`.
* **Salidas:** Vector en cada pasada y resultado ordenado final.

*(Archivos completos: `pseint/m06_p06_burbuja_paso_a_paso.psc` y `cpp/m06_p06_burbuja_paso_a_paso.cpp`. Ver la tabla de prueba de escritorio en la sección del Patrón 8).*

---

### Problema 7: Eliminar Duplicados y Contar Frecuencias
**Enunciado:** Dado un vector estático `datos[50]` con `n` enteros, construir dos vectores paralelos `unicos[50]` y `conteo[50]` de tamaño lógico `m` que guarden cada valor distinto (en orden de aparición) y cuántas veces se repitió.

#### Análisis EPS
* **Entradas:** `n`, `datos[50]`.
* **Proceso:** Inicializar `m = 0`. Para cada `datos[i]`, buscarlo en `unicos[0..m-1]`. Si está en `posEncontrado`, incrementar `conteo[posEncontrado]`. Si no está, agregarlo en `unicos[m]`, poner `conteo[m] = 1` y hacer `m++`.
* **Salidas:** Pares `(unicos[j], conteo[j])` para `j = 0..m-1`.

#### C++ (`cpp/m06_p07_filtrar_sin_duplicados.cpp`) — *(PSeInt en `pseint/m06_p07_filtrar_sin_duplicados.psc`)*
```cpp
#include <iostream>
using namespace std;

int main() {
    const int MAX = 50;
    int datos[MAX], unicos[MAX], conteo[MAX] = {0};
    int n, m = 0;

    do { cin >> n; } while (n < 1 || n > MAX);
    for (int i = 0; i < n; i++) cin >> datos[i];

    for (int i = 0; i < n; i++) {
        int posEncontrado = -1;
        for (int j = 0; j < m; j++) {
            if (unicos[j] == datos[i]) {
                posEncontrado = j;
                break;
            }
        }
        if (posEncontrado != -1) {
            conteo[posEncontrado]++;
        } else {
            unicos[m] = datos[i];
            conteo[m] = 1;
            m++;
        }
    }

    for (int j = 0; j < m; j++) {
        cout << "Valor " << unicos[j] << " aparece " << conteo[j] << " vez/veces.\n";
    }
    return 0;
}
```

#### Prueba de Escritorio (`datos = {7, 3, 7, 9, 3, 7}`)
| `i` | `datos[i]` | ¿En `unicos`? | `unicos[0..m-1]` | `conteo[0..m-1]` | `m` |
| :---: | :---: | :---: | :--- | :--- | :---: |
| `0` | `7` | No (`-1`) | `[7]` | `[1]` | `1` |
| `1` | `3` | No (`-1`) | `[7, 3]` | `[1, 1]` | `2` |
| `2` | `7` | Sí (`0`) | `[7, 3]` | `[2, 1]` | `2` |
| `3` | `9` | No (`-1`) | `[7, 3, 9]` | `[2, 1, 1]` | `3` |
| `4` | `3` | Sí (`1`) | `[7, 3, 9]` | `[2, 2, 1]` | `3` |
| `5` | `7` | Sí (`0`) | `[7, 3, 9]` | `[3, 2, 1]` | `3` |

---

### Problema 8: Fusión (*Merge*) de Dos Vectores Estáticos Ordenados
**Enunciado:** Dados dos vectores ordenados ascendentemente `A[30]` (`nA` datos) y `B[30]` (`nB` datos), fusionarlos en un tercer arreglo estático `C[60]` de tamaño `nA + nB` en orden ascendente sin usar Burbuja.

#### Análisis EPS
* **Entradas:** `nA`, `A[30]`, `nB`, `B[30]`.
* **Proceso:** Usar tres índices `i = 0` (para `A`), `j = 0` (para `B`) y `k = 0` (para `C`). Mientras ambos tengan elementos, copiar el menor a `C[k]`. Al agotarse uno, copiar todo lo que quede del otro.
* **Salidas:** Vector `C[0 .. nA + nB - 1]`.

#### C++ (`cpp/m06_p08_mezcla_dos_arreglos.cpp`) — *(PSeInt en `pseint/m06_p08_mezcla_dos_arreglos.psc`)*
```cpp
#include <iostream>
using namespace std;

int main() {
    const int MAX = 30;
    int A[MAX], B[MAX], C[2 * MAX];
    int nA, nB;

    do { cin >> nA; } while (nA < 1 || nA > MAX);
    for (int i = 0; i < nA; i++) cin >> A[i];

    do { cin >> nB; } while (nB < 1 || nB > MAX);
    for (int i = 0; i < nB; i++) cin >> B[i];

    int i = 0, j = 0, k = 0;
    while (i < nA && j < nB) {
        if (A[i] <= B[j]) { C[k++] = A[i++]; }
        else { C[k++] = B[j++]; }
    }
    while (i < nA) C[k++] = A[i++];
    while (j < nB) C[k++] = B[j++];

    for (int idx = 0; idx < k; idx++) cout << C[idx] << " ";
    cout << "\n";
    return 0;
}
```

#### Prueba de Escritorio (`A = {2, 5, 9}`, `B = {1, 3, 5, 12}`)
* Compara `2 vs 1` $\rightarrow$ `C[0]=1`; `2 vs 3` $\rightarrow$ `C[1]=2`; `5 vs 3` $\rightarrow$ `C[2]=3`; `5 vs 5` $\rightarrow$ `C[3]=5`; `9 vs 5` $\rightarrow$ `C[4]=5`; `9 vs 12` $\rightarrow$ `C[5]=9` (`A` termina); sobra `12` en `B` $\rightarrow$ `C[6]=12`.
* Resultado: `[1, 2, 3, 5, 5, 9, 12]`.

---

## 7. Catorce Ejercicios Propuestos (con Pistas)

> **Regla:** Usa exclusivamente vectores estáticos (`const int MAX = ...; tipo v[MAX];` o tamaño fijo literal) y valida `1 <= n <= MAX`. ¡Nada de `std::vector`, `new` ni `int v[n]`!

1. **[Básico] Suma de pares e impares:** Lee `n` enteros (`MAX = 50`). Calcula por separado la suma de los números pares y la suma de los números impares (cuidado: paridad del **valor** `v[i] % 2 == 0`, no del índice).  
   *Pista:* Usa `v[i] % 2 == 0`, no `i % 2 == 0`.
2. **[Básico] Desviación respecto al promedio:** Lee `n` estaturas (`MAX = 40`). Calcula el promedio y luego muestra cuántas estaturas están por encima del promedio y cuántas por debajo.  
   *Pista:* Necesitas dos ciclos `for` separados: primero hallar el promedio, luego comparar cada `v[i]` contra ese promedio.
3. **[Básico] Producto escalar de dos vectores:** Lee `n` (`MAX = 25`) y dos vectores `A[MAX]` y `B[MAX]`. Calcula $\sum_{i=0}^{n-1} A[i] \cdot B[i]$.  
   *Pista:* Usa un único ciclo `for` acumulando `producto += A[i] * B[i]`.
4. **[Básico] Segundo mayor (sin ordenar):** Dado un arreglo de `n` enteros (`2 <= n <= 50`), encuentra el mayor y el segundo mayor distinto (o indica si todos son iguales).  
   *Pista:* Halla primero `mayor` y luego busca el máximo entre los elementos `< mayor` usando una bandera `haySegundo`.
5. **[Intermedio] Separar positivos, negativos y ceros:** Lee `n` enteros (`MAX = 60`). Guárdalos clasificados en dos vectores estáticos `pos[MAX]` (con `nPos`) y `neg[MAX]` (con `nNeg`), contando aparte cuántos ceros hubo.  
   *Pista:* Cada vector destino lleva su propio contador/índice lógico (`nPos`, `nNeg`) que inicia en `0`.
6. **[Intermedio] Suma de vectores invertidos:** Dados dos vectores `A` y `B` de tamaño `n` (`MAX = 30`), genera `C[MAX]` tal que `C[i] = A[i] + B[n - 1 - i]`.  
   *Pista:* Cuando `i` avanza desde `0`, `n - 1 - i` retrocede desde el final.
7. **[Intermedio] Eliminar todas las ocurrencias de `x`:** Dado `v[MAX]` (`n` elementos) y un entero `x`, elimina todas las apariciones de `x` preservando el orden relativo de los demás.  
   *Pista:* En lugar de desplazar en cada borrado, puedes usar un índice de escritura `j = 0`: si `v[i] != x`, copias `v[j++] = v[i]`, y al final `n = j`.
8. **[Intermedio] Insertar manteniendo el orden:** Dado un vector estático `v[50]` con `n` elementos (`n < 50`) **ya ordenado ascendentemente**, lee un nuevo entero `x` e insértalo en la posición exacta para que `v` siga ordenado.  
   *Pista:* Desplaza hacia la derecha desde `i = n - 1` mientras `i >= 0 && v[i] > x`: `v[i + 1] = v[i]`. Al salir, coloca `v[i + 1] = x` e incrementa `n`.
9. **[Intermedio] Búsqueda binaria en vector ordenado:** Dado un vector ordenado ascendentemente (`MAX = 100`), busca `x` dividiendo el intervalo a la mitad (`izq = 0`, `der = n - 1`, `medio = (izq + der) / 2`).  
   *Pista:* Si `v[medio] < x` haces `izq = medio + 1`; si `v[medio] > x` haces `der = medio - 1`.
10. **[Intermedio] Ordenamiento por Selección (*Selection Sort*):** Ordena un vector de `n` reales (`MAX = 40`) buscando en cada posición `i` el índice del menor elemento entre `i .. n-1` e intercambiándolo con `v[i]`.  
    *Pista:* Solo haces UN intercambio por cada iteración externa de `i`, no en cada comparación.
11. **[Reto] Histograma de calificaciones (0 a 5):** Lee `n` notas enteras entre `0` y `5` (`MAX = 100`) y usa un vector de frecuencias `freq[6] = {0}` donde cada índice representa la nota (`0..5`). Imprime barras con `*`.  
    *Pista:* Haz `freq[nota]++` directamente sin usar 6 `if` distintos.
12. **[Reto] Subarreglo consecutivo creciente más largo:** Dado `v[50]` de `n` enteros, encuentra la longitud máxima y la posición de inicio de una racha estrictamente creciente (`v[i] > v[i-1]`).  
    *Pista:* Mantén `rachaActual` y `mejorRacha` (ambas inician en `1`), junto con `inicioActual` y `mejorInicio`.
13. **[Reto] Unión e intersección de dos conjuntos (vectores sin repetidos):** Dados `A[30]` (`nA` elementos) y `B[30]` (`nB` elementos) sin duplicados internos, construye `I[30]` (intersección) y `U[60]` (unión sin repetidos).  
    *Pista:* Para intersección, busca cada `A[i]` en `B`. Para unión, copia todo `A` en `U` y luego agrega solo los `B[j]` que no estén en `A`.
14. **[Parcial] Polinomio evaluado y derivado:** Representa un polinomio $P(x) = c_0 + c_1 x + \dots + c_g x^g$ en un vector estático `coef[21]` (grado `g <= 20`). Lee `g` y los `g + 1` coeficientes, evalúa $P(x_0)$ para un `x0` dado y muestra los coeficientes de su derivada $P'(x)$.  
    *Pista:* En la derivada, `deriv[i - 1] = i * coef[i]` para `i = 1 .. g`.

---

## 8. Solucionario Paso a Paso de los 14 Ejercicios

> **Nota:** Todas las soluciones usan arreglos estáticos con capacidad fija (`MAX`), compilables en `g++ -std=c++17 -Wall -Wextra -Werror`.

### Solución 1: Suma de pares e impares
* **EPS:** Entradas `n`, `v[50]`. Salidas `sumaPares`, `sumaImpares`.
```cpp
const int MAX = 50;
int v[MAX], n, sumaPares = 0, sumaImpares = 0;
do { cin >> n; } while (n < 1 || n > MAX);
for (int i = 0; i < n; i++) {
    cin >> v[i];
    if (v[i] % 2 == 0) sumaPares += v[i];
    else sumaImpares += v[i];
}
cout << "Suma pares: " << sumaPares << " | Suma impares: " << sumaImpares << "\n";
```
* *Prueba rápida:* `v = {4, 7, -2, 3}` $\rightarrow$ `sumaPares = 4 + (-2) = 2`, `sumaImpares = 7 + 3 = 10`.

### Solución 2: Desviación respecto al promedio
* **EPS:** Entradas `n`, `est[40]`. Salidas `prom`, `arriba`, `abajo`.
```cpp
const int MAX = 40;
double est[MAX], suma = 0.0;
int n, arriba = 0, abajo = 0;
do { cin >> n; } while (n < 1 || n > MAX);
for (int i = 0; i < n; i++) { cin >> est[i]; suma += est[i]; }
double prom = suma / n;
for (int i = 0; i < n; i++) {
    if (est[i] > prom) arriba++;
    else if (est[i] < prom) abajo++;
}
cout << "Promedio: " << prom << " | Encima: " << arriba << " | Debajo: " << abajo << "\n";
```
* *Prueba rápida:* `{1.60, 1.70, 1.80}` $\rightarrow$ `prom = 1.70`, `arriba = 1`, `abajo = 1`.

### Solución 3: Producto escalar
```cpp
const int MAX = 25;
double A[MAX], B[MAX], prod = 0.0;
int n;
do { cin >> n; } while (n < 1 || n > MAX);
for (int i = 0; i < n; i++) cin >> A[i];
for (int i = 0; i < n; i++) { cin >> B[i]; prod += A[i] * B[i]; }
cout << "Producto escalar: " << prod << "\n";
```
* *Prueba rápida:* `A={1,2,3}`, `B={4,5,6}` $\rightarrow$ `1*4 + 2*5 + 3*6 = 32`.

### Solución 4: Segundo mayor (sin ordenar)
```cpp
const int MAX = 50;
int v[MAX], n;
do { cin >> n; } while (n < 2 || n > MAX);
for (int i = 0; i < n; i++) cin >> v[i];

int mayor = v[0];
for (int i = 1; i < n; i++) {
    if (v[i] > mayor) mayor = v[i];
}
bool haySegundo = false;
int segundo = 0;
for (int i = 0; i < n; i++) {
    if (v[i] < mayor && (!haySegundo || v[i] > segundo)) {
        segundo = v[i];
        haySegundo = true;
    }
}
if (haySegundo) cout << "Mayor: " << mayor << " | Segundo mayor: " << segundo << "\n";
else cout << "Todos los elementos son iguales a " << mayor << "\n";
```
* *Prueba rápida:* `{9, 9, 4, 7}` $\rightarrow$ `mayor = 9`, `segundo = 7`. `{5, 5, 5}` $\rightarrow$ `haySegundo = false`.

### Solución 5: Separar positivos, negativos y ceros
```cpp
const int MAX = 60;
int v[MAX], pos[MAX], neg[MAX];
int n, nPos = 0, nNeg = 0, ceros = 0;
do { cin >> n; } while (n < 1 || n > MAX);
for (int i = 0; i < n; i++) {
    cin >> v[i];
    if (v[i] > 0) pos[nPos++] = v[i];
    else if (v[i] < 0) neg[nNeg++] = v[i];
    else ceros++;
}
cout << "Positivos (" << nPos << "): ";
for (int i = 0; i < nPos; i++) cout << pos[i] << " ";
cout << "\nNegativos (" << nNeg << "): ";
for (int i = 0; i < nNeg; i++) cout << neg[i] << " ";
cout << "\nCeros: " << ceros << "\n";
```
* *Prueba rápida:* `{5, 0, -3, 8, -1}` $\rightarrow$ `pos=[5,8]` (`nPos=2`), `neg=[-3,-1]` (`nNeg=2`), `ceros=1`.

### Solución 6: Suma de vectores invertidos
```cpp
const int MAX = 30;
int A[MAX], B[MAX], C[MAX], n;
do { cin >> n; } while (n < 1 || n > MAX);
for (int i = 0; i < n; i++) cin >> A[i];
for (int i = 0; i < n; i++) cin >> B[i];
for (int i = 0; i < n; i++) {
    C[i] = A[i] + B[n - 1 - i];
    cout << C[i] << " ";
}
cout << "\n";
```
* *Prueba rápida:* `A={1,2,3}`, `B={10,20,30}` $\rightarrow$ `C[0]=1+30=31`, `C[1]=2+20=22`, `C[2]=3+10=13`.

### Solución 7: Eliminar todas las ocurrencias de `x`
```cpp
const int MAX = 50;
int v[MAX], n, x;
do { cin >> n; } while (n < 1 || n > MAX);
for (int i = 0; i < n; i++) cin >> v[i];
cin >> x;

int j = 0; // Indice de escritura compacto
for (int i = 0; i < n; i++) {
    if (v[i] != x) {
        v[j] = v[i];
        j++;
    }
}
n = j; // Nuevo tamano logico
for (int i = 0; i < n; i++) cout << v[i] << " ";
cout << "\n";
```
* *Prueba rápida:* `v={2, 5, 2, 8, 2}`, `x=2` $\rightarrow$ copia `5` a `v[0]`, `8` a `v[1]` $\rightarrow$ `n=2`, `v={5, 8}`.

### Solución 8: Insertar manteniendo el orden
```cpp
const int MAX = 50;
int v[MAX], n, x;
do { cin >> n; } while (n < 0 || n >= MAX); // Debe quedar al menos 1 espacio!
for (int i = 0; i < n; i++) cin >> v[i];
cin >> x;

int i = n - 1;
while (i >= 0 && v[i] > x) {
    v[i + 1] = v[i];
    i--;
}
v[i + 1] = x;
n++;
for (int k = 0; k < n; k++) cout << v[k] << " ";
cout << "\n";
```
* *Prueba rápida:* `v={10, 20, 40}`, `x=25` $\rightarrow$ mueve `40` a `v[3]`, para en `i=1` (`20 <= 25`), inserta `25` en `v[2]` $\rightarrow$ `{10, 20, 25, 40}`.

### Solución 9: Búsqueda binaria en vector ordenado
```cpp
const int MAX = 100;
int v[MAX], n, x;
do { cin >> n; } while (n < 1 || n > MAX);
for (int i = 0; i < n; i++) cin >> v[i];
cin >> x;

int izq = 0, der = n - 1, pos = -1;
while (izq <= der) {
    int medio = izq + (der - izq) / 2;
    if (v[medio] == x) { pos = medio; break; }
    else if (v[medio] < x) izq = medio + 1;
    else der = medio - 1;
}
if (pos != -1) cout << "Encontrado en indice " << pos << "\n";
else cout << "No encontrado\n";
```
* *Prueba rápida:* `v={3, 7, 11, 15, 20}`, `x=15` $\rightarrow$ `medio=2` (`11<15`) $\rightarrow$ `izq=3, der=4, medio=3` (`v[3]==15`) $\rightarrow$ `pos=3`.

### Solución 10: Ordenamiento por Selección (*Selection Sort*)
```cpp
const int MAX = 40;
double v[MAX];
int n;
do { cin >> n; } while (n < 1 || n > MAX);
for (int i = 0; i < n; i++) cin >> v[i];

for (int i = 0; i < n - 1; i++) {
    int idxMin = i;
    for (int j = i + 1; j < n; j++) {
        if (v[j] < v[idxMin]) idxMin = j;
    }
    if (idxMin != i) {
        double aux = v[i];
        v[i] = v[idxMin];
        v[idxMin] = aux;
    }
}
for (int i = 0; i < n; i++) cout << v[i] << " ";
cout << "\n";
```
* *Prueba rápida:* `{30, 10, 20}`: `i=0` halla `idxMin=1` (`10`) $\rightarrow$ `{10, 30, 20}`; `i=1` halla `idxMin=2` (`20`) $\rightarrow$ `{10, 20, 30}`.

### Solución 11: Histograma de calificaciones (0 a 5)
```cpp
const int MAX = 100;
int notas[MAX], freq[6] = {0}, n;
do { cin >> n; } while (n < 1 || n > MAX);
for (int i = 0; i < n; i++) {
    do { cin >> notas[i]; } while (notas[i] < 0 || notas[i] > 5);
    freq[notas[i]]++;
}
for (int k = 0; k <= 5; k++) {
    cout << k << " (" << freq[k] << "): ";
    for (int c = 0; c < freq[k]; c++) cout << "*";
    cout << "\n";
}
```
* *Prueba rápida:* `{5, 3, 5, 0, 3}` $\rightarrow$ `0(1):*`, `3(2):**`, `5(2):**`.

### Solución 12: Subarreglo consecutivo creciente más largo
```cpp
const int MAX = 50;
int v[MAX], n;
do { cin >> n; } while (n < 1 || n > MAX);
for (int i = 0; i < n; i++) cin >> v[i];

int racha = 1, mejorRacha = 1, iniActual = 0, mejorIni = 0;
for (int i = 1; i < n; i++) {
    if (v[i] > v[i - 1]) {
        racha++;
        if (racha > mejorRacha) {
            mejorRacha = racha;
            mejorIni = iniActual;
        }
    } else {
        racha = 1;
        iniActual = i;
    }
}
cout << "Longitud maxima: " << mejorRacha << " desde indice " << mejorIni << "\n";
```
* *Prueba rápida:* `{5, 1, 2, 4, 3, 6}` $\rightarrow$ racha `{1, 2, 4}` longitud `3` desde índice `1`.

### Solución 13: Unión e intersección de dos conjuntos
```cpp
const int MAX = 30;
int A[MAX], B[MAX], I[MAX], U[2 * MAX];
int nA, nB, nI = 0, nU = 0;
do { cin >> nA; } while (nA < 1 || nA > MAX);
for (int i = 0; i < nA; i++) { cin >> A[i]; U[nU++] = A[i]; }
do { cin >> nB; } while (nB < 1 || nB > MAX);
for (int j = 0; j < nB; j++) cin >> B[j];

for (int j = 0; j < nB; j++) {
    bool estaEnA = false;
    for (int i = 0; i < nA; i++) {
        if (B[j] == A[i]) { estaEnA = true; break; }
    }
    if (estaEnA) I[nI++] = B[j];
    else U[nU++] = B[j];
}
cout << "Interseccion: "; for (int k = 0; k < nI; k++) cout << I[k] << " ";
cout << "\nUnion: "; for (int k = 0; k < nU; k++) cout << U[k] << " ";
cout << "\n";
```
* *Prueba rápida:* `A={1,2,3}`, `B={2,3,4}` $\rightarrow$ `I={2,3}`, `U={1,2,3,4}`.

### Solución 14: Evaluación y derivada de un polinomio
```cpp
const int MAX_COEF = 21; // Grado maximo 20 => 21 coeficientes
double coef[MAX_COEF], deriv[MAX_COEF] = {0.0};
int g;
do { cin >> g; } while (g < 0 || g > 20);
for (int i = 0; i <= g; i++) cin >> coef[i];

double x0;
cin >> x0;
double eval = 0.0, potencia = 1.0;
for (int i = 0; i <= g; i++) {
    eval += coef[i] * potencia;
    potencia *= x0;
}
cout << "P(" << x0 << ") = " << eval << "\nDerivada P'(x): ";
if (g == 0) {
    cout << "0\n";
} else {
    for (int i = 1; i <= g; i++) {
        deriv[i - 1] = i * coef[i];
        cout << deriv[i - 1] << "x^" << (i - 1) << (i < g ? " + " : "");
    }
    cout << "\n";
}
```
* *Prueba rápida:* $P(x) = 3 + 2x + 5x^2$ (`g=2`, `coef={3, 2, 5}`), `x0=2` $\rightarrow$ $P(2) = 3 + 4 + 20 = 27$, $P'(x) = 2x^0 + 10x^1$.
