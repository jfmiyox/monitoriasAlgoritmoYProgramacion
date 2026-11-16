#include <iostream>

using namespace std;

int main() {
    const int MAX = 10;
    int lista[MAX] = {0};
    int n;

    do {
        cout << "Cantidad inicial de elementos (0 a " << MAX << "): ";
        cin >> n;
    } while (n < 0 || n > MAX);

    for (int i = 0; i < n; i++) {
        cout << "Elemento[" << i << "]: ";
        cin >> lista[i];
    }

    int opcion;
    do {
        cout << "\n--- GESTOR DE LISTA ESTATICA (" << n << "/" << MAX << " usados) ---\n";
        cout << "1. Mostrar arreglo\n";
        cout << "2. Insertar en posicion\n";
        cout << "3. Eliminar de posicion\n";
        cout << "0. Salir\n";
        cout << "Opcion: ";
        if (!(cin >> opcion)) break;

        if (opcion == 1) {
            if (n == 0) {
                cout << "Lista vacia.\n";
            } else {
                cout << "Lista: [ ";
                for (int i = 0; i < n; i++) {
                    cout << lista[i] << " ";
                }
                cout << "]\n";
            }
        } else if (opcion == 2) {
            if (n == MAX) {
                cout << "No se puede insertar: el arreglo alcanzo su capacidad MAX (" << MAX << ").\n";
            } else {
                int pos, valor;
                cout << "Posicion a insertar (0 a " << n << "): ";
                cin >> pos;
                if (pos < 0 || pos > n) {
                    cout << "Posicion invalida.\n";
                } else {
                    cout << "Valor entero a insertar: ";
                    cin >> valor;
                    // Desplazar a la derecha desde n hacia pos + 1
                    for (int i = n; i > pos; i--) {
                        lista[i] = lista[i - 1];
                    }
                    lista[pos] = valor;
                    n++;
                    cout << "Insertado correctamente.\n";
                }
            }
        } else if (opcion == 3) {
            if (n == 0) {
                cout << "No se puede eliminar: la lista esta vacia.\n";
            } else {
                int pos;
                cout << "Posicion a eliminar (0 a " << (n - 1) << "): ";
                cin >> pos;
                if (pos < 0 || pos >= n) {
                    cout << "Posicion invalida.\n";
                } else {
                    int eliminado = lista[pos];
                    // Desplazar a la izquierda desde pos hasta n - 2
                    for (int i = pos; i < n - 1; i++) {
                        lista[i] = lista[i + 1];
                    }
                    n--;
                    cout << "Elemento " << eliminado << " eliminado.\n";
                }
            }
        } else if (opcion != 0) {
            cout << "Opcion no reconocida.\n";
        }
    } while (opcion != 0);

    return 0;
}
