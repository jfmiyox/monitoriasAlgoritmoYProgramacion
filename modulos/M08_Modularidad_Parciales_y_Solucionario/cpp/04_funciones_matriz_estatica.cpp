// ============================================================================
// Modulo 08 - Ejemplo 04: Pasar Matrices ESTATICAS a Funciones
// Regla de oro en C++: la segunda dimension [MAX_C] ES OBLIGATORIA en parametros
// ============================================================================

#include <iostream>
#include <iomanip>
using namespace std;

const int MAX_F = 10;
const int MAX_C = 10;

void leerMatriz(int m[][MAX_C], int filas, int cols);
void mostrarMatriz(const int m[][MAX_C], int filas, int cols);
int sumarFila(const int m[][MAX_C], int filaObjetivo, int cols);
int sumarColumna(const int m[][MAX_C], int filas, int colObjetivo);
int sumarDiagonalPrincipal(const int m[][MAX_C], int n);

int main() {
    int mat[MAX_F][MAX_C] = {{0}};
    int f = 0, c = 0;

    do {
        cout << "Numero de filas (1.." << MAX_F << "): ";
        if (!(cin >> f)) {
            return 0;
        }
    } while (f < 1 || f > MAX_F);

    do {
        cout << "Numero de columnas (1.." << MAX_C << "): ";
        if (!(cin >> c)) {
            return 0;
        }
    } while (c < 1 || c > MAX_C);

    leerMatriz(mat, f, c);

    cout << "\nMatriz registrada:\n";
    mostrarMatriz(mat, f, c);

    cout << "\nTotales por fila:\n";
    for (int i = 0; i < f; i++) {
        cout << "  Fila " << i << ": " << sumarFila(mat, i, c) << endl;
    }

    cout << "\nTotales por columna:\n";
    for (int j = 0; j < c; j++) {
        cout << "  Columna " << j << ": " << sumarColumna(mat, f, j) << endl;
    }

    if (f == c) {
        cout << "\nLa matriz es cuadrada. Suma diagonal principal = "
             << sumarDiagonalPrincipal(mat, f) << endl;
    } else {
        cout << "\nLa matriz NO es cuadrada; no tiene diagonal principal unica." << endl;
    }

    return 0;
}

void leerMatriz(int m[][MAX_C], int filas, int cols) {
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < cols; j++) {
            cout << "  m[" << i << "][" << j << "] = ";
            cin >> m[i][j];
        }
    }
}

void mostrarMatriz(const int m[][MAX_C], int filas, int cols) {
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < cols; j++) {
            cout << setw(6) << m[i][j];
        }
        cout << endl;
    }
}

int sumarFila(const int m[][MAX_C], int filaObjetivo, int cols) {
    int suma = 0;
    for (int j = 0; j < cols; j++) {
        suma += m[filaObjetivo][j];
    }
    return suma;
}

int sumarColumna(const int m[][MAX_C], int filas, int colObjetivo) {
    int suma = 0;
    for (int i = 0; i < filas; i++) {
        suma += m[i][colObjetivo];
    }
    return suma;
}

int sumarDiagonalPrincipal(const int m[][MAX_C], int n) {
    int suma = 0;
    for (int i = 0; i < n; i++) {
        suma += m[i][i];
    }
    return suma;
}
