Algoritmo InvertirYCapicua
    // Indices en PSeInt por defecto: 1 hasta n
    Definir MAX, n, i, mitad, aux Como Entero;
    Definir esCapicua Como Logico;
    Dimension vec[50];

    MAX <- 50;

    Repetir
        Escribir "Cantidad de elementos (1 a ", MAX, "): ";
        Leer n;
    Hasta Que n >= 1 Y n <= MAX

    Para i <- 1 Hasta n Con Paso 1 Hacer
        Escribir "vec[", i, "] = ";
        Leer vec[i];
    FinPara

    // 1. Verificar si es capicua (en base 1, el espejo de i es n + 1 - i)
    esCapicua <- Verdadero;
    mitad <- trunc(n / 2);
    i <- 1;

    Mientras i <= mitad Y esCapicua Hacer
        Si vec[i] <> vec[n + 1 - i] Entonces
            esCapicua <- Falso;
        FinSi
        i <- i + 1;
    FinMientras

    Si esCapicua Entonces
        Escribir "Resultado: El arreglo ES capicua.";
    SiNo
        Escribir "Resultado: El arreglo NO es capicua.";
    FinSi

    // 2. Invertir el arreglo in-place (en el mismo vector)
    Para i <- 1 Hasta mitad Con Paso 1 Hacer
        aux <- vec[i];
        vec[i] <- vec[n + 1 - i];
        vec[n + 1 - i] <- aux;
    FinPara

    Escribir "Arreglo invertido:";
    Para i <- 1 Hasta n Con Paso 1 Hacer
        Escribir vec[i], " " Sin Saltar;
    FinPara
    Escribir "";
FinAlgoritmo
