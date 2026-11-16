Algoritmo BusquedaInventario
    // Dos vectores paralelos estaticos (indices de 1 a n en PSeInt)
    Definir MAX, n, i, codigoBuscado, pos Como Entero;
    Definir encontrado Como Logico;
    Dimension codigos[40];
    Dimension precios[40];

    MAX <- 40;

    Repetir
        Escribir "Cantidad de productos a registrar (1 a ", MAX, "): ";
        Leer n;
        Si n < 1 O n > MAX Entonces
            Escribir "Error: cantidad fuera del rango permitido.";
        FinSi
    Hasta Que n >= 1 Y n <= MAX

    Para i <- 1 Hasta n Con Paso 1 Hacer
        Escribir "Producto #", i, " - Codigo entero: ";
        Leer codigos[i];
        Escribir "Producto #", i, " - Precio: ";
        Leer precios[i];
    FinPara

    Escribir "Ingrese el codigo del producto a buscar: ";
    Leer codigoBuscado;

    // Busqueda secuencial con bandera logica
    encontrado <- Falso;
    pos <- -1;
    i <- 1;

    Mientras i <= n Y NO encontrado Hacer
        Si codigos[i] = codigoBuscado Entonces
            encontrado <- Verdadero;
            pos <- i;
        SiNo
            i <- i + 1;
        FinSi
    FinMientras

    Si encontrado Entonces
        Escribir "Producto ENCONTRADO en la posicion ", pos, " | Precio: $", precios[pos];
    SiNo
        Escribir "El codigo ", codigoBuscado, " NO existe en el inventario.";
    FinSi
FinAlgoritmo
