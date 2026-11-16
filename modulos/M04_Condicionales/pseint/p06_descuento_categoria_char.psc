// ============================================================================
// Modulo 04 - Problema Resuelto 06: Tienda TechStore (Descuento por Categoria)
// Conceptos: Segun sobre Caracter con multiples valores + Si adicional por monto
// ============================================================================
Algoritmo DescuentoCategoriaChar
    Definir montoCompra, porcentaje, descuento, totalPagar Como Real;
    Definir categoria Como Caracter;
    Definir nombreCat Como Cadena;
    Definir categoriaValida, bonoAplicado Como Logico;

    Escribir "=== TIENDA TECHSTORE ===";
    Escribir "Ingrese el monto de la compra ($): ";
    Leer montoCompra;
    Escribir "Categoria del cliente (A = VIP, B = Frecuente, C = Nuevo): ";
    Leer categoria;

    Si montoCompra <= 0 Entonces
        Escribir "ERROR: El monto de compra debe ser mayor a cero.";
    SiNo
        categoriaValida <- Verdadero;
        porcentaje <- 0.0;
        nombreCat <- "";

        // En PSeInt, Segun acepta varios valores separados por coma en el mismo caso
        Segun categoria Hacer
            'a', 'A':
                porcentaje <- 20.0;
                nombreCat <- "VIP";
            'b', 'B':
                porcentaje <- 12.0;
                nombreCat <- "Frecuente";
            'c', 'C':
                porcentaje <- 5.0;
                nombreCat <- "Nuevo";
            De Otro Modo:
                categoriaValida <- Falso;
        FinSegun

        Si NO categoriaValida Entonces
            Escribir "ERROR: Categoria no reconocida. Use A, B o C.";
        SiNo
            bonoAplicado <- Falso;
            Si montoCompra > 500000.0 Entonces
                porcentaje <- porcentaje + 5.0;
                bonoAplicado <- Verdadero;
            FinSi

            descuento <- montoCompra * (porcentaje / 100.0);
            totalPagar <- montoCompra - descuento;

            Escribir "--- TIRILLA DE COMPRA ---";
            Escribir "Categoria         : ", nombreCat;
            Escribir "Bono > $500.000   : ", bonoAplicado;
            Escribir "Descuento total % : ", porcentaje, "%";
            Escribir "Valor descontado  : $", descuento;
            Escribir "TOTAL A PAGAR     : $", totalPagar;
        FinSi
    FinSi
FinAlgoritmo
