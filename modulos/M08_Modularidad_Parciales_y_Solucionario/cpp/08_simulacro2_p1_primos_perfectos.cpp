// ============================================================================
// Modulo 08 - Simulacro 2, Punto 1: Primos y Numeros Perfectos en un Rango
// Temas Corte Final: Modularidad (bool/int/void) + ciclos anidados
// ============================================================================

#include <iostream>
using namespace std;

void leerRangoValido(int &inicio, int &fin);
bool esPrimo(int n);
int sumaDivisoresPropios(int n);
bool esPerfecto(int n);
void analizarRango(int inicio, int fin);

int main() {
    int inicio = 0, fin = 0;

    cout << "=== ANALIZADOR NUMERICO MODULAR ===" << endl;
    leerRangoValido(inicio, fin);
    analizarRango(inicio, fin);

    return 0;
}

void leerRangoValido(int &inicio, int &fin) {
    do {
        cout << "Ingrese limite inferior (>= 1): ";
        if (!(cin >> inicio)) {
            inicio = 1;
            fin = 1;
            return;
        }
        cout << "Ingrese limite superior (>= inferior): ";
        if (!(cin >> fin)) {
            inicio = 1;
            fin = 1;
            return;
        }
        if (inicio < 1 || fin < inicio) {
            cout << "  [Error] Rango invalido. Intente de nuevo.\n";
        }
    } while (inicio < 1 || fin < inicio);
}

bool esPrimo(int n) {
    if (n <= 1) {
        return false;
    }
    for (int d = 2; d * d <= n; d++) {
        if (n % d == 0) {
            return false; // Si tiene un divisor, ya sabemos que no es primo
        }
    }
    return true;
}

int sumaDivisoresPropios(int n) {
    int suma = 0;
    for (int d = 1; d <= n / 2; d++) {
        if (n % d == 0) {
            suma += d;
        }
    }
    return suma;
}

bool esPerfecto(int n) {
    if (n <= 1) {
        return false;
    }
    return (sumaDivisoresPropios(n) == n);
}

void analizarRango(int inicio, int fin) {
    int cantPrimos = 0;
    int cantPerfectos = 0;

    cout << "\nPrimos encontrados: ";
    for (int num = inicio; num <= fin; num++) {
        if (esPrimo(num)) {
            cout << num << " ";
            cantPrimos++;
        }
    }
    if (cantPrimos == 0) {
        cout << "(ninguno)";
    }
    cout << "\nTotal de primos: " << cantPrimos << endl;

    cout << "\nNumeros perfectos encontrados: ";
    for (int num = inicio; num <= fin; num++) {
        if (esPerfecto(num)) {
            cout << num << " ";
            cantPerfectos++;
        }
    }
    if (cantPerfectos == 0) {
        cout << "(ninguno)";
    }
    cout << "\nTotal de perfectos: " << cantPerfectos << endl;
}
