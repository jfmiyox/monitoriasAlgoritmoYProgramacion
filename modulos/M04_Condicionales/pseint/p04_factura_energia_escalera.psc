// ============================================================================
// Modulo 04 - Problema Resuelto 04: Factura Escalonada de Energia Electrica
// Conceptos: Escalera Si...SiNo por tramos marginales + ajuste por estrato
// ============================================================================
Algoritmo FacturaEnergiaElectrica
    Definir consumo, estrato Como Entero;
    Definir subtotal, factor, ajuste, totalPagar Como Real;

    Escribir "=== FACTURA DE ENERGIA ELECTRICA ===";
    Escribir "Consumo del mes en kWh (entero >= 0): ";
    Leer consumo;
    Escribir "Estrato socioeconomico (1 a 6): ";
    Leer estrato;

    Si consumo < 0 O estrato < 1 O estrato > 6 Entonces
        Escribir "ERROR: El consumo debe ser >= 0 y el estrato entre 1 y 6.";
    SiNo
        // Escalera ordenada de menor a mayor para tramos marginales
        Si consumo <= 100 Entonces
            subtotal <- consumo * 450.0;
        SiNo
            Si consumo <= 250 Entonces
                subtotal <- (100 * 450.0) + (consumo - 100) * 600.0;
            SiNo
                Si consumo <= 450 Entonces
                    subtotal <- (100 * 450.0) + (150 * 600.0) + (consumo - 250) * 800.0;
                SiNo
                    subtotal <- (100 * 450.0) + (150 * 600.0) + (200 * 800.0) + (consumo - 450) * 1050.0;
                FinSi
            FinSi
        FinSi

        // Factor segun estrato: 1 (-40%), 2 (-25%), 3 (-10%), 4 (0%), 5-6 (+20%)
        Segun estrato Hacer
            1:
                factor <- 0.60;
            2:
                factor <- 0.75;
            3:
                factor <- 0.90;
            4:
                factor <- 1.00;
            De Otro Modo:
                factor <- 1.20;
        FinSegun

        totalPagar <- subtotal * factor;
        ajuste <- totalPagar - subtotal;

        Escribir "--- RESUMEN DE FACTURA ---";
        Escribir "Subtotal base      : $", subtotal;
        Escribir "Ajuste por estrato : $", ajuste;
        Escribir "TOTAL A PAGAR      : $", totalPagar;
    FinSi
FinAlgoritmo
