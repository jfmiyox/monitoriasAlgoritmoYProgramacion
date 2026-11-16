// ============================================================================
// Modulo 03 - Problema Resuelto 02: Conversion de Segundos a Horas/Min/Seg
// Conceptos: const int, division entera (/), modulo (%), precedencia
// Prueba sugerida: echo "3725" | ./p02_conversion_tiempo
// ============================================================================
#include <iostream>
using namespace std;

int main() {
    const int SEG_POR_HORA = 3600;
    const int SEG_POR_MIN = 60;

    int totalSegundos = 0;
    cout << "=== CONVERSOR DE TIEMPO (SEGUNDOS A HH:MM:SS) ===" << endl;
    cout << "Ingrese la cantidad total de segundos (ej. 3725): ";
    cin >> totalSegundos;

    int horas = totalSegundos / SEG_POR_HORA;
    int resto = totalSegundos % SEG_POR_HORA;
    int minutos = resto / SEG_POR_MIN;
    int segundos = resto % SEG_POR_MIN;

    cout << "\n" << totalSegundos << " segundos equivalen a: "
         << horas << " hora(s), "
         << minutos << " minuto(s) y "
         << segundos << " segundo(s)." << endl;

    return 0;
}
