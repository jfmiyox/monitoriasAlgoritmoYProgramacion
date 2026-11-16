// Modulo 02 - Ejemplo 05: Factura sencilla de cafeteria
// Objetivo: Combinar variables enteras (cantidad) y reales (precios y propina)

Algoritmo FacturaCafeteria
    Definir cantidad Como Entero;
    Definir precioUnitario, subtotal, propina, totalPagar Como Real;

    Escribir "=== CAJA REGISTRADORA DE CAFETERIA ===";
    Escribir "Ingresa el precio unitario del producto:";
    Leer precioUnitario;

    Escribir "Ingresa la cantidad comprada:";
    Leer cantidad;

    subtotal <- precioUnitario * cantidad;
    propina <- subtotal * 0.10;
    totalPagar <- subtotal + propina;

    Escribir "Subtotal: $", subtotal;
    Escribir "Propina sugerida (10%): $", propina;
    Escribir "Total a pagar: $", totalPagar;
FinAlgoritmo
