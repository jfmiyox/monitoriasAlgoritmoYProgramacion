#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    // Dos vectores paralelos estaticos de capacidad fija MAX
    const int MAX = 40;
    int codigos[MAX];
    double precios[MAX];
    int n;

    do {
        cout << "Cantidad de productos a registrar (1 a " << MAX << "): ";
        cin >> n;
        if (n < 1 || n > MAX) {
            cout << "Error: cantidad fuera del rango permitido.\n";
        }
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

    // Busqueda secuencial con bandera booleana
    bool encontrado = false;
    int pos = -1;

    for (int i = 0; i < n; i++) {
        if (codigos[i] == codigoBuscado) {
            encontrado = true;
            pos = i;
            break; // Ya lo encontramos, salimos del ciclo
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
