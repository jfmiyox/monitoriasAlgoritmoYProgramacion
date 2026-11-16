Algoritmo VentasTiendasMeses
    Definir MAX_T, MAX_M, t, m, i, j, mejorTienda, peorMes Como Entero;
    Definir totalGlobal, sumaTienda, sumaMes, maxVentaTienda, minVentaMes Como Real;
    Dimension ventas[15, 12];

    MAX_T <- 15;
    MAX_M <- 12;

    Repetir
        Escribir "Numero de tiendas (1 a ", MAX_T, "): ";
        Leer t;
    Hasta Que t >= 1 Y t <= MAX_T

    Repetir
        Escribir "Numero de meses (1 a ", MAX_M, "): ";
        Leer m;
    Hasta Que m >= 1 Y m <= MAX_M

    Para i <- 1 Hasta t Con Paso 1 Hacer
        Para j <- 1 Hasta m Con Paso 1 Hacer
            Repetir
                Escribir "Ventas tienda ", i, ", mes ", j, " (>= 0): ";
                Leer ventas[i, j];
            Hasta Que ventas[i, j] >= 0
        FinPara
    FinPara

    totalGlobal <- 0;
    maxVentaTienda <- -1;
    mejorTienda <- 1;

    Escribir "--- VENTAS POR TIENDA ---";
    Para i <- 1 Hasta t Con Paso 1 Hacer
        sumaTienda <- 0;
        Para j <- 1 Hasta m Con Paso 1 Hacer
            sumaTienda <- sumaTienda + ventas[i, j];
            totalGlobal <- totalGlobal + ventas[i, j];
        FinPara
        Escribir "Tienda ", i, ": $", sumaTienda;
        Si i = 1 O sumaTienda > maxVentaTienda Entonces
            maxVentaTienda <- sumaTienda;
            mejorTienda <- i;
        FinSi
    FinPara

    minVentaMes <- 0;
    peorMes <- 1;

    Escribir "--- VENTAS POR MES ---";
    Para j <- 1 Hasta m Con Paso 1 Hacer
        sumaMes <- 0;
        Para i <- 1 Hasta t Con Paso 1 Hacer
            sumaMes <- sumaMes + ventas[i, j];
        FinPara
        Escribir "Mes ", j, ": $", sumaMes;
        Si j = 1 O sumaMes < minVentaMes Entonces
            minVentaMes <- sumaMes;
            peorMes <- j;
        FinSi
    FinPara

    Escribir "Total global de la cadena: $", totalGlobal;
    Escribir "Tienda lider: Tienda ", mejorTienda, " con $", maxVentaTienda;
    Escribir "Mes de menor venta: Mes ", peorMes, " con $", minVentaMes;
FinAlgoritmo
