//RUN: 20.468.370-0
//SECCION: 0-L-2
//FECHA: 14-07-19
//Arturo Cadenas
/*
Se importan las bibliotecas.
Se definen todas las funciones a utilizar.
Se ingresa al main declarando todas las variables a utilizar, para posteriormente ingresar a un while.
Esto genera que el programa se mantenga abierto hasta que el usuario determine lo contrario.
Se le mostraran las opciones y el usuario debe ingresar modo de juego.
Se deben seguir los pasos indicados por pantalla para el modo manual.
En el modo automatico se comienza a resolver inmediatamente al ingresar la opcion (este no termina en un tiempo prudente).
Luego de finalizar alguno de los modos, se le dara la opcion de si desea volver a jugar.
Dando la opcion de volver a elegir modo.
Se finaliza el programa cerrando el archivo y liberando la memoria.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
//Constantes: Dimension del tablero.
#define TAMANO 9

//Struct que guarda la informacion de las jaulas. Cantidad, valor a sumar y las coordenadas de cada una.
typedef struct jaulas
{
    int cantCeldas;
    int sumaCeldas;
    int **posiciones;

} jaulas;

/*
Objetivo: Validar si el dato ingresado es un numero entero.
Entrada: Cadena de caracteres.
Salida: Valor 1 indica que es entero, valor 0 indica que no es entero.
*/
int validar_numero(char numero[])
{
    int i;
    for (i = 0; i < strlen(numero); i++)
    {
        if (!(isdigit(numero[i])))
        {
            printf("\nINGRESE SOLO NUMEROS\n");
            return 0;
        }
    }
    return 1;
}

/*
Objetivo: Crear una matriz de la dimension deseada.
Entrada: Una matriz de enteros.
Salida: Una matriz cuadrada de enteros (0).
*/
int **crearMatriz(int **matriz)
{
    matriz = (int **)(malloc(TAMANO * sizeof(int *)));
    for (int i = 0; i < TAMANO; i++)
        matriz[i] = (int *)(malloc(TAMANO * sizeof(int)));

    for (int i = 0; i < TAMANO; i++)
    {
        for (int j = 0; j < TAMANO; j++)
        {
            matriz[i][j] = 0;
        }
    }

    return matriz;
}

/*
Objetivo: Mostrar por pantalla la matriz deseada.
Entrada: Matriz cuadrada de enteros.
Salida: No tiene.
*/
void imprimirMatriz(int **matriz)
{
    printf("-------------------------\n");
    for (int i = 0; i < TAMANO; i++)
    {
        printf("| ");
        for (int j = 0; j < TAMANO; j++)
        {
            printf("%d ", matriz[i][j]);
            if (((j + 1) % 3) == 0)
            {
                printf("| ");
            }
        }
        printf("\n");
        if (((i + 1) % 3) == 0)
        {
            printf("-------------------------\n");
        }
    }
    printf("\n");
}

/*
Objetivo: Verificar si los datos son validos en el sudoku.
Entrada: Matriz cuadrada de enteros, fila, columa y numero obtenido de el usuario.
Salida: Valor 1 indica que es valido, valor 0 indica que no es valido.
*/
int verificarSudoku(int **matriz, int fila, int columna, int numero)
{
    //Verificar si ya esta ocupado el espacio.
    if (matriz[fila][columna] != 0)
    {
        return 0;
    }
    //Verifico en fila o columna.
    for (int i = 0; i < TAMANO; i++)
    {
        if (matriz[fila][i] == numero)
        {
            return 0;
        }
        if (matriz[i][columna] == numero)
        {
            return 0;
        }
    }
    //Verifico en el cuadrante.
    int filaCuadrante = fila / 3;
    int columnaCuadrante = columna / 3;
    for (int i = filaCuadrante; i < filaCuadrante + 3; i++)
    {
        for (int j = columnaCuadrante; j < columnaCuadrante + 3; j++)
        {
            if (matriz[i][j] == numero)
            {
                return 0;
            }
        }
    }
    return 1;
}

/*
Objetivo: Verificar la suma de las jaulas.
Entrada: Matriz cuadrada de enteros, lista de struct, cantidad de jaulas.
Salida: Valor 1 indica que se cumple la condicion, valor 0 indica que no se cumple la condicion.
*/
int verificarSuma(int **matriz, jaulas *listaJaulas, int numeroJaulas)
{
    int jaulasVerificadas = 0;
    int contador;
    for (int i = 0; i < numeroJaulas; i++)
    {
        contador = 0;
        for (int j = 0; j < listaJaulas[i].cantCeldas; j++)
        {
            contador = contador + matriz[listaJaulas[i].posiciones[j][0]][listaJaulas[i].posiciones[j][1]];
        }
        if (contador == listaJaulas[i].sumaCeldas)
        {
            jaulasVerificadas = jaulasVerificadas + 1;
        }
    }

    if (jaulasVerificadas == numeroJaulas)
    {
        return 1;
    }
    return 0;
}

/*
Objetivo: LLenar la matriz con valores que indiquen el numero de cada una de las jaulas.
Entrada: Lista de struct, numero de jaulas y matriz cuadrada de enteros.
Salida: Matriz cuadrada de enteros con los datos deseados.
*/
int **rellenarTablero(jaulas *listaJaula, int numeroJaulas, int **tablero)
{
    int *jaulas = (int *)malloc(numeroJaulas * sizeof(int));
    for (int i = 0; i < numeroJaulas; i++)
    {
        for (int j = 0; j < listaJaula[i].cantCeldas; j++)
        {
            tablero[listaJaula[i].posiciones[j][0]][listaJaula[i].posiciones[j][1]] = i;
        }
        jaulas[i] = listaJaula[i].sumaCeldas;
    }
    return tablero;
}

/*
Objetivo: Mostrar el tablero que indica las jaulas.
Entrada: Matriz cuadrada de enteros.
Salida: No tiene.
*/
void mostrarTablero(int **tablero)
{
    for (int i = 0; i < TAMANO; i++)
    {
        for (int j = 0; j < TAMANO; j++)
        {
            if (tablero[i][j] / 10 == 0)
                printf("%d  ", tablero[i][j]);
            else
                printf("%d ", tablero[i][j]);
        }
        printf("\n");
    }
    return;
}

/*
Objetivo: Mostrar por pantalla lo que debe sumar cada una de las jaulas.
Entrada: Lista de struct, numero de jaulas.
Salida: No tiene.
*/
void mostrarJaulas(jaulas *listaJaulas, int numeroJaulas)
{

    printf("El valor que deben sumar las jaulas son:\n");
    for (int i = 0; i < numeroJaulas; i++)
    {
        printf("Jaula %d: %d\n", i, listaJaulas[i].sumaCeldas);
    }
}

/*
Objetivo: Cambiar todos los valores de la matriz a 0.
Entrada: Matriz cuadrada de enteros.
Salida: Matriz cuadrada de enteros de valor 0.
*/
int **resetearMatrices(int **matriz)
{
    for (int i = 0; i < TAMANO; i++)
    {
        for (int j = 0; j < TAMANO; j++)
        {
            matriz[i][j] = 0;
        }
    }
    return matriz;
}

int main()
{
    //Declaracion de variables.
    FILE *archivo;
    int **matriz;
    int **matrizAutomatica;
    int **posicionesCeldas;
    int **tablero;
    jaulas *listaJaulas;
    jaulas nuevaJaula;
    //Se abre el archivo.
    archivo = fopen("adoku.in", "r");
    //Si el archivo esta vacio finalizo el programa.
    if (archivo == NULL)
    {
        printf("ERROR LECTURA DE ARCHIVO");
        return 0;
    }
    //Creo las matrices.
    matriz = crearMatriz(matriz);
    tablero = crearMatriz(tablero);
    matrizAutomatica = crearMatriz(matrizAutomatica);

    //Variables del archivo a abrir.
    int numeroJaulas, cantCeldas, sumaCeldas, filaCelda, columnaCelda;

    fscanf(archivo, "%d", &numeroJaulas);
    //printf("%d\n", numeroJaulas);

    //Creo una Lista de struct.
    listaJaulas = (jaulas *)(malloc(numeroJaulas * sizeof(jaulas)));

    //Obtengo los valores deseados del archivo.
    for (int i = 0; i < numeroJaulas; i++)
    {
        fscanf(archivo, "%d,%d", &cantCeldas, &sumaCeldas);
        //printf("%d,%d\n", cantCeldas, sumaCeldas);
        nuevaJaula.cantCeldas = cantCeldas;
        nuevaJaula.sumaCeldas = sumaCeldas;

        nuevaJaula.posiciones = (int **)malloc(cantCeldas * sizeof(int *));
        for (int j = 0; j < cantCeldas; j++)
        {
            nuevaJaula.posiciones[j] = (int *)malloc(2 * sizeof(int));
        }
        for (int j = 0; j < cantCeldas; j++)
        {
            fscanf(archivo, "%d,%d", &filaCelda, &columnaCelda);
            //printf("%d,%d\n", filaCelda, columnaCelda);
            nuevaJaula.posiciones[j][0] = filaCelda;
            nuevaJaula.posiciones[j][1] = columnaCelda;
        }
        //Agrego el struct a la lista de struct.
        listaJaulas[i] = nuevaJaula;
    }
    fclose(archivo); //Cierro el archivo.
    //Variables que van ciclando.
    int ciclar = 1;
    char modalidad, opcion, rejugar;
    char numero[5];
    int N;
    int filaBorrar, columnaBorrar;
    int filaIngresar, columnaIngresar;
    int valorAIngresar;

    //Le doy valores al tablero, con respecto a las jaulas.
    tablero = rellenarTablero(listaJaulas, numeroJaulas, tablero);

    while (ciclar == 1)
    {
        //Reseteo Matrices en 0.
        matriz = resetearMatrices(matriz);
        matrizAutomatica = resetearMatrices(matrizAutomatica);
        int contadorCasillas = 0; //Cantidad de casillas ingresadas.
        //Se ingresa modalidad.
        printf("Ingrese modalidad de juego J/A:\n");
        scanf("%s", &modalidad);
        if (modalidad == 'J' || modalidad == 'j')
        {
            //Se le muestran las matrices.
            mostrarTablero(tablero);
            mostrarJaulas(listaJaulas, numeroJaulas);
            imprimirMatriz(matriz);
            printf("Modalidad Ingresada: Un jugador\n");
            int opcionCiclar = 1;
            while (opcionCiclar == 1)
            {
                //Se le pide la opcion, fila, columna y valor a ingresar si es necesario, validando ademas la entrada.
                printf("Ingrese Opcion:\nBorrar (B)\nIngresar(I):\n");
                scanf("%s", &opcion);
                if (opcion == 'B' || opcion == 'b')
                {
                    int opcionBorrar = 1;
                    while (opcionBorrar == 1)
                    {
                        printf("Ingrese coordenadas de Celda a borrar, fila y luego columna [0-8]:\n");

                        do
                        {
                            printf("Ingrese Fila: ");
                            scanf("%s", numero);
                            N = validar_numero(numero);

                        } while (N == 0);
                        filaBorrar = atoi(numero);
                        N = 0;
                        do
                        {
                            printf("Ingrese Columna: ");
                            scanf("%s", numero);
                            N = validar_numero(numero);

                        } while (N == 0);
                        columnaBorrar = atoi(numero);

                        if (filaBorrar >= 0 && filaBorrar < 9 && columnaBorrar >= 0 && columnaBorrar < 9)
                        {
                            opcionBorrar = 0;
                            if (matriz[filaBorrar][columnaBorrar] != 0)
                            {
                                contadorCasillas = contadorCasillas - 1;
                            }
                            matriz[filaBorrar][columnaBorrar] = 0;
                        }
                    }
                }
                if (opcion == 'I' || opcion == 'i')
                {
                    int opcionIngresar = 1;
                    while (opcionIngresar == 1)
                    {
                        printf("Ingrese coordenadas de Celda a Ingresar, fila y luego columna [0-8]:\n");

                        do
                        {
                            printf("Ingrese Fila: ");
                            scanf("%s", numero);
                            N = validar_numero(numero);

                        } while (N == 0);
                        filaIngresar = atoi(numero);
                        N = 0;
                        do
                        {
                            printf("Ingrese Columna: ");
                            scanf("%s", numero);
                            N = validar_numero(numero);

                        } while (N == 0);
                        columnaIngresar = atoi(numero);

                        if (filaIngresar >= 0 && filaIngresar < 9 && columnaIngresar >= 0 && columnaIngresar < 9)
                        {
                            opcionIngresar = 0;
                            int opcionIngresarValor = 1;
                            while (opcionIngresarValor == 1)
                            {
                                N = 0;
                                do
                                {
                                    printf("Ingrese valor [1-9]: ");
                                    scanf("%s", numero);
                                    N = validar_numero(numero);

                                } while (N == 0);
                                valorAIngresar = atoi(numero);

                                if (valorAIngresar > 0 && valorAIngresar < 10)
                                {
                                    if (verificarSudoku(matriz, filaIngresar, columnaIngresar, valorAIngresar) == 1)
                                    {
                                        opcionIngresarValor = 0;
                                        contadorCasillas = contadorCasillas + 1;
                                        matriz[filaIngresar][columnaIngresar] = valorAIngresar;
                                        printf(">>>Valor Ingresado<<<\n");
                                    }
                                    if (verificarSudoku(matriz, filaIngresar, columnaIngresar, valorAIngresar) == 0)
                                    {
                                        //printf("Ese valor ya se encuentra en la fila, columna o cuadrante\n");
                                        opcionIngresarValor = 0;
                                    }
                                }
                            }
                        }
                    }
                }

                mostrarTablero(tablero);
                mostrarJaulas(listaJaulas, numeroJaulas);
                imprimirMatriz(matriz);
                //printf(">>>%d<<<\n>%d<\n", verificarSuma(matriz, listaJaulas, numeroJaulas), contadorCasillas);

                //Si la cantidad de casillas ingresadas son 81 y cumple que sumen lo necesario en cada jaula.
                //Se obtiene la victoria, pidiendole al usuario si desea volver a jugar o no.
                if (contadorCasillas == 81 && verificarSuma(matriz, listaJaulas, numeroJaulas) == 1)
                {
                    printf("Victoria!\n");
                    printf("Desea volver a jugar (S/N)\n");
                    int volver = 1;
                    while (volver == 1)
                    {
                        scanf("%s", &rejugar);
                        if (rejugar == 'S' || rejugar == 's')
                        {
                            volver = 0;
                            opcionCiclar = 0;
                        }
                        if (rejugar == 'N' || rejugar == 'n')
                        {
                            volver = 0;
                            opcionCiclar = 0;
                            ciclar = 0;
                        }
                    }
                }
            }
        }
        //Modalidad automatica.
        if (modalidad == 'A' || modalidad == 'a')
        {
            printf("Modalidad Ingresada: Automatica\n");
            int contadorCombinaciones = 0;
            int iterador = 0;
            //inicia los for anidados que generaran todos los numeros posibles para cada una de las casillas de la matriz.
            for (int i1 = 0; i1 < 9; i1++)
            {
                matrizAutomatica[0][0] = i1 + 1;
                for (int i2 = 0; i2 < 9; i2++)
                {
                    matrizAutomatica[0][1] = i2 + 1;
                    for (int i3 = 0; i3 < 9; i3++)
                    {
                        matrizAutomatica[0][2] = i3 + 1;
                        for (int i4 = 0; i4 < 9; i4++)
                        {
                            matrizAutomatica[0][3] = i4 + 1;
                            for (int i5 = 0; i5 < 9; i5++)
                            {
                                matrizAutomatica[0][4] = i5 + 1;
                                for (int i6 = 0; i6 < 9; i6++)
                                {
                                    matrizAutomatica[0][5] = i6 + 1;
                                    for (int i7 = 0; i7 < 9; i7++)
                                    {
                                        matrizAutomatica[0][6] = i7 + 1;
                                        for (int i8 = 0; i8 < 9; i8++)
                                        {
                                            matrizAutomatica[0][7] = i8 + 1;
                                            for (int i9 = 0; i9 < 9; i9++)
                                            {
                                                matrizAutomatica[0][8] = i9 + 1;
                                                for (int i10 = 0; i10 < 9; i10++)
                                                {
                                                    matrizAutomatica[1][0] = i10 + 1;
                                                    for (int i11 = 0; i11 < 9; i11++)
                                                    {
                                                        matrizAutomatica[1][1] = i11 + 1;
                                                        for (int i12 = 0; i12 < 9; i12++)
                                                        {
                                                            matrizAutomatica[1][2] = i12 + 1;
                                                            for (int i13 = 0; i13 < 9; i13++)
                                                            {
                                                                matrizAutomatica[1][3] = i13 + 1;
                                                                for (int i14 = 0; i14 < 9; i14++)
                                                                {
                                                                    matrizAutomatica[1][4] = i14 + 1;
                                                                    for (int i15 = 0; i15 < 9; i15++)
                                                                    {
                                                                        matrizAutomatica[1][5] = i15 + 1;
                                                                        for (int i16 = 0; i16 < 9; i16++)
                                                                        {
                                                                            matrizAutomatica[1][6] = i16 + 1;
                                                                            for (int i17 = 0; i17 < 9; i17++)
                                                                            {
                                                                                matrizAutomatica[1][7] = i17 + 1;
                                                                                for (int i18 = 0; i18 < 9; i18++)
                                                                                {
                                                                                    matrizAutomatica[1][8] = i18 + 1;
                                                                                    for (int i19 = 0; i19 < 9; i19++)
                                                                                    {
                                                                                        matrizAutomatica[2][0] = i19 + 1;
                                                                                        for (int i20 = 0; i20 < 9; i20++)
                                                                                        {
                                                                                            matrizAutomatica[2][1] = i20 + 1;
                                                                                            for (int i21 = 0; i21 < 9; i21++)
                                                                                            {
                                                                                                matrizAutomatica[2][2] = i21 + 1;
                                                                                                for (int i22 = 0; i22 < 9; i22++)
                                                                                                {
                                                                                                    matrizAutomatica[2][3] = i22 + 1;
                                                                                                    for (int i23 = 0; i23 < 9; i23++)
                                                                                                    {
                                                                                                        matrizAutomatica[2][4] = i23 + 1;
                                                                                                        for (int i24 = 0; i24 < 9; i24++)
                                                                                                        {
                                                                                                            matrizAutomatica[2][5] = i24 + 1;
                                                                                                            for (int i25 = 0; i25 < 9; i25++)
                                                                                                            {
                                                                                                                matrizAutomatica[2][6] = i25 + 1;
                                                                                                                for (int i26 = 0; i26 < 9; i26++)
                                                                                                                {
                                                                                                                    matrizAutomatica[2][7] = i26 + 1;
                                                                                                                    for (int i27 = 0; i27 < 9; i27++)
                                                                                                                    {
                                                                                                                        matrizAutomatica[2][8] = i27 + 1;
                                                                                                                        for (int i28 = 0; i28 < 9; i28++)
                                                                                                                        {
                                                                                                                            matrizAutomatica[3][0] = i28 + 1;
                                                                                                                            for (int i29 = 0; i29 < 9; i29++)
                                                                                                                            {
                                                                                                                                matrizAutomatica[3][1] = i29 + 1;
                                                                                                                                for (int i30 = 0; i30 < 9; i30++)
                                                                                                                                {
                                                                                                                                    matrizAutomatica[3][2] = i30 + 1;
                                                                                                                                    for (int i31 = 0; i31 < 9; i31++)
                                                                                                                                    {
                                                                                                                                        matrizAutomatica[3][3] = i31 + 1;
                                                                                                                                        for (int i32 = 0; i32 < 9; i32++)
                                                                                                                                        {
                                                                                                                                            matrizAutomatica[3][4] = i32 + 1;
                                                                                                                                            for (int i33 = 0; i33 < 9; i33++)
                                                                                                                                            {
                                                                                                                                                matrizAutomatica[3][5] = i33 + 1;
                                                                                                                                                for (int i34 = 0; i34 < 9; i34++)
                                                                                                                                                {
                                                                                                                                                    matrizAutomatica[3][6] = i34 + 1;
                                                                                                                                                    for (int i35 = 0; i35 < 9; i35++)
                                                                                                                                                    {
                                                                                                                                                        matrizAutomatica[3][7] = i35 + 1;
                                                                                                                                                        for (int i36 = 0; i36 < 9; i36++)
                                                                                                                                                        {
                                                                                                                                                            matrizAutomatica[3][8] = i36 + 1;
                                                                                                                                                            for (int i37 = 0; i37 < 9; i37++)
                                                                                                                                                            {
                                                                                                                                                                matrizAutomatica[4][0] = i37 + 1;
                                                                                                                                                                for (int i38 = 0; i38 < 9; i38++)
                                                                                                                                                                {
                                                                                                                                                                    matrizAutomatica[4][1] = i38 + 1;
                                                                                                                                                                    for (int i39 = 0; i39 < 9; i39++)
                                                                                                                                                                    {
                                                                                                                                                                        matrizAutomatica[4][2] = i39 + 1;
                                                                                                                                                                        for (int i40 = 0; i40 < 9; i40++)
                                                                                                                                                                        {
                                                                                                                                                                            matrizAutomatica[4][3] = i40 + 1;
                                                                                                                                                                            for (int i41 = 0; i41 < 9; i41++)
                                                                                                                                                                            {
                                                                                                                                                                                matrizAutomatica[4][4] = i41 + 1;
                                                                                                                                                                                for (int i42 = 0; i42 < 9; i42++)
                                                                                                                                                                                {
                                                                                                                                                                                    matrizAutomatica[4][5] = i2 + 1;
                                                                                                                                                                                    for (int i43 = 0; i43 < 9; i43++)
                                                                                                                                                                                    {
                                                                                                                                                                                        matrizAutomatica[4][6] = i43 + 1;
                                                                                                                                                                                        for (int i44 = 0; i44 < 9; i44++)
                                                                                                                                                                                        {
                                                                                                                                                                                            matrizAutomatica[4][7] = i44 + 1;
                                                                                                                                                                                            for (int i45 = 0; i45 < 9; i45++)
                                                                                                                                                                                            {
                                                                                                                                                                                                matrizAutomatica[4][8] = i45 + 1;
                                                                                                                                                                                                for (int i46 = 0; i46 < 9; i46++)
                                                                                                                                                                                                {
                                                                                                                                                                                                    matrizAutomatica[5][0] = i46 + 1;
                                                                                                                                                                                                    for (int i47 = 0; i47 < 9; i47++)
                                                                                                                                                                                                    {
                                                                                                                                                                                                        matrizAutomatica[5][1] = i47 + 1;
                                                                                                                                                                                                        for (int i48 = 0; i48 < 9; i48++)
                                                                                                                                                                                                        {
                                                                                                                                                                                                            matrizAutomatica[5][2] = i48 + 1;
                                                                                                                                                                                                            for (int i49 = 0; i49 < 9; i49++)
                                                                                                                                                                                                            {
                                                                                                                                                                                                                matrizAutomatica[5][3] = i49 + 1;
                                                                                                                                                                                                                for (int i50 = 0; i50 < 9; i50++)
                                                                                                                                                                                                                {
                                                                                                                                                                                                                    matrizAutomatica[5][4] = i50 + 1;
                                                                                                                                                                                                                    for (int i51 = 0; i51 < 9; i51++)
                                                                                                                                                                                                                    {
                                                                                                                                                                                                                        matrizAutomatica[5][5] = i51 + 1;
                                                                                                                                                                                                                        for (int i52 = 0; i52 < 9; i52++)
                                                                                                                                                                                                                        {
                                                                                                                                                                                                                            matrizAutomatica[5][6] = i52 + 1;
                                                                                                                                                                                                                            for (int i53 = 0; i53 < 9; i53++)
                                                                                                                                                                                                                            {
                                                                                                                                                                                                                                matrizAutomatica[5][7] = i53 + 1;
                                                                                                                                                                                                                                for (int i54 = 0; i54 < 9; i54++)
                                                                                                                                                                                                                                {
                                                                                                                                                                                                                                    matrizAutomatica[5][8] = i54 + 1;
                                                                                                                                                                                                                                    for (int i55 = 0; i55 < 9; i55++)
                                                                                                                                                                                                                                    {
                                                                                                                                                                                                                                        matrizAutomatica[6][0] = i55 + 1;
                                                                                                                                                                                                                                        for (int i56 = 0; i56 < 9; i56++)
                                                                                                                                                                                                                                        {
                                                                                                                                                                                                                                            matrizAutomatica[6][1] = i56 + 1;
                                                                                                                                                                                                                                            for (int i57 = 0; i57 < 9; i57++)
                                                                                                                                                                                                                                            {
                                                                                                                                                                                                                                                matrizAutomatica[6][2] = i57 + 1;
                                                                                                                                                                                                                                                for (int i58 = 0; i58 < 9; i58++)
                                                                                                                                                                                                                                                {
                                                                                                                                                                                                                                                    matrizAutomatica[6][3] = i58 + 1;
                                                                                                                                                                                                                                                    for (int i59 = 0; i59 < 9; i59++)
                                                                                                                                                                                                                                                    {
                                                                                                                                                                                                                                                        matrizAutomatica[6][4] = i59 + 1;
                                                                                                                                                                                                                                                        for (int i60 = 0; i60 < 9; i60++)
                                                                                                                                                                                                                                                        {
                                                                                                                                                                                                                                                            matrizAutomatica[6][5] = i60 + 1;
                                                                                                                                                                                                                                                            for (int i61 = 0; i61 < 9; i61++)
                                                                                                                                                                                                                                                            {
                                                                                                                                                                                                                                                                matrizAutomatica[6][6] = i61 + 1;
                                                                                                                                                                                                                                                                for (int i62 = 0; i62 < 9; i62++)
                                                                                                                                                                                                                                                                {
                                                                                                                                                                                                                                                                    matrizAutomatica[6][7] = i62 + 1;
                                                                                                                                                                                                                                                                    for (int i63 = 0; i63 < 9; i63++)
                                                                                                                                                                                                                                                                    {
                                                                                                                                                                                                                                                                        matrizAutomatica[6][8] = i63 + 1;
                                                                                                                                                                                                                                                                        for (int i64 = 0; i64 < 9; i64++)
                                                                                                                                                                                                                                                                        {
                                                                                                                                                                                                                                                                            matrizAutomatica[7][0] = i64 + 1;
                                                                                                                                                                                                                                                                            for (int i65 = 0; i65 < 9; i65++)
                                                                                                                                                                                                                                                                            {
                                                                                                                                                                                                                                                                                matrizAutomatica[7][1] = i65 + 1;
                                                                                                                                                                                                                                                                                for (int i66 = 0; i66 < 9; i66++)
                                                                                                                                                                                                                                                                                {
                                                                                                                                                                                                                                                                                    matrizAutomatica[7][2] = i66 + 1;
                                                                                                                                                                                                                                                                                    for (int i67 = 0; i67 < 9; i67++)
                                                                                                                                                                                                                                                                                    {
                                                                                                                                                                                                                                                                                        matrizAutomatica[7][3] = i67 + 1;
                                                                                                                                                                                                                                                                                        for (int i68 = 0; i68 < 9; i68++)
                                                                                                                                                                                                                                                                                        {
                                                                                                                                                                                                                                                                                            matrizAutomatica[7][4] = i68 + 1;
                                                                                                                                                                                                                                                                                            for (int i69 = 0; i69 < 9; i69++)
                                                                                                                                                                                                                                                                                            {
                                                                                                                                                                                                                                                                                                matrizAutomatica[7][5] = i69 + 1;
                                                                                                                                                                                                                                                                                                for (int i70 = 0; i70 < 9; i70++)
                                                                                                                                                                                                                                                                                                {
                                                                                                                                                                                                                                                                                                    matrizAutomatica[7][6] = i70 + 1;
                                                                                                                                                                                                                                                                                                    for (int i71 = 0; i71 < 9; i71++)
                                                                                                                                                                                                                                                                                                    {
                                                                                                                                                                                                                                                                                                        matrizAutomatica[7][7] = i71 + 1;
                                                                                                                                                                                                                                                                                                        for (int i72 = 0; i72 < 9; i72++)
                                                                                                                                                                                                                                                                                                        {
                                                                                                                                                                                                                                                                                                            matrizAutomatica[7][8] = i72 + 1;
                                                                                                                                                                                                                                                                                                            for (int i73 = 0; i73 < 9; i73++)
                                                                                                                                                                                                                                                                                                            {
                                                                                                                                                                                                                                                                                                                matrizAutomatica[8][0] = i73 + 1;
                                                                                                                                                                                                                                                                                                                for (int i74 = 0; i74 < 9; i74++)
                                                                                                                                                                                                                                                                                                                {
                                                                                                                                                                                                                                                                                                                    matrizAutomatica[8][1] = i74 + 1;
                                                                                                                                                                                                                                                                                                                    for (int i75 = 0; i75 < 9; i75++)
                                                                                                                                                                                                                                                                                                                    {
                                                                                                                                                                                                                                                                                                                        matrizAutomatica[8][2] = i75 + 1;
                                                                                                                                                                                                                                                                                                                        for (int i76 = 0; i76 < 9; i76++)
                                                                                                                                                                                                                                                                                                                        {
                                                                                                                                                                                                                                                                                                                            matrizAutomatica[8][3] = i76 + 1;
                                                                                                                                                                                                                                                                                                                            for (int i77 = 0; i77 < 9; i77++)
                                                                                                                                                                                                                                                                                                                            {
                                                                                                                                                                                                                                                                                                                                matrizAutomatica[8][4] = i77 + 1;
                                                                                                                                                                                                                                                                                                                                for (int i78 = 0; i78 < 9; i78++)
                                                                                                                                                                                                                                                                                                                                {
                                                                                                                                                                                                                                                                                                                                    matrizAutomatica[8][5] = i78 + 1;
                                                                                                                                                                                                                                                                                                                                    for (int i79 = 0; i79 < 9; i79++)
                                                                                                                                                                                                                                                                                                                                    {
                                                                                                                                                                                                                                                                                                                                        matrizAutomatica[8][6] = i79 + 1;
                                                                                                                                                                                                                                                                                                                                        for (int i80 = 0; i80 < 9; i80++)
                                                                                                                                                                                                                                                                                                                                        {
                                                                                                                                                                                                                                                                                                                                            matrizAutomatica[8][7] = i80 + 1;
                                                                                                                                                                                                                                                                                                                                            for (int i81 = 0; i81 < 9; i81++)
                                                                                                                                                                                                                                                                                                                                            {
                                                                                                                                                                                                                                                                                                                                                matrizAutomatica[8][8] = i81 + 1;

                                                                                                                                                                                                                                                                                                                                                contadorCombinaciones++;

                                                                                                                                                                                                                                                                                                                                                //Se mostrara el iterador cada 10000000 combinaciones.
                                                                                                                                                                                                                                                                                                                                                if (contadorCombinaciones % 10000000 == 0)
                                                                                                                                                                                                                                                                                                                                                {
                                                                                                                                                                                                                                                                                                                                                    iterador++;
                                                                                                                                                                                                                                                                                                                                                    printf("%d\n", iterador);
                                                                                                                                                                                                                                                                                                                                                    imprimirMatriz(matrizAutomatica);
                                                                                                                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                if (verificarSuma(matrizAutomatica, listaJaulas, numeroJaulas) == 1)
                                                                                                                                                                                                                                                                                                                                                {
                                                                                                                                                                                                                                                                                                                                                    //Si la matriz cumple con la restriccion se imprime como posible solucion.
                                                                                                                                                                                                                                                                                                                                                    printf("Posible solucion:\n");
                                                                                                                                                                                                                                                                                                                                                    imprimirMatriz(matrizAutomatica);
                                                                                                                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                }
                                                                                                                                                                                                                            }
                                                                                                                                                                                                                        }
                                                                                                                                                                                                                    }
                                                                                                                                                                                                                }
                                                                                                                                                                                                            }
                                                                                                                                                                                                        }
                                                                                                                                                                                                    }
                                                                                                                                                                                                }
                                                                                                                                                                                            }
                                                                                                                                                                                        }
                                                                                                                                                                                    }
                                                                                                                                                                                }
                                                                                                                                                                            }
                                                                                                                                                                        }
                                                                                                                                                                    }
                                                                                                                                                                }
                                                                                                                                                            }
                                                                                                                                                        }
                                                                                                                                                    }
                                                                                                                                                }
                                                                                                                                            }
                                                                                                                                        }
                                                                                                                                    }
                                                                                                                                }
                                                                                                                            }
                                                                                                                        }
                                                                                                                    }
                                                                                                                }
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                }
                                                                                            }
                                                                                        }
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            //terminan los for anidados

            printf("Desea volver a jugar (S/N)\n");
            int volver = 1;
            while (volver == 1)
            {
                scanf("%s", &rejugar);
                if (rejugar == 'S' || rejugar == 's')
                {
                    volver = 0;
                }
                if (rejugar == 'N' || rejugar == 'n')
                {
                    volver = 0;
                    ciclar = 0;
                }
            }

        } //termina la modalidad automatica
    }     //termina el while ciclar

    //Se libera la memoria.
    for (int i; i < TAMANO; i++)
    {
        free(matriz[i]);
    }
    free(matrizAutomatica);

    for (int i; i < TAMANO; i++)
    {
        free(matrizAutomatica[i]);
    }
    free(matrizAutomatica);

    for (int i; i < TAMANO; i++)
    {
        free(tablero[i]);
    }
    free(tablero);

} //termina el main