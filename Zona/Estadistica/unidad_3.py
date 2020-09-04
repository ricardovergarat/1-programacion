import math
from unidad_1 import *

def proceso(x,mu,desviacion,n=0):
    if n == 0:
        numerador = x - mu
        return numerador / desviacion
    else:
        numerador = x - mu
        denominador = desviacion / math.sqrt(n)
        return numerador / denominador

def obtener_alfa(n):
    n = n / 100
    alfa = 1 - n
    return alfa

def obtener_confianza(n):
    alfa = obtener_alfa(n)
    return 1 - (alfa / 2)

def obtener_exprecion(promedio,z_de_alfa,desviacion,cantidad_elementos):
    lista = [promedio,"±",z_de_alfa," X ",desviacion / math.sqrt(cantidad_elementos)]
    return lista

def obtener_margen_error(a,b):
    return a * b

def aplicar_margen_error(promedio,z_de_alfa,desviacion,cantidad_elementos):
    exprecion = obtener_exprecion(promedio,z_de_alfa,desviacion,cantidad_elementos)
    print(exprecion)
    error = obtener_margen_error(exprecion[2],exprecion[4])
    print("la exprecion es: ",[ exprecion[0],exprecion[1], error ])
    resultado = [promedio - error,promedio + error]
    print("Los rangos son:  ",resultado)

def obtener_aplitud(promedio,z_de_alfa,desviacion,cantidad_elementos):
    exprecion = obtener_exprecion(promedio, z_de_alfa, desviacion, cantidad_elementos)
    error = obtener_margen_error(exprecion[2], exprecion[4])
    print("La amplitud es: ",2 * error)

def obtener_s(lista):
    desviacion = obtener_desviacion_estantar(lista,2)
    desviacion = math.sqrt(desviacion)
    return desviacion