// Modulo 02 - Ejemplo 04: Conversion de temperatura (Celsius a Fahrenheit y Kelvin)
// Objetivo: Evitar la trampa de la division entera usando 9.0 / 5.0

#include <iostream>
using namespace std;

int main() {
    double celsius;
    double fahrenheit;
    double kelvin;

    cout << "=== CONVERSOR DE TEMPERATURA ===" << endl;
    cout << "Ingresa la temperatura en grados Celsius: ";
    cin >> celsius;

    fahrenheit = (9.0 / 5.0) * celsius + 32.0;
    kelvin = celsius + 273.15;

    cout << celsius << " C equivalen a " << fahrenheit << " F" << endl;
    cout << celsius << " C equivalen a " << kelvin << " K" << endl;

    return 0;
}
