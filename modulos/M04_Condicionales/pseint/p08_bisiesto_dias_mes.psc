// ============================================================================
// Modulo 04 - Problema Resuelto 08: Anio Bisiesto y Dias del Mes
// Conceptos: Formula booleana compuesta + Segun agrupado + Si dentro de caso 2
// ============================================================================
Algoritmo BisiestoDiasMes
    Definir mes, anio, dias Como Entero;
    Definir esBisiesto Como Logico;

    Escribir "=== CALENDARIO MAESTRO: BISIESTO Y DIAS DEL MES ===";
    Escribir "Ingrese el numero del mes (1 a 12): ";
    Leer mes;
    Escribir "Ingrese el anio (entero > 0): ";
    Leer anio;

    Si (mes < 1 O mes > 12) O anio <= 0 Entonces
        Escribir "ERROR: El mes debe estar entre 1 y 12, y el anio debe ser > 0.";
    SiNo
        esBisiesto <- (anio MOD 4 = 0 Y anio MOD 100 <> 0) O (anio MOD 400 = 0);

        Segun mes Hacer
            1, 3, 5, 7, 8, 10, 12:
                dias <- 31;
            4, 6, 9, 11:
                dias <- 30;
            2:
                Si esBisiesto Entonces
                    dias <- 29;
                SiNo
                    dias <- 28;
                FinSi
        FinSegun

        Si esBisiesto Entonces
            Escribir "El anio ", anio, " SI es bisiesto.";
        SiNo
            Escribir "El anio ", anio, " NO es bisiesto.";
        FinSi
        Escribir "El mes ", mes, " del anio ", anio, " tiene ", dias, " dias.";
    FinSi
FinAlgoritmo
