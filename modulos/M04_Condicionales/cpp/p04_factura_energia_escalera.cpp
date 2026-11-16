// ============================================================================
// Modulo 04 - Problema Resuelto 04: Factura Escalonada de Energia Electrica
// Conceptos: Escalera else-if ordenada por tramos marginales + switch por estrato
// Prueba sugerida: printf "320\n2\n" | ./p04_factura_energia_escalera
// ============================================================================
#include <iomanip>
#include <iostream>
using namespace std;

int main() {
    int consumo = 0;
    int estrato = 0;
    double subtotal = 0.0;
    double factor = 1.0;

    cout << "=== FACTURA DE ENERGIA ELECTRICA ===" << endl;
    cout << "Consumo del mes en kWh (entero >= 0): ";
    cin >> consumo;
    cout << "Estrato socioeconomico (1 a 6): ";
    cin >> estrato;

    if (consumo < 0 || estrato < 1 || estrato > 6) {
        cout << "ERROR: El consumo debe ser >= 0 y el estrato estar entre 1 y 6." << endl;
        return 0;
    }

    // Escalera else-if por tramos progresivos (orden ascendente obligatorio)
    if (consumo <= 100) {
        subtotal = consumo * 450.0;
    } else if (consumo <= 250) {
        subtotal = (100 * 450.0) + (consumo - 100) * 600.0;
    } else if (consumo <= 450) {
        subtotal = (100 * 450.0) + (150 * 600.0) + (consumo - 250) * 800.0;
    } else {
        subtotal = (100 * 450.0) + (150 * 600.0) + (200 * 800.0) + (consumo - 450) * 1050.0;
    }

    // Ajuste segun estrato: 1 (-40%), 2 (-25%), 3 (-10%), 4 (0%), 5 y 6 (+20%)
    switch (estrato) {
        case 1:
            factor = 0.60;
            break;
        case 2:
            factor = 0.75;
            break;
        case 3:
            factor = 0.90;
            break;
        case 4:
            factor = 1.00;
            break;
        case 5:
        case 6:
            factor = 1.20;
            break;
        default:
            factor = 1.00;
            break;
    }

    double totalPagar = subtotal * factor;
    double ajuste = totalPagar - subtotal;

    cout << fixed << setprecision(2);
    cout << "\n--- RESUMEN DE FACTURA ---" << endl;
    cout << "Subtotal base      : $" << subtotal << endl;
    cout << "Ajuste por estrato : $" << ajuste << endl;
    cout << "TOTAL A PAGAR      : $" << totalPagar << endl;

    return 0;
}
