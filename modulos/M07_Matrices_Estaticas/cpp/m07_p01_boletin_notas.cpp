#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    // Matriz estatica con capacidad fija definida por constantes
    const int MAX_EST = 30;
    const int MAX_MAT = 10;
    double notas[MAX_EST][MAX_MAT];
    int f, c; // f = estudiantes, c = materias

    do {
        cout << "Cantidad de estudiantes (1 a " << MAX_EST << "): ";
        cin >> f;
    } while (f < 1 || f > MAX_EST);

    do {
        cout << "Cantidad de materias (1 a " << MAX_MAT << "): ";
        cin >> c;
    } while (c < 1 || c > MAX_MAT);

    // 1. Lectura por filas (estudiante por estudiante)
    for (int i = 0; i < f; i++) {
        cout << "\n--- Estudiante " << i << " ---\n";
        for (int j = 0; j < c; j++) {
            do {
                cout << "  Nota materia [" << j << "] (0.0 a 5.0): ";
                cin >> notas[i][j];
            } while (notas[i][j] < 0.0 || notas[i][j] > 5.0);
        }
    }

    cout << fixed << setprecision(2);

    // 2. Promedio por estudiante: Recorrido POR FILAS (for i, luego for j)
    cout << "\n=== PROMEDIO POR ESTUDIANTE ===\n";
    for (int i = 0; i < f; i++) {
        double sumaEst = 0.0; // Reiniciar acumulador para cada fila!
        for (int j = 0; j < c; j++) {
            sumaEst += notas[i][j];
        }
        cout << "Estudiante " << i << ": " << (sumaEst / c) << "\n";
    }

    // 3. Promedio por materia: Recorrido POR COLUMNAS (for j, luego for i)
    cout << "\n=== PROMEDIO POR MATERIA ===\n";
    for (int j = 0; j < c; j++) {
        double sumaMat = 0.0; // Reiniciar acumulador para cada columna!
        for (int i = 0; i < f; i++) {
            sumaMat += notas[i][j];
        }
        cout << "Materia " << j << ": " << (sumaMat / f) << "\n";
    }

    // 4. Mayor nota global con sus coordenadas (fila, col)
    double mayor = notas[0][0];
    int filaMayor = 0;
    int colMayor = 0;

    for (int i = 0; i < f; i++) {
        for (int j = 0; j < c; j++) {
            if (notas[i][j] > mayor) {
                mayor = notas[i][j];
                filaMayor = i;
                colMayor = j;
            }
        }
    }

    cout << "\nMejor nota del curso: " << mayor
         << " en coordenadas (estudiante=" << filaMayor
         << ", materia=" << colMayor << ")\n";

    return 0;
}
