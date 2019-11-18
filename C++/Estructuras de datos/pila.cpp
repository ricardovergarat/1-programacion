# include <iostream>
# include <stdlib.h>

using namespace std;

struct nodo{
	int numero;
	nodo *sgt;
};

void agregar_elementos(nodo *&pila , int n){
	nodo *espacio = new nodo();
	espacio -> numero = n;
	cout << espacio -> numero << endl;
	espacio -> sgt = pila;
	cout << espacio-> sgt << endl;
	pila = espacio;

}

int main(){
	nodo *pila = NULL;
	for (int x = 0; x != 13; x++){
		agregar_elementos(pila,x);
	}
	return 0;
}
