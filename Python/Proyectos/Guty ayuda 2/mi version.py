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

def abrir_archivo(nombre):
    archivo = open(nombre)
    lineas = archivo.readlines()
    archivo.close()
    return lineas

def arreglar_txt(lista):
    x = 0
    while x != len(lista):
        eliminar = str(x + 1) + ", "
        lista[x] = lista[x].replace(eliminar,"")
        lista[x] = lista[x].replace("\n","")
        x = x + 1
    return lista

def redondear(numero,cantidad_de_decimales):
    numero = round(numero, cantidad_de_decimales)
    return numero

def obtener_promedio(lista,cantidad_decimales):
    x = 0
    sumatoria = 0
    while x != len(lista):
        sumatoria = sumatoria + lista[x]
        x = x + 1
    promedio = sumatoria / len(lista)
    promedio = redondear(promedio,cantidad_decimales)
    return  promedio

def recuperar_notas(lista):
    x = 3
    while x != len(lista):
        lista[x] = float(lista[x])
        x = x + 1
    return lista[3:len(lista)]

def obtener_promedios_pruebas(datos):
    x = 3
    promedio_cada_pruebas = []
    while x != len(datos[0]):
        y = 1
        notas_alumnos_en_prueba = []
        while y != len(datos):
            notas_alumno = recuperar_notas(datos[y])
            notas_alumnos_en_prueba.append(notas_alumno[x - 3])
            y = y + 1
        promedio_prueba = obtener_promedio(notas_alumnos_en_prueba,1)
        promedio_cada_pruebas.append(promedio_prueba)
        x = x + 1
    return  promedio_cada_pruebas

def obtener_desviaciones_estandar(datos,promedios_cada_prueba):
    # aclaracion el x actua como columna, la y actua como fila del archivo csv
    x = 0
    desviacion_cada_prueba = []
    while x != len(promedios_cada_prueba):
        y = 1
        sumatoria = 0
        while y != len(datos):
            notas_alumno = recuperar_notas(datos[y])
            resultado = notas_alumno[x] - promedios_cada_prueba[x]
            resultado = resultado * resultado
            sumatoria = sumatoria + resultado
            y = y + 1
        cantidad_elementos = len(datos) - 1
        division = sumatoria / cantidad_elementos
        desviacion = math.sqrt(division)
        desviacion = redondear(desviacion,2)
        desviacion_cada_prueba.append(desviacion)
        x = x + 1
    return desviacion_cada_prueba

def instrucion_consola(instruccion):
    os.system(instruccion)

def generar_pdfs(datos,archivo_txt,promedio_cada_prueba,promedio_curso,desviaciones):
    x = 1
    while x != len(datos):
        plantilla = abrir_archivo("Tarea_Programacion.tex")
        nombre_latex = convertir_nombre_a_latex(datos[x][1])
        notas_alumno = recuperar_notas(datos[x])
        promedio_alumno = obtener_promedio(notas_alumno,1)
        nombre_imagen = crear_grafico(datos[x][1],datos[x][2],notas_alumno,promedio_cada_prueba,desviaciones)
        pasa_palabra = obtener_pasa_palabra(promedio_alumno,promedio_curso)
        frases_motivacionales = obtener_frases_motivacional(notas_alumno,promedio_cada_prueba)
        plantilla_alumno,nombre_tex,nombre_log,nombre_aux = actualizar_plantilla(plantilla,archivo_txt,nombre_latex,datos[x][2],nombre_imagen,promedio_alumno,promedio_curso,notas_alumno,promedio_cada_prueba,pasa_palabra,frases_motivacionales)
        crear_archivo(nombre_tex,plantilla_alumno)
        instrucion_consola("pdflatex " + nombre_tex)
        instrucion_consola("DEL " + nombre_imagen)
        instrucion_consola("DEL " + nombre_tex)
        instrucion_consola("DEL " + nombre_log)
        instrucion_consola("DEl " + nombre_aux)
        #print("estudiante: ",nombre_latex,"   notas: ",notas_alumno,"       nombre imagen: ",nombre_imagen,"    pasa palabra: ",pasa_palabra," curso: ",promedio_curso,"  alumno: ",promedio_alumno, "   nombre .tex: ",nombre_tex)
        x = x + 1

def convertir_nombre_a_latex(nombre):
    mayusculas_tilde = ["Á", "É", "Í", "Ó", "Ú", "Ñ"]
    mayusculas = ["\\'A", "\\'E", "\\'I", "\\'O", "\\'U", "\\~N"]
    minusculas_tilde = ["á", "é", "í", "ó", "ú", "ñ"]
    minusculas = ["\\'a", "\\'e", "\\'i", "\\'o", "\\'u", "\\~n"]
    nombre = list(nombre)
    x = 0
    while x != len(nombre):
        y = 0
        while y != len(mayusculas_tilde):
            if nombre[x] == mayusculas_tilde[y]:
                nombre[x] = nombre[x].replace(mayusculas_tilde[y], mayusculas[y])

            if nombre[x] == minusculas_tilde[y]:
                nombre[x] = nombre[x].replace(minusculas_tilde[y], minusculas[y])
            y = y + 1
        x = x + 1
    x = 0
    union = ""
    while x != len(nombre):
        union = union + nombre[x]
        x = x + 1
    return union

def crear_grafico(nombre,rut,notas,promedios_cada_prueba,desviaciones):
    x = np.arange(len(desviaciones))
    n = 0
    while n != len(desviaciones):
        x[n] = n + 1
        n = n + 1
    fig, grafico = plt.subplots()
    grafico.errorbar(x,promedios_cada_prueba,yerr=desviaciones,color="c",label="Promedio curso")
    grafico.errorbar(x,notas,yerr=0,color="r",label="Notas obtenidas",marker="s")
    plt.ylim(1, 8)  # de 1 a 7 por que ese es el rango de notas en nuestro pais
    # la siguiente linea permite mostrar los datos label de cada graficacion
    plt.legend()
    plt.title(nombre)  # aqui va el nombre del estudiante
    plt.xlabel("Prueba")
    plt.ylabel("Notas")
    nombre_imagen = "-" + rut + ".pdf"
    plt.savefig(nombre_imagen)
    return nombre_imagen

def obtener_pasa_palabra(promedio_alumno,promedio_curso):
    if promedio_curso< promedio_alumno:
        return "favorablemente"
    elif promedio_alumno < promedio_curso:
        return "desfavorablemente"
    else:
        return "regularmente"

def obtener_frases_motivacional(notas_alumno,promedio_cada_prueba):
    x = 0
    frases_motivacionales = []
    while x != len(notas_alumno):
        if notas_alumno[x] >= 4:
            if 1.7 < notas_alumno[x] - promedio_cada_prueba[x]:
                frases_motivacionales.append("Te fue excelente compa, madre m\\'ia willy! loca(o) revisa tu tel\\'efono en vol\\'a te empiecen a llamar de la nasa .\\\\")
            elif 1 < notas_alumno[x] - promedio_cada_prueba[x] <= 1.7:
                frases_motivacionales.append("Buen\\'isima al fin esos horas y horas de estudio valieron la pena, ahora sal a celebrar y disfruta!.\\\\")
            elif 0 < notas_alumno[x] - promedio_cada_prueba[x] <= 1:
                frases_motivacionales.append("Te fue un poco mejor que al resto, parece que te contuviste, as\\'i que te lo perdono <3, pero para la otra hay tabla 77.\\\\")
            elif -1 <= notas_alumno[x] - promedio_cada_prueba[x] < 0:
                frases_motivacionales.append("Que rico llegar con una buena noticia a la casa para carretear tranquilo o no? pero te recomiendo no carretear todos los viernes y pescar un libro mejor...\\\\")
            elif -1.7 <= notas_alumno[x] - promedio_cada_prueba[x] < -1:
                frases_motivacionales.append("Al parecer igual te cost\\'o la prueba, es normal, uno no puede ser bueno en todo, pero ponte las pilas viejo!.\\\\")
            elif notas_alumno[x] - promedio_cada_prueba[x] < -1.7:
                frases_motivacionales.append("Igual m\\'as de 4 es yapa asi que tranqui,para la otra acuerdate de resolver bien tus dudas y m\\'as importante que eso, gambary massuu!.\\\\")
            else:
                frases_motivacionales.append("Ser\\'as un genio escondido que quiere pasar desapercibido a traves de las masas? (pensamiento pez...).\\\\ ")
        else:
            if notas_alumno[x] - promedio_cada_prueba[x] > 1:
                frases_motivacionales.append("Pucha que les va mal a tus compas, deberian ponerse a estudiar juntose e ir a resolver sus dudas m\\'as seguido 77.\\\\")
            elif 0 < notas_alumno[x] - promedio_cada_prueba[x] <= 1:
                frases_motivacionales.append("Lo importante es que fuiste mejor que el promedio, espero tu mamita lo entienda, pero te recomiendo nunca mas decepcionarla.\\\\")
            elif -1.5 <= notas_alumno[x] - promedio_cada_prueba[x] < 0:
                frases_motivacionales.append("Mucho carrete y poco estudio, no es cierto mijo? pongale mah weno a lah clase po e\\~nor.\\\\")
            elif -2 <= notas_alumno[x] - promedio_cada_prueba[x] < -1.5:
                frases_motivacionales.append("Recuerda que lo m\\'as importante es comprender la materia y nunca olvides que una nota te define, m\\'as estudio para la pr\\'oxima.\\\\")
            elif -2.5 <= notas_alumno[x] - promedio_cada_prueba[x] < -2:
                frases_motivacionales.append("Tsss... y como estan las notas sobrino? o me salio porro?... tranqui te recomiendo no bajonearte por lo que dicen los demas y resolver tus dudas despues de clase.\\\\")
            elif notas_alumno[x] - promedio_cada_prueba[x] < -2.5:
                frases_motivacionales.append("Ulala se\\~nor franc\\'es, deberias reconsiderar cada vez que omitas el estudio porque andas como auto sin ruedas, empieza a ponerle m\\'as empe\\~no ser\\'a mejor.\\\\")
            else:
                frases_motivacionales.append("Igual al curso le fue mas o menos, debe ser la culpa del profe. jijiji broma (pensamiento pez...).\\\\")
        x = x + 1
    return frases_motivacionales

def actualizar_plantilla(plantilla,archivo_txt,nombre,rut,nombre_imagen,promedio_alumno,promedio_curso,notas_alumno,promedio_cada_prueba,pasa_palabra,frases_motivacionales):
    x = 0
    while x != len(plantilla):
        plantilla[x] = plantilla[x].replace("NOMBRE", nombre)
        plantilla[x] = plantilla[x].replace("GATO", nombre_imagen)  # gato por que el guty no es creativo
        plantilla[x] = plantilla[x].replace("RUT", rut)
        plantilla[x] = plantilla[x].replace("PROMEDIOALUMNO", str(promedio_alumno))
        plantilla[x] = plantilla[x].replace("PASAPALABRA", pasa_palabra)
        plantilla[x] = plantilla[x].replace("PROMEDIOCURSO", str(promedio_curso))
        y = 0
        union = ""
        while y != len(archivo_txt):
            plantilla[x] = plantilla[x].replace("PRUEBA" + str(y + 1),archivo_txt[y] + " " + str(notas_alumno[y]) + " (curso: " + str(promedio_cada_prueba[y]) + ")." + "\n")
            union = union + "Para tu prueba " + str(y + 1) + " sobre " + archivo_txt[y] + " esto es lo que opino al respecto: " + frases_motivacionales[y] + "\\\\"
            y = y + 1
        plantilla[x] = plantilla[x].replace("FRASEMOTIVACIONAL", union)
        x = x + 1
    nombre_tex = rut + ".tex"
    nombre_log = rut + ".log"
    nombre_aux = rut + ".aux"
    return plantilla,nombre_tex,nombre_log,nombre_aux

def crear_archivo(nombre,lista):
    archivo = open(nombre,"w")
    x = 0
    while x != len(lista):
        archivo.write(lista[x])
        x = x + 1
    archivo.close()

if __name__ == "__main__":
    datos = recuperar_datos("o.csv")
    archivo_txt = abrir_archivo("1_temas_prueba.txt")
    archivo_txt = arreglar_txt(archivo_txt)
    promedio_cada_prueba = obtener_promedios_pruebas(datos)
    promedio_curso = obtener_promedio(promedio_cada_prueba,1)
    desviaciones = obtener_desviaciones_estandar(datos,promedio_cada_prueba)
    generar_pdfs(datos,archivo_txt,promedio_cada_prueba,promedio_curso,desviaciones)
    instrucion_consola("cls")
    print("El programa a finalizado")