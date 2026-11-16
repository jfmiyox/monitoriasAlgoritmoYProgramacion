Algoritmo CuadradoMagico
    Definir MAX, n, i, j, sumaObjetivo, sumaFila, sumaCol, diagP, diagS Como Entero;
    Definir esMagico Como Logico;
    Dimension mat[10, 10];

    MAX <- 10;

    Repetir
        Escribir "Orden N de la matriz cuadrada (1 a ", MAX, "): ";
        Leer n;
    Hasta Que n >= 1 Y n <= MAX

    Para i <- 1 Hasta n Con Paso 1 Hacer
        Para j <- 1 Hasta n Con Paso 1 Hacer
            Escribir "mat[", i, ",", j, "] = ";
            Leer mat[i, j];
        FinPara
    FinPara

    sumaObjetivo <- 0;
    Para j <- 1 Hasta n Con Paso 1 Hacer
        sumaObjetivo <- sumaObjetivo + mat[1, j];
    FinPara

    esMagico <- Verdadero;

    // Verificar filas
    i <- 1;
    Mientras i <= n Y esMagico Hacer
        sumaFila <- 0;
        Para j <- 1 Hasta n Con Paso 1 Hacer
            sumaFila <- sumaFila + mat[i, j];
        FinPara
        Si sumaFila <> sumaObjetivo Entonces
            esMagico <- Falso;
        FinSi
        i <- i + 1;
    FinMientras

    // Verificar columnas
    j <- 1;
    Mientras j <= n Y esMagico Hacer
        sumaCol <- 0;
        Para i <- 1 Hasta n Con Paso 1 Hacer
            sumaCol <- sumaCol + mat[i, j];
        FinPara
        Si sumaCol <> sumaObjetivo Entonces
            esMagico <- Falso;
        FinSi
        j <- j + 1;
    FinMientras

    // Verificar diagonales
    Si esMagico Entonces
        diagP <- 0;
        diagS <- 0;
        Para i <- 1 Hasta n Con Paso 1 Hacer
            diagP <- diagP + mat[i, i];
            diagS <- diagS + mat[i, n + 1 - i];
        FinPara
        Si diagP <> sumaObjetivo O diagS <> sumaObjetivo Entonces
            esMagico <- Falso;
        FinSi
    FinSi

    Si esMagico Entonces
        Escribir "ES un Cuadrado Magico! Constante magica = ", sumaObjetivo;
    SiNo
        Escribir "NO es un Cuadrado Magico.";
    FinSi
FinAlgoritmo
