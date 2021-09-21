from mapa import *
import os

if __name__ == "__main__":
   os.system("cls")
   print("---------")
   mapa = mapa(76,72)
   mapa.agregar_objeto(10,34,32,"B")
   mapa.agregar_objeto(4,30,32,"T")
   mapa.mostrar_mapa()