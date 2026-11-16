Algoritmo ReservaCine5x6
    // Sala fija de 5 filas x 6 columnas (en PSeInt: filas 1..5, cols 1..6)
    Definir FILAS, COLS, i, j, opcion, f, c, ocupadas, libres, total Como Entero;
    Definir porcentaje Como Real;
    Dimension sala[5, 6];

    FILAS <- 5;
    COLS <- 6;

    Para i <- 1 Hasta FILAS Con Paso 1 Hacer
        Para j <- 1 Hasta COLS Con Paso 1 Hacer
            sala[i, j] <- "L";
        FinPara
    FinPara

    Repetir
        Escribir "=== SALA DE CINE 5x6 ===";
        Escribir "1. Ver mapa de sillas";
        Escribir "2. Reservar silla";
        Escribir "3. Estadisticas de ocupacion";
        Escribir "0. Salir";
        Escribir "Opcion: ";
        Leer opcion;

        Segun opcion Hacer
            1:
                Escribir "    C1 C2 C3 C4 C5 C6";
                Para i <- 1 Hasta FILAS Con Paso 1 Hacer
                    Escribir "F", i, " | " Sin Saltar;
                    Para j <- 1 Hasta COLS Con Paso 1 Hacer
                        Escribir sala[i, j], "  " Sin Saltar;
                    FinPara
                    Escribir "";
                FinPara
            2:
                Escribir "Ingrese fila (1 a ", FILAS, "): ";
                Leer f;
                Escribir "Ingrese columna (1 a ", COLS, "): ";
                Leer c;
                Si f < 1 O f > FILAS O c < 1 O c > COLS Entonces
                    Escribir "Error: coordenada fuera de la sala.";
                SiNo
                    Si sala[f, c] = "X" Entonces
                        Escribir "La silla (", f, ", ", c, ") ya esta ocupada.";
                    SiNo
                        sala[f, c] <- "X";
                        Escribir "Reserva confirmada para silla (", f, ", ", c, ").";
                    FinSi
                FinSi
            3:
                ocupadas <- 0;
                Para i <- 1 Hasta FILAS Con Paso 1 Hacer
                    Para j <- 1 Hasta COLS Con Paso 1 Hacer
                        Si sala[i, j] = "X" Entonces
                            ocupadas <- ocupadas + 1;
                        FinSi
                    FinPara
                FinPara
                total <- FILAS * COLS;
                libres <- total - ocupadas;
                porcentaje <- (ocupadas / total) * 100;
                Escribir "Ocupadas: ", ocupadas, " | Libres: ", libres, " | Ocupacion: ", porcentaje, "%";
            0:
                Escribir "Fin del sistema de reservas.";
            De Otro Modo:
                Escribir "Opcion invalida.";
        FinSegun
    Hasta Que opcion = 0
FinAlgoritmo
