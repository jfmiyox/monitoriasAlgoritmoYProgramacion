// ============================================================================
// Modulo 03 - Problema Resuelto 07: Extraccion e Inversion de Digitos (4 cifras)
// Conceptos: Descomposicion decimal con trunc(/10) y MOD 10
// ============================================================================
Algoritmo DigitosNumero
    Definir numero, dMiles, dCentenas, dDecenas, dUnidades Como Entero;
    Definir sumaDigitos, invertido Como Entero;

    Escribir "=== DESCOMPOSICION DE UN NUMERO DE 4 CIFRAS ===";
    Escribir "Ingrese un entero positivo de 4 cifras (ej. 4829): ";
    Leer numero;

    // Extraemos de izquierda a derecha o usando cociente y residuo
    dMiles <- trunc(numero / 1000);
    dCentenas <- trunc(numero / 100) MOD 10;
    dDecenas <- trunc(numero / 10) MOD 10;
    dUnidades <- numero MOD 10;

    sumaDigitos <- dMiles + dCentenas + dDecenas + dUnidades;
    invertido <- dUnidades * 1000 + dDecenas * 100 + dCentenas * 10 + dMiles;

    Escribir "--- ANALISIS POSICIONAL ---";
    Escribir "Unidades de mil : ", dMiles;
    Escribir "Centenas        : ", dCentenas;
    Escribir "Decenas         : ", dDecenas;
    Escribir "Unidades        : ", dUnidades;
    Escribir "Suma de digitos : ", sumaDigitos;
    Escribir "Numero invertido: ", invertido;
FinAlgoritmo
