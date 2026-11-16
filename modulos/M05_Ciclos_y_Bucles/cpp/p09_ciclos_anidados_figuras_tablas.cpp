#include <iomanip>
#include <iostream>

using namespace std;

int main() {
    int n = 0;
    bool entradaOk = true;

    cout << "=== CICLOS ANIDADOS: FIGURAS Y TABLA DE MULTIPLICAR ===" << endl;
    do {
        cout << "Ingrese el tamano n (1 a 10): ";
        if (!(cin >> n)) {
            entradaOk = false;
            break;
        }
        if (n < 1 || n > 10) {
            cout << "Error: n debe estar entre 1 y 10." << endl;
        }
    } while (n < 1 || n > 10);

    if (!entradaOk) {
        return 0;
    }

    // 1. Triangulo rectangulo de asteriscos
    cout << "\n--- 1. Triangulo Rectangulo (" << n << " filas) ---" << endl;
    for (int fila = 1; fila <= n; fila++) {
        for (int col = 1; col <= fila; col++) {
            cout << "* ";
        }
        cout << endl;
    }

    // 2. Piramide centrada de asteriscos
    cout << "\n--- 2. Piramide Centrada (" << n << " filas) ---" << endl;
    for (int fila = 1; fila <= n; fila++) {
        for (int esp = 1; esp <= n - fila; esp++) {
            cout << " ";
        }
        for (int ast = 1; ast <= 2 * fila - 1; ast++) {
            cout << "*";
        }
        cout << endl;
    }

    // 3. Cuadricula de tablas de multiplicar de 1 a n
    cout << "\n--- 3. Tabla de Multiplicar Cruzada (1.." << n << ") ---" << endl;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cout << setw(4) << (i * j);
        }
        cout << endl;
    }

    return 0;
}
