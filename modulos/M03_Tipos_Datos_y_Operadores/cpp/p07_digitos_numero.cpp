// ============================================================================
// Modulo 03 - Problema Resuelto 07: Extraccion e Inversion de Digitos (4 cifras)
// Conceptos: Division entera (/ 10, / 100, / 1000) y modulo (% 10)
// Prueba sugerida: echo "4829" | ./bin
// ============================================================================
#include <iostream>
using namespace std;

int main() {
    int numero = 0;

    cout << "=== DESCOMPOSICION DE UN NUMERO DE 4 CIFRAS ===" << endl;
    cout << "Ingrese un entero positivo de 4 cifras (ej. 4829): ";
    cin >> numero;

    int dMiles = numero / 1000;
    int dCentenas = (numero / 100) % 10;
    int dDecenas = (numero / 10) % 10;
    int dUnidades = numero % 10;

    int sumaDigitos = dMiles + dCentenas + dDecenas + dUnidades;
    int invertido = dUnidades * 1000 + dDecenas * 100 + dCentenas * 10 + dMiles;

    cout << "\n--- ANALISIS POSICIONAL ---" << endl;
    cout << "Unidades de mil : " << dMiles << endl;
    cout << "Centenas        : " << dCentenas << endl;
    cout << "Decenas         : " << dDecenas << endl;
    cout << "Unidades        : " << dUnidades << endl;
    cout << "Suma de digitos : " << sumaDigitos << endl;
    cout << "Numero invertido: " << invertido << endl;

    return 0;
}
