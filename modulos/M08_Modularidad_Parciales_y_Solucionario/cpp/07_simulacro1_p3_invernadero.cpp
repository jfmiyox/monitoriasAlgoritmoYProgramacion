// ============================================================================
// Modulo 08 - Simulacro 1, Punto 3: Monitor de Temperaturas de Invernadero
// Temas Corte 1: Ciclo while con centinela (-999), validacion, max/min SIN arreglos
// ============================================================================

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const double CENTINELA = -999.0;
    const double TEMP_MIN_VALIDA = -10.0;
    const double TEMP_MAX_VALIDA = 60.0;

    double temp = 0.0;
    int validas = 0;
    int alertasFrio = 0;
    int alertasCalor = 0;
    double suma = 0.0;
    double tempMin = 0.0;
    double tempMax = 0.0;

    cout << "=== MONITOR DE INVERNADERO (Centinela: -999) ===" << endl;
    cout << "Ingrese lectura de temperatura (-10.0 a 60.0 C, o -999 para salir): ";
    cin >> temp;

    while (temp != CENTINELA) {
        if (temp < TEMP_MIN_VALIDA || temp > TEMP_MAX_VALIDA) {
            cout << "  [Aviso] Sensor fuera de rango fisico. Lectura descartada." << endl;
        } else {
            // Inicializar min y max con el PRIMER dato valido (regla de oro)
            if (validas == 0) {
                tempMin = temp;
                tempMax = temp;
            } else {
                if (temp < tempMin) {
                    tempMin = temp;
                }
                if (temp > tempMax) {
                    tempMax = temp;
                }
            }

            validas++;
            suma += temp;

            if (temp < 12.0) {
                alertasFrio++;
            } else if (temp > 32.0) {
                alertasCalor++;
            }
        }

        cout << "Ingrese lectura (-999 para terminar): ";
        if (!(cin >> temp)) {
            break;
        }
    }

    cout << fixed << setprecision(2);
    cout << "\n--- REPORTE DE TURNO ---" << endl;
    if (validas == 0) {
        cout << "No se registraron lecturas validas." << endl;
    } else {
        double promedio = suma / validas;
        cout << "Lecturas validas : " << validas << endl;
        cout << "Promedio termico : " << promedio << " C" << endl;
        cout << "Temperatura min  : " << tempMin << " C" << endl;
        cout << "Temperatura max  : " << tempMax << " C" << endl;
        cout << "Alertas frio (<12 C)  : " << alertasFrio << endl;
        cout << "Alertas calor (>32 C) : " << alertasCalor << endl;
    }

    return 0;
}
