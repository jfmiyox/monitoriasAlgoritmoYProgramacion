Algoritmo FiltrarSinDuplicados
    Definir MAX, n, m, i, j, posEncontrado Como Entero;
    Dimension datos[50];
    Dimension unicos[50];
    Dimension conteo[50];

    MAX <- 50;
    m <- 0;

    Repetir
        Escribir "Cantidad de datos (1 a ", MAX, "): ";
        Leer n;
    Hasta Que n >= 1 Y n <= MAX

    Para i <- 1 Hasta n Con Paso 1 Hacer
        Escribir "datos[", i, "] = ";
        Leer datos[i];
    FinPara

    Para i <- 1 Hasta n Con Paso 1 Hacer
        posEncontrado <- -1;
        j <- 1;
        Mientras j <= m Y posEncontrado = -1 Hacer
            Si unicos[j] = datos[i] Entonces
                posEncontrado <- j;
            SiNo
                j <- j + 1;
            FinSi
        FinMientras

        Si posEncontrado <> -1 Entonces
            conteo[posEncontrado] <- conteo[posEncontrado] + 1;
        SiNo
            m <- m + 1;
            unicos[m] <- datos[i];
            conteo[m] <- 1;
        FinSi
    FinPara

    Escribir "--- VALORES UNICOS Y FRECUENCIAS ---";
    Para j <- 1 Hasta m Con Paso 1 Hacer
        Escribir "Valor ", unicos[j], " aparece ", conteo[j], " vez/veces.";
    FinPara
FinAlgoritmo
