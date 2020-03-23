# include <stdlib.h>

typedef struct nodo{
	int dato;
	struct nodo *sgt; // aqui guardamos donde esta el siguiente elemento
}nodo;
/*
void mostrar_pila(nodo *pila){
	nodo *pila_actual = pila;
	if (pila_actual == NULL){
		printf("[]\n");
	}else{
		printf("[");
		while (pila_actual -> sgt != NULL){
			printf("%i,",pila_actual -> dato);
			pila_actual = pila_actual -> sgt;
		}
		printf("]\n");
	}
}
*/
void agregar_elemento(nodo *pila, int a){
	nodo *nuevo_espacio = (nodo*) malloc(sizeof(nodo)); // reservamos espacio en memoria de tamaño nodo(su tamaño en bytes)
	nuevo_espacio -> dato = a;
	nuevo_espacio -> sgt = pila;
	pila = nuevo_espacio;
	printf("El dato es: %i     ubicacion pila anterior: %i\n",nuevo_espacio -> dato,nuevo_espacio -> sgt);
}


int main(){
	nodo *pila = NULL;
	agregar_elemento(&pila,3);
	agregar_elemento(&pila,4);
	agregar_elemento(&pila,42);
	agregar_elemento(&pila,443);
	agregar_elemento(&pila,123);
	//mostrar_pila(pila);
	return 0;
}
