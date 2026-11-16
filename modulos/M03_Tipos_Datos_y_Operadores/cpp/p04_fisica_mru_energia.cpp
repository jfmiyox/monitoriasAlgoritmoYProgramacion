// ============================================================================
// Modulo 03 - Problema Resuelto 04: Fisica Basica (MRUV y Energia Cinetica)
// Conceptos: double, const, trampa de 1/2 (enteros) vs 0.5 o 1.0/2.0 (real)
// Prueba sugerida: printf "10\n5\n2\n4\n" | ./bin
// ============================================================================
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const double FACTOR_KMH = 3.6;

    double masa = 0.0;
    double vInicial = 0.0;
    double aceleracion = 0.0;
    double tiempo = 0.0;

    cout << "=== SIMULADOR DE CINEMATICA Y ENERGIA (MRUV) ===" << endl;
    cout << "Ingrese masa del objeto (kg): ";
    cin >> masa;
    cout << "Ingrese velocidad inicial v0 (m/s): ";
    cin >> vInicial;
    cout << "Ingrese aceleracion constante a (m/s^2): ";
    cin >> aceleracion;
    cout << "Ingrese tiempo transcurrido t (s): ";
    cin >> tiempo;

    // OJO: Si escribieras (1 / 2) * aceleracion * ..., (1 / 2) vale 0 en C++!
    // Por eso usamos 0.5 o (1.0 / 2.0).
    double distancia = vInicial * tiempo + 0.5 * aceleracion * tiempo * tiempo;
    double vFinal = vInicial + aceleracion * tiempo;
    double vFinalKmh = vFinal * FACTOR_KMH;
    double energiaCinetica = 0.5 * masa * vFinal * vFinal;

    cout << fixed << setprecision(2);
    cout << "\n--- RESULTADOS FISICOS ---" << endl;
    cout << "Distancia recorrida : " << distancia << " m" << endl;
    cout << "Velocidad final     : " << vFinal << " m/s (" << vFinalKmh << " km/h)" << endl;
    cout << "Energia cinetica    : " << energiaCinetica << " Joules" << endl;

    return 0;
}
