#dimensión del tablero
n = 6 

#Crea del Tablero:
T = []
i = 1
while (i<=n):
    F = ['.'] * n
    T.append(F)
    i = i+1
    
#Llena el Tablero con las Minas (y cuenta el número real que existe):
strPos = input('Ingresa el string con las posiciones de las minas: ')
strPos = strPos.upper()
numMinas = 0
i=0
while i<len(strPos):
    if T[ord(strPos[i])-65][int(strPos[i+1])-1] != '*':
        T[ord(strPos[i])-65][int(strPos[i+1])-1] = '*'
        numMinas += 1
    i=i+2

#Establece la cantidad de posiciones sin minas:
celdasSinMinas = n*n-numMinas

#Imprime el Tablero:
#Imprime los títulos de cada columna (números):
print('', end='  ')
j=0
while j<n:
    print(j+1, end=' ')
    j=j+1
print('', end='\n')

#Imprime el tablero con letras mayúsculas al principio de cada fila:
i=0
while i<n:
    j=0
    print(chr(i+65), end=' ') #Letra al principio de cada fila.
    while j<n:
        if T[i][j] == '*':
            print('.', end=' ')
        else:
            print(T[i][j], end=' ')
        j=j+1
    print('', end='\n')
    i=i+1

#INICIO DEL JUEGO:
ganaste = False
perdiste = False

while perdiste == False and ganaste == False:

    #Pide posición de Juego (letra y luego número):
    strPos = input('Ingresa la casilla del tablero que quieres abrir: ')
    strPos = strPos.upper()
    
    x = ord(strPos[0])-65
    y = int(strPos[1])-1

    #Realiza una jugada solo si las posiciones están dentro del rango definido.
    if 0 <= x < n and 0 <= y < n:
        #cuenta las minas entorno
        contMinas = 0
        if T[x][y] == '*':
            perdiste = True
        elif T[x][y] == '.':
            if x>0 and y>0 and T[x-1][y-1] == '*': #ARRIBA-IZQUIERDA
                contMinas += 1
            if x>0 and T[x-1][y] == '*': #ARRIBA
                contMinas += 1
            if x>0 and y<n-1 and T[x-1][y+1] == '*': #ARRIBA-DERECHA
                contMinas += 1
            if y>0 and T[x][y-1] == '*': #IZQUIERDA
                contMinas += 1
            if y<n-1 and T[x][y+1] == '*': #DERECHA
                contMinas += 1
            if x<n-1 and y>0 and T[x+1][y-1] == '*': #ABAJO-IZQUIERDA
                contMinas += 1
            if x<n-1 and T[x+1][y] == '*': #ABAJO
                contMinas += 1
            if x<n-1 and y<n-1 and T[x+1][y+1] == '*': #ABAJO-DERECHA
                contMinas += 1
            T[x][y] = str(contMinas)
            celdasSinMinas -= 1        

    #Analiza si abrió todas las casillas sin minas:
    if celdasSinMinas == 0:
        ganaste = True

    #Imprime el Tablero:
    #Imprime los títulos de cada columna (números):
    print('', end='  ')
    j=0
    while j<n:
        print(j+1, end=' ')
        j=j+1
    print('', end='\n')

    #Imprime el tablero con letras mayúsculas al principio de cada fila:        
    i=0
    while i<n:
        j=0
        print(chr(i+65), end=' ')   #Letra al principio de cada fila.
        while j<n:
            if perdiste == True or ganaste == True:
                print(T[i][j], end=' ')
            else:
                if T[i][j] == '*':
                    print('.', end=' ')
                else:
                    print(T[i][j], end=' ')
            j=j+1
        print('', end='\n')
        i=i+1
        
    #Mensaje de cierre de jugo:            
    if ganaste == True:
        print('GANASTE')
    if perdiste == True:
        print('PERDISTE')        

#FIN DEL JUEGO
