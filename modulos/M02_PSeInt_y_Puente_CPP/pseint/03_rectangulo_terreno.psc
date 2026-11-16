// Modulo 02 - Ejemplo 03: Area y perimetro de un terreno rectangular
// Objetivo: Calcular multiples salidas a partir de dos entradas reales

Algoritmo RectanguloTerreno
    Definir base, altura, area, perimetro Como Real;

    Escribir "=== AREA Y PERIMETRO DE UN TERRENO ===";
    Escribir "Ingresa el ancho (base) en metros:";
    Leer base;

    Escribir "Ingresa el largo (altura) en metros:";
    Leer altura;

    area <- base * altura;
    perimetro <- 2.0 * (base + altura);

    Escribir "Area del terreno: ", area, " m2";
    Escribir "Perimetro del terreno: ", perimetro, " m";
FinAlgoritmo
