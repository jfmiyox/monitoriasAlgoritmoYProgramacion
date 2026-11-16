// ============================================================================
// Modulo 03 - Problema Resuelto 03: Promedio Ponderado con Nombre Completo
// Conceptos: Cadena, Real, Entero, ponderacion de cortes
// ============================================================================
Algoritmo PromedioPonderado
    Definir codigo Como Entero;
    Definir nombreCompleto Como Cadena;
    Definir nota1, nota2, nota3, definitiva Como Real;
    Definir PESO1, PESO2, PESO3 Como Real;

    PESO1 <- 0.30;
    PESO2 <- 0.30;
    PESO3 <- 0.40;

    Escribir "=== CALCULO DE NOTA DEFINITIVA (30% + 30% + 40%) ===";
    Escribir "Ingrese el codigo numerico del estudiante: ";
    Leer codigo;
    Escribir "Ingrese el nombre completo del estudiante: ";
    Leer nombreCompleto;

    Escribir "Ingrese nota Corte 1 (0.0 a 5.0): ";
    Leer nota1;
    Escribir "Ingrese nota Corte 2 (0.0 a 5.0): ";
    Leer nota2;
    Escribir "Ingrese nota Corte 3 (0.0 a 5.0): ";
    Leer nota3;

    definitiva <- (nota1 * PESO1) + (nota2 * PESO2) + (nota3 * PESO3);

    Escribir "--- BOLETIN ACADEMICO ---";
    Escribir "Codigo     : ", codigo;
    Escribir "Estudiante : ", nombreCompleto;
    Escribir "Definitiva : ", definitiva;
FinAlgoritmo
