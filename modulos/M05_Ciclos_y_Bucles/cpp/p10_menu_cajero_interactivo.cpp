#include <iomanip>
#include <iostream>

using namespace std;

int main() {
    double saldo = 100000.0;
    double totalConsignado = 0.0;
    double totalRetirado = 0.0;
    int operacionesExitosas = 0;
    int opcion = 0;

    cout << fixed << setprecision(2);
    cout << "=== CAJERO AUTOMATICO (MENU DO-WHILE + SWITCH) ===" << endl;

    // El menu debe mostrarse al menos 1 vez => do-while
    // En C++ continua mientras opcion != 4 (en PSeInt: Hasta Que opcion = 4)
    do {
        cout << "\n--- MENU PRINCIPAL ---" << endl;
        cout << "1. Consultar saldo" << endl;
        cout << "2. Consignar dinero" << endl;
        cout << "3. Retirar dinero" << endl;
        cout << "4. Salir" << endl;
        cout << "Elija una opcion (1-4): ";

        if (!(cin >> opcion)) {
            cout << "\nFin de entrada detectado. Cerrando sesion." << endl;
            break;
        }

        switch (opcion) {
            case 1:
                cout << "Saldo actual disponible: $" << saldo << endl;
                break;

            case 2: {
                double monto = 0.0;
                cout << "Ingrese monto a consignar: $";
                if (!(cin >> monto)) {
                    opcion = 4;
                    break;
                }
                if (monto <= 0.0) {
                    cout << "Error: el monto a consignar debe ser positivo." << endl;
                } else {
                    saldo += monto;
                    totalConsignado += monto;
                    operacionesExitosas++;
                    cout << "Consignacion exitosa. Nuevo saldo: $" << saldo << endl;
                }
                break;
            }

            case 3: {
                double monto = 0.0;
                cout << "Ingrese monto a retirar: $";
                if (!(cin >> monto)) {
                    opcion = 4;
                    break;
                }
                if (monto <= 0.0) {
                    cout << "Error: el monto a retirar debe ser positivo." << endl;
                } else if (monto > saldo) {
                    cout << "Fondos insuficientes. Saldo disponible: $" << saldo << endl;
                } else {
                    saldo -= monto;
                    totalRetirado += monto;
                    operacionesExitosas++;
                    cout << "Retiro exitoso. Nuevo saldo: $" << saldo << endl;
                }
                break;
            }

            case 4:
                cout << "Saliendo del cajero..." << endl;
                break;

            default:
                cout << "Opcion invalida. Por favor elija entre 1 y 4." << endl;
                break;
        }
    } while (opcion != 4);

    cout << "\n=== RESUMEN DE SESION ===" << endl;
    cout << "Transacciones monetarias exitosas: " << operacionesExitosas << endl;
    cout << "Total consignado: $" << totalConsignado << endl;
    cout << "Total retirado:   $" << totalRetirado << endl;
    cout << "Saldo final:      $" << saldo << endl;

    return 0;
}
