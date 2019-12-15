import os

def listar_archivos(n,lugar):
	print("estamos en: ",lugar)
	if n == 0:
		lista_de_archivos = os.listdir()
	else:
		try:
			lista_de_archivos = os.listdir(lugar)
		except:
			print("archivo sin extencion")
	return lista_de_archivos

def mostrar_lista(lista):
	for x in range(len(lista)):
		print(lista[x])

def cambiar_lista(lista,directorio):
	for x in range(len(lista)):
		carpeta = determinador_de_carpetas(lista[x])
		if carpeta == "si":
			sgt_ruta = determinar_siguiente_directorio(directorio,lista[x])
			sub_archivos = listar_archivos(1,sgt_ruta)
			archivos = cambiar_lista(sub_archivos,sgt_ruta)
			lista[x] = archivos
			print(lista[x])

	return lista

def obtener_ruta():
	return os.getcwd()

def determinador_de_carpetas(elemento):
	indice = elemento.find(".")
	if indice == -1:
		return "si"
	else:
		return "no"


def determinar_siguiente_directorio(directorio_actual,carpeta):
	nuevo_directorio = directorio_actual + "\\" + carpeta
	return nuevo_directorio

archivos = listar_archivos(0,"")
ruta = obtener_ruta()
archivos = cambiar_lista(archivos,ruta)
mostrar_lista(archivos)




