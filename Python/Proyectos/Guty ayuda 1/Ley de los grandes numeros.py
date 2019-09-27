import random
from matplotlib import pyplot as plt

def Numero_de_lanzamientos():
	x=input("Ingrese la cantidad de lanzamientos: ")
	return int(x)

def Ciclo(Lanzamientos):
	x=0
	Lista_dados_1=[]
	Lista_dados_2=[]
	Suma_dados=[]
	while x<Lanzamientos:
		D1,D2,RE=Lanzamiento_de_dados()
		Lista_dados_1,Lista_dados_2,Suma_dados=Listas(D1,D2,RE,Lista_dados_1,Lista_dados_2,Suma_dados)
		x=x+1
	return Lista_dados_1,Lista_dados_2,Suma_dados

def Lanzamiento_de_dados():
	dado_1=random.randint(1,6)
	dado_2=random.randint(1,6)
	Resultado=Suma_de_dados(dado_1,dado_2)
	return dado_1,dado_2,Resultado

def Suma_de_dados(a,b):
	c=a+b
	return c
     
def Listas(D1,D2,RE,Lista_dados_1,Lista_dados_2,Suma_dados):
	Lista_dados_1.append(D1)
	Lista_dados_2.append(D2)
	Suma_dados.append(RE)
	return Lista_dados_1,Lista_dados_2,Suma_dados

def Contar_Sumas(Suma_dados):
	y=2
	x=0
	Lista_de_Sumas=[]
	while x<11:
		x=x+1
		Repeticiones=Suma_dados.count(y)
		y=y+1
		Lista_de_Sumas.append(Repeticiones)
	return Lista_de_Sumas

def Probabilidad(Lanzamientos,Lista_de_Sumas):
	x=0
	Lista_de_Probabilidad=[]
	while x<11:
		Probabilidad_Relativa=(Lista_de_Sumas[x]/Lanzamientos)*100
		x=x+1
		Lista_de_Probabilidad.append(Probabilidad_Relativa)
	return Lista_de_Probabilidad

def Mostrar_Sumas(Lista_de_Sumas,Lista_de_Probabilidad):
	x=0
	y=1
	while x<11:
		y=y+1
		print("(Numero ",y,",Probabilidad ",y,")=(",Lista_de_Sumas[x],",",Lista_de_Probabilidad[x],"%)")
		x=x+1

def Grafico(Lista_de_Sumas):
	figura = plt.figure(u'Grafico de barras')
	grafico = figura.add_subplot(111)
	numero_string = ["2","3","4","5","6","7","8","9","10","11","12"]
	xx = range(len(Lista_de_Sumas))
	print(Lista_de_Sumas)
	print(xx)
	grafico.bar(xx, Lista_de_Sumas, width=0.8, align='center')
	grafico.set_xticks(xx)
	grafico.set_xticklabels(numero_string)
	plt.show()

Lanzamientos=Numero_de_lanzamientos()
Lista_dados_1,Lista_dados_2,Suma_dados=Ciclo(Lanzamientos)
Lista_de_Sumas=Contar_Sumas(Suma_dados)
Lista_de_Probabilidad=Probabilidad(Lanzamientos,Lista_de_Sumas)
Mostrar_Sumas(Lista_de_Sumas,Lista_de_Probabilidad)
Grafico(Lista_de_Sumas)