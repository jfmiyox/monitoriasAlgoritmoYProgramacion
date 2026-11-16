Algoritmo NumeroPrimoBandera
    Definir n, d, menorDivisor Como Entero;
    Definir esPrimo Como Logico;

    Escribir "=== DETECTOR DE NUMERO PRIMO CON BANDERA LOGICA ===";
    Repetir
        Escribir "Ingrese un entero positivo (>= 1):";
        Leer n;
        Si n < 1 Entonces
            Escribir "Error: ingrese un numero mayor o igual a 1.";
        FinSi
    Hasta Que n >= 1

    esPrimo <- Verdadero;
    menorDivisor <- 0;

    Si n = 1 Entonces
        esPrimo <- Falso;
    SiNo
        d <- 2;
        Mientras d * d <= n Y esPrimo Hacer
            Si n MOD d = 0 Entonces
                esPrimo <- Falso;
                menorDivisor <- d;
            FinSi
            d <- d + 1;
        FinMientras
    FinSi

    Escribir "Resultado para ", n, ":";
    Si esPrimo Entonces
        Escribir n, " ES un numero primo.";
    SiNo
        Si n = 1 Entonces
            Escribir "1 NO es primo por definicion (solo tiene un divisor).";
        SiNo
            Escribir n, " NO es primo (es compuesto). Menor divisor > 1: ", menorDivisor;
        FinSi
    FinSi
FinAlgoritmo
