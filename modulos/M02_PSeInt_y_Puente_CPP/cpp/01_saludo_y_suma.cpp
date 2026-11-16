// Modulo 02 - Ejemplo 01: Suma de dos numeros enteros
// Objetivo: Aprender entrada (cin), proceso (=) y salida (cout)

#include <iostream>
using namespace std;

int main() {
    int numero1;
    int numero2;
    int suma;

    cout << "=== MI PRIMER PROGRAMA: SUMA DE DOS NUMEROS ===" << endl;
    cout << "Ingresa el primer numero entero: ";
    cin >> numero1;

    cout << "Ingresa el segundo numero entero: ";
    cin >> numero2;

    suma = numero1 + numero2;

    cout << "La suma de " << numero1 << " + " << numero2 << " es: " << suma << endl;

    return 0;
}
