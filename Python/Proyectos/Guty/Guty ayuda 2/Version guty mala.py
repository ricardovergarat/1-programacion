#UTF-8
import matplotlib.pyplot as plt
import os
import math
import csv
import numpy as np
def recuperar_datos(nombre):
    with open(nombre, encoding="utf-8") as archivo:
        lineas = csv.reader(archivo)
        #print(lineas)
        datos = []
        for row in lineas:
            #print(row)
            datos.append(row)
            #print("agregamos",row)
    return datos

def los_promedios(datos_0,y):
    suma=0
    #print(tamaño)
    x=1
    while x!=len(datos_0):
        #print(datos[x][y])
        suma=suma+float(datos_0[x][y])
        x=x+1
    #print(suma)        
    El=round(suma/len(datos_0),1)
    #print(El)
    return El

def obtener_todos_los_promedios(datos_1):
    z=3
    notas=[]
    while z!=len(datos_1[2]):
        b=los_promedios(datos_1,z)
        z=z+1
        notas.append(b)
    return notas

def crear_archivo(nombre):
    archivo = open(nombre,"w")
    x = 0
    while x < 10:
        archivo.write(str(x) + "\n")
        x = x + 1
    archivo.close()

def desviacion_estandar(datos_0,promedio,columna):
    Sumatoria=0
    x=1
    while x!=len(datos_0):
        #print(datos_0[x][columna])
        resultado=float(datos_0[x][columna])-promedio #elementos de la sumatoria
        resultado=resultado*resultado #elevando al cuadrado
        Sumatoria=Sumatoria+resultado #blucle de sumas
        x=x+1
    n=len(datos_0)-1
    resultado_division=Sumatoria/n
    resultado_raiz=math.sqrt(resultado_division)
    print("desviacion_estandar: ",round(resultado_raiz,2))    
    return round(resultado_raiz,2)    

def todas_las_desviaciones(datos,los_promedios):
    x=0
    print (len(los_promedios))
    lista_desviaciones=[]
    while x!=len(los_promedios):
        desviacion=desviacion_estandar(datos,los_promedios[x],x+3)
        lista_desviaciones.append(desviacion)
        x=x+1
    return lista_desviaciones

def crear_grafico(desviacion,los_promedios,notas,nombre,numero):
    x=np.arange(len(desviacion))
    z=0
    while z!=len(x):
        x[z]=z+1
        z=z+1
    fig,grafico=plt.subplots()
    grafico.errorbar(x,los_promedios,yerr=desviacion,color="b",label="Promedio curso")
    grafico.errorbar(x,notas,yerr=0,color="r",label="Notas obtenidas",marker="s")
    plt.legend()
    plt.title(nombre)
    plt.xlabel("Prueba")
    plt.ylabel("Notas")
    Nombre_imagen=str(numero)+"ª "+nombre+".png"
    plt.savefig(Nombre_imagen)

def graficos(datos,los_promedios,desviaciones):
    x=1
    while x!=len(datos):
        notas=notas_string(datos[x],len(datos[0]))
        crear_grafico(desviaciones,los_promedios,notas,datos[x][1],x)
        x=x+1

def notas_string(notas,cantidad_de_notas):
    x=3
    Notas=[]
    while x!=cantidad_de_notas:
        nota_numero=float(notas[x])
        Notas.append(nota_numero)
        x=x+1
    return Notas

def abrir_archivo(nombre):
    archivo=open(nombre)
    contenido=archivo.readlines()
    return contenido

def promedio_alumno(datos,fila):
    x=0
    notas=notas_string(datos[fila],len(datos[0]))
    Sumatoria=0
    #print (notas)
    while x!=len(notas):
        Sumatoria=Sumatoria+notas[x]
        x=x+1
    Promedio=Sumatoria/len(notas)
    Promedio=round(Promedio,1)
    return Promedio

def promedio_todos_los_alumnos(datos):
    x=1
    Todos_los_promedios=[]
    while x!=len(datos):
        Promedio=promedio_alumno(datos,x)
        Todos_los_promedios.append(Promedio)
        x=x+1
    return Todos_los_promedios
    

#def replacion(plantilla,nombre,rut,promedio):










if __name__ == "__main__":

    datos = recuperar_datos("o.csv")
    #los_promedios = obtener_todos_los_promedios(datos)   
    #desviaciones=todas_las_desviaciones(datos,los_promedios)
    #graficos(datos,los_promedios,desviaciones)
    #contenido=abrir_archivo("1_temas_prueba.txt")
    #print (contenido)
    #latex=abrir_archivo("Tarea_Programacion.tex")
    #print (latex)
    Promedios_generales=promedio_todos_los_alumnos(datos)
    print(Promedios_generales)
    #os.system("pdflatex chupala.tex")