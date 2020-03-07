# -*- coding: utf-8 -*-

def jugar(intento=1):
	respuesta = "azul" #raw_input("¿De qué color es una naranja? ")
	if respuesta != "naranja":
		if intento < 3:
			print "\nFallaste! Inténtalo de nuevo"
			print "Llamada recursiva nº " + str(intento)
			intento -= 1
			jugar(intento) # Llamada recursiva
		else:
			print "\nPerdiste!"
	else:
		print "\nGanaste!"

jugar()
