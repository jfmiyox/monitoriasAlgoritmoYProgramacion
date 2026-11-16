Algoritmo MezclaDosArreglos
    Definir MAX, nA, nB, nC, i, j, k, idx Como Entero;
    Dimension A[30];
    Dimension B[30];
    Dimension C[60]; // Capacidad fija 2 * MAX

    MAX <- 30;

    Repetir
        Escribir "Tamano de A ordenado (1 a ", MAX, "): ";
        Leer nA;
    Hasta Que nA >= 1 Y nA <= MAX

    Para i <- 1 Hasta nA Con Paso 1 Hacer
        Escribir "A[", i, "] = ";
        Leer A[i];
    FinPara

    Repetir
        Escribir "Tamano de B ordenado (1 a ", MAX, "): ";
        Leer nB;
    Hasta Que nB >= 1 Y nB <= MAX

    Para i <- 1 Hasta nB Con Paso 1 Hacer
        Escribir "B[", i, "] = ";
        Leer B[i];
    FinPara

    // Mezcla lineal (indices 1..nA y 1..nB)
    i <- 1;
    j <- 1;
    k <- 1;

    Mientras i <= nA Y j <= nB Hacer
        Si A[i] <= B[j] Entonces
            C[k] <- A[i];
            i <- i + 1;
        SiNo
            C[k] <- B[j];
            j <- j + 1;
        FinSi
        k <- k + 1;
    FinMientras

    Mientras i <= nA Hacer
        C[k] <- A[i];
        i <- i + 1;
        k <- k + 1;
    FinMientras

    Mientras j <= nB Hacer
        C[k] <- B[j];
        j <- j + 1;
        k <- k + 1;
    FinMientras

    nC <- nA + nB;
    Escribir "Vector fusionado C:";
    Para idx <- 1 Hasta nC Con Paso 1 Hacer
        Escribir C[idx], " " Sin Saltar;
    FinPara
    Escribir "";
FinAlgoritmo
