#include <iostream>

using namespace std;

int main() {
    const int MAX = 50;
    int vec[MAX];
    int n;

    do {
        cout << "Cantidad de elementos (1 a " << MAX << "): ";
        cin >> n;
    } while (n < 1 || n > MAX);

    for (int i = 0; i < n; i++) {
        cout << "vec[" << i << "] = ";
        cin >> vec[i];
    }

    // 1. Verificar si es capicua (palindromo) comparando extremos
    bool esCapicua = true;
    for (int i = 0; i < n / 2; i++) {
        if (vec[i] != vec[n - 1 - i]) {
            esCapicua = false;
            break;
        }
    }

    cout << "\nArreglo original: [ ";
    for (int i = 0; i < n; i++) {
        cout << vec[i] << " ";
    }
    cout << "]\n";

    if (esCapicua) {
        cout << "Resultado: El arreglo ES capicua.\n";
    } else {
        cout << "Resultado: El arreglo NO es capicua.\n";
    }

    // 2. Invertir el arreglo in-place (sobre el mismo vector)
    for (int i = 0; i < n / 2; i++) {
        int aux = vec[i];
        vec[i] = vec[n - 1 - i];
        vec[n - 1 - i] = aux;
    }

    cout << "Arreglo invertido: [ ";
    for (int i = 0; i < n; i++) {
        cout << vec[i] << " ";
    }
    cout << "]\n";

    return 0;
}
