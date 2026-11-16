// ============================================================================
// Modulo 03 - Problema Resuelto 06: Factura Comercial con Descuento e IVA
// Conceptos: Cadena, Caracter, const TASA_IVA, orden de operaciones financieras
// ============================================================================
Algoritmo FacturaIVA
    Definir categoria Como Caracter;
    Definir producto Como Cadena;
    Definir cantidad Como Entero;
    Definir precioUnitario, porcDescuento Como Real;
    Definir subtotal, descuento, baseGravable, valorIva, totalPagar Como Real;
    Definir TASA_IVA Como Real;

    TASA_IVA <- 0.19;

    Escribir "=== FACTURACION TIENDA UNIVERSITARIA ===";
    Escribir "Ingrese letra de categoria (A/B/C): ";
    Leer categoria;
    Escribir "Ingrese nombre del producto: ";
    Leer producto;
    Escribir "Ingrese precio unitario sin IVA: ";
    Leer precioUnitario;
    Escribir "Ingrese cantidad comprada: ";
    Leer cantidad;
    Escribir "Ingrese porcentaje de descuento (ej. 10 para 10%): ";
    Leer porcDescuento;

    subtotal <- precioUnitario * cantidad;
    descuento <- subtotal * (porcDescuento / 100);
    baseGravable <- subtotal - descuento;
    valorIva <- baseGravable * TASA_IVA;
    totalPagar <- baseGravable + valorIva;

    Escribir "=== TIRILLA DE PAGO ===";
    Escribir "Categoria     : ", categoria;
    Escribir "Producto      : ", producto;
    Escribir "Subtotal      : $", subtotal;
    Escribir "Descuento     : -$", descuento;
    Escribir "Base gravable : $", baseGravable;
    Escribir "IVA (19%)     : +$", valorIva;
    Escribir "TOTAL A PAGAR : $", totalPagar;
FinAlgoritmo
