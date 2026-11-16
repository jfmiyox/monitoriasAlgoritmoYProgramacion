Algoritmo TranspuestaYSimetria
    Definir MAX_F, MAX_C, f, c, i, j Como Entero;
    Definir esSimetrica Como Logico;
    Dimension A[15, 15];
    Dimension T[15, 15];

    MAX_F <- 15;
    MAX_C <- 15;

    Repetir
        Escribir "Filas F (1 a ", MAX_F, "): ";
        Leer f;
    Hasta Que f >= 1 Y f <= MAX_F

    Repetir
        Escribir "Columnas C (1 a ", MAX_C, "): ";
        Leer c;
    Hasta Que c >= 1 Y c <= MAX_C

    Para i <- 1 Hasta f Con Paso 1 Hacer
        Para j <- 1 Hasta c Con Paso 1 Hacer
            Escribir "A[", i, ",", j, "] = ";
            Leer A[i, j];
        FinPara
    FinPara

    Para i <- 1 Hasta f Con Paso 1 Hacer
        Para j <- 1 Hasta c Con Paso 1 Hacer
            T[j, i] <- A[i, j];
        FinPara
    FinPara

    Escribir "Matriz transpuesta T (", c, "x", f, "):";
    Para i <- 1 Hasta c Con Paso 1 Hacer
        Para j <- 1 Hasta f Con Paso 1 Hacer
            Escribir T[i, j], "  " Sin Saltar;
        FinPara
        Escribir "";
    FinPara

    Si f <> c Entonces
        Escribir "No es cuadrada, por lo tanto NO puede ser simetrica.";
    SiNo
        esSimetrica <- Verdadero;
        i <- 1;
        Mientras i <= f Y esSimetrica Hacer
            j <- i + 1;
            Mientras j <= c Y esSimetrica Hacer
                Si A[i, j] <> A[j, i] Entonces
                    esSimetrica <- Falso;
                FinSi
                j <- j + 1;
            FinMientras
            i <- i + 1;
        FinMientras

        Si esSimetrica Entonces
            Escribir "La matriz ES simetrica.";
        SiNo
            Escribir "La matriz NO es simetrica.";
        FinSi
    FinSi
FinAlgoritmo
