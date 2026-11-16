// ============================================================================
// Modulo 03 - Problema Resuelto 05: Ficha Salud e Indice de Masa Corporal
// Conceptos: Caracter, Logico, Entero a Real, calculo de IMC
// ============================================================================
Algoritmo CalculoIMC
    Definir sexo Como Caracter;
    Definir haceDeporte Como Logico;
    Definir estaturaCm Como Entero;
    Definir pesoKg, estaturaM, imc Como Real;

    Escribir "=== FICHA MEDICA Y CALCULO DE IMC ===";
    Escribir "Ingrese inicial del sexo (M / F): ";
    Leer sexo;
    Escribir "Practica deporte regularmente? (Verdadero / Falso): ";
    Leer haceDeporte;
    Escribir "Ingrese peso en kilogramos (ej. 68.5): ";
    Leer pesoKg;
    Escribir "Ingrese estatura en CENTIMETROS enteros (ej. 175): ";
    Leer estaturaCm;

    estaturaM <- estaturaCm / 100;
    imc <- pesoKg / (estaturaM * estaturaM);

    Escribir "--- RESUMEN DE SALUD ---";
    Escribir "Sexo              : ", sexo;
    Escribir "Deportista activo : ", haceDeporte;
    Escribir "Estatura (m)      : ", estaturaM;
    Escribir "IMC calculado     : ", imc;
FinAlgoritmo
