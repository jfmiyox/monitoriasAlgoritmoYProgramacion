// ============================================================================
// Modulo 04 - Problema Resuelto 08: Anio Bisiesto y Dias del Mes
// Conceptos: Compuertas && / || combinadas + switch agrupado + if dentro de case
// Prueba sugerida: printf "2\n2024\n" | ./p08_bisiesto_dias_mes
// ============================================================================
#include <iostream>
using namespace std;

int main() {
    int mes = 0;
    int anio = 0;
    int dias = 0;

    cout << "=== CALENDARIO MAESTRO: BISIESTO Y DIAS DEL MES ===" << endl;
    cout << "Ingrese el numero del mes (1 a 12): ";
    cin >> mes;
    cout << "Ingrese el anio (entero > 0): ";
    cin >> anio;

    if (mes < 1 || mes > 12 || anio <= 0) {
        cout << "ERROR: El mes debe estar entre 1 y 12, y el anio debe ser > 0." << endl;
        return 0;
    }

    // Regla del calendario gregoriano para anio bisiesto
    bool esBisiesto = (anio % 4 == 0 && anio % 100 != 0) || (anio % 400 == 0);

    // En C++, agrupar varios case sin break comparte un mismo bloque
    switch (mes) {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
            dias = 31;
            break;

        case 4:
        case 6:
        case 9:
        case 11:
            dias = 30;
            break;

        case 2:
            if (esBisiesto) {
                dias = 29;
            } else {
                dias = 28;
            }
            break;

        default:
            dias = 0;
            break;
    }

    if (esBisiesto) {
        cout << "El anio " << anio << " SI es bisiesto." << endl;
    } else {
        cout << "El anio " << anio << " NO es bisiesto." << endl;
    }
    cout << "El mes " << mes << " del anio " << anio << " tiene " << dias << " dias." << endl;

    return 0;
}
