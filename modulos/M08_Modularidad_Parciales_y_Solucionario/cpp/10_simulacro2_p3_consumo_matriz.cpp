// ============================================================================
// Modulo 08 - Simulacro 2, Punto 3: Consumo Energetico por Pisos y Dias
// Temas Corte Final: Matriz estatica [MAX_P][MAX_D], recorrido filas/cols, &ref
// ============================================================================

#include <iostream>
#include <iomanip>
using namespace std;

const int MAX_P = 10;
const int MAX_D = 7;

void leerConsumos(double m[][MAX_D], int pisos, int dias);
void mostrarTabla(const double m[][MAX_D], int pisos, int dias);
double totalPorPiso(const double m[][MAX_D], int piso, int dias);
double promedioPorDia(const double m[][MAX_D], int pisos, int dia);
void encontrarPicoMaximo(const double m[][MAX_D], int pisos, int dias, int &pisoMax, int &diaMax);
double sumarDiagonalPrincipal(const double m[][MAX_D], int n);

int main() {
    double consumo[MAX_P][MAX_D] = {{0.0}};
    int p = 0, d = 0;

    cout << "=== MONITOR ENERGETICO DE EDIFICIO ===" << endl;
    do {
        cout << "Cantidad de pisos (1.." << MAX_P << "): ";
        if (!(cin >> p)) {
            return 0;
        }
    } while (p < 1 || p > MAX_P);

    do {
        cout << "Cantidad de dias registrados (1.." << MAX_D << "): ";
        if (!(cin >> d)) {
            return 0;
        }
    } while (d < 1 || d > MAX_D);

    leerConsumos(consumo, p, d);

    cout << "\n--- MATRIZ DE CONSUMO (kWh) ---\n";
    mostrarTabla(consumo, p, d);

    cout << fixed << setprecision(2);
    cout << "\nTotal acumulado por piso:\n";
    for (int i = 0; i < p; i++) {
        cout << "  Piso " << (i + 1) << ": " << totalPorPiso(consumo, i, d) << " kWh" << endl;
    }

    cout << "\nPromedio diario del edificio:\n";
    for (int j = 0; j < d; j++) {
        cout << "  Dia " << (j + 1) << ": " << promedioPorDia(consumo, p, j) << " kWh" << endl;
    }

    int pisoMax = 0, diaMax = 0;
    encontrarPicoMaximo(consumo, p, d, pisoMax, diaMax);
    cout << "\nPico maximo de consumo: " << consumo[pisoMax][diaMax]
         << " kWh (Piso " << (pisoMax + 1) << ", Dia " << (diaMax + 1) << ")" << endl;

    if (p == d) {
        cout << "Matriz cuadrada detectada => Suma diagonal principal: "
             << sumarDiagonalPrincipal(consumo, p) << " kWh" << endl;
    }

    return 0;
}

void leerConsumos(double m[][MAX_D], int pisos, int dias) {
    for (int i = 0; i < pisos; i++) {
        for (int j = 0; j < dias; j++) {
            do {
                cout << "  Piso " << (i + 1) << ", Dia " << (j + 1) << " (kWh >= 0): ";
                if (!(cin >> m[i][j])) {
                    m[i][j] = 0.0;
                    break;
                }
            } while (m[i][j] < 0.0);
        }
    }
}

void mostrarTabla(const double m[][MAX_D], int pisos, int dias) {
    cout << fixed << setprecision(1);
    cout << "        ";
    for (int j = 0; j < dias; j++) {
        cout << "     D" << (j + 1);
    }
    cout << endl;
    for (int i = 0; i < pisos; i++) {
        cout << "Piso " << setw(2) << (i + 1) << " ";
        for (int j = 0; j < dias; j++) {
            cout << setw(7) << m[i][j];
        }
        cout << endl;
    }
}

double totalPorPiso(const double m[][MAX_D], int piso, int dias) {
    double suma = 0.0;
    for (int j = 0; j < dias; j++) {
        suma += m[piso][j];
    }
    return suma;
}

double promedioPorDia(const double m[][MAX_D], int pisos, int dia) {
    double suma = 0.0;
    for (int i = 0; i < pisos; i++) {
        suma += m[i][dia];
    }
    return suma / pisos;
}

void encontrarPicoMaximo(const double m[][MAX_D], int pisos, int dias, int &pisoMax, int &diaMax) {
    pisoMax = 0;
    diaMax = 0;
    for (int i = 0; i < pisos; i++) {
        for (int j = 0; j < dias; j++) {
            if (m[i][j] > m[pisoMax][diaMax]) {
                pisoMax = i;
                diaMax = j;
            }
        }
    }
}

double sumarDiagonalPrincipal(const double m[][MAX_D], int n) {
    double suma = 0.0;
    for (int i = 0; i < n; i++) {
        suma += m[i][i];
    }
    return suma;
}
