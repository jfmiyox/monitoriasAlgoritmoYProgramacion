Algoritmo BoletinNotas
    // Matriz estatica en PSeInt: indices de 1..f y 1..c por defecto
    Definir MAX_EST, MAX_MAT, f, c, i, j, filaMayor, colMayor Como Entero;
    Definir sumaEst, sumaMat, mayor Como Real;
    Dimension notas[30, 10]; // Capacidad fisica fija 30x10

    MAX_EST <- 30;
    MAX_MAT <- 10;

    Repetir
        Escribir "Cantidad de estudiantes (1 a ", MAX_EST, "): ";
        Leer f;
    Hasta Que f >= 1 Y f <= MAX_EST

    Repetir
        Escribir "Cantidad de materias (1 a ", MAX_MAT, "): ";
        Leer c;
    Hasta Que c >= 1 Y c <= MAX_MAT

    // 1. Lectura por filas
    Para i <- 1 Hasta f Con Paso 1 Hacer
        Escribir "--- Estudiante ", i, " ---";
        Para j <- 1 Hasta c Con Paso 1 Hacer
            Repetir
                Escribir "Nota materia [", j, "] (0.0 a 5.0): ";
                Leer notas[i, j];
            Hasta Que notas[i, j] >= 0 Y notas[i, j] <= 5
        FinPara
    FinPara

    // 2. Promedio por estudiante (recorrido POR FILAS)
    Escribir "=== PROMEDIO POR ESTUDIANTE ===";
    Para i <- 1 Hasta f Con Paso 1 Hacer
        sumaEst <- 0;
        Para j <- 1 Hasta c Con Paso 1 Hacer
            sumaEst <- sumaEst + notas[i, j];
        FinPara
        Escribir "Estudiante ", i, ": ", sumaEst / c;
    FinPara

    // 3. Promedio por materia (recorrido POR COLUMNAS)
    Escribir "=== PROMEDIO POR MATERIA ===";
    Para j <- 1 Hasta c Con Paso 1 Hacer
        sumaMat <- 0;
        Para i <- 1 Hasta f Con Paso 1 Hacer
            sumaMat <- sumaMat + notas[i, j];
        FinPara
        Escribir "Materia ", j, ": ", sumaMat / f;
    FinPara

    // 4. Mayor nota global con coordenadas
    mayor <- notas[1, 1];
    filaMayor <- 1;
    colMayor <- 1;

    Para i <- 1 Hasta f Con Paso 1 Hacer
        Para j <- 1 Hasta c Con Paso 1 Hacer
            Si notas[i, j] > mayor Entonces
                mayor <- notas[i, j];
                filaMayor <- i;
                colMayor <- j;
            FinSi
        FinPara
    FinPara

    Escribir "Mejor nota del curso: ", mayor, " en (estudiante=", filaMayor, ", materia=", colMayor, ")";
FinAlgoritmo
