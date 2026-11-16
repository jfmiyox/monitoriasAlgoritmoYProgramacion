// Modulo 02 - Ejemplo 04: Conversion de temperatura (Celsius a Fahrenheit y Kelvin)
// Objetivo: Aplicar formulas reales cuidando la precedencia de operadores

Algoritmo ConversionTemperatura
    Definir celsius, fahrenheit, kelvin Como Real;

    Escribir "=== CONVERSOR DE TEMPERATURA ===";
    Escribir "Ingresa la temperatura en grados Celsius:";
    Leer celsius;

    fahrenheit <- (9.0 / 5.0) * celsius + 32.0;
    kelvin <- celsius + 273.15;

    Escribir celsius, " C equivalen a ", fahrenheit, " F";
    Escribir celsius, " C equivalen a ", kelvin, " K";
FinAlgoritmo
