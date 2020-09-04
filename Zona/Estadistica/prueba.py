from unidad_1 import *
from unidad_3 import  *
import os

if __name__ == "__main__":
    os.system("cls")
    poner_r = obtener_confianza(99)
    print("debemos pone: ",poner_r," en el R")
    # este numero tenemos que ponerlo en el R y el numero que de es el que tendremos que dar en las funciones
    valor_r = 1.96
    promedio = 176
    desviacion = 6
    n = 138
    aplicar_margen_error(promedio,valor_r,desviacion,n)
    obtener_aplitud(promedio,valor_r,desviacion,n)


