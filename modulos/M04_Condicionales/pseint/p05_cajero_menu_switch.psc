// ============================================================================
// Modulo 04 - Problema Resuelto 05: Cajero Automatico (Una Operacion)
// Conceptos: Segun (switch) con enteros + Si anidado para validar fondos
// ============================================================================
Algoritmo CajeroMenuSwitch
    Definir saldo, monto Como Real;
    Definir opcion Como Entero;

    Escribir "=== CAJERO AUTOMATICO (1 OPERACION) ===";
    Escribir "Ingrese el saldo inicial de la cuenta: ";
    Leer saldo;

    Si saldo < 0 Entonces
        Escribir "ERROR: El saldo inicial no puede ser negativo.";
    SiNo
        Escribir "--- MENU DE OPERACIONES ---";
        Escribir "1. Consultar saldo";
        Escribir "2. Consignar dinero";
        Escribir "3. Retirar dinero";
        Escribir "4. Salir";
        Escribir "Elija una opcion (1 a 4): ";
        Leer opcion;

        Segun opcion Hacer
            1:
                Escribir "Su saldo actual es: $", saldo;
            2:
                Escribir "Ingrese el monto a consignar: ";
                Leer monto;
                Si monto > 0 Entonces
                    saldo <- saldo + monto;
                    Escribir "Consignacion exitosa. Nuevo saldo: $", saldo;
                SiNo
                    Escribir "ERROR: El monto a consignar debe ser mayor a cero.";
                FinSi
            3:
                Escribir "Ingrese el monto a retirar: ";
                Leer monto;
                Si monto <= 0 Entonces
                    Escribir "ERROR: El monto a retirar debe ser mayor a cero.";
                SiNo
                    Si monto > saldo Entonces
                        Escribir "ERROR: Fondos insuficientes. Saldo disponible: $", saldo;
                    SiNo
                        saldo <- saldo - monto;
                        Escribir "Retiro exitoso. Nuevo saldo: $", saldo;
                    FinSi
                FinSi
            4:
                Escribir "Gracias por usar nuestro cajero. Hasta pronto.";
            De Otro Modo:
                Escribir "ERROR: Opcion invalida. Debe elegir entre 1 y 4.";
        FinSegun
    FinSi
FinAlgoritmo
