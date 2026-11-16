// ============================================================================
// Modulo 04 - Problema Resuelto 07: Existencia y Clasificacion de Triangulo
// Conceptos: Validacion geometrica con Y, clasificacion con O, Pitagoras con tolerancia
// ============================================================================
Algoritmo ClasificadorTriangulo
    Definir a, b, c, eps Como Real;
    Definir rectA, rectB, rectC Como Logico;

    eps <- 0.000001;

    Escribir "=== CLASIFICADOR DE TRIANGULOS ===";
    Escribir "Ingrese lado a: ";
    Leer a;
    Escribir "Ingrese lado b: ";
    Leer b;
    Escribir "Ingrese lado c: ";
    Leer c;

    Si a <= 0 O b <= 0 O c <= 0 Entonces
        Escribir "ERROR: Todos los lados deben ser estrictamente positivos (> 0).";
    SiNo
        Si NO ((a + b > c) Y (a + c > b) Y (b + c > a)) Entonces
            Escribir "NO EXISTE: Los lados no cumplen la desigualdad triangular.";
        SiNo
            // 1) Clasificacion segun sus lados
            Si a = b Y b = c Entonces
                Escribir "Tipo por lados    : EQUILATERO (tres lados iguales).";
            SiNo
                Si a = b O a = c O b = c Entonces
                    Escribir "Tipo por lados    : ISOSCELES (dos lados iguales).";
                SiNo
                    Escribir "Tipo por lados    : ESCALENO (todos los lados distintos).";
                FinSi
            FinSi

            // 2) Verificacion de triangulo rectangulo con tolerancia para decimales
            rectA <- abs((b * b + c * c) - (a * a)) < eps;
            rectB <- abs((a * a + c * c) - (b * b)) < eps;
            rectC <- abs((a * a + b * b) - (c * c)) < eps;

            Si rectA O rectB O rectC Entonces
                Escribir "Angulo recto      : SI es un triangulo RECTANGULO.";
            SiNo
                Escribir "Angulo recto      : NO es un triangulo rectangulo.";
            FinSi
        FinSi
    FinSi
FinAlgoritmo
