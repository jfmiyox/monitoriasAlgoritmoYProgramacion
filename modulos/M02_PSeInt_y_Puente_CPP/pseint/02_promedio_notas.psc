// Modulo 02 - Ejemplo 02: Promedio de tres calificaciones
// Objetivo: Usar variables reales (decimales) y parentesis en operaciones

Algoritmo PromedioNotas
    Definir nota1, nota2, nota3, suma, promedio Como Real;

    Escribir "=== CALCULADORA DE PROMEDIO DE NOTAS ===";
    Escribir "Ingresa la primera nota:";
    Leer nota1;

    Escribir "Ingresa la segunda nota:";
    Leer nota2;

    Escribir "Ingresa la tercera nota:";
    Leer nota3;

    suma <- nota1 + nota2 + nota3;
    promedio <- suma / 3.0;

    Escribir "Suma total de notas: ", suma;
    Escribir "Tu promedio final es: ", promedio;
FinAlgoritmo
