// Modulo 02 - Ejemplo 06: Calculo de salario semanal con bonificacion
// Objetivo: Traducir un problema de nomina basica desde PSeInt a C++

#include <iostream>
using namespace std;

int main() {
    int horasTrabajadas;
    double pagoPorHora;
    double bonoFijo;
    double pagoBase;
    double salarioTotal;

    cout << "=== LIQUIDACION DE SALARIO SEMANAL ===" << endl;
    cout << "Ingresa las horas trabajadas en la semana: ";
    cin >> horasTrabajadas;

    cout << "Ingresa el valor pagado por hora: ";
    cin >> pagoPorHora;

    cout << "Ingresa el bono fijo de transporte: ";
    cin >> bonoFijo;

    pagoBase = horasTrabajadas * pagoPorHora;
    salarioTotal = pagoBase + bonoFijo;

    cout << "Pago por horas: $" << pagoBase << endl;
    cout << "Bono de transporte: $" << bonoFijo << endl;
    cout << "Salario total a recibir: $" << salarioTotal << endl;

    return 0;
}
