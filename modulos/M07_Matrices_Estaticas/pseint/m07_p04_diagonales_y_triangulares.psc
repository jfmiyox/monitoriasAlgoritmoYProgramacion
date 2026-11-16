Algoritmo DiagonalesYTriangulares
    // En PSeInt (base 1): diagonal principal i = j, secundaria i + j = n + 1
    // En C++ (base 0): diagonal principal i == j, secundaria i + j == n - 1
    Definir MAX, n, i, j Como Entero;
    Definir sumaDiagP, sumaDiagS, sumaTriSup, sumaTriInf Como Entero;
    Dimension mat[15, 15];

    MAX <- 15;

    Repetir
        Escribir "Dimension N de la matriz cuadrada NxN (1 a ", MAX, "): ";
        Leer n;
    Hasta Que n >= 1 Y n <= MAX

    Para i <- 1 Hasta n Con Paso 1 Hacer
        Para j <- 1 Hasta n Con Paso 1 Hacer
            Escribir "mat[", i, ",", j, "] = ";
            Leer mat[i, j];
        FinPara
    FinPara

    sumaDiagP <- 0;
    sumaDiagS <- 0;
    sumaTriSup <- 0;
    sumaTriInf <- 0;

    Escribir "Diagonal principal:";
    Para i <- 1 Hasta n Con Paso 1 Hacer
        Escribir mat[i, i], " " Sin Saltar;
        sumaDiagP <- sumaDiagP + mat[i, i];
    FinPara
    Escribir "";

    Escribir "Diagonal secundaria:";
    Para i <- 1 Hasta n Con Paso 1 Hacer
        Escribir mat[i, n + 1 - i], " " Sin Saltar;
        sumaDiagS <- sumaDiagS + mat[i, n + 1 - i];
    FinPara
    Escribir "";

    Para i <- 1 Hasta n Con Paso 1 Hacer
        Para j <- 1 Hasta n Con Paso 1 Hacer
            Si i < j Entonces
                sumaTriSup <- sumaTriSup + mat[i, j];
            SiNo
                Si i > j Entonces
                    sumaTriInf <- sumaTriInf + mat[i, j];
                FinSi
            FinSi
        FinPara
    FinPara

    Escribir "Suma diagonal principal: ", sumaDiagP;
    Escribir "Suma diagonal secundaria: ", sumaDiagS;
    Escribir "Suma triangular superior (i < j): ", sumaTriSup;
    Escribir "Suma triangular inferior (i > j): ", sumaTriInf;
FinAlgoritmo
