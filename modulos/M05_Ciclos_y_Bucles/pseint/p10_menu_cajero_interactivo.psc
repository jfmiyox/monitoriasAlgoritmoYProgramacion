Algoritmo MenuCajeroInteractivo
    Definir saldo, totalConsignado, totalRetirado, monto Como Real;
    Definir operacionesExitosas, opcion Como Entero;

    saldo <- 100000;
    totalConsignado <- 0;
    totalRetirado <- 0;
    operacionesExitosas <- 0;

    Escribir "=== CAJERO AUTOMATICO (MENU REPETIR + SEGUN) ===";

    // TRAMPA: en PSeInt TERMINA cuando opcion = 4 es VERDADERO
    Repetir
        Escribir "--- MENU PRINCIPAL ---";
        Escribir "1. Consultar saldo";
        Escribir "2. Consignar dinero";
        Escribir "3. Retirar dinero";
        Escribir "4. Salir";
        Escribir "Elija una opcion (1-4):";
        Leer opcion;

        Segun opcion Hacer
            1:
                Escribir "Saldo actual disponible: $", saldo;
            2:
                Escribir "Ingrese monto a consignar:";
                Leer monto;
                Si monto <= 0 Entonces
                    Escribir "Error: el monto a consignar debe ser positivo.";
                SiNo
                    saldo <- saldo + monto;
                    totalConsignado <- totalConsignado + monto;
                    operacionesExitosas <- operacionesExitosas + 1;
                    Escribir "Consignacion exitosa. Nuevo saldo: $", saldo;
                FinSi
            3:
                Escribir "Ingrese monto a retirar:";
                Leer monto;
                Si monto <= 0 Entonces
                    Escribir "Error: el monto a retirar debe ser positivo.";
                SiNo
                    Si monto > saldo Entonces
                        Escribir "Fondos insuficientes. Saldo disponible: $", saldo;
                    SiNo
                        saldo <- saldo - monto;
                        totalRetirado <- totalRetirado + monto;
                        operacionesExitosas <- operacionesExitosas + 1;
                        Escribir "Retiro exitoso. Nuevo saldo: $", saldo;
                    FinSi
                FinSi
            4:
                Escribir "Saliendo del cajero...";
            De Otro Modo:
                Escribir "Opcion invalida. Por favor elija entre 1 y 4.";
        FinSegun
    Hasta Que opcion = 4

    Escribir "=== RESUMEN DE SESION ===";
    Escribir "Transacciones monetarias exitosas: ", operacionesExitosas;
    Escribir "Total consignado: $", totalConsignado;
    Escribir "Total retirado: $", totalRetirado;
    Escribir "Saldo final: $", saldo;
FinAlgoritmo
