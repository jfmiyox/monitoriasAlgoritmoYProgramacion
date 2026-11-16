// ============================================================================
// Modulo 08 - Ejemplo 02: Paso por Valor vs Paso por Referencia (&)
// Analogia: Fotocopia (valor) vs Documento Original (referencia &)
// ============================================================================

#include <iostream>
using namespace std;

void intentoFallidoDuplicar(int x);
void duplicarOriginal(int &x);
void intercambiar(int &a, int &b);
void leerEnteroEnRango(int &destino, int minimo, int maximo, const char mensaje[]);

int main() {
    int saldo = 100;

    cout << "1) Antes de intentoFallidoDuplicar, saldo = " << saldo << endl;
    intentoFallidoDuplicar(saldo);
    cout << "   Despues de intentoFallidoDuplicar, saldo = " << saldo
         << " (NO cambio porque recibio una copia)" << endl;

    cout << "\n2) Antes de duplicarOriginal, saldo = " << saldo << endl;
    duplicarOriginal(saldo);
    cout << "   Despues de duplicarOriginal, saldo = " << saldo
         << " (SI cambio porque uso &)" << endl;

    int primero = 0, segundo = 0;
    cout << "\n3) Probando intercambio (swap):" << endl;
    leerEnteroEnRango(primero, 1, 1000, "Ingrese primer entero (1..1000): ");
    leerEnteroEnRango(segundo, 1, 1000, "Ingrese segundo entero (1..1000): ");

    cout << "   Antes de intercambiar: primero = " << primero
         << ", segundo = " << segundo << endl;
    intercambiar(primero, segundo);
    cout << "   Despues de intercambiar: primero = " << primero
         << ", segundo = " << segundo << endl;

    return 0;
}

// Paso por VALOR: 'x' es una variable local independiente (copia)
void intentoFallidoDuplicar(int x) {
    x = x * 2;
    cout << "   [Dentro de intentoFallidoDuplicar] copia x = " << x << endl;
}

// Paso por REFERENCIA (&): 'x' es un alias del casillero original en main
void duplicarOriginal(int &x) {
    x = x * 2;
}

// Clasico algoritmo de intercambio con variable auxiliar temporal
void intercambiar(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

// Reutilizable en cualquier parcial para leer y validar sin ensuciar el main
void leerEnteroEnRango(int &destino, int minimo, int maximo, const char mensaje[]) {
    do {
        cout << mensaje;
        if (!(cin >> destino)) {
            destino = minimo;
            return;
        }
        if (destino < minimo || destino > maximo) {
            cout << "   [Error] Debe estar entre " << minimo << " y " << maximo << ".\n";
        }
    } while (destino < minimo || destino > maximo);
}
