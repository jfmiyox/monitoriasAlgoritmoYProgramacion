// ============================================================================
// Modulo 03 - Problema Resuelto 01: Desglose de Billetes en Cajero Automatico
// Conceptos: int, division entera (/), operador modulo (%), asignacion (% =)
// Prueba sugerida: echo "188500" | ./p01_desglose_billetes
// ============================================================================
#include <iostream>
using namespace std;

int main() {
    int monto = 0;
    int resto = 0;

    cout << "=== CAJERO AUTOMATICO: DESGLOSE DE BILLETES ===" << endl;
    cout << "Ingrese el monto entero en pesos (ej. 188500): ";
    cin >> monto;

    resto = monto;

    // En C++, entero / entero trunca automaticamente la parte decimal
    int b50 = resto / 50000;
    resto %= 50000; // Equivale a: resto = resto % 50000;

    int b20 = resto / 20000;
    resto %= 20000;

    int b10 = resto / 10000;
    resto %= 10000;

    int b5 = resto / 5000;
    resto %= 5000;

    int b2 = resto / 2000;
    resto %= 2000;

    int b1 = resto / 1000;
    int sobrante = resto % 1000;

    cout << "\n--- Desglose optimo para $" << monto << " ---" << endl;
    cout << "Billetes de $50.000 : " << b50 << endl;
    cout << "Billetes de $20.000 : " << b20 << endl;
    cout << "Billetes de $10.000 : " << b10 << endl;
    cout << "Billetes de $5.000  : " << b5 << endl;
    cout << "Billetes de $2.000  : " << b2 << endl;
    cout << "Billetes de $1.000  : " << b1 << endl;
    cout << "Sobrante en monedas : $" << sobrante << endl;

    return 0;
}
