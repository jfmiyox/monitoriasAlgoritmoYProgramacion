Algoritmo RotarTurnos
    Definir MAX, n, i, p, direccion, k, pasos, primero, ultimo Como Entero;
    Dimension turnos[30];

    MAX <- 30;

    Repetir
        Escribir "Cantidad de turnos (1 a ", MAX, "): ";
        Leer n;
    Hasta Que n >= 1 Y n <= MAX

    Para i <- 1 Hasta n Con Paso 1 Hacer
        Escribir "Turno[", i, "]: ";
        Leer turnos[i];
    FinPara

    Repetir
        Escribir "Direccion de rotacion (1 = Izquierda, 2 = Derecha): ";
        Leer direccion;
    Hasta Que direccion = 1 O direccion = 2

    Repetir
        Escribir "Cuantas posiciones rotar (>= 0): ";
        Leer k;
    Hasta Que k >= 0

    Escribir "Antes:";
    Para i <- 1 Hasta n Con Paso 1 Hacer
        Escribir turnos[i], " " Sin Saltar;
    FinPara
    Escribir "";

    pasos <- k MOD n;

    Si direccion = 1 Entonces
        Para p <- 1 Hasta pasos Con Paso 1 Hacer
            primero <- turnos[1];
            Para i <- 1 Hasta n - 1 Con Paso 1 Hacer
                turnos[i] <- turnos[i + 1];
            FinPara
            turnos[n] <- primero;
        FinPara
    SiNo
        Para p <- 1 Hasta pasos Con Paso 1 Hacer
            ultimo <- turnos[n];
            Para i <- n Hasta 2 Con Paso -1 Hacer
                turnos[i] <- turnos[i - 1];
            FinPara
            turnos[1] <- ultimo;
        FinPara
    FinSi

    Escribir "Despues:";
    Para i <- 1 Hasta n Con Paso 1 Hacer
        Escribir turnos[i], " " Sin Saltar;
    FinPara
    Escribir "";
FinAlgoritmo
