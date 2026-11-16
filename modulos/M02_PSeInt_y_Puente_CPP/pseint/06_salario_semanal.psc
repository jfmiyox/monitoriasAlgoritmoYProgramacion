// Modulo 02 - Ejemplo 06: Calculo de salario semanal con bonificacion
// Objetivo: Traducir un problema de nomina basica paso a paso

Algoritmo SalarioSemanal
    Definir horasTrabajadas Como Entero;
    Definir pagoPorHora, bonoFijo, pagoBase, salarioTotal Como Real;

    Escribir "=== LIQUIDACION DE SALARIO SEMANAL ===";
    Escribir "Ingresa las horas trabajadas en la semana:";
    Leer horasTrabajadas;

    Escribir "Ingresa el valor pagado por hora:";
    Leer pagoPorHora;

    Escribir "Ingresa el bono fijo de transporte:";
    Leer bonoFijo;

    pagoBase <- horasTrabajadas * pagoPorHora;
    salarioTotal <- pagoBase + bonoFijo;

    Escribir "Pago por horas: $", pagoBase;
    Escribir "Bono de transporte: $", bonoFijo;
    Escribir "Salario total a recibir: $", salarioTotal;
FinAlgoritmo
