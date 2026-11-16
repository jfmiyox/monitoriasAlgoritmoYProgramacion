// ============================================================================
// Modulo 04 - Problema Resuelto 01: El Portero Numerico (Signo, Paridad y Multiplo)
// Estructuras: Escalera Si...SiNo (mutuamente excluyente) + Si independientes
// ============================================================================
Algoritmo PorteroNumerico
    Definir numero Como Entero;

    Escribir "=== EL PORTERO NUMERICO ===";
    Escribir "Ingrese un numero entero (ej. -15, 0, 10, 7): ";
    Leer numero;

    // 1) Signo: escalera mutuamente excluyente (solo entra a una rama)
    Si numero > 0 Entonces
        Escribir "1. Signo      : El numero es POSITIVO.";
    SiNo
        Si numero < 0 Entonces
            Escribir "1. Signo      : El numero es NEGATIVO.";
        SiNo
            Escribir "1. Signo      : El numero es CERO (neutro).";
        FinSi
    FinSi

    // 2) Paridad: condicion independiente (usa operador MOD)
    Si numero MOD 2 = 0 Entonces
        Escribir "2. Paridad    : Es PAR.";
    SiNo
        Escribir "2. Paridad    : Es IMPAR.";
    FinSi

    // 3) Multiplo de 5: condicion independiente
    Si numero MOD 5 = 0 Entonces
        Escribir "3. Multiplo 5 : SI es multiplo de 5.";
    SiNo
        Escribir "3. Multiplo 5 : NO es multiplo de 5.";
    FinSi
FinAlgoritmo
