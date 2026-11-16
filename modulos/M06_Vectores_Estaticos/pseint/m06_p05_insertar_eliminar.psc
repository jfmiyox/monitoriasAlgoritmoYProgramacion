Algoritmo InsertarEliminarLista
    // Capacidad fija MAX = 10, tamano logico n, indices 1..n en PSeInt
    Definir MAX, n, i, opcion, pos, valor, eliminado Como Entero;
    Dimension lista[10];

    MAX <- 10;

    Repetir
        Escribir "Cantidad inicial de elementos (0 a ", MAX, "): ";
        Leer n;
    Hasta Que n >= 0 Y n <= MAX

    Si n > 0 Entonces
        Para i <- 1 Hasta n Con Paso 1 Hacer
            Escribir "Elemento[", i, "]: ";
            Leer lista[i];
        FinPara
    FinSi

    Repetir
        Escribir "--- GESTOR DE LISTA ESTATICA (", n, "/", MAX, " usados) ---";
        Escribir "1. Mostrar arreglo";
        Escribir "2. Insertar en posicion";
        Escribir "3. Eliminar de posicion";
        Escribir "0. Salir";
        Escribir "Opcion: ";
        Leer opcion;

        Segun opcion Hacer
            1:
                Si n = 0 Entonces
                    Escribir "Lista vacia.";
                SiNo
                    Para i <- 1 Hasta n Con Paso 1 Hacer
                        Escribir lista[i], " " Sin Saltar;
                    FinPara
                    Escribir "";
                FinSi
            2:
                Si n = MAX Entonces
                    Escribir "No se puede insertar: capacidad MAX (", MAX, ") llena.";
                SiNo
                    Escribir "Posicion a insertar (1 a ", n + 1, "): ";
                    Leer pos;
                    Si pos < 1 O pos > n + 1 Entonces
                        Escribir "Posicion invalida.";
                    SiNo
                        Escribir "Valor entero a insertar: ";
                        Leer valor;
                        Para i <- n + 1 Hasta pos + 1 Con Paso -1 Hacer
                            lista[i] <- lista[i - 1];
                        FinPara
                        lista[pos] <- valor;
                        n <- n + 1;
                        Escribir "Insertado correctamente.";
                    FinSi
                FinSi
            3:
                Si n = 0 Entonces
                    Escribir "No se puede eliminar: lista vacia.";
                SiNo
                    Escribir "Posicion a eliminar (1 a ", n, "): ";
                    Leer pos;
                    Si pos < 1 O pos > n Entonces
                        Escribir "Posicion invalida.";
                    SiNo
                        eliminado <- lista[pos];
                        Para i <- pos Hasta n - 1 Con Paso 1 Hacer
                            lista[i] <- lista[i + 1];
                        FinPara
                        n <- n - 1;
                        Escribir "Elemento ", eliminado, " eliminado.";
                    FinSi
                FinSi
            0:
                Escribir "Saliendo del gestor.";
            De Otro Modo:
                Escribir "Opcion no reconocida.";
        FinSegun
    Hasta Que opcion = 0
FinAlgoritmo
