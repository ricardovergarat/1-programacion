# include <stdlib.h>

struct nodo{
	int dato;
	struct nodo *sgt; // aqui guardamos donde esta el siguiente elemento
};

struct nodo *cabeza = NULL;

void insertar_nodo(int a){
	struct nodo *nuevo_espacio = (nodo*) malloc(sizeof(nodo));
	nuevo_espacio -> a;
	
}

int main(){

	return 0;
}
