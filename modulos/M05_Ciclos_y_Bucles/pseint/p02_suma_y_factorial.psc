Algoritmo SumaYFactorial
    Definir n, i Como Entero;
    Definir suma, factorial Como Real;

    Escribir "=== SUMA Y FACTORIAL DE 1 A N ===";

    // En PSeInt: Hasta Que indica la condicion de SALIDA (cuando n es valido)
    Repetir
        Escribir "Ingrese un entero n (entre 0 y 20):";
        Leer n;
        Si n < 0 O n > 20 Entonces
            Escribir "Valor fuera de rango. Intente nuevamente.";
        FinSi
    Hasta Que n >= 0 Y n <= 20

    suma <- 0;
    factorial <- 1;

    Para i <- 1 Hasta n Con Paso 1 Hacer
        suma <- suma + i;
        factorial <- factorial * i;
    FinPara

    Escribir "Resultados para n = ", n, ":";
    Escribir "Suma de 1 hasta ", n, " = ", suma;
    Escribir "Factorial ", n, "! = ", factorial;
FinAlgoritmo
