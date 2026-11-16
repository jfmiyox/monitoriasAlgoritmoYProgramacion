// ============================================================================
// Modulo 08 - Simulacro 1, Punto 1: Control de Peaje Vehicular
// Temas Corte 1: Variables, tipos, condicionales, calculo de descuentos/recargos
// ============================================================================

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int categoria = 0;
    int ejes = 0;
    char horaPico = 'N';
    char tieneTag = 'N';

    cout << "=== PEAJE NACIONAL: LIQUIDACION DE TARIFA ===" << endl;
    cout << "Categorias: 1=Automovil, 2=Camioneta/Microbus, 3=Camion pesado" << endl;
    cout << "Ingrese categoria (1-3): ";
    cin >> categoria;

    if (categoria < 1 || categoria > 3) {
        cout << "Error: categoria invalida." << endl;
        return 0;
    }

    double tarifaBase = 0.0;
    if (categoria == 1) {
        tarifaBase = 12000.0;
    } else if (categoria == 2) {
        tarifaBase = 18500.0;
    } else {
        cout << "Ingrese numero de ejes del camion (minimo 2): ";
        cin >> ejes;
        if (ejes < 2) {
            cout << "Error: un camion debe tener al menos 2 ejes." << endl;
            return 0;
        }
        // Tarifa base de 2 ejes: $28.000 + $7.500 por cada eje adicional
        tarifaBase = 28000.0 + (ejes - 2) * 7500.0;
    }

    cout << "Transita en hora pico? (S/N): ";
    cin >> horaPico;
    cout << "Tiene dispositivo Telepeaje/TAG? (S/N): ";
    cin >> tieneTag;

    double recargoPico = 0.0;
    if (horaPico == 'S' || horaPico == 's') {
        recargoPico = tarifaBase * 0.15;
    }

    double subtotal = tarifaBase + recargoPico;

    double descuentoTag = 0.0;
    if (tieneTag == 'S' || tieneTag == 's') {
        descuentoTag = subtotal * 0.10;
    }

    double totalPagar = subtotal - descuentoTag;

    cout << fixed << setprecision(2);
    cout << "\n--- TIRILLA DE PAGO ---" << endl;
    cout << "Tarifa base    : $" << tarifaBase << endl;
    cout << "Recargo pico   : $" << recargoPico << endl;
    cout << "Descuento TAG  : -$" << descuentoTag << endl;
    cout << "TOTAL A PAGAR  : $" << totalPagar << endl;

    return 0;
}
