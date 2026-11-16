#include <iostream>

using namespace std;

int main() {
    int n = 0;
    int sumaProductos = 0;

    cout << "=== TABLA DE MULTIPLICAR (CICLO FOR) ===" << endl;
    cout << "Ingrese un numero entero para ver su tabla del 1 al 10: ";
    if (!(cin >> n)) {
        return 0;
    }

    cout << "\nTabla del " << n << ":" << endl;
    for (int i = 1; i <= 10; i++) {
        int producto = n * i;
        cout << n << " x " << i << " = " << producto << endl;
        sumaProductos += producto;
    }

    cout << "Suma de los 10 productos: " << sumaProductos << endl;
    return 0;
}
