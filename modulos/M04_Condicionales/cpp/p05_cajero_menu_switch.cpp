// ============================================================================
// Modulo 04 - Problema Resuelto 05: Cajero Automatico (Una Operacion)
// Conceptos: switch-case con enteros, break obligatorio, default e if anidado
// Prueba sugerida: printf "500000\n3\n120000\n" | ./p05_cajero_menu_switch
// ============================================================================
#include <iomanip>
#include <iostream>
using namespace std;

int main() {
    double saldo = 0.0;
    double monto = 0.0;
    int opcion = 0;

    cout << "=== CAJERO AUTOMATICO (1 OPERACION) ===" << endl;
    cout << "Ingrese el saldo inicial de la cuenta: ";
    cin >> saldo;

    if (saldo < 0.0) {
        cout << "ERROR: El saldo inicial no puede ser negativo." << endl;
        return 0;
    }

    cout << "\n--- MENU DE OPERACIONES ---" << endl;
    cout << "1. Consultar saldo" << endl;
    cout << "2. Consignar dinero" << endl;
    cout << "3. Retirar dinero" << endl;
    cout << "4. Salir" << endl;
    cout << "Elija una opcion (1 a 4): ";
    cin >> opcion;

    cout << fixed << setprecision(2);

    switch (opcion) {
        case 1:
            cout << "Su saldo actual es: $" << saldo << endl;
            break; // Sin este break, caeria automaticamente dentro del case 2!

        case 2:
            cout << "Ingrese el monto a consignar: ";
            cin >> monto;
            if (monto > 0.0) {
                saldo = saldo + monto;
                cout << "Consignacion exitosa. Nuevo saldo: $" << saldo << endl;
            } else {
                cout << "ERROR: El monto a consignar debe ser mayor a cero." << endl;
            }
            break;

        case 3:
            cout << "Ingrese el monto a retirar: ";
            cin >> monto;
            if (monto <= 0.0) {
                cout << "ERROR: El monto a retirar debe ser mayor a cero." << endl;
            } else if (monto > saldo) {
                cout << "ERROR: Fondos insuficientes. Saldo disponible: $" << saldo << endl;
            } else {
                saldo = saldo - monto;
                cout << "Retiro exitoso. Nuevo saldo: $" << saldo << endl;
            }
            break;

        case 4:
            cout << "Gracias por usar nuestro cajero. Hasta pronto." << endl;
            break;

        default:
            cout << "ERROR: Opcion invalida. Debe elegir entre 1 y 4." << endl;
            break;
    }

    return 0;
}
