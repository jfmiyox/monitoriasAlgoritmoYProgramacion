// ============================================================================
// Modulo 04 - Problema Resuelto 02: Filtro de Beca Universitaria
// Conceptos: Logica booleana (&&, ||, !) y validacion de rangos A <= x && x <= B
// Prueba sugerida: printf "20\n4.6\n2\n0\n" | ./p02_beca_universitaria_rangos
// ============================================================================
#include <iostream>
using namespace std;

int main() {
    int edad = 0;
    double promedio = 0.0;
    int estrato = 0;
    int sancionInput = 0;

    cout << "=== FILTRO DE BECA UNIVERSITARIA ===" << endl;
    cout << "Edad del estudiante (15 a 80): ";
    cin >> edad;
    cout << "Promedio acumulado (0.0 a 5.0): ";
    cin >> promedio;
    cout << "Estrato socioeconomico (1 a 6): ";
    cin >> estrato;
    cout << "Tiene sancion disciplinaria vigente? (1 = Si, 0 = No): ";
    cin >> sancionInput;

    // Trampa evitada: en C++ SIEMPRE se escribe (A <= x && x <= B), nunca (A <= x <= B)
    bool edadValida = (15 <= edad && edad <= 80);
    bool promedioValido = (0.0 <= promedio && promedio <= 5.0);
    bool estratoValido = (1 <= estrato && estrato <= 6);
    bool sancionValida = (sancionInput == 0 || sancionInput == 1);

    bool datosValidos = edadValida && promedioValido && estratoValido && sancionValida;

    if (!datosValidos) {
        cout << "ERROR: Datos fuera de rango permitido." << endl;
        if (!edadValida) {
            cout << "  - La edad debe estar entre 15 y 80." << endl;
        }
        if (!promedioValido) {
            cout << "  - El promedio debe estar entre 0.0 y 5.0." << endl;
        }
        if (!estratoValido) {
            cout << "  - El estrato debe estar entre 1 y 6." << endl;
        }
        if (!sancionValida) {
            cout << "  - El indicador de sancion debe ser 0 o 1." << endl;
        }
        return 0;
    }

    bool tieneSancion = (sancionInput == 1);

    if (tieneSancion) {
        cout << "RESULTADO: Beca RECHAZADA por sancion disciplinaria vigente." << endl;
    } else if (promedio >= 4.5 && (estrato == 1 || estrato == 2)) {
        cout << "RESULTADO: Beca COMPLETA (100% de la matricula)." << endl;
    } else if (promedio >= 4.0 && estrato <= 3) {
        cout << "RESULTADO: MEDIA Beca (50% de la matricula)." << endl;
    } else if (promedio >= 4.7) {
        cout << "RESULTADO: Bono de EXCELENCIA ACADEMICA (25%)." << endl;
    } else {
        cout << "RESULTADO: No cumple los requisitos de promedio o estrato." << endl;
    }

    return 0;
}
