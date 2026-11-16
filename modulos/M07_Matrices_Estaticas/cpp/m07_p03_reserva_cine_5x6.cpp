#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    // Matriz estatica de tamano fijo literal 5 filas x 6 columnas
    const int FILAS = 5;
    const int COLS = 6;
    char sala[5][6];

    // Inicializar todas las sillas como Libres ('L')
    for (int i = 0; i < FILAS; i++) {
        for (int j = 0; j < COLS; j++) {
            sala[i][j] = 'L';
        }
    }

    int opcion;
    do {
        cout << "\n=== SALA DE CINE 5x6 ===\n";
        cout << "1. Ver mapa de sillas\n";
        cout << "2. Reservar silla\n";
        cout << "3. Estadisticas de ocupacion\n";
        cout << "0. Salir\n";
        cout << "Opcion: ";
        if (!(cin >> opcion)) break;

        if (opcion == 1) {
            cout << "\n     ";
            for (int j = 0; j < COLS; j++) {
                cout << "C" << j << " ";
            }
            cout << "\n";
            for (int i = 0; i < FILAS; i++) {
                cout << "F" << i << " | ";
                for (int j = 0; j < COLS; j++) {
                    cout << " " << sala[i][j] << " ";
                }
                cout << "\n";
            }
        } else if (opcion == 2) {
            int f, c;
            cout << "Ingrese fila (0 a " << (FILAS - 1) << "): ";
            cin >> f;
            cout << "Ingrese columna (0 a " << (COLS - 1) << "): ";
            cin >> c;

            if (f < 0 || f >= FILAS || c < 0 || c >= COLS) {
                cout << "Error: coordenada fuera de la sala.\n";
            } else if (sala[f][c] == 'X') {
                cout << "Lo siento, la silla (" << f << ", " << c << ") ya esta ocupada.\n";
            } else {
                sala[f][c] = 'X';
                cout << "Reserva confirmada para silla (" << f << ", " << c << ").\n";
            }
        } else if (opcion == 3) {
            int ocupadas = 0;
            for (int i = 0; i < FILAS; i++) {
                for (int j = 0; j < COLS; j++) {
                    if (sala[i][j] == 'X') {
                        ocupadas++;
                    }
                }
            }
            int total = FILAS * COLS;
            int libres = total - ocupadas;
            double porcentaje = (static_cast<double>(ocupadas) / total) * 100.0;
            cout << fixed << setprecision(1);
            cout << "Ocupadas: " << ocupadas << " | Libres: " << libres
                 << " | Ocupacion: " << porcentaje << "%\n";
        } else if (opcion != 0) {
            cout << "Opcion invalida.\n";
        }
    } while (opcion != 0);

    return 0;
}
