#include <iostream>

using namespace std;

int main() {
    int n = 0;
    bool entradaOk = true;

    cout << "=== SERIE DE FIBONACCI CON VARIABLES DESLIZANTES ===" << endl;
    do {
        cout << "Cuantos terminos desea generar? (1 a 50): ";
        if (!(cin >> n)) {
            entradaOk = false;
            break;
        }
        if (n < 1 || n > 50) {
            cout << "Error: elija un valor entre 1 y 50." << endl;
        }
    } while (n < 1 || n > 50);

    if (!entradaOk) {
        return 0;
    }

    long long a = 0;
    long long b = 1;
    long long sumaTotal = 0;
    int cantidadPares = 0;

    cout << "\nSerie (" << n << " terminos):" << endl;
    for (int i = 1; i <= n; i++) {
        cout << a;
        if (i < n) {
            cout << ", ";
        }

        sumaTotal += a;
        if (a % 2 == 0) {
            cantidadPares++;
        }

        // Deslizamos la ventana: el siguiente es a + b
        long long siguiente = a + b;
        a = b;
        b = siguiente;
    }
    cout << endl;

    cout << "Suma de los " << n << " terminos: " << sumaTotal << endl;
    cout << "Terminos pares en la serie: " << cantidadPares << endl;

    return 0;
}
