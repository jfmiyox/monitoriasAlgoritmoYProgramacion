Algoritmo TablaMultiplicar
    Definir n, i, producto, sumaProductos Como Entero;

    sumaProductos <- 0;
    Escribir "=== TABLA DE MULTIPLICAR (CICLO PARA) ===";
    Escribir "Ingrese un numero entero para ver su tabla del 1 al 10:";
    Leer n;

    Escribir "Tabla del ", n, ":";
    Para i <- 1 Hasta 10 Con Paso 1 Hacer
        producto <- n * i;
        Escribir n, " x ", i, " = ", producto;
        sumaProductos <- sumaProductos + producto;
    FinPara

    Escribir "Suma de los 10 productos: ", sumaProductos;
FinAlgoritmo
