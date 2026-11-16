// ============================================================================
// Modulo 08 - Simulacro 2, Punto 2: Gestion de Inventario (Vectores Estaticos)
// Temas Corte Final: Vectores paralelos estaticos, busqueda, burbuja, funciones
// ============================================================================

#include <iostream>
#include <iomanip>
using namespace std;

const int MAX_PROD = 50;

void cargarInventario(int cod[], int stock[], double precio[], int n);
void mostrarInventario(const int cod[], const int stock[], const double precio[], int n);
int buscarPorCodigo(const int cod[], int n, int objetivo);
int indiceMasCaro(const double precio[], int n);
int contarStockCritico(const int stock[], int n, int umbral);
void ordenarPorPrecioDesc(int cod[], int stock[], double precio[], int n);

int main() {
    int codigos[MAX_PROD] = {0};
    int stocks[MAX_PROD] = {0};
    double precios[MAX_PROD] = {0.0};
    int n = 0;

    cout << "=== INVENTARIO DE TIENDA (Capacidad MAX = " << MAX_PROD << ") ===" << endl;
    do {
        cout << "Cantidad de productos a registrar (1.." << MAX_PROD << "): ";
        if (!(cin >> n)) {
            return 0;
        }
    } while (n < 1 || n > MAX_PROD);

    cargarInventario(codigos, stocks, precios, n);

    cout << "\n--- LISTADO INICIAL ---\n";
    mostrarInventario(codigos, stocks, precios, n);

    int posCaro = indiceMasCaro(precios, n);
    cout << fixed << setprecision(2);
    cout << "\nProducto mas costoso => Codigo: " << codigos[posCaro]
         << " | Precio: $" << precios[posCaro] << endl;

    cout << "Productos con stock critico (< 5 unidades): "
         << contarStockCritico(stocks, n, 5) << endl;

    int codBuscado = 0;
    cout << "\nIngrese codigo a consultar: ";
    cin >> codBuscado;
    int pos = buscarPorCodigo(codigos, n, codBuscado);
    if (pos != -1) {
        cout << "Encontrado => Stock: " << stocks[pos]
             << " | Precio: $" << precios[pos] << endl;
    } else {
        cout << "Codigo " << codBuscado << " no encontrado." << endl;
    }

    ordenarPorPrecioDesc(codigos, stocks, precios, n);
    cout << "\n--- INVENTARIO ORDENADO POR PRECIO (MAYOR A MENOR) ---\n";
    mostrarInventario(codigos, stocks, precios, n);

    return 0;
}

void cargarInventario(int cod[], int stock[], double precio[], int n) {
    for (int i = 0; i < n; i++) {
        cout << "\nProducto #" << (i + 1) << ":" << endl;
        cout << "  Codigo entero: ";
        cin >> cod[i];
        do {
            cout << "  Stock (>= 0): ";
            if (!(cin >> stock[i])) {
                stock[i] = 0;
                break;
            }
        } while (stock[i] < 0);
        do {
            cout << "  Precio unitario (> 0): ";
            if (!(cin >> precio[i])) {
                precio[i] = 1.0;
                break;
            }
        } while (precio[i] <= 0.0);
    }
}

void mostrarInventario(const int cod[], const int stock[], const double precio[], int n) {
    cout << fixed << setprecision(2);
    cout << left << setw(10) << "CODIGO" << setw(10) << "STOCK" << "PRECIO" << endl;
    cout << "------------------------------" << endl;
    for (int i = 0; i < n; i++) {
        cout << left << setw(10) << cod[i]
             << setw(10) << stock[i]
             << "$" << precio[i] << endl;
    }
}

int buscarPorCodigo(const int cod[], int n, int objetivo) {
    for (int i = 0; i < n; i++) {
        if (cod[i] == objetivo) {
            return i;
        }
    }
    return -1;
}

int indiceMasCaro(const double precio[], int n) {
    int posMax = 0;
    for (int i = 1; i < n; i++) {
        if (precio[i] > precio[posMax]) {
            posMax = i;
        }
    }
    return posMax;
}

int contarStockCritico(const int stock[], int n, int umbral) {
    int cont = 0;
    for (int i = 0; i < n; i++) {
        if (stock[i] < umbral) {
            cont++;
        }
    }
    return cont;
}

void ordenarPorPrecioDesc(int cod[], int stock[], double precio[], int n) {
    for (int pasada = 0; pasada < n - 1; pasada++) {
        for (int j = 0; j < n - 1 - pasada; j++) {
            if (precio[j] < precio[j + 1]) {
                // Al intercambiar en arreglos paralelos, debemos mover LOS TRES juntos
                double tmpPrecio = precio[j];
                precio[j] = precio[j + 1];
                precio[j + 1] = tmpPrecio;

                int tmpCod = cod[j];
                cod[j] = cod[j + 1];
                cod[j + 1] = tmpCod;

                int tmpStock = stock[j];
                stock[j] = stock[j + 1];
                stock[j + 1] = tmpStock;
            }
        }
    }
}
