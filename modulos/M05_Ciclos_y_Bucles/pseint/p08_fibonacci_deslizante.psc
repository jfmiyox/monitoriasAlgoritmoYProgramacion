Algoritmo FibonacciDeslizante
    Definir n, i, cantidadPares Como Entero;
    Definir a, b, siguiente, sumaTotal Como Real;

    Escribir "=== SERIE DE FIBONACCI CON VARIABLES DESLIZANTES ===";
    Repetir
        Escribir "Cuantos terminos desea generar? (1 a 50):";
        Leer n;
        Si n < 1 O n > 50 Entonces
            Escribir "Error: elija un valor entre 1 y 50.";
        FinSi
    Hasta Que n >= 1 Y n <= 50

    a <- 0;
    b <- 1;
    sumaTotal <- 0;
    cantidadPares <- 0;

    Escribir "Serie (", n, " terminos):";
    Para i <- 1 Hasta n Con Paso 1 Hacer
        Si i < n Entonces
            Escribir Sin Saltar a, ", ";
        SiNo
            Escribir a;
        FinSi

        sumaTotal <- sumaTotal + a;
        Si a MOD 2 = 0 Entonces
            cantidadPares <- cantidadPares + 1;
        FinSi

        siguiente <- a + b;
        a <- b;
        b <- siguiente;
    FinPara

    Escribir "Suma de los ", n, " terminos: ", sumaTotal;
    Escribir "Terminos pares en la serie: ", cantidadPares;
FinAlgoritmo
