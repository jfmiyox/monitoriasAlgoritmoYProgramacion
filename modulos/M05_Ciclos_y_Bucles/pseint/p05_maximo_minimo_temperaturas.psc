Algoritmo MaximoMinimoTemperaturas
    Definir temp, mayor, menor, suma, promedio Como Real;
    Definir diaMayor, diaMenor, contador Como Entero;
    Definir esPrimero Como Logico;

    mayor <- 0;
    menor <- 0;
    suma <- 0;
    diaMayor <- 0;
    diaMenor <- 0;
    contador <- 0;
    esPrimero <- Verdadero;

    Escribir "=== MAXIMO Y MINIMO DE TEMPERATURAS (CENTINELA -999) ===";
    Escribir "Ingrese temperatura del dia 1 (-999 para terminar):";
    Leer temp;

    Mientras temp <> -999 Hacer
        contador <- contador + 1;
        suma <- suma + temp;

        Si esPrimero Entonces
            mayor <- temp;
            menor <- temp;
            diaMayor <- contador;
            diaMenor <- contador;
            esPrimero <- Falso;
        SiNo
            Si temp > mayor Entonces
                mayor <- temp;
                diaMayor <- contador;
            FinSi
            Si temp < menor Entonces
                menor <- temp;
                diaMenor <- contador;
            FinSi
        FinSi

        Escribir "Ingrese temperatura del dia ", contador + 1, " (-999 para terminar):";
        Leer temp;
    FinMientras

    Escribir "=== ESTADISTICAS TERMOMETRICAS ===";
    Si esPrimero Entonces
        Escribir "No se ingresaron temperaturas.";
    SiNo
        promedio <- suma / contador;
        Escribir "Dias registrados: ", contador;
        Escribir "Temperatura maxima: ", mayor, " C (dia ", diaMayor, ")";
        Escribir "Temperatura minima: ", menor, " C (dia ", diaMenor, ")";
        Escribir "Promedio general: ", promedio, " C";
    FinSi
FinAlgoritmo
