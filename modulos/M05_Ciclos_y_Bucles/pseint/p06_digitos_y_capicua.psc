Algoritmo DigitosYCapicua
    Definir n, aux, cantidadDigitos, sumaDigitos, invertido, digito Como Entero;

    Escribir "=== ANALISIS DE DIGITOS Y NUMERO CAPICUA ===";
    Repetir
        Escribir "Ingrese un numero entero no negativo (>= 0):";
        Leer n;
        Si n < 0 Entonces
            Escribir "Error: el numero debe ser mayor o igual a 0.";
        FinSi
    Hasta Que n >= 0

    aux <- n;
    cantidadDigitos <- 0;
    sumaDigitos <- 0;
    invertido <- 0;

    // Usamos Repetir...Hasta Que para que n = 0 tambien cuente 1 digito
    Repetir
        digito <- aux MOD 10;
        cantidadDigitos <- cantidadDigitos + 1;
        sumaDigitos <- sumaDigitos + digito;
        invertido <- invertido * 10 + digito;
        aux <- trunc(aux / 10);
    Hasta Que aux = 0

    Escribir "Resultados para n = ", n, ":";
    Escribir "Cantidad de digitos: ", cantidadDigitos;
    Escribir "Suma de digitos: ", sumaDigitos;
    Escribir "Numero invertido: ", invertido;
    Si invertido = n Entonces
        Escribir "Es capicua: SI";
    SiNo
        Escribir "Es capicua: NO";
    FinSi
FinAlgoritmo
