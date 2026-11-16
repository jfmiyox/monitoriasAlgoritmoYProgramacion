// ============================================================================
// Modulo 08 - Ejemplo 01: Anatomia de Funciones (void y con retorno)
// Curso de Monitoria: Algoritmos y Programacion (30 horas)
// Estandar: C++17 basico (solo estructuras y tipos basicos)
// ============================================================================

#include <iostream>
#include <iomanip>
using namespace std;

// --- PROTOTIPOS (avisan al compilador que estas funciones existen) ---
void mostrarBanner();
double calcularAreaRectangulo(double base, double altura);
bool esNumeroPar(int numero);
char clasificarNota(double nota);

int main() {
    mostrarBanner();

    double base = 0.0, altura = 0.0;
    cout << "Ingrese la base del rectangulo: ";
    cin >> base;
    cout << "Ingrese la altura del rectangulo: ";
    cin >> altura;

    // Una funcion con retorno devuelve un valor que podemos guardar o imprimir
    double area = calcularAreaRectangulo(base, altura);
    cout << fixed << setprecision(2);
    cout << "Area calculada: " << area << endl;

    int numero = 0;
    cout << "\nIngrese un numero entero para verificar paridad: ";
    cin >> numero;

    if (esNumeroPar(numero)) {
        cout << numero << " es PAR." << endl;
    } else {
        cout << numero << " es IMPAR." << endl;
    }

    double nota = 0.0;
    cout << "\nIngrese una nota (0.0 a 5.0): ";
    cin >> nota;
    cout << "Calificacion literal: " << clasificarNota(nota) << endl;

    return 0;
}

// --- DEFINICIONES ---

// Funcion void: ejecuta una accion y NO devuelve ningun dato (sin return de valor)
void mostrarBanner() {
    cout << "==========================================" << endl;
    cout << "   MODULO 08: PRIMERAS FUNCIONES EN C++   " << endl;
    cout << "==========================================" << endl;
}

// Funcion con retorno double: recibe dos copias (base y altura) y devuelve el area
double calcularAreaRectangulo(double base, double altura) {
    if (base <= 0.0 || altura <= 0.0) {
        return 0.0; // Retorno temprano seguro si los datos no son positivos
    }
    return base * altura;
}

// Funcion con retorno bool: muy util para condiciones limpias en if / while
bool esNumeroPar(int numero) {
    return (numero % 2 == 0);
}

// Funcion con retorno char: traduce una nota numerica a letra (A, B, C, F)
char clasificarNota(double nota) {
    if (nota >= 4.5) {
        return 'A';
    } else if (nota >= 3.8) {
        return 'B';
    } else if (nota >= 3.0) {
        return 'C';
    } else {
        return 'F';
    }
}
