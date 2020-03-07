#* *-* coding: utf-8 -*-
import os

def algoritmo():
	mensajes_menu()
	opcion = pedir_numero(0,3)
	las_opciones_menu(opcion)
	return 0
	
def mensajes_menu():
	print("¿Que desea hacer?")
	print("0-Terminar")
	print("1-Crear")
	print("2-Agregar")
	print("3-Trasformar")
	return 0
def mostrar_no_esta():
    print("Esa opcion no esta")
    return 0
def mostrar_opcion_no_valida():
    print("Opcion no valida")
    return 0
def pedir_numero(a,b):
    while True:
        while True:
            x = input("Ingrese algun numero: ")
            try:
                x = int(x)
                break
            except:
                mostrar_opcion_no_valida()
        if a <= x <= b:
            return x
        else:
            mostrar_no_esta()
def las_opciones_menu(entero):
	if entero == 0:
		pass
	if entero == 1:
		crear()
	if entero == 2:
		agregar()
	if entero == 3:
		trasformar()
	return 0
def mensajes_lenguajes_programacion():
	print("¿Que lenguaje de programacion?")
	print("1-Python")
	print("2-Python 3")
	print("3-Java")
	print("4-C")
	print("5-Arduino")
	return 0
def crear():
	mensajes_lenguajes_programacion()
	opcion = pedir_numero(1,4)
	las_opciones_crear(opcion)
	return 0
def las_opciones_crear(entero):
	if entero == 1:
		mostrar_no_esta()
	if entero == 2:
		mostrar_no_esta()
	if entero == 3:
		mostrar_no_esta()
	if entero == 4:
		crear_C()
	return 0
def crear_C():
	nombre = nombre_archivo(".c")
	codigo_basico = ["//","\n#include<stdio.h>","\nint main(){","\treturn 0","}"]
	escribir(codigo_basico,nombre)
def agregar():
	mensajes_lenguajes_programacion()
	opcion = pedir_numero(1,5)
	las_opciones_agregar(opcion)
	return 0
def las_opciones_agregar(entero):
	if entero == 1:
		mostrar_no_esta()
	if entero == 2:
		mostrar_no_esta()
	if entero == 3:
		mostrar_no_esta()
	if entero == 4:
		mensajes_agregar_en_c()
		opcion = pedir_numero(0,2)
		las_opciones_agregar_en_c(opcion)
	if entero == 5:
		nombre = nombre_archivo(".ino")
		datos = abrir_archivo(nombre)
		if datos == "vacio":
			pass
		else:
			datos = punto_coma(datos)
			datos = quitar_espacios_vacios(datos)
			escribir(datos,nombre)
	return 0
def mensajes_agregar_en_c():
	print("0-Terminar")
	print("1-Punto y coma")
	print("2-Enter en print")
	return 0
def las_opciones_agregar_en_c(entero):
	if entero == 0:
		pass
	if entero == 1:
		nombre = nombre_archivo(".c")
		datos = abrir_archivo(nombre)
		if datos == "vacio":
			pass
		else:
			datos = punto_coma(datos)
			datos = quitar_espacios_vacios(datos)
			escribir(datos,nombre)
	if entero == 2:
		mostrar_no_esta()
	return 0
def trasformar():
	print("1-Python 2----Python 3")
	print("2-Python 3----Python 2")
	opcion = pedir_numero(1,2)
	trasformacion_python(opcion)
def trasformacion_python(version):
	nombre = nombre_archivo(".py")
	datos = abrir_archivo(nombre)
	if datos == "vacio":
		return 0
	else:
		datos = convertir_los_input(datos,version)
		datos = convertir_los_parentesis(datos,version)
		escribir(datos,nombre)
def convertir_los_input(datos,version):
	lista = ["raw_input","input","raw_input"]
	x = 0
	while x != len(datos):
		datos[x] = datos[x].replace(lista[version - 1],lista[version])
		x = x + 1
	return datos
def convertir_los_parentesis(datos,version):
	version = version + 1
	if version == 3: # codigo para pasar a python 2
		x = 0
		while x != len(datos):
			q = datos[x].find("print")
			if q == -1:
				pass
			else:
				datos[x] = datos[x].replace("("," ")
				datos[x] = datos[x].replace(")","")
			x = x + 1
		return datos
	else:
		x = 0
		while x != len(datos):
			q = datos[x].find("print")
			if q == -1:
				pass
			else:
				ubicacion = datos[x].find("t")
				lista = list(datos[x])
				lista[ubicacion + 1] = "("
				lista.append(")")
				w = 0
				linea = ""
				while w != len(lista):
					linea = linea + lista[w] 
					w = w + 1
				datos[x] = linea
			x = x + 1
		return datos

	

def nombre_archivo(formato):
	x = input("Como se llama el archivo: ")
	q = x.find(formato)
	if q == -1:
		return x + formato
	else:
		return x
def abrir_archivo(nombre):
	try:
		x = open(nombre)
		q = x.readlines()
		q = quitar_enter(q)
		x.close()
		return q
	except:
		print("El archivo no se encuentra en el mismo directorio")
		return "vacio"
def quitar_enter(lista):
	x = 0
	while x != len(lista):
		lista[x] = lista[x].replace("\n","")
		x = x + 1
	return lista
def punto_coma(lista):
	x = 0
	L = ["//","/*","#","main","{","}",";","struct","type","else","if",]
	while x != len(lista):
		q = 0
		while q != len(L):
			w = lista[x].find(L[q])
			if w == -1:
				q = q + 1
			else:
				if L[q] == "{":
					e = lista[x].find("[")
					if e == -1:
						pass
					else:
						q = len(L)
				break
		if q == len(L):
			lista[x] = lista[x] + ";"
		x = x + 1
	return lista
def quitar_espacios_vacios(lista):
	x = 0
	while x != len(lista):
		respaldo = lista[x]
		lista[x] = lista[x].replace("\t","")
		if lista[x] == ";":
			lista[x] = ""
		else:
			lista[x] = respaldo
			x = x + 1
	return lista
def escribir(lista,nombre):
	x = open(nombre,"w")
	q = 0
	while q != len(lista):
		x.write(lista[q] + "\n")
		q = q + 1
	x.close()
	return 0
def repetir():
	while True:
		print("¿Desea repetir el programa?")
		print("1-Si")
		print("2-No")
		while True:
			x = input("Ingrese alguna opcion: ")
			try:
				x = int(x)
				break
			except:
				print("No ingreso un numero")
		if x != 1 and x != 2:
			print("Esa opcion no esta")
		if x == 1 or x == 2:
			return x
def limpiar():
	os.system("cls")
	return 0

_name_ = "_main_"
if _name_ == "_main_":
	z = 0
	while z != 2:
		limpiar()
		algoritmo()
		z = repetir()
print("El programa a finalizado")
