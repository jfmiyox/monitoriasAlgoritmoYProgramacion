// ============================================================================
// Modulo 03 - Problema Resuelto 03: Promedio Ponderado con Nombre Completo
// Conceptos: string, getline(cin, ...), cin.ignore(), const double, setprecision
// Prueba sugerida: printf "2026101\nLaura Sofia Perez\n4.2\n3.8\n4.5\n" | ./bin
// ============================================================================
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main() {
    const double PESO_C1 = 0.30;
    const double PESO_C2 = 0.30;
    const double PESO_C3 = 0.40;

    int codigo = 0;
    string nombreCompleto;
    double nota1 = 0.0, nota2 = 0.0, nota3 = 0.0;

    cout << "=== CALCULO DE NOTA DEFINITIVA (30% + 30% + 40%) ===" << endl;
    cout << "Ingrese el codigo numerico del estudiante: ";
    cin >> codigo;

    // CLAVE: cin >> codigo deja el salto de linea '\n' en el buffer de entrada.
    // Si no llamamos cin.ignore(), getline() leeria una cadena vacia!
    cin.ignore();

    cout << "Ingrese el nombre completo del estudiante: ";
    getline(cin, nombreCompleto);

    cout << "Ingrese nota Corte 1 (0.0 a 5.0): ";
    cin >> nota1;
    cout << "Ingrese nota Corte 2 (0.0 a 5.0): ";
    cin >> nota2;
    cout << "Ingrese nota Corte 3 (0.0 a 5.0): ";
    cin >> nota3;

    double definitiva = (nota1 * PESO_C1) + (nota2 * PESO_C2) + (nota3 * PESO_C3);

    cout << "\n--- BOLETIN ACADEMICO ---" << endl;
    cout << "Codigo     : " << codigo << endl;
    cout << "Estudiante : " << nombreCompleto << endl;
    cout << fixed << setprecision(2);
    cout << "Definitiva : " << definitiva << endl;

    return 0;
}
