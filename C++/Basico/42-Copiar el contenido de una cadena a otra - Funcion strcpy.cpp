# include <iostream>
# include <string.h>

using namespace std;

int main(){
	char x[] = "ricardo vergara toloza";
	char y[20];
	strcpy(y,x);
	// strcpy(al que copiar, contenido original)
	// aun que el contenido original sea mayor al numeros de espacios declarado lo compiara de todas formas
	cout << y;
	return 0;
}