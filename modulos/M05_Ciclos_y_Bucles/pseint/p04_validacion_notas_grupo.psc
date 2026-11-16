Algoritmo ValidacionNotasGrupo
    Definir n, i, aprobados, reprobados Como Entero;
    Definir nota, sumaNotas, promedio Como Real;

    Escribir "=== REGISTRO DE NOTAS CON VALIDACION ===";

    // TRAMPA: en PSeInt TERMINA cuando n >= 1 es VERDADERO
    Repetir
        Escribir "Cuantos estudiantes hay en el grupo? (>= 1):";
        Leer n;
        Si n < 1 Entonces
            Escribir "Error: debe haber al menos 1 estudiante.";
        FinSi
    Hasta Que n >= 1

    sumaNotas <- 0;
    aprobados <- 0;
    reprobados <- 0;

    Para i <- 1 Hasta n Con Paso 1 Hacer
        // TRAMPA: en PSeInt TERMINA cuando la nota ya esta entre 0.0 y 5.0
        Repetir
            Escribir "Nota del estudiante ", i, " (0.0 a 5.0):";
            Leer nota;
            Si nota < 0.0 O nota > 5.0 Entonces
                Escribir "Nota invalida. Debe estar entre 0.0 y 5.0.";
            FinSi
        Hasta Que nota >= 0.0 Y nota <= 5.0

        sumaNotas <- sumaNotas + nota;
        Si nota >= 3.0 Entonces
            aprobados <- aprobados + 1;
        SiNo
            reprobados <- reprobados + 1;
        FinSi
    FinPara

    promedio <- sumaNotas / n;
    Escribir "=== REPORTE DEL GRUPO ===";
    Escribir "Estudiantes procesados: ", n;
    Escribir "Aprobados (>= 3.0): ", aprobados;
    Escribir "Reprobados (< 3.0): ", reprobados;
    Escribir "Promedio del grupo: ", promedio;
FinAlgoritmo
