import os

def listar_archivos(n,lugar):
	if n == 0:
		lista_de_archivos = os.listdir()

	else:
		lista_de_archivos = os.listdir(lugar)
	return lista_de_archivos

def mostrar_lista_de_archivos(lista):
	for x in range(len(lista)):
		posicion = determinador_de_extenciones(lista[x])
		elegir_camino(posicion,lista[x])

def obtener_ruta():
	return os.getcwd()

def determinador_de_extenciones(elemento):
	indice = elemento.find(".")
	return indice

def elegir_camino(n,elemento):
	if n == -1:
		ruta = obtener_ruta()
		sgt_ruta = determinar_siguiente_directorio(ruta,elemento)
		archivos = listar_archivos(1,sgt_ruta)
		print(archivos)
	else:
		print(elemento)

def determinar_siguiente_directorio(directorio_actual,carpeta):
	nuevo_directorio = directorio_actual + "\\" + carpeta
	return nuevo_directorio

archivos = listar_archivos(0,"")
mostrar_lista_de_archivos(archivos)



