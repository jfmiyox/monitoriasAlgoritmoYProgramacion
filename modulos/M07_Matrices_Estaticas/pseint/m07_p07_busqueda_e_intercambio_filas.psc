Algoritmo BusquedaEIntercambioFilas
    Definir MAX_F, MAX_C, f, c, i, j, objetivo, apariciones Como Entero;
    Definir menor, filaMenor, colMenor, aux Como Entero;
    Dimension mat[20, 20];

    MAX_F <- 20;
    MAX_C <- 20;

    Repetir
        Escribir "Filas (1 a ", MAX_F, "): ";
        Leer f;
    Hasta Que f >= 1 Y f <= MAX_F

    Repetir
        Escribir "Columnas (1 a ", MAX_C, "): ";
        Leer c;
    Hasta Que c >= 1 Y c <= MAX_C

    Para i <- 1 Hasta f Con Paso 1 Hacer
        Para j <- 1 Hasta c Con Paso 1 Hacer
            Escribir "mat[", i, ",", j, "] = ";
            Leer mat[i, j];
        FinPara
    FinPara

    Escribir "Numero a buscar en la matriz: ";
    Leer objetivo;

    apariciones <- 0;
    Para i <- 1 Hasta f Con Paso 1 Hacer
        Para j <- 1 Hasta c Con Paso 1 Hacer
            Si mat[i, j] = objetivo Entonces
                Escribir "Encontrado en (", i, ", ", j, ")";
                apariciones <- apariciones + 1;
            FinSi
        FinPara
    FinPara

    Si apariciones = 0 Entonces
        Escribir "El valor ", objetivo, " no aparece en la matriz.";
    SiNo
        Escribir "Total de apariciones: ", apariciones;
    FinSi

    menor <- mat[1, 1];
    filaMenor <- 1;
    colMenor <- 1;

    Para i <- 1 Hasta f Con Paso 1 Hacer
        Para j <- 1 Hasta c Con Paso 1 Hacer
            Si mat[i, j] < menor Entonces
                menor <- mat[i, j];
                filaMenor <- i;
                colMenor <- j;
            FinSi
        FinPara
    FinPara

    Escribir "Menor global: ", menor, " en (", filaMenor, ", ", colMenor, ").";
    Si filaMenor <> 1 Entonces
        Para j <- 1 Hasta c Con Paso 1 Hacer
            aux <- mat[1, j];
            mat[1, j] <- mat[filaMenor, j];
            mat[filaMenor, j] <- aux;
        FinPara
        Escribir "Se intercambio la fila ", filaMenor, " con la fila 1.";
    FinSi

    Escribir "Matriz resultante:";
    Para i <- 1 Hasta f Con Paso 1 Hacer
        Para j <- 1 Hasta c Con Paso 1 Hacer
            Escribir mat[i, j], "  " Sin Saltar;
        FinPara
        Escribir "";
    FinPara
FinAlgoritmo
