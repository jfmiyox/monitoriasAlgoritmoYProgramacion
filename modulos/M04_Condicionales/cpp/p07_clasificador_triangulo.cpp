// ============================================================================
// Modulo 04 - Problema Resuelto 07: Existencia y Clasificacion de Triangulo
// Conceptos: Validacion con &&, clasificacion con ||, Pitagoras con tolerancia
// Prueba sugerida: printf "3\n4\n5\n" | ./p07_clasificador_triangulo
// ============================================================================
#include <cmath>
#include <iostream>
using namespace std;

int main() {
    const double EPS = 1e-6;
    double a = 0.0;
    double b = 0.0;
    double c = 0.0;

    cout << "=== CLASIFICADOR DE TRIANGULOS ===" << endl;
    cout << "Ingrese lado a: ";
    cin >> a;
    cout << "Ingrese lado b: ";
    cin >> b;
    cout << "Ingrese lado c: ";
    cin >> c;

    if (a <= 0.0 || b <= 0.0 || c <= 0.0) {
        cout << "ERROR: Todos los lados deben ser estrictamente positivos (> 0)." << endl;
        return 0;
    }

    // Desigualdad triangular: la suma de dos lados siempre debe superar al tercero
    bool existeTriangulo = (a + b > c) && (a + c > b) && (b + c > a);
    if (!existeTriangulo) {
        cout << "NO EXISTE: Los lados no cumplen la desigualdad triangular." << endl;
        return 0;
    }

    // 1) Clasificacion segun la longitud de sus lados
    if (a == b && b == c) {
        cout << "Tipo por lados : EQUILATERO (tres lados iguales)." << endl;
    } else if (a == b || a == c || b == c) {
        cout << "Tipo por lados : ISOSCELES (dos lados iguales)." << endl;
    } else {
        cout << "Tipo por lados : ESCALENO (todos los lados distintos)." << endl;
    }

    // 2) Verificacion de triangulo rectangulo usando tolerancia flotante
    bool rectA = fabs((b * b + c * c) - (a * a)) < EPS;
    bool rectB = fabs((a * a + c * c) - (b * b)) < EPS;
    bool rectC = fabs((a * a + b * b) - (c * c)) < EPS;

    if (rectA || rectB || rectC) {
        cout << "Angulo recto   : SI es un triangulo RECTANGULO." << endl;
    } else {
        cout << "Angulo recto   : NO es un triangulo rectangulo." << endl;
    }

    return 0;
}
