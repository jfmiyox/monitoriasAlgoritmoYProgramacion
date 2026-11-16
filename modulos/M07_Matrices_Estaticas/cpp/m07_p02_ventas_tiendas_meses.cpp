#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    const int MAX_TIENDAS = 15;
    const int MAX_MESES = 12;
    double ventas[MAX_TIENDAS][MAX_MESES];
    int t, m;

    do {
        cout << "Numero de tiendas (1 a " << MAX_TIENDAS << "): ";
        cin >> t;
    } while (t < 1 || t > MAX_TIENDAS);

    do {
        cout << "Numero de meses (1 a " << MAX_MESES << "): ";
        cin >> m;
    } while (m < 1 || m > MAX_MESES);

    for (int i = 0; i < t; i++) {
        for (int j = 0; j < m; j++) {
            do {
                cout << "Ventas tienda " << i << ", mes " << j << " (>= 0): ";
                cin >> ventas[i][j];
            } while (ventas[i][j] < 0.0);
        }
    }

    // Total global y tienda con mayor venta acumulada (suma por filas)
    double totalGlobal = 0.0;
    double maxVentaTienda = -1.0;
    int mejorTienda = 0;

    cout << fixed << setprecision(2);
    cout << "\n--- VENTAS POR TIENDA ---\n";
    for (int i = 0; i < t; i++) {
        double sumaTienda = 0.0;
        for (int j = 0; j < m; j++) {
            sumaTienda += ventas[i][j];
            totalGlobal += ventas[i][j];
        }
        cout << "Tienda " << i << ": $" << sumaTienda << "\n";
        if (i == 0 || sumaTienda > maxVentaTienda) {
            maxVentaTienda = sumaTienda;
            mejorTienda = i;
        }
    }

    // Mes con menor venta total (suma por columnas)
    double minVentaMes = 0.0;
    int peorMes = 0;

    cout << "\n--- VENTAS POR MES ---\n";
    for (int j = 0; j < m; j++) {
        double sumaMes = 0.0;
        for (int i = 0; i < t; i++) {
            sumaMes += ventas[i][j];
        }
        cout << "Mes " << j << ": $" << sumaMes << "\n";
        if (j == 0 || sumaMes < minVentaMes) {
            minVentaMes = sumaMes;
            peorMes = j;
        }
    }

    cout << "\nTotal global de la cadena: $" << totalGlobal << "\n";
    cout << "Tienda lider: Tienda " << mejorTienda << " con $" << maxVentaTienda << "\n";
    cout << "Mes de menor venta: Mes " << peorMes << " con $" << minVentaMes << "\n";

    return 0;
}
