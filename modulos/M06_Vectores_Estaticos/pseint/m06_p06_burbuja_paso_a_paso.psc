Algoritmo BurbujaPasoAPaso
    Definir MAX, n, i, j, pasada, aux Como Entero;
    Definir huboCambio Como Logico;
    Dimension puntajes[30];

    MAX <- 30;

    Repetir
        Escribir "Cantidad de puntajes a ordenar (1 a ", MAX, "): ";
        Leer n;
    Hasta Que n >= 1 Y n <= MAX

    Para i <- 1 Hasta n Con Paso 1 Hacer
        Escribir "Puntaje[", i, "]: ";
        Leer puntajes[i];
    FinPara

    // Ordenamiento Burbuja optimizado (base 1 en PSeInt)
    pasada <- 1;
    huboCambio <- Verdadero;

    Mientras pasada <= n - 1 Y huboCambio Hacer
        huboCambio <- Falso;
        Para j <- 1 Hasta n - pasada Con Paso 1 Hacer
            Si puntajes[j] > puntajes[j + 1] Entonces
                aux <- puntajes[j];
                puntajes[j] <- puntajes[j + 1];
                puntajes[j + 1] <- aux;
                huboCambio <- Verdadero;
            FinSi
        FinPara

        Escribir "Tras pasada ", pasada, ": " Sin Saltar;
        Para i <- 1 Hasta n Con Paso 1 Hacer
            Escribir puntajes[i], " " Sin Saltar;
        FinPara
        Escribir "";

        pasada <- pasada + 1;
    FinMientras

    Escribir "Ordenado final:";
    Para i <- 1 Hasta n Con Paso 1 Hacer
        Escribir puntajes[i], " " Sin Saltar;
    FinPara
    Escribir "";
FinAlgoritmo
