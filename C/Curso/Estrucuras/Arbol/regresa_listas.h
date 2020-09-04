# include <stdlib.h>

int suma(int a,int b){
	return a + b;
}

int resta(int a,int b){
	return a - b;
}

int multiplicar(int a,int b){
	return a * b;
}

int dividir(int a,int b){
	return a / b;
}

int raro(int a,int b){
	int x,y,z;
	x = suma(a,b);
	y = multiplicar(a,b);
	return multiplicar(x,y);
}


