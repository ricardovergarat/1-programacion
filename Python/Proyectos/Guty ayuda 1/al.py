import random

def Lanzamiento_de_dados():
	dado_1=random.randint(1,6)
	dado_2=random.randint(1,6)
	Resultado=Suma_de_dados(dado_1,dado_2)
	print("Suma de dados: ",Resultado)
	return dado_1,dado_2,Resultado

def Suma_de_dados(a,b):
	c=a+b
	return c

def Numero_de_lanzamientos():
	x=input("Ingrese la cantidad de lanzamientos: ")
	print("Cantidad de lanzamientos: ",x)
	return int(x)

def Ciclo(Lanzamientos):
	x=0
	Lista_dados_1=[]
	Lista_dados_2=[]
	Suma_dados=[]
	while x<Lanzamientos:
		D1,D2,RE=Lanzamiento_de_dados()
		Lista_dados_1,Lista_dados_2,Suma_dados = Listas(D1,D2,RE,Lista_dados_1,Lista_dados_2,Suma_dados)
		print("dado 1: ",Lista_dados_1[x],"  dado 2: ",Lista_dados_2[x]," suma = ",Suma_dados[x])
		x=x+1

def Listas(D1,D2,RE,Lista_dados_1,Lista_dados_2,Suma_dados):
	Lista_dados_1.append(D1)
	Lista_dados_2.append(D2)
	Suma_dados.append(RE)
	return Lista_dados_1,Lista_dados_2,Suma_dados

Lanzamientos=Numero_de_lanzamientos()
Ciclo(Lanzamientos)