import math

def obtener_solucion_cuadratica(a,b,c):
    raiz = math.sqrt( (b * b) - (4 * a * c) )
    denominador = 2 * a
    soluciones = [ (b + raiz) / denominador, (b - raiz) / denominador ]
    return soluciones

def obtener_matrices_homogeneas(matriz,a,b):
    solucion_1 = []
    solucion_2 = []
    for i in range(len(matriz)):
        fila_n_1 = []
        fila_n_2 = []
        for j in range(len(matriz[i])):
            if i == j:
                fila_n_1.append(matriz[i][j] - a)
                fila_n_2.append(matriz[i][j] - b)
            else:
                fila_n_1.append(matriz[i][j])
                fila_n_2.append(matriz[i][j])
        solucion_1.append(fila_n_1)
        solucion_2.append(fila_n_2)
    soluciones = [solucion_1,solucion_2]
    return soluciones

def mostrar_lista(lista):
    for i in range(len(lista)):
        print(lista[i])

def mostrar_soluciones_homogeneas(lista):
    for i in range(len(lista)):
        mostrar_lista(lista[i])
        print("\n\n")

if __name__ == "__main__":
    print("hola mundo")
    s = obtener_solucion_cuadratica(1,2,1)
    print(s)
    matrix = [
        [0,1],
        [-1,-2]
    ]
    xh = obtener_matrices_homogeneas(matrix,-1,-1)
    mostrar_soluciones_homogeneas(xh)