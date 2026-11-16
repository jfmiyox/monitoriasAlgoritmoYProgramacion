// Modulo 02 - Ejemplo 05: Factura sencilla de cafeteria
// Objetivo: Combinar variables enteras (cantidad) y reales (precios y propina)

#include <iostream>
using namespace std;

int main() {
    int cantidad;
    double precioUnitario;
    double subtotal;
    double propina;
    double totalPagar;

    cout << "=== CAJA REGISTRADORA DE CAFETERIA ===" << endl;
    cout << "Ingresa el precio unitario del producto: ";
    cin >> precioUnitario;

    cout << "Ingresa la cantidad comprada: ";
    cin >> cantidad;

    subtotal = precioUnitario * cantidad;
    propina = subtotal * 0.10;
    totalPagar = subtotal + propina;

    cout << "Subtotal: $" << subtotal << endl;
    cout << "Propina sugerida (10%): $" << propina << endl;
    cout << "Total a pagar: $" << totalPagar << endl;

    return 0;
}
