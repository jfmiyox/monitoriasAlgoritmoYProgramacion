#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    const int MAX_F = 20;
    const int MAX_C = 20;
    int mat[MAX_F][MAX_C];
    int f, c;

    do {
        cout << "Filas (1 a " << MAX_F << "): ";
        cin >> f;
    } while (f < 1 || f > MAX_F);

    do {
        cout << "Columnas (1 a " << MAX_C << "): ";
        cin >> c;
    } while (c < 1 || c > MAX_C);

    for (int i = 0; i < f; i++) {
        for (int j = 0; j < c; j++) {
            cout << "mat[" << i << "][" << j << "] = ";
            cin >> mat[i][j];
        }
    }

    int objetivo;
    cout << "Numero a buscar en la matriz: ";
    cin >> objetivo;

    // 1. Busqueda exhaustiva de coordenadas
    int apariciones = 0;
    cout << "\nCoordenadas encontradas:\n";
    for (int i = 0; i < f; i++) {
        for (int j = 0; j < c; j++) {
            if (mat[i][j] == objetivo) {
                cout << " => (" << i << ", " << j << ")\n";
                apariciones++;
            }
        }
    }
    if (apariciones == 0) {
        cout << "El valor " << objetivo << " no aparece en la matriz.\n";
    } else {
        cout << "Total de apariciones: " << apariciones << "\n";
    }

    // 2. Hallar fila del elemento menor global e intercambiarla con la fila 0
    int menor = mat[0][0];
    int filaMenor = 0;
    int colMenor = 0;

    for (int i = 0; i < f; i++) {
        for (int j = 0; j < c; j++) {
            if (mat[i][j] < menor) {
                menor = mat[i][j];
                filaMenor = i;
                colMenor = j;
            }
        }
    }

    cout << "\nMenor global: " << menor << " en (" << filaMenor << ", " << colMenor << ").\n";
    if (filaMenor != 0) {
        for (int j = 0; j < c; j++) {
            int aux = mat[0][j];
            mat[0][j] = mat[filaMenor][j];
            mat[filaMenor][j] = aux;
        }
        cout << "Se intercambio la fila " << filaMenor << " con la fila 0.\n";
    } else {
        cout << "El menor ya estaba en la fila 0, no hace falta intercambiar.\n";
    }

    cout << "\nMatriz resultante:\n";
    for (int i = 0; i < f; i++) {
        for (int j = 0; j < c; j++) {
            cout << setw(5) << mat[i][j];
        }
        cout << "\n";
    }

    return 0;
}
