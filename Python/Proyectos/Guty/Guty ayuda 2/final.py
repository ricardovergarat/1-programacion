# UTF-8
import csv
import math
import numpy as np
import matplotlib.pyplot as plt
import os

def recuperar_datos(nombre):
    with open(nombre,encoding = "utf-8") as archivo:
        lineas = csv.reader(archivo)
        #print(lineas)
        datos = []
        for row in lineas:
            #print(row)
            datos.append(row)
            #print("agregamos",row)
    return datos

def obtener_promedio(lista):
    x = 0
    sumatoria = 0
    while x != len(lista):
        sumatoria = sumatoria + lista[x]
        x = x + 1
    promedio = sumatoria / len(lista)
    return  promedio

def redondear(numero,cantidad_de_decimales):
    numero = round(numero, cantidad_de_decimales)
    return numero

def recuperar_notas(lista):
    x = 3
    while x != len(lista):
        lista[x] = float(lista[x])
        x = x + 1
    return lista[3:len(lista)]

def obtener_promedios_curso(datos):
    # aclaracion el x actua como columna, la y actua como fila del archivo csv
    x = 3 # por que necesitamos empezar por el INDICE 3 del archivo, por que ahi empiezan las pruebas
    promedios_curso = []
    while x != len(datos[0]):
        y = 1 # por que empezaremos por el INDICE de cada fila del archivo
        notas_todos_los_alumnos = []
        while y != len(datos):
            notas_alumno = recuperar_notas(datos[y])
            notas_todos_los_alumnos.append(notas_alumno[x - 3])
            y = y + 1
        promedio_prueba = obtener_promedio(notas_todos_los_alumnos)
        promedio_prueba = redondear(promedio_prueba,1)
        promedios_curso.append(promedio_prueba)
        x = x + 1
    return promedios_curso

def obtener_desviaciones(datos,promedios_curso):
    # aclaracion el x actua como columna, la y actua como fila del archivo csv
    x = 0
    desviaciones_curso = []
    while x != len(promedios_curso):
        y = 1
        sumatoria = 0
        while y != len(datos):
            notas_alumno = recuperar_notas(datos[y])
            resultado = notas_alumno[x] - promedios_curso[x]
            resultado = resultado * resultado
            sumatoria = sumatoria + resultado
            y = y + 1
        cantidad_elementos = len(datos) - 1
        division = sumatoria / cantidad_elementos
        desviacion = math.sqrt(division)
        desviacion = redondear(desviacion,2)
        desviaciones_curso.append(desviacion)
        x = x + 1
    return desviaciones_curso

def obtener_promedios_de_los_alumnos(datos):
    x = 1
    promedios_de_los_alumnos = []
    while x != len(datos):
        notas_alumno = recuperar_notas(datos[x])
        promedio_alumno = obtener_promedio(notas_alumno)
        promedio_alumno = redondear(promedio_alumno,1)
        promedios_de_los_alumnos.append(promedio_alumno)
        x = x + 1
    return promedios_de_los_alumnos

def crear_grafico(desviacion,promedios,notas,rut,nombre,numero):
    x = np.arange(len(desviacion)) # creacion de una matrix con n datos, de dimension 1
    n = 0
    while n != len(desviacion):
        x[n] = n + 1
        n = n + 1
    fig, grafico = plt.subplots()
    grafico.errorbar(x, promedios, yerr=desviacion, color="c",label="Promedio curso")
    grafico.errorbar(x,notas,yerr= 0, color = "r",label="Notas obtenidas",marker="s")
    plt.ylim(1,8) # de 1 a 7 por que ese es el rango de notas en nuestro pais
    # la siguiente linea permite mostrar los datos label de cada graficacion
    plt.legend()
    plt.title(nombre) # aqui va el nombre del estudiante
    plt.xlabel("Prueba")
    plt.ylabel("Notas")
    nombre_imagen = "-" + rut + ".pdf"
    plt.savefig(nombre_imagen)

def crea_todos_los_graficos(datos,promedios,desviaciones):
    x = 1
    while x != len(datos):
        notas = recuperar_notas(datos[x])
        crear_grafico(desviaciones,promedios,notas,datos[x][2],datos[x][1],datos[x][0])
        x = x + 1

def abrir_archivo(nombre):
    archivo = open(nombre)
    lineas = archivo.readlines()
    archivo.close()
    return lineas

def crear_archivo(nombre,lista):
    archivo = open(nombre,"w")
	x = 0
	while x != len(lista):
		archivo.write(lista[x])
		x = x + 1
	archivo.close()
	
def instrucion_consola(intruccion):
	os.system(intruccion)

def arreglar_txt(lista):
	x = 0
	while x != len(lista):
		eliminar = str(x + 1) + ", "
		lista[x] = lista[x].replace(eliminar,"")
		lista[x] = lista[x].replace("\n","")
		x = x + 1
	return lista

def convertir_nombre_a_latex(nombre):
	mayusculas_tilde = ["Á","É","Í","Ó","Ú","Ñ"]
	mayusculas = ["\\'A","\\'E","\\'I","\\'O","\\'U","\\~N"]
	minusculas_tilde = ["á","é","í","ó","ú","ñ"]
	minusculas = ["\\'a","\\'e","\\'i","\\'o","\\'u","\\~n"]
	nombre=list(nombre)
	x = 0
	while x != len(nombre):
		y = 0
		while y != len(mayusculas_tilde):
			if nombre[x] == mayusculas_tilde[y]:
				nombre[x] = nombre[x].replace(mayusculas_tilde[y],mayusculas[y])
			
			if nombre[x] == minusculas_tilde[y]:
				nombre[x] = nombre[x].replace(minusculas_tilde[y],minusculas[y])
			y = y + 1
		x = x + 1
	x = 0
	union = ""
	while x != len(nombre):
		union = union + nombre[x]
		x = x + 1
	return union

def obtener_pasa_palabra(promedioalumno,promediogeneral):
	if promediogeneral < promedioalumno:
		return "favorablemente"
	elif promedioalumno < promediogeneral:
		return "desfavorablemente"
	else: 
		return "regularmente"

def obtener_frase_motivacional(notas_alumno,promedios_curso):
    x = 0
    frases_motivacionales = []
    while x != len(notas_alumno):
        if notas_alumno[x] >= 4:
            if 1.7 < notas_alumno[x] - promedios_curso[x]:
                frases_motivacionales.append("Te fue excelente compa, madre m\\'ia willy! loca(o) revisa tu tel\\'efono en vol\\'a te empiecen a llamar de la nasa .\\\\")
            elif 1 < notas_alumno[x] - promedios_curso[x] <= 1.7:
                frases_motivacionales.append("Buen\\'isima al fin esos horas y horas de estudio valieron la pena, ahora sal a celebrar y disfruta!.\\\\")
            elif 0 < notas_alumno[x] - promedios_curso[x] <= 1:
                frases_motivacionales.append("Te fue un poco mejor que al resto, parece que te contuviste, as\\'i que te lo perdono <3, pero para la otra hay tabla 77.\\\\")
            elif -1 <= notas_alumno[x] - promedios_curso[x] < 0:
                frases_motivacionales.append("Que rico llegar con una buena noticia a la casa para carretear tranquilo o no? pero te recomiendo no carretear todos los viernes y pescar un libro mejor...\\\\")
            elif -1.7 <= notas_alumno[x] - promedios_curso[x] < -1:
                frases_motivacionales.append("Al parecer igual te cost\\'o la prueba, es normal, uno no puede ser bueno en todo, pero ponte las pilas viejo!.\\\\")
            elif notas_alumno[x] - promedios_curso[x] < -1.7:
                frases_motivacionales.append("Igual m\\'as de 4 es yapa asi que tranqui,para la otra acuerdate de resolver bien tus dudas y m\\'as importante que eso, gambary massuu!.\\\\")
            else:
                frases_motivacionales.append("Ser\\'as un genio escondido que quiere pasar desapercibido a traves de las masas? (pensamiento pez...).\\\\ ")
        else:
            if notas_alumno[x] - promedios_curso[x] > 1:
                frases_motivacionales.append("Pucha que les va mal a tus compas, deberian ponerse a estudiar juntose e ir a resolver sus dudas m\\'as seguido 77.\\\\")
            elif 0 < notas_alumno[x] - promedios_curso[x] <= 1:
                frases_motivacionales.append("Lo importante es que fuiste mejor que el promedio, espero tu mamita lo entienda, pero te recomiendo nunca mas decepcionarla.\\\\")
            elif -1.5 <= notas_alumno[x] - promedios_curso[x] < 0:
                frases_motivacionales.append("Mucho carrete y poco estudio, no es cierto mijo? pongale mah weno a lah clase po e\\~nor.\\\\")
            elif -2 <= notas_alumno[x] - promedios_curso[x] < -1.5:
                frases_motivacionales.append("Recuerda que lo m\\'as importante es comprender la materia y nunca olvides que una nota te define, m\\'as estudio para la pr\\'oxima.\\\\")
            elif -2.5 <= notas_alumno[x] - promedios_curso[x] < -2:
                frases_motivacionales.append("Tsss... y como estan las notas sobrino? o me salio porro?... tranqui te recomiendo no bajonearte por lo que dicen los demas y resolver tus dudas despues de clase.\\\\")
            elif notas_alumno[x] - promedios_curso[x] < -2.5:
                frases_motivacionales.append("Ulala se\\~nor franc\\'es, deberias reconsiderar cada vez que omitas el estudio porque andas como auto sin ruedas, empieza a ponerle m\\'as empe\\~no ser\\'a mejor.\\\\")
            else:
                frases_motivacionales.append("Igual al curso le fue mas o menos, debe ser la culpa del profe. jijiji broma (pensamiento pez...).\\\\")
        x = x + 1
    return frases_motivacionales

def actualizar_plantilla(plantilla,archivo_txt,nombre,imagen,rut,promedio_alumno,pasalabra,promedio_curso,frases_motivacionales,notas_alumno,notas_promedio):
    x = 0
    while x != len(plantilla):
        plantilla[x] = plantilla[x].replace("NOMBRE", nombre)
        plantilla[x] = plantilla[x].replace("GATO", imagen) # gato por que el guty no es creativo
        plantilla[x] = plantilla[x].replace("RUT", rut)
        plantilla[x] = plantilla[x].replace("PROMEDIOALUMNO", promedio_alumno)
        plantilla[x] = plantilla[x].replace("PASAPALABRA", pasalabra)
        plantilla[x] = plantilla[x].replace("PROMEDIOCURSO", promedio_curso)
        y = 0
        union = ""
        while y != len(archivo_txt):
            plantilla[x] = plantilla[x].replace("PRUEBA" + str(y + 1), archivo_txt[y] + " " + str(notas_alumno[y]) + " (curso: " + str(notas_promedio[y]) + ")." + "\n")
            union = union + "Para tu prueba " + str(y + 1) + " sobre " + archivo_txt[y] + " esto es lo que opino al respecto: " + frases_motivacionales[y] + "\\\\"
            y = y + 1
        plantilla[x] = plantilla[x].replace("FRASEMOTIVACIONAL", union)
        x = x + 1
    return plantilla

def generar_pdfs(datos,promedios_alumnos,promedio_general):
    x = 1
    while x != len(datos):
        archivo_txt = abrir_archivo("1_temas_prueba.txt")
        archivo_txt = arreglar_txt(archivo_txt)
        plantilla = abrir_archivo("Tarea_Programacion.tex")
        nombre_latex = convertir_nombre_a_latex(datos[x][1])
        notas_alumno = recuperar_notas(datos[x])
        pasa_palabra = obtener_pasa_palabra(promedios_alumnos[x - 1],promedio_general)
        frases_motivacionales = obtener_frase_motivacional(notas_alumno,promedios_curso)
        plantilla_alumno = actualizar_plantilla(plantilla,archivo_txt,nombre_latex,"-" + datos[x][2],datos[x][2],str(promedios_alumnos[x-1]),pasa_palabra,str(promedio_general),frases_motivacionales,notas_alumno,promedios_curso)
        crear_archivo(datos[x][2] + ".tex",plantilla_alumno)
        instrucion_consola("pdflatex "+ datos[x][2] + ".tex") # crear el pdf con el compilador de latex
        instrucion_consola("DEL -" + datos[x][2] + ".pdf") # eliminar imagen del grafico del estudiante
        instrucion_consola("DEL " + datos[x][2] + ".tex") # eliminar plantilla del estudiante
        instrucion_consola("DEL " + datos[x][2] + ".log") # archivo que se crea al compilar el pdf
        instrucion_consola("DEL " + datos[x][2] + ".aux") # archivo que se crea al compilar el pdf
        x = x + 1

if __name__ == "__main__":
    datos = recuperar_datos("o.csv")
    promedios_curso = obtener_promedios_curso(datos) # promedio de cada nota
    desviaciones = obtener_desviaciones(datos,promedios_curso)
    promedios_alumnos = obtener_promedios_de_los_alumnos(datos) # el promedio de cada alumno
    promedio_general = obtener_promedio(promedios_curso)
    promedio_general = redondear(promedio_general,1) # esto es un numero
    crea_todos_los_graficos(datos,promedios_curso,desviaciones)
    instrucion_consola("cls") # por que en crear graficos salen muchos mensajes al crear muchas figuras
    generar_pdfs(datos,promedios_alumnos,promedio_general)
    instrucion_consola("cls")
    print("El programa a finalizado")
