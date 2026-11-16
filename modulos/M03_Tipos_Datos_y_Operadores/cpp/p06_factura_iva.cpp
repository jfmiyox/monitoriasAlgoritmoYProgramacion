// ============================================================================
// Modulo 03 - Problema Resuelto 06: Factura Comercial con Descuento e IVA
// Conceptos: char + cin.ignore() + getline(), const double, formatos
// Prueba sugerida: printf "A\nCuaderno Profesional\n12000\n3\n10\n" | ./bin
// ============================================================================
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main() {
    const double TASA_IVA = 0.19;

    char categoria = ' ';
    string producto;
    double precioUnitario = 0.0;
    int cantidad = 0;
    double porcDescuento = 0.0;

    cout << "=== FACTURACION TIENDA UNIVERSITARIA ===" << endl;
    cout << "Ingrese letra de categoria (A/B/C): ";
    cin >> categoria;
    cin.ignore(); // Limpia el '\n' que dejo cin >> categoria

    cout << "Ingrese nombre del producto: ";
    getline(cin, producto);

    cout << "Ingrese precio unitario sin IVA: ";
    cin >> precioUnitario;
    cout << "Ingrese cantidad comprada: ";
    cin >> cantidad;
    cout << "Ingrese porcentaje de descuento (ej. 10 para 10%): ";
    cin >> porcDescuento;

    double subtotal = precioUnitario * cantidad;
    double descuento = subtotal * (porcDescuento / 100.0);
    double baseGravable = subtotal - descuento;
    double valorIva = baseGravable * TASA_IVA;
    double totalPagar = baseGravable + valorIva;

    cout << fixed << setprecision(2);
    cout << "\n=== TIRILLA DE PAGO ===" << endl;
    cout << "Categoria     : " << categoria << endl;
    cout << "Producto      : " << producto << endl;
    cout << "Subtotal      : $" << subtotal << endl;
    cout << "Descuento     : -$" << descuento << endl;
    cout << "Base gravable : $" << baseGravable << endl;
    cout << "IVA (19%)     : +$" << valorIva << endl;
    cout << "TOTAL A PAGAR : $" << totalPagar << endl;

    return 0;
}
