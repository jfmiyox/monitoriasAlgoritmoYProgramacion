#include <iostream>

using namespace std;

int main() {
    const int MAX = 30;
    int puntajes[MAX];
    int n;

    do {
        cout << "Cantidad de puntajes a ordenar (1 a " << MAX << "): ";
        cin >> n;
    } while (n < 1 || n > MAX);

    for (int i = 0; i < n; i++) {
        cout << "Puntaje[" << i << "]: ";
        cin >> puntajes[i];
    }

    cout << "\nEstado inicial: [ ";
    for (int i = 0; i < n; i++) {
        cout << puntajes[i] << " ";
    }
    cout << "]\n";

    // Ordenamiento Burbuja optimizado con bandera huboCambio
    for (int pasada = 0; pasada < n - 1; pasada++) {
        bool huboCambio = false;

        for (int j = 0; j < n - 1 - pasada; j++) {
            if (puntajes[j] > puntajes[j + 1]) {
                int aux = puntajes[j];
                puntajes[j] = puntajes[j + 1];
                puntajes[j + 1] = aux;
                huboCambio = true;
            }
        }

        cout << "Tras pasada " << (pasada + 1) << ": [ ";
        for (int i = 0; i < n; i++) {
            cout << puntajes[i] << " ";
        }
        cout << "]\n";

        if (!huboCambio) {
            cout << "Sin intercambios en esta pasada: el arreglo ya quedo ordenado.\n";
            break;
        }
    }

    cout << "\nOrdenado final: [ ";
    for (int i = 0; i < n; i++) {
        cout << puntajes[i] << " ";
    }
    cout << "]\n";

    return 0;
}
