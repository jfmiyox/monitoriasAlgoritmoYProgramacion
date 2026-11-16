#include <iostream>

using namespace std;

int main() {
    long long n = 0;
    bool entradaOk = true;

    cout << "=== DETECTOR DE NUMERO PRIMO CON BANDERA BOOL ===" << endl;
    do {
        cout << "Ingrese un entero positivo (>= 1): ";
        if (!(cin >> n)) {
            entradaOk = false;
            break;
        }
        if (n < 1) {
            cout << "Error: ingrese un numero mayor o igual a 1." << endl;
        }
    } while (n < 1);

    if (!entradaOk) {
        return 0;
    }

    bool esPrimo = true;
    long long menorDivisor = 0;

    if (n == 1) {
        esPrimo = false;
    } else {
        // Basta probar divisores d hasta la raiz de n (d <= n / d)
        // La bandera esPrimo detiene el ciclo apenas hallamos un divisor
        for (long long d = 2; d <= n / d && esPrimo; d++) {
            if (n % d == 0) {
                esPrimo = false;
                menorDivisor = d;
            }
        }
    }

    cout << "\nResultado para " << n << ":" << endl;
    if (esPrimo) {
        cout << n << " ES un numero primo." << endl;
    } else if (n == 1) {
        cout << "1 NO es primo por definicion (solo tiene un divisor)." << endl;
    } else {
        cout << n << " NO es primo (es compuesto). Menor divisor > 1: " << menorDivisor << endl;
    }

    return 0;
}
