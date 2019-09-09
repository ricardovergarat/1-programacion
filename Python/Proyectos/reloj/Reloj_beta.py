from tkinter import *
import numpy as np

# UTF-8

def abrir_archivo():
	archivo = open("manifiesto.txt")
	lineas = archivo.readlines()
	lineas = quitar_enter(lineas)
	return lineas

def quitar_enter(lineas):
	i = 0
	while i != len(lineas):
		lineas[i] = lineas[i].replace("\n","")
		i = i + 1
	return lineas

def GUI(datos):
	ventana = Tk()
	#ventana.geometry("700x700")
	agregar_reloj(ventana,datos)
	ventana.mainloop()

def agregar_reloj(ventana,datos):
	i = 0
	while i != len(datos):
		canvas = Canvas(width=124, height=124)
		canvas.pack(expand=YES, fill=BOTH)
		canvas.create_oval(2,2,122,122)
		h,m = separar_hora_y_minuto(datos[i])
		agregar_palo_minuto(m,30,canvas)
		agregar_palo_hora(h,50,canvas)
		agregar_puntos(55,canvas)
		i = i + 1

def separar_hora_y_minuto(hora):
	hora = hora.split(":")
	return int(hora[0]),int(hora[1])

def agregar_palo_minuto(n,tamaño,canvas):
	grado = 6*(15 - n)
	angulo = convertir_radiales(grado)
	x = np.cos(angulo) * tamaño
	y = np.sin(angulo) * tamaño
	x = x + 62
	y = 62 - y
	canvas.create_line(62,62,x,y)

def agregar_palo_hora(n,tamaño,canvas):
	n = n * 5
	grado = 6*(15 - n)
	angulo = convertir_radiales(grado)
	x = np.cos(angulo) * tamaño
	y = np.sin(angulo) * tamaño
	x = x + 62
	y = 62 - y
	canvas.create_line(62,62,x,y)

def convertir_radiales(a):
	radial = a/180 * np.pi
	return radial

def agregar_puntos(tamaño,canvas):
	i = 0
	while i != 12:
		n = i * 5
		print(n)
		grado = 6*(15 - n)
		angulo = convertir_radiales(grado)
		x = np.cos(angulo) * tamaño
		y = np.sin(angulo) * tamaño
		x = x + 62
		y = 62 - y
		canvas.create_oval(x-2,y-2,x+2,y+2,fill='black')
		i = i + 1

_name_ = "_main_"
if _name_ == "_main_":
	datos = abrir_archivo()
	GUI(datos)


