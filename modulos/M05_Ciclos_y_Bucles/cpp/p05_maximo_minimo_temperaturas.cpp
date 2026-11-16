#include <iomanip>
#include <iostream>

using namespace std;

int main() {
    double temp = 0.0;
    double mayor = 0.0;
    double menor = 0.0;
    double suma = 0.0;
    int diaMayor = 0;
    int diaMenor = 0;
    int contador = 0;
    bool esPrimero = true;

    cout << "=== MAXIMO Y MINIMO DE TEMPERATURAS (CENTINELA -999) ===" << endl;
    cout << "Ingrese temperatura del dia 1 (-999 para terminar): ";
    if (!(cin >> temp)) {
        return 0;
    }

    while (temp != -999.0) {
        contador++;
        suma += temp;

        // Tecnica de la bandera esPrimero: funciona incluso con todos negativos
        if (esPrimero) {
            mayor = temp;
            menor = temp;
            diaMayor = contador;
            diaMenor = contador;
            esPrimero = false;
        } else {
            if (temp > mayor) {
                mayor = temp;
                diaMayor = contador;
            }
            if (temp < menor) {
                menor = temp;
                diaMenor = contador;
            }
        }

        cout << "Ingrese temperatura del dia " << (contador + 1) << " (-999 para terminar): ";
        if (!(cin >> temp)) {
            break;
        }
    }

    cout << fixed << setprecision(2);
    cout << "\n=== ESTADISTICAS TERMOMETRICAS ===" << endl;
    if (esPrimero) {
        cout << "No se ingresaron temperaturas." << endl;
    } else {
        cout << "Dias registrados: " << contador << endl;
        cout << "Temperatura maxima: " << mayor << " C (dia " << diaMayor << ")" << endl;
        cout << "Temperatura minima: " << menor << " C (dia " << diaMenor << ")" << endl;
        cout << "Promedio general:   " << (suma / contador) << " C" << endl;
    }

    return 0;
}
