Algoritmo NotasEstadisticas
    // En PSeInt por defecto los indices van de 1 a n (en C++ van de 0 a n-1)
    Definir MAX, n, i, aprobados, posMayor, posMenor Como Entero;
    Definir suma, promedio, mayor, menor Como Real;
    Dimension notas[50]; // Capacidad fisica fija MAX = 50

    MAX <- 50;

    // 1. Validar tamano logico n dentro de [1, MAX]
    Repetir
        Escribir "Ingrese cantidad de estudiantes (1 a ", MAX, "): ";
        Leer n;
        Si n < 1 O n > MAX Entonces
            Escribir "Error: la cantidad debe estar entre 1 y ", MAX, ".";
        FinSi
    Hasta Que n >= 1 Y n <= MAX

    // 2. Lectura de notas (indices en PSeInt: 1 hasta n)
    Para i <- 1 Hasta n Con Paso 1 Hacer
        Repetir
            Escribir "Nota del estudiante [", i, "] (0.0 a 5.0): ";
            Leer notas[i];
            Si notas[i] < 0 O notas[i] > 5 Entonces
                Escribir "Error: ingrese una nota valida entre 0.0 y 5.0.";
            FinSi
        Hasta Que notas[i] >= 0 Y notas[i] <= 5
    FinPara

    // 3. Calculos estadisticos
    suma <- 0;
    aprobados <- 0;
    mayor <- notas[1];
    menor <- notas[1];
    posMayor <- 1;
    posMenor <- 1;

    Para i <- 1 Hasta n Con Paso 1 Hacer
        suma <- suma + notas[i];
        Si notas[i] >= 3.0 Entonces
            aprobados <- aprobados + 1;
        FinSi
        Si notas[i] > mayor Entonces
            mayor <- notas[i];
            posMayor <- i;
        FinSi
        Si notas[i] < menor Entonces
            menor <- notas[i];
            posMenor <- i;
        FinSi
    FinPara

    promedio <- suma / n;

    // 4. Salida de resultados
    Escribir "--- RESUMEN DEL GRUPO ---";
    Escribir "Promedio general: ", promedio;
    Escribir "Mayor nota: ", mayor, " (posicion ", posMayor, ")";
    Escribir "Menor nota: ", menor, " (posicion ", posMenor, ")";
    Escribir "Aprobados (>= 3.0): ", aprobados, " de ", n;
FinAlgoritmo
