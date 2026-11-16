#include <iomanip>
#include <iostream>

using namespace std;

int main() {
    int n = 0;
    bool entradaOk = true;

    cout << "=== REGISTRO DE NOTAS CON VALIDACION ===" << endl;

    // En PSeInt: Repetir ... Hasta Que n >= 1 (termina cuando es VERDADERO)
    // En C++:    do { ... } while (n < 1);    (continua mientras es VERDADERO)
    do {
        cout << "Cuantos estudiantes hay en el grupo? (>= 1): ";
        if (!(cin >> n)) {
            entradaOk = false;
            break;
        }
        if (n < 1) {
            cout << "Error: debe haber al menos 1 estudiante." << endl;
        }
    } while (n < 1);

    if (!entradaOk) {
        return 0;
    }

    double sumaNotas = 0.0;
    int aprobados = 0;
    int reprobados = 0;

    for (int i = 1; i <= n; i++) {
        double nota = 0.0;
        do {
            cout << "Nota del estudiante " << i << " (0.0 a 5.0): ";
            if (!(cin >> nota)) {
                entradaOk = false;
                break;
            }
            if (nota < 0.0 || nota > 5.0) {
                cout << "Nota invalida. Debe estar entre 0.0 y 5.0." << endl;
            }
        } while (nota < 0.0 || nota > 5.0);

        if (!entradaOk) {
            break;
        }

        sumaNotas += nota;
        if (nota >= 3.0) {
            aprobados++;
        } else {
            reprobados++;
        }
    }

    int procesados = aprobados + reprobados;
    cout << fixed << setprecision(2);
    cout << "\n=== REPORTE DEL GRUPO ===" << endl;
    if (procesados == 0) {
        cout << "No se completaron registros." << endl;
    } else {
        cout << "Estudiantes procesados: " << procesados << endl;
        cout << "Aprobados (>= 3.0):     " << aprobados << endl;
        cout << "Reprobados (< 3.0):     " << reprobados << endl;
        cout << "Promedio del grupo:     " << (sumaNotas / procesados) << endl;
    }

    return 0;
}
