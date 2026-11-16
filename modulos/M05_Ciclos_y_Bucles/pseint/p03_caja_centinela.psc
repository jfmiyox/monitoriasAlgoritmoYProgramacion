Algoritmo CajaCentinela
    Definir precio, total, promedio Como Real;
    Definir cantidad Como Entero;

    total <- 0;
    cantidad <- 0;

    Escribir "=== CAJA REGISTRADORA CON CENTINELA (CICLO MIENTRAS) ===";
    Escribir "Ingrese el precio de cada producto (0 para terminar):";
    Leer precio;

    Mientras precio <> 0 Hacer
        Si precio < 0 Entonces
            Escribir "Advertencia: precio negativo ignorado (", precio, ").";
        SiNo
            total <- total + precio;
            cantidad <- cantidad + 1;
        FinSi
        Escribir "Ingrese siguiente precio (0 para terminar):";
        Leer precio;
    FinMientras

    Escribir "=== RESUMEN DE COMPRA ===";
    Si cantidad = 0 Entonces
        Escribir "No se registraron productos validos.";
    SiNo
        promedio <- total / cantidad;
        Escribir "Productos validos: ", cantidad;
        Escribir "Total a pagar: $", total;
        Escribir "Precio promedio: $", promedio;
    FinSi
FinAlgoritmo
