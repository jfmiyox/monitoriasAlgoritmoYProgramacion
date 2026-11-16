// ============================================================================
// Modulo 04 - Problema Resuelto 02: Filtro de Beca Universitaria
// Conceptos: Logica booleana (Y, O, NO), validacion de rangos (A <= x Y x <= B)
// ============================================================================
Algoritmo FiltroBecaUniversitaria
    Definir edad, estrato, sancionInput Como Entero;
    Definir promedio Como Real;
    Definir tieneSancion, datosValidos Como Logico;

    Escribir "=== FILTRO DE BECA UNIVERSITARIA ===";
    Escribir "Edad del estudiante (15 a 80): ";
    Leer edad;
    Escribir "Promedio acumulado (0.0 a 5.0): ";
    Leer promedio;
    Escribir "Estrato socioeconomico (1 a 6): ";
    Leer estrato;
    Escribir "Tiene sancion disciplinaria vigente? (1 = Si, 0 = No): ";
    Leer sancionInput;

    // Validacion de rangos: NUNCA escribir 15 <= edad <= 80 en C++
    datosValidos <- (15 <= edad Y edad <= 80) Y (0.0 <= promedio Y promedio <= 5.0) Y (1 <= estrato Y estrato <= 6) Y (sancionInput = 0 O sancionInput = 1);

    Si NO datosValidos Entonces
        Escribir "ERROR: Alguno de los datos ingresados esta fuera de rango.";
    SiNo
        tieneSancion <- (sancionInput = 1);

        Si tieneSancion Entonces
            Escribir "RESULTADO: Beca RECHAZADA por sancion disciplinaria vigente.";
        SiNo
            Si promedio >= 4.5 Y (estrato = 1 O estrato = 2) Entonces
                Escribir "RESULTADO: Beca COMPLETA (100% de la matricula).";
            SiNo
                Si promedio >= 4.0 Y estrato <= 3 Entonces
                    Escribir "RESULTADO: MEDIA Beca (50% de la matricula).";
                SiNo
                    Si promedio >= 4.7 Entonces
                        Escribir "RESULTADO: Bono de EXCELENCIA ACADEMICA (25%).";
                    SiNo
                        Escribir "RESULTADO: No cumple requisitos de promedio/estrato.";
                    FinSi
                FinSi
            FinSi
        FinSi
    FinSi
FinAlgoritmo
