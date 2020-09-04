
def determinante_orden_2(matrix):
    izquierda = matrix[0][0] * matrix[1][1]
    derecha = matrix[0][1] * matrix[1][0]
    determinante = izquierda - derecha
    return determinante

def obtener_matriz_cofactor(matrix,columna):
    y = 1 # esto por que no nesesitamos la fila 0 de la matrix
    matrix_cofactor = []
    while y != len(matrix):
        fila_n = []
        for x in range(len(matrix[0])):
            if x == columna:
                pass
            else:
                fila_n.append(matrix[y][x])
        matrix_cofactor.append(fila_n)
        y = y + 1
    return matrix_cofactor

def determinante_orden_3(matrix):
    cofactor_1 = obtener_matriz_cofactor(matrix,0)
    determinante_cofactor_1 = determinante_orden_2(cofactor_1)
    primero = matrix[0][0] * determinante_cofactor_1
    cofactor_2 = obtener_matriz_cofactor(matrix,1)
    determinante_cofactor_2 = determinante_orden_2(cofactor_2)
    segundo = matrix[0][1] * determinante_cofactor_2
    cofactor_3 = obtener_matriz_cofactor(matrix,2)
    determinante_cofactor_3 = determinante_orden_2(cofactor_3)
    tercero = matrix[0][2] * determinante_cofactor_3
    determinante = primero - segundo + tercero
    return determinante

def determinar_signo(n):
    if n % 2 == 0:
        return "positivo"
    else:
        return "negativo"

def determinar_orden_n(matrix):




if __name__ == "__main__":
    print("hola mundo")
    d = determinante_orden_2([ [8,12],[2,1] ])
    print(d)
    d2 = determinante_orden_3([ [8,11,4],[2,8,1],[3,5,8] ])
    print(d2)
    signo = determinar_signo(2)
    print(signo)
    c4 = obtener_matriz_cofactor([ [8,15,16,12],[12,5,3,8],[1,2,4,6],[13,4,7,2] ],1)
    print(c4)

