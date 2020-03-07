# -*- coding: utf-8 -*-

from paquete1.matematica import *
from paquete2.cadena import *

def ejecutar(funcion=""):
	if funcion in globals():
		print "Función encontrada"
		if callable(globals()[funcion]):
			print "Función llamable"
			numero1 = int(raw_input("Ingresa el primer numero: "))
			numero2 = int(raw_input("Ahora el segundo: "))
			return globals()[funcion](numero1, numero2)
	else:
		return "Función no encontrada"

operacion = raw_input("¿Que quieres hacer?, ¿Una suma?, ¿O una resta talvéz?: ")

if operacion == "suma":
	print ejecutar("sumasss")
elif operacion == "resta":
	print ejecutar("resta")
else:
	print "Lo siento, no puedo hacer eso"
