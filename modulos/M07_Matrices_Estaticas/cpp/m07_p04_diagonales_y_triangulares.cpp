#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    const int MAX = 15;
    int mat[MAX][MAX];
    int n;

    do {
        cout << "Dimension N de la matriz cuadrada NxN (1 a " << MAX << "): ";
        cin >> n;
    } while (n < 1 || n > MAX);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << "mat[" << i << "][" << j << "] = ";
            cin >> mat[i][j];
        }
    }

    cout << "\nMatriz ingresada:\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << setw(5) << mat[i][j];
        }
        cout << "\n";
    }

    int sumaDiagPrincipal = 0;
    int sumaDiagSecundaria = 0;
    int sumaTriangSup = 0; // Estrictamente encima: i < j
    int sumaTriangInf = 0; // Estrictamente debajo: i > j

    cout << "\nDiagonal principal (i == j): ";
    for (int i = 0; i < n; i++) {
        cout << mat[i][i] << " ";
        sumaDiagPrincipal += mat[i][i];
    }

    cout << "\nDiagonal secundaria (i + j == n - 1): ";
    for (int i = 0; i < n; i++) {
        cout << mat[i][n - 1 - i] << " ";
        sumaDiagSecundaria += mat[i][n - 1 - i];
    }
    cout << "\n";

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i < j) {
                sumaTriangSup += mat[i][j];
            } else if (i > j) {
                sumaTriangInf += mat[i][j];
            }
        }
    }

    cout << "Suma diagonal principal: " << sumaDiagPrincipal << "\n";
    cout << "Suma diagonal secundaria: " << sumaDiagSecundaria << "\n";
    cout << "Suma triangular superior (i < j): " << sumaTriangSup << "\n";
    cout << "Suma triangular inferior (i > j): " << sumaTriangInf << "\n";

    return 0;
}
