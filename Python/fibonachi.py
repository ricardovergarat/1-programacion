
def pedir_numero():
	x = input("ingrese que hasta que posicion quiere los nuemros de fibonachi: ")
	return int(x)

def fibonachi(n):
	x = 0
	while x != n:
		if x == 0:
			suma = 0
			ant = suma
			ant2 = 1
			print(suma)
		else:
			suma = ant + ant2
			print(suma)
			ant2 = ant
			ant = suma
		x = x + 1

if __name__ == "__main__":
 	a = pedir_numero()
 	fibonachi(a)

