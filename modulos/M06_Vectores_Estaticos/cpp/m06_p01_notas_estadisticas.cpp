#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    // Capacidad maxima fija en memoria estatica (NO tamano variable en declaracion)
    const int MAX = 50;
    double notas[MAX];
    int n;

    // 1. Validar tamano logico n dentro de [1, MAX]
    do {
        cout << "Ingrese cantidad de estudiantes (1 a " << MAX << "): ";
        cin >> n;
        if (n < 1 || n > MAX) {
            cout << "Error: la cantidad debe estar entre 1 y " << MAX << ".\n";
        }
    } while (n < 1 || n > MAX);

    // 2. Lectura de notas (indices en C++: 0 hasta n - 1)
    for (int i = 0; i < n; i++) {
        do {
            cout << "Nota del estudiante [" << i << "] (0.0 a 5.0): ";
            cin >> notas[i];
            if (notas[i] < 0.0 || notas[i] > 5.0) {
                cout << "Error: ingrese una nota valida entre 0.0 y 5.0.\n";
            }
        } while (notas[i] < 0.0 || notas[i] > 5.0);
    }

    // 3. Calculo de suma, promedio, aprobados, mayor y menor con su posicion
    double suma = 0.0;
    int aprobados = 0;
    double mayor = notas[0];
    double menor = notas[0];
    int posMayor = 0;
    int posMenor = 0;

    for (int i = 0; i < n; i++) {
        suma += notas[i];
        if (notas[i] >= 3.0) {
            aprobados++;
        }
        if (notas[i] > mayor) {
            mayor = notas[i];
            posMayor = i;
        }
        if (notas[i] < menor) {
            menor = notas[i];
            posMenor = i;
        }
    }

    double promedio = suma / n;

    // 4. Salida formateada
    cout << fixed << setprecision(2);
    cout << "\n--- RESUMEN DEL GRUPO ---\n";
    cout << "Promedio general: " << promedio << "\n";
    cout << "Mayor nota: " << mayor << " (indice " << posMayor << ")\n";
    cout << "Menor nota: " << menor << " (indice " << posMenor << ")\n";
    cout << "Aprobados (>= 3.0): " << aprobados << " de " << n << "\n";

    return 0;
}
