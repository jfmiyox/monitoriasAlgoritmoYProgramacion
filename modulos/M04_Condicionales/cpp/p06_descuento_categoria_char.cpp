// ============================================================================
// Modulo 04 - Problema Resuelto 06: Tienda TechStore (Descuento por Categoria)
// Conceptos: switch sobre char agrupando minuscula/mayuscula + if por monto
// Prueba sugerida: printf "600000\na\n" | ./p06_descuento_categoria_char
// ============================================================================
#include <iomanip>
#include <iostream>
#include <string>
using namespace std;

int main() {
    double montoCompra = 0.0;
    double porcentaje = 0.0;
    char categoria = ' ';
    string nombreCat = "";
    bool categoriaValida = true;
    bool bonoAplicado = false;

    cout << "=== TIENDA TECHSTORE ===" << endl;
    cout << "Ingrese el monto de la compra ($): ";
    cin >> montoCompra;
    cout << "Categoria del cliente (A = VIP, B = Frecuente, C = Nuevo): ";
    cin >> categoria;

    if (montoCompra <= 0.0) {
        cout << "ERROR: El monto de compra debe ser mayor a cero." << endl;
        return 0;
    }

    // Caida controlada intencional: 'a' comparte el bloque con 'A'
    switch (categoria) {
        case 'a':
        case 'A':
            porcentaje = 20.0;
            nombreCat = "VIP";
            break;

        case 'b':
        case 'B':
            porcentaje = 12.0;
            nombreCat = "Frecuente";
            break;

        case 'c':
        case 'C':
            porcentaje = 5.0;
            nombreCat = "Nuevo";
            break;

        default:
            categoriaValida = false;
            break;
    }

    if (!categoriaValida) {
        cout << "ERROR: Categoria no reconocida. Use A, B o C." << endl;
        return 0;
    }

    // Bono adicional si la compra supera $500.000
    if (montoCompra > 500000.0) {
        porcentaje = porcentaje + 5.0;
        bonoAplicado = true;
    }

    double descuento = montoCompra * (porcentaje / 100.0);
    double totalPagar = montoCompra - descuento;

    cout << fixed << setprecision(2);
    cout << "\n--- TIRILLA DE COMPRA ---" << endl;
    cout << "Categoria         : " << nombreCat << endl;
    cout << "Bono > $500.000   : " << (bonoAplicado ? "SI (+5%)" : "NO") << endl;
    cout << "Descuento total % : " << porcentaje << "%" << endl;
    cout << "Valor descontado  : $" << descuento << endl;
    cout << "TOTAL A PAGAR     : $" << totalPagar << endl;

    return 0;
}
