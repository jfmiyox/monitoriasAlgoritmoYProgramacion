// ============================================================================
// Modulo 04 - Problema Resuelto 01: El Portero Numerico (Signo, Paridad y Multiplo)
// Estructuras: Escalera if / else if / else + condicionales if-else independientes
// Prueba sugerida: printf "%s\n" "-15" | ./p01_par_multiplo_signo
// ============================================================================
#include <iostream>
using namespace std;

int main() {
    int numero = 0;

    cout << "=== EL PORTERO NUMERICO ===" << endl;
    cout << "Ingrese un numero entero (ej. -15, 0, 10, 7): ";
    if (!(cin >> numero)) {
        cout << "ERROR: Entrada no valida. Debe ingresar un numero entero." << endl;
        return 1;
    }

    // 1) Signo: escalera mutuamente excluyente (solo entra a una de las 3 ramas)
    if (numero > 0) {
        cout << "1. Signo      : El numero es POSITIVO." << endl;
    } else if (numero < 0) {
        cout << "1. Signo      : El numero es NEGATIVO." << endl;
    } else {
        cout << "1. Signo      : El numero es CERO (neutro)." << endl;
    }

    // 2) Paridad: pregunta independiente (un positivo tambien puede ser par)
    if (numero % 2 == 0) {
        cout << "2. Paridad    : Es PAR." << endl;
    } else {
        cout << "2. Paridad    : Es IMPAR." << endl;
    }

    // 3) Multiplo de 5: pregunta independiente usando operador modulo (%)
    if (numero % 5 == 0) {
        cout << "3. Multiplo 5 : SI es multiplo de 5." << endl;
    } else {
        cout << "3. Multiplo 5 : NO es multiplo de 5." << endl;
    }

    return 0;
}
