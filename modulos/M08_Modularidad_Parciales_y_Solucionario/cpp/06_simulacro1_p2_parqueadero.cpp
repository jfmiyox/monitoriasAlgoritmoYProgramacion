// ============================================================================
// Modulo 08 - Simulacro 1, Punto 2: Parqueadero Inteligente
// Temas Corte 1: switch-case, division entera (/), modulo (%), condicionales
// ============================================================================

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    char tipo = ' ';
    int minutosTotales = 0;
    char tieneConvenio = 'N';

    cout << "=== PARQUEADERO CENTRAL: LIQUIDACION ===" << endl;
    cout << "Tipo de vehiculo (M=Moto, C=Carro, V=Van): ";
    cin >> tipo;

    double tarifaHora = 0.0;
    switch (tipo) {
        case 'M':
        case 'm':
            tarifaHora = 1800.0;
            break;
        case 'C':
        case 'c':
            tarifaHora = 3500.0;
            break;
        case 'V':
        case 'v':
            tarifaHora = 5000.0;
            break;
        default:
            cout << "Error: tipo de vehiculo no reconocido." << endl;
            return 0;
    }

    cout << "Ingrese tiempo total de estadia en minutos (>= 1): ";
    cin >> minutosTotales;
    if (minutosTotales < 1) {
        cout << "Error: el tiempo minimo de estadia es 1 minuto." << endl;
        return 0;
    }

    // Desglose exacto con division entera y modulo
    int horasCompletas = minutosTotales / 60;
    int minutosSobrantes = minutosTotales % 60;

    // Regla de cobro: minimo 1 hora; tolerancia de 15 min si ya paso 1 hora
    int horasCobradas = horasCompletas;
    if (horasCompletas == 0) {
        horasCobradas = 1;
    } else if (minutosSobrantes > 15) {
        horasCobradas = horasCompletas + 1;
    }

    double subtotal = horasCobradas * tarifaHora;
    double descuentoEstadia = 0.0;
    if (horasCobradas >= 6) {
        descuentoEstadia = subtotal * 0.15; // 15% por larga estadia
    }

    cout << "Presenta tiquete sellado de convenio comercial? (S/N): ";
    cin >> tieneConvenio;

    double descuentoConvenio = 0.0;
    if (tieneConvenio == 'S' || tieneConvenio == 's') {
        descuentoConvenio = 2000.0;
    }

    double total = subtotal - descuentoEstadia - descuentoConvenio;
    if (total < 0.0) {
        total = 0.0;
    }

    cout << fixed << setprecision(2);
    cout << "\n--- RESUMEN DE ESTADIA ---" << endl;
    cout << "Tiempo real        : " << horasCompletas << "h " << minutosSobrantes << "m" << endl;
    cout << "Horas facturadas   : " << horasCobradas << " h" << endl;
    cout << "Subtotal           : $" << subtotal << endl;
    cout << "Desc. larga estadia: -$" << descuentoEstadia << endl;
    cout << "Desc. convenio     : -$" << descuentoConvenio << endl;
    cout << "TOTAL A PAGAR      : $" << total << endl;

    return 0;
}
