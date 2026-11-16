// ============================================================================
// Modulo 08 - Ejemplo 03: Pasar Vectores ESTATICOS a Funciones
// Regla: Se pasa el nombre del arreglo SIN corchetes + el tamano logico n
// ============================================================================

#include <iostream>
#include <iomanip>
using namespace std;

const int MAX = 50; // Capacidad fisica fija definida en tiempo de compilacion

void leerVector(int v[], int n);
void mostrarVector(const int v[], int n);
double calcularPromedio(const int v[], int n);
void obtenerMinMax(const int v[], int n, int &minimo, int &maximo);
int buscarPosicion(const int v[], int n, int objetivo);

int main() {
    int datos[MAX] = {0};
    int n = 0;

    do {
        cout << "Cuantos elementos desea ingresar (1.." << MAX << "): ";
        if (!(cin >> n)) {
            return 0;
        }
    } while (n < 1 || n > MAX);

    leerVector(datos, n);

    cout << "\nContenido del vector: ";
    mostrarVector(datos, n);

    cout << fixed << setprecision(2);
    cout << "Promedio: " << calcularPromedio(datos, n) << endl;

    int minVal = 0, maxVal = 0;
    // Devuelve dos resultados a la vez usando parametros por referencia (&)
    obtenerMinMax(datos, n, minVal, maxVal);
    cout << "Minimo: " << minVal << " | Maximo: " << maxVal << endl;

    int buscado = 0;
    cout << "Ingrese un valor entero a buscar: ";
    cin >> buscado;

    int pos = buscarPosicion(datos, n, buscado);
    if (pos != -1) {
        cout << "Encontrado en la posicion (indice 0-based): " << pos << endl;
    } else {
        cout << "El valor " << buscado << " no existe en el vector." << endl;
    }

    return 0;
}

// Aunque no lleva '&', en C++ los arreglos se pasan por referencia de base:
// lo que escribas en v[i] modifica directamente el arreglo del main.
void leerVector(int v[], int n) {
    for (int i = 0; i < n; i++) {
        cout << "  Elemento [" << i << "]: ";
        cin >> v[i];
    }
}

// 'const' protege el arreglo para que esta funcion solo pueda leerlo, no alterarlo.
void mostrarVector(const int v[], int n) {
    cout << "[ ";
    for (int i = 0; i < n; i++) {
        cout << v[i];
        if (i < n - 1) {
            cout << ", ";
        }
    }
    cout << " ]" << endl;
}

double calcularPromedio(const int v[], int n) {
    if (n <= 0) {
        return 0.0;
    }
    int suma = 0;
    for (int i = 0; i < n; i++) {
        suma += v[i];
    }
    return static_cast<double>(suma) / n;
}

void obtenerMinMax(const int v[], int n, int &minimo, int &maximo) {
    minimo = v[0];
    maximo = v[0];
    for (int i = 1; i < n; i++) {
        if (v[i] < minimo) {
            minimo = v[i];
        }
        if (v[i] > maximo) {
            maximo = v[i];
        }
    }
}

int buscarPosicion(const int v[], int n, int objetivo) {
    for (int i = 0; i < n; i++) {
        if (v[i] == objetivo) {
            return i;
        }
    }
    return -1; // Convencion estandar: -1 significa "no encontrado"
}
