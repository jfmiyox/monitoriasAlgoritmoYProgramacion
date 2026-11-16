// Modulo 02 - Ejemplo 02: Promedio de tres calificaciones
// Objetivo: Usar variables double (decimales) y division real (/ 3.0)

#include <iostream>
using namespace std;

int main() {
    double nota1;
    double nota2;
    double nota3;
    double suma;
    double promedio;

    cout << "=== CALCULADORA DE PROMEDIO DE NOTAS ===" << endl;
    cout << "Ingresa la primera nota: ";
    cin >> nota1;

    cout << "Ingresa la segunda nota: ";
    cin >> nota2;

    cout << "Ingresa la tercera nota: ";
    cin >> nota3;

    suma = nota1 + nota2 + nota3;
    promedio = suma / 3.0;

    cout << "Suma total de notas: " << suma << endl;
    cout << "Tu promedio final es: " << promedio << endl;

    return 0;
}
