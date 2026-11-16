// Modulo 02 - Ejemplo 03: Area y perimetro de un terreno rectangular
// Objetivo: Calcular multiples salidas a partir de dos entradas reales

#include <iostream>
using namespace std;

int main() {
    double base;
    double altura;
    double area;
    double perimetro;

    cout << "=== AREA Y PERIMETRO DE UN TERRENO ===" << endl;
    cout << "Ingresa el ancho (base) en metros: ";
    cin >> base;

    cout << "Ingresa el largo (altura) en metros: ";
    cin >> altura;

    area = base * altura;
    perimetro = 2.0 * (base + altura);

    cout << "Area del terreno: " << area << " m2" << endl;
    cout << "Perimetro del terreno: " << perimetro << " m" << endl;

    return 0;
}
