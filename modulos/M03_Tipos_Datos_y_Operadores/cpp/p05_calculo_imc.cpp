// ============================================================================
// Modulo 03 - Problema Resuelto 05: Ficha Salud e Indice de Masa Corporal
// Conceptos: char, bool (boolalpha), static_cast<double>, division real
// Prueba sugerida: printf "M\n1\n68.5\n175\n" | ./bin
// ============================================================================
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    char sexo = ' ';
    bool haceDeporte = false;
    double pesoKg = 0.0;
    int estaturaCm = 0;

    cout << "=== FICHA MEDICA Y CALCULO DE IMC ===" << endl;
    cout << "Ingrese inicial del sexo (M / F): ";
    cin >> sexo;
    cout << "Practica deporte regularmente? (1 = Si, 0 = No): ";
    cin >> haceDeporte;
    cout << "Ingrese peso en kilogramos (ej. 68.5): ";
    cin >> pesoKg;
    cout << "Ingrese estatura en CENTIMETROS enteros (ej. 175): ";
    cin >> estaturaCm;

    // Casting explicito: si hicieramos (estaturaCm / 100), 175/100 daria 1 entero!
    double estaturaM = static_cast<double>(estaturaCm) / 100.0;
    double imc = pesoKg / (estaturaM * estaturaM);

    cout << fixed << setprecision(2);
    cout << "\n--- RESUMEN DE SALUD ---" << endl;
    cout << "Sexo              : " << sexo << endl;
    cout << "Deportista activo : " << boolalpha << haceDeporte << endl;
    cout << "Estatura (m)      : " << estaturaM << " m" << endl;
    cout << "IMC calculado     : " << imc << endl;

    return 0;
}
