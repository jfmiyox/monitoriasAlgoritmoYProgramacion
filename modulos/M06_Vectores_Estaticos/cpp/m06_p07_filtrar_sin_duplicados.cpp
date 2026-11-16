#include <iostream>

using namespace std;

int main() {
    const int MAX = 50;
    int datos[MAX];
    int unicos[MAX];
    int conteo[MAX] = {0};
    int n;
    int m = 0; // Tamano logico de unicos y conteo

    do {
        cout << "Cantidad de datos (1 a " << MAX << "): ";
        cin >> n;
    } while (n < 1 || n > MAX);

    for (int i = 0; i < n; i++) {
        cout << "datos[" << i << "] = ";
        cin >> datos[i];
    }

    // Recorrer datos y verificar si ya fue registrado en unicos
    for (int i = 0; i < n; i++) {
        int posEncontrado = -1;
        for (int j = 0; j < m; j++) {
            if (unicos[j] == datos[i]) {
                posEncontrado = j;
                break;
            }
        }

        if (posEncontrado != -1) {
            conteo[posEncontrado]++;
        } else {
            unicos[m] = datos[i];
            conteo[m] = 1;
            m++;
        }
    }

    cout << "\n--- VALORES UNICOS Y FRECUENCIAS ---\n";
    for (int j = 0; j < m; j++) {
        cout << "Valor " << unicos[j] << " aparece " << conteo[j] << " vez/veces.\n";
    }

    return 0;
}
