import math
import os

def obtener_raiz(a,b,c):
    respuesta = (b * b) - (4 * a * c)
    return math.sqrt(respuesta)

def obtener_solucion(a,b,c):
    raiz = obtener_raiz(a,b,c)
    solucion_1 = ( (-b) + raiz ) / ( 2 * a)
    solucion_2 = ( (-b) - raiz ) / ( 2 * a)
    return solucion_1,solucion_2

if __name__ == "__main__":
    os.system("cls")
    m1, m2 = obtener_solucion(1,2,1)
    print("solucion 1: ",m1)
    print("solucion 2: ",m2)