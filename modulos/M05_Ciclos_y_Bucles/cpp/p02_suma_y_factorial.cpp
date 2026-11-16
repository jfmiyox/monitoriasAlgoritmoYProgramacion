#include <iostream>

using namespace std;

int main() {
    int n = 0;
    bool entradaOk = true;

    cout << "=== SUMA Y FACTORIAL DE 1 A N ===" << endl;

    // Validacion con do-while: se ejecuta al menos 1 vez
    // Condicion en C++: CONTINUA mientras n sea invalido
    do {
        cout << "Ingrese un entero n (entre 0 y 20): ";
        if (!(cin >> n)) {
            entradaOk = false;
            break;
        }
        if (n < 0 || n > 20) {
            cout << "Valor fuera de rango. Intente nuevamente." << endl;
        }
    } while (n < 0 || n > 20);

    if (!entradaOk) {
        return 0;
    }

    long long suma = 0;        // Neutro aditivo = 0
    long long factorial = 1;   // Neutro multiplicativo = 1 (0! = 1)

    for (int i = 1; i <= n; i++) {
        suma += i;
        factorial *= i;
    }

    cout << "\nResultados para n = " << n << ":" << endl;
    cout << "Suma de 1 hasta " << n << " = " << suma << endl;
    cout << "Factorial " << n << "! = " << factorial << endl;

    return 0;
}
