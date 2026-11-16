#include <iostream>

using namespace std;

int main() {
    long long n = 0;
    bool entradaOk = true;

    cout << "=== ANALISIS DE DIGITOS Y NUMERO CAPICUA ===" << endl;
    do {
        cout << "Ingrese un numero entero no negativo (>= 0): ";
        if (!(cin >> n)) {
            entradaOk = false;
            break;
        }
        if (n < 0) {
            cout << "Error: el numero debe ser mayor o igual a 0." << endl;
        }
    } while (n < 0);

    if (!entradaOk) {
        return 0;
    }

    long long aux = n;
    int cantidadDigitos = 0;
    long long sumaDigitos = 0;
    long long invertido = 0;

    // Usamos do-while para que el caso n = 0 tambien ejecute 1 vez (1 digito)
    do {
        long long digito = aux % 10;
        cantidadDigitos++;
        sumaDigitos += digito;
        invertido = invertido * 10 + digito;
        aux = aux / 10;
    } while (aux > 0);

    cout << "\nResultados para n = " << n << ":" << endl;
    cout << "Cantidad de digitos: " << cantidadDigitos << endl;
    cout << "Suma de digitos:     " << sumaDigitos << endl;
    cout << "Numero invertido:    " << invertido << endl;
    if (invertido == n) {
        cout << "Es capicua:          SI" << endl;
    } else {
        cout << "Es capicua:          NO" << endl;
    }

    return 0;
}
