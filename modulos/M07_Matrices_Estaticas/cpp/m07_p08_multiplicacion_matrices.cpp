#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    const int MAX = 15;
    int A[MAX][MAX];
    int B[MAX][MAX];
    int R[MAX][MAX] = {0};
    int f1, c1, f2, c2;

    do {
        cout << "Filas de A (1 a " << MAX << "): ";
        cin >> f1;
        cout << "Columnas de A (1 a " << MAX << "): ";
        cin >> c1;
    } while (f1 < 1 || f1 > MAX || c1 < 1 || c1 > MAX);

    do {
        cout << "Filas de B (1 a " << MAX << "): ";
        cin >> f2;
        cout << "Columnas de B (1 a " << MAX << "): ";
        cin >> c2;
    } while (f2 < 1 || f2 > MAX || c2 < 1 || c2 > MAX);

    if (c1 != f2) {
        cout << "\nError matematico: no se puede multiplicar A(" << f1 << "x" << c1
             << ") por B(" << f2 << "x" << c2 << ") porque c1 != f2.\n";
        return 0;
    }

    cout << "\nIngrese matriz A (" << f1 << "x" << c1 << "):\n";
    for (int i = 0; i < f1; i++) {
        for (int j = 0; j < c1; j++) {
            cout << "A[" << i << "][" << j << "] = ";
            cin >> A[i][j];
        }
    }

    cout << "\nIngrese matriz B (" << f2 << "x" << c2 << "):\n";
    for (int i = 0; i < f2; i++) {
        for (int j = 0; j < c2; j++) {
            cout << "B[" << i << "][" << j << "] = ";
            cin >> B[i][j];
        }
    }

    // Multiplicacion de matrices: R[i][j] = sumatoria A[i][k] * B[k][j]
    for (int i = 0; i < f1; i++) {
        for (int j = 0; j < c2; j++) {
            int suma = 0;
            for (int k = 0; k < c1; k++) {
                suma += A[i][k] * B[k][j];
            }
            R[i][j] = suma;
        }
    }

    cout << "\nMatriz resultado R = A x B (" << f1 << "x" << c2 << "):\n";
    for (int i = 0; i < f1; i++) {
        for (int j = 0; j < c2; j++) {
            cout << setw(6) << R[i][j];
        }
        cout << "\n";
    }

    return 0;
}
