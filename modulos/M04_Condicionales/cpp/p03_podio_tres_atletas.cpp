// ============================================================================
// Modulo 04 - Problema Resuelto 03: Podio de Tres Atletas
// Conceptos: if anidados (arbol de decision), mayor, menor y analisis de empates
// Prueba sugerida: printf "9.5\n12.0\n9.5\n" | ./p03_podio_tres_atletas
// ============================================================================
#include <iomanip>
#include <iostream>
using namespace std;

int main() {
    double a = 0.0;
    double b = 0.0;
    double c = 0.0;
    double mayor = 0.0;
    double menor = 0.0;

    cout << "=== PODIO DE TRES ATLETAS ===" << endl;
    cout << "Ingrese el puntaje del atleta A: ";
    cin >> a;
    cout << "Ingrese el puntaje del atleta B: ";
    cin >> b;
    cout << "Ingrese el puntaje del atleta C: ";
    cin >> c;

    // Arbol de if anidados para hallar el MAYOR de los tres valores
    if (a >= b) {
        if (a >= c) {
            mayor = a;
        } else {
            mayor = c;
        }
    } else {
        if (b >= c) {
            mayor = b;
        } else {
            mayor = c;
        }
    }

    // Arbol de if anidados para hallar el MENOR de los tres valores
    if (a <= b) {
        if (a <= c) {
            menor = a;
        } else {
            menor = c;
        }
    } else {
        if (b <= c) {
            menor = b;
        } else {
            menor = c;
        }
    }

    cout << fixed << setprecision(2);
    cout << "\nMayor puntaje registrado: " << mayor << endl;
    cout << "Menor puntaje registrado: " << menor << endl;

    // Deteccion de empates con && y ||
    if (a == b && b == c) {
        cout << "Estado del podio: EMPATE TRIPLE (todos empatados en " << mayor << ")." << endl;
    } else if (a == b || a == c || b == c) {
        cout << "Estado del podio: EMPATE PARCIAL entre al menos dos atletas." << endl;
    } else {
        cout << "Estado del podio: Sin empates, los tres puntajes son distintos." << endl;
    }

    return 0;
}
