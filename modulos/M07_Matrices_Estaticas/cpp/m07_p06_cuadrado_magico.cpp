#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    const int MAX = 10;
    int mat[MAX][MAX];
    int n;

    do {
        cout << "Orden N de la matriz cuadrada (1 a " << MAX << "): ";
        cin >> n;
    } while (n < 1 || n > MAX);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << "mat[" << i << "][" << j << "] = ";
            cin >> mat[i][j];
        }
    }

    // Usar la suma de la fila 0 como suma objetivo de referencia
    int sumaObjetivo = 0;
    for (int j = 0; j < n; j++) {
        sumaObjetivo += mat[0][j];
    }

    bool esMagico = true;

    // 1. Verificar todas las filas
    for (int i = 0; i < n && esMagico; i++) {
        int sumaFila = 0;
        for (int j = 0; j < n; j++) {
            sumaFila += mat[i][j];
        }
        if (sumaFila != sumaObjetivo) {
            esMagico = false;
        }
    }

    // 2. Verificar todas las columnas
    for (int j = 0; j < n && esMagico; j++) {
        int sumaCol = 0;
        for (int i = 0; i < n; i++) {
            sumaCol += mat[i][j];
        }
        if (sumaCol != sumaObjetivo) {
            esMagico = false;
        }
    }

    // 3. Verificar diagonal principal y secundaria
    if (esMagico) {
        int diagP = 0;
        int diagS = 0;
        for (int i = 0; i < n; i++) {
            diagP += mat[i][i];
            diagS += mat[i][n - 1 - i];
        }
        if (diagP != sumaObjetivo || diagS != sumaObjetivo) {
            esMagico = false;
        }
    }

    cout << "\nMatriz evaluada:\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << setw(5) << mat[i][j];
        }
        cout << "\n";
    }

    if (esMagico) {
        cout << "\nES un Cuadrado Magico! Constante magica = " << sumaObjetivo << "\n";
    } else {
        cout << "\nNO es un Cuadrado Magico.\n";
    }

    return 0;
}
