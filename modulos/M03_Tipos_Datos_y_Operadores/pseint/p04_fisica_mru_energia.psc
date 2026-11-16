// ============================================================================
// Modulo 03 - Problema Resuelto 04: Fisica Basica (MRUV y Energia Cinetica)
// Conceptos: Precedencia de operadores, literales reales, formulas fisicas
// ============================================================================
Algoritmo FisicaMRUV
    Definir masa, vInicial, aceleracion, tiempo Como Real;
    Definir distancia, vFinal, vFinalKmh, energiaCinetica Como Real;
    Definir FACTOR_KMH Como Real;

    FACTOR_KMH <- 3.6;

    Escribir "=== SIMULADOR DE CINEMATICA Y ENERGIA (MRUV) ===";
    Escribir "Ingrese masa del objeto (kg): ";
    Leer masa;
    Escribir "Ingrese velocidad inicial v0 (m/s): ";
    Leer vInicial;
    Escribir "Ingrese aceleracion constante a (m/s^2): ";
    Leer aceleracion;
    Escribir "Ingrese tiempo transcurrido t (s): ";
    Leer tiempo;

    distancia <- vInicial * tiempo + 0.5 * aceleracion * tiempo * tiempo;
    vFinal <- vInicial + aceleracion * tiempo;
    vFinalKmh <- vFinal * FACTOR_KMH;
    energiaCinetica <- 0.5 * masa * vFinal * vFinal;

    Escribir "--- RESULTADOS FISICOS ---";
    Escribir "Distancia recorrida : ", distancia, " m";
    Escribir "Velocidad final     : ", vFinal, " m/s (", vFinalKmh, " km/h)";
    Escribir "Energia cinetica    : ", energiaCinetica, " Joules";
FinAlgoritmo
