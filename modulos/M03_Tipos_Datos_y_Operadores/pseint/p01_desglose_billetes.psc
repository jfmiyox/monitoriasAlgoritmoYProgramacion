// ============================================================================
// Modulo 03 - Problema Resuelto 01: Desglose de Billetes en Cajero Automatico
// Conceptos: Division entera (trunc en PSeInt), modulo (MOD), asignacion
// ============================================================================
Algoritmo DesgloseBilletes
    Definir monto, resto Como Entero;
    Definir b50, b20, b10, b5, b2, b1, sobrante Como Entero;

    Escribir "=== CAJERO AUTOMATICO: DESGLOSE DE BILLETES ===";
    Escribir "Ingrese el monto entero en pesos (ej. 188500): ";
    Leer monto;

    resto <- monto;

    // En PSeInt, / devuelve Real; usamos trunc() para obtener division entera
    b50 <- trunc(resto / 50000);
    resto <- resto MOD 50000;

    b20 <- trunc(resto / 20000);
    resto <- resto MOD 20000;

    b10 <- trunc(resto / 10000);
    resto <- resto MOD 10000;

    b5 <- trunc(resto / 5000);
    resto <- resto MOD 5000;

    b2 <- trunc(resto / 2000);
    resto <- resto MOD 2000;

    b1 <- trunc(resto / 1000);
    sobrante <- resto MOD 1000;

    Escribir "--- Desglose optimo para $", monto, " ---";
    Escribir "Billetes de $50.000 : ", b50;
    Escribir "Billetes de $20.000 : ", b20;
    Escribir "Billetes de $10.000 : ", b10;
    Escribir "Billetes de $5.000  : ", b5;
    Escribir "Billetes de $2.000  : ", b2;
    Escribir "Billetes de $1.000  : ", b1;
    Escribir "Sobrante en monedas : $", sobrante;
FinAlgoritmo
