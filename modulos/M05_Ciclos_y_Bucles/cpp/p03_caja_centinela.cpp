#include <iomanip>
#include <iostream>

using namespace std;

int main() {
    double precio = 0.0;
    double total = 0.0;
    int cantidad = 0;

    cout << "=== CAJA REGISTRADORA CON CENTINELA (CICLO WHILE) ===" << endl;
    cout << "Ingrese el precio de cada producto (0 para terminar): ";

    // Lectura cebadora: si el usuario ingresa 0 de una vez, el ciclo hace 0 vueltas
    if (!(cin >> precio)) {
        return 0;
    }

    while (precio != 0.0) {
        if (precio < 0.0) {
            cout << "Advertencia: precio negativo ignorado (" << precio << ")." << endl;
        } else {
            total += precio;
            cantidad++;
        }

        cout << "Ingrese siguiente precio (0 para terminar): ";
        if (!(cin >> precio)) {
            break;
        }
    }

    cout << fixed << setprecision(2);
    cout << "\n=== RESUMEN DE COMPRA ===" << endl;
    if (cantidad == 0) {
        cout << "No se registraron productos validos." << endl;
    } else {
        double promedio = total / cantidad;
        cout << "Productos validos: " << cantidad << endl;
        cout << "Total a pagar:     $" << total << endl;
        cout << "Precio promedio:   $" << promedio << endl;
    }

    return 0;
}
