# -*- coding: utf-8 -*-

def saludar(nombre, profesion, edad):
	print "Nombre: " + nombre
	print "Profesión: " + profesion
	print "Edad: " + edad
	print "El valor de PI: " + PI()
	print locals()
	return "Hola " #+ nombre

def PI():
	pi = "3.1415926"
	return pi

saludo = saludar(*["Jerman", "Ingeniero", "42"])
print saludo
print globals()

#valorPI = PI()
#print valorPI
