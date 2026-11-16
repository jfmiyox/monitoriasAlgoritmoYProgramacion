Algoritmo MultiplicacionMatrices
    Definir MAX, f1, c1, f2, c2, i, j, k, suma Como Entero;
    Dimension A[15, 15];
    Dimension B[15, 15];
    Dimension R[15, 15];

    MAX <- 15;

    Repetir
        Escribir "Filas de A (1 a ", MAX, "): ";
        Leer f1;
        Escribir "Columnas de A (1 a ", MAX, "): ";
        Leer c1;
    Hasta Que f1 >= 1 Y f1 <= MAX Y c1 >= 1 Y c1 <= MAX

    Repetir
        Escribir "Filas de B (1 a ", MAX, "): ";
        Leer f2;
        Escribir "Columnas de B (1 a ", MAX, "): ";
        Leer c2;
    Hasta Que f2 >= 1 Y f2 <= MAX Y c2 >= 1 Y c2 <= MAX

    Si c1 <> f2 Entonces
        Escribir "Error matematico: no se puede multiplicar porque c1 <> f2.";
    SiNo
        Para i <- 1 Hasta f1 Con Paso 1 Hacer
            Para j <- 1 Hasta c1 Con Paso 1 Hacer
                Escribir "A[", i, ",", j, "] = ";
                Leer A[i, j];
            FinPara
        FinPara

        Para i <- 1 Hasta f2 Con Paso 1 Hacer
            Para j <- 1 Hasta c2 Con Paso 1 Hacer
                Escribir "B[", i, ",", j, "] = ";
                Leer B[i, j];
            FinPara
        FinPara

        Para i <- 1 Hasta f1 Con Paso 1 Hacer
            Para j <- 1 Hasta c2 Con Paso 1 Hacer
                suma <- 0;
                Para k <- 1 Hasta c1 Con Paso 1 Hacer
                    suma <- suma + A[i, k] * B[k, j];
                FinPara
                R[i, j] <- suma;
            FinPara
        FinPara

        Escribir "Matriz resultado R = A x B:";
        Para i <- 1 Hasta f1 Con Paso 1 Hacer
            Para j <- 1 Hasta c2 Con Paso 1 Hacer
                Escribir R[i, j], "  " Sin Saltar;
            FinPara
            Escribir "";
        FinPara
    FinSi
FinAlgoritmo
