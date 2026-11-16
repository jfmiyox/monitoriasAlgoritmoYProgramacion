// ============================================================================
// Modulo 03 - Problema Resuelto 02: Conversion de Segundos a Horas/Min/Seg
// Conceptos: Constantes conceptuales, division entera y residuo encadenados
// ============================================================================
Algoritmo ConversionTiempo
    Definir totalSegundos, horas, resto, minutos, segundos Como Entero;
    Definir SEG_POR_HORA, SEG_POR_MIN Como Entero;

    SEG_POR_HORA <- 3600;
    SEG_POR_MIN <- 60;

    Escribir "=== CONVERSOR DE TIEMPO (SEGUNDOS A HH:MM:SS) ===";
    Escribir "Ingrese la cantidad total de segundos (ej. 3725): ";
    Leer totalSegundos;

    horas <- trunc(totalSegundos / SEG_POR_HORA);
    resto <- totalSegundos MOD SEG_POR_HORA;
    minutos <- trunc(resto / SEG_POR_MIN);
    segundos <- resto MOD SEG_POR_MIN;

    Escribir totalSegundos, " segundos equivalen a:";
    Escribir horas, " hora(s), ", minutos, " minuto(s) y ", segundos, " segundo(s).";
FinAlgoritmo
