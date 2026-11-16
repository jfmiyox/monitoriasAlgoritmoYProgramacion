#include <iostream>

using namespace std;

int main() {
    const int MAX = 30;
    int A[MAX];
    int B[MAX];
    int C[2 * MAX];
    int nA, nB;

    do {
        cout << "Tamano de A ordenado (1 a " << MAX << "): ";
        cin >> nA;
    } while (nA < 1 || nA > MAX);

    cout << "Ingrese los " << nA << " elementos de A en orden ascendente:\n";
    for (int i = 0; i < nA; i++) {
        cout << "A[" << i << "] = ";
        cin >> A[i];
    }

    do {
        cout << "Tamano de B ordenado (1 a " << MAX << "): ";
        cin >> nB;
    } while (nB < 1 || nB > MAX);

    cout << "Ingrese los " << nB << " elementos de B en orden ascendente:\n";
    for (int i = 0; i < nB; i++) {
        cout << "B[" << i << "] = ";
        cin >> B[i];
    }

    // Mezcla (merge) en una sola pasada
    int i = 0, j = 0, k = 0;
    while (i < nA && j < nB) {
        if (A[i] <= B[j]) {
            C[k] = A[i];
            i++;
        } else {
            C[k] = B[j];
            j++;
        }
        k++;
    }

    // Copiar elementos sobrantes de A (si quedan)
    while (i < nA) {
        C[k] = A[i];
        i++;
        k++;
    }

    // Copiar elementos sobrantes de B (si quedan)
    while (j < nB) {
        C[k] = B[j];
        j++;
        k++;
    }

    int nC = k; // Equivale a nA + nB
    cout << "\nVector fusionado C (" << nC << " elementos): [ ";
    for (int idx = 0; idx < nC; idx++) {
        cout << C[idx] << " ";
    }
    cout << "]\n";

    return 0;
}
