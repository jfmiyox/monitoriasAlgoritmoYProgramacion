#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    const int MAX_F = 15;
    const int MAX_C = 15;
    int A[MAX_F][MAX_C];
    int T[MAX_C][MAX_F];
    int f, c;

    do {
        cout << "Filas F (1 a " << MAX_F << "): ";
        cin >> f;
    } while (f < 1 || f > MAX_F);

    do {
        cout << "Columnas C (1 a " << MAX_C << "): ";
        cin >> c;
    } while (c < 1 || c > MAX_C);

    for (int i = 0; i < f; i++) {
        for (int j = 0; j < c; j++) {
            cout << "A[" << i << "][" << j << "] = ";
            cin >> A[i][j];
        }
    }

    // Calcular transpuesta T de dimension C x F
    for (int i = 0; i < f; i++) {
        for (int j = 0; j < c; j++) {
            T[j][i] = A[i][j];
        }
    }

    cout << "\nMatriz original A (" << f << "x" << c << "):\n";
    for (int i = 0; i < f; i++) {
        for (int j = 0; j < c; j++) {
            cout << setw(5) << A[i][j];
        }
        cout << "\n";
    }

    cout << "\nMatriz transpuesta T (" << c << "x" << f << "):\n";
    for (int i = 0; i < c; i++) {
        for (int j = 0; j < f; j++) {
            cout << setw(5) << T[i][j];
        }
        cout << "\n";
    }

    // Verificar simetria solo si es cuadrada (f == c)
    if (f != c) {
        cout << "\nNo es cuadrada, por lo tanto NO puede ser simetrica.\n";
    } else {
        bool esSimetrica = true;
        for (int i = 0; i < f && esSimetrica; i++) {
            for (int j = i + 1; j < c; j++) {
                if (A[i][j] != A[j][i]) {
                    esSimetrica = false;
                    break;
                }
            }
        }
        if (esSimetrica) {
            cout << "\nLa matriz ES simetrica (A[i][j] == A[j][i]).\n";
        } else {
            cout << "\nLa matriz NO es simetrica.\n";
        }
    }

    return 0;
}
