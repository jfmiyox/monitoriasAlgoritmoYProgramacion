#include <iostream>

using namespace std;

int main() {
    const int MAX = 30;
    int turnos[MAX];
    int n;

    do {
        cout << "Cantidad de turnos (1 a " << MAX << "): ";
        cin >> n;
    } while (n < 1 || n > MAX);

    for (int i = 0; i < n; i++) {
        cout << "Turno[" << i << "]: ";
        cin >> turnos[i];
    }

    int direccion;
    do {
        cout << "Direccion de rotacion (1 = Izquierda, 2 = Derecha): ";
        cin >> direccion;
    } while (direccion != 1 && direccion != 2);

    int k;
    do {
        cout << "Cuantas posiciones rotar (>= 0): ";
        cin >> k;
    } while (k < 0);

    cout << "\nAntes:   [ ";
    for (int i = 0; i < n; i++) {
        cout << turnos[i] << " ";
    }
    cout << "]\n";

    // Evitar vueltas completas innecesarias
    int pasos = k % n;

    if (direccion == 1) {
        // Rotar a la izquierda: el primero pasa al final
        for (int p = 0; p < pasos; p++) {
            int primero = turnos[0];
            for (int i = 0; i < n - 1; i++) {
                turnos[i] = turnos[i + 1];
            }
            turnos[n - 1] = primero;
        }
    } else {
        // Rotar a la derecha: el ultimo pasa al inicio
        for (int p = 0; p < pasos; p++) {
            int ultimo = turnos[n - 1];
            for (int i = n - 1; i > 0; i--) {
                turnos[i] = turnos[i - 1];
            }
            turnos[0] = ultimo;
        }
    }

    cout << "Despues: [ ";
    for (int i = 0; i < n; i++) {
        cout << turnos[i] << " ";
    }
    cout << "]\n";

    return 0;
}
