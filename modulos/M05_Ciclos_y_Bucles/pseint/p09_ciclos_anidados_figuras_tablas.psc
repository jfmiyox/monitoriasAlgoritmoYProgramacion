Algoritmo CiclosAnidadosFigurasTablas
    Definir n, fila, col, esp, ast, i, j Como Entero;

    Escribir "=== CICLOS ANIDADOS: FIGURAS Y TABLA DE MULTIPLICAR ===";
    Repetir
        Escribir "Ingrese el tamano n (1 a 10):";
        Leer n;
        Si n < 1 O n > 10 Entonces
            Escribir "Error: n debe estar entre 1 y 10.";
        FinSi
    Hasta Que n >= 1 Y n <= 10

    Escribir "--- 1. Triangulo Rectangulo (", n, " filas) ---";
    Para fila <- 1 Hasta n Con Paso 1 Hacer
        Para col <- 1 Hasta fila Con Paso 1 Hacer
            Escribir Sin Saltar "* ";
        FinPara
        Escribir "";
    FinPara

    Escribir "--- 2. Piramide Centrada (", n, " filas) ---";
    Para fila <- 1 Hasta n Con Paso 1 Hacer
        Para esp <- 1 Hasta n - fila Con Paso 1 Hacer
            Escribir Sin Saltar " ";
        FinPara
        Para ast <- 1 Hasta 2 * fila - 1 Con Paso 1 Hacer
            Escribir Sin Saltar "*";
        FinPara
        Escribir "";
    FinPara

    Escribir "--- 3. Tabla de Multiplicar Cruzada (1..", n, ") ---";
    Para i <- 1 Hasta n Con Paso 1 Hacer
        Para j <- 1 Hasta n Con Paso 1 Hacer
            Escribir Sin Saltar i * j, "   ";
        FinPara
        Escribir "";
    FinPara
FinAlgoritmo
