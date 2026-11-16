// ============================================================================
// Modulo 04 - Problema Resuelto 03: Podio de Tres Atletas
// Conceptos: Si anidados (arbol de decision), mayor, menor y deteccion de empates
// ============================================================================
Algoritmo PodioTresAtletas
    Definir a, b, c, mayor, menor Como Real;

    Escribir "=== PODIO DE TRES ATLETAS ===";
    Escribir "Ingrese el puntaje del atleta A: ";
    Leer a;
    Escribir "Ingrese el puntaje del atleta B: ";
    Leer b;
    Escribir "Ingrese el puntaje del atleta C: ";
    Leer c;

    // Arbol de decisiones anidadas para hallar el MAYOR
    Si a >= b Entonces
        Si a >= c Entonces
            mayor <- a;
        SiNo
            mayor <- c;
        FinSi
    SiNo
        Si b >= c Entonces
            mayor <- b;
        SiNo
            mayor <- c;
        FinSi
    FinSi

    // Arbol de decisiones anidadas para hallar el MENOR
    Si a <= b Entonces
        Si a <= c Entonces
            menor <- a;
        SiNo
            menor <- c;
        FinSi
    SiNo
        Si b <= c Entonces
            menor <- b;
        SiNo
            menor <- c;
        FinSi
    FinSi

    Escribir "Mayor puntaje registrado: ", mayor;
    Escribir "Menor puntaje registrado: ", menor;

    // Analisis de empates
    Si a = b Y b = c Entonces
        Escribir "Estado del podio: EMPATE TRIPLE (todos tienen ", mayor, ").";
    SiNo
        Si a = b O a = c O b = c Entonces
            Escribir "Estado del podio: EMPATE PARCIAL entre dos atletas.";
        SiNo
            Escribir "Estado del podio: Sin empates, los tres puntajes son distintos.";
        FinSi
    FinSi
FinAlgoritmo
