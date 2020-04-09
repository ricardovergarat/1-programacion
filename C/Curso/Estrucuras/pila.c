# include <stdlib.h>

typedef struct nodo{
	int dato;
	struct nodo *sgt; // aqui guardamos donde esta el siguiente elemento
}nodo;

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

void agregar_elemento(nodo *pila, int numero){
	printf("Esta es la ubicacion de la pila al entrar: %i\n",pila);
	nodo *nuevo_espacio = (nodo*) malloc(sizeof(nodo)); // reservamos espacio en memoria de tamaño nodo(su tamaño en bytes)
	nuevo_espacio -> dato = numero;
	nuevo_espacio -> sgt = pila;
	printf("El dato es: %i     ubicacion pila anterior: %i\n",nuevo_espacio -> dato,nuevo_espacio -> sgt);
	printf("Ubicacion del nuevo nodo: %i      Ubicacion nueva pila: %i\n",nuevo_espacio,pila);
	*pila = *nuevo_espacio;
	printf("Ubicacion del nuevo nodo: %i      Ubicacion nueva pila: %i\n",nuevo_espacio,pila);
}

int main(){
	nodo *pila = NULL;
	if (pila == NULL){
		printf("Apunta a null\n");
	}
	printf("esto es el apuntador: %i\n",pila);
	printf("Esto es su ubicacion: %i\n",&pila );
	agregar_elemento(&*pila,3);
	agregar_elemento(&*pila,4);
	printf("fuera 2: %i\n",pila);
	//mostrar_pila(pila);
	//agregar_elemento(&pila,42);
	//agregar_elemento(&pila,443);
	//agregar_elemento(&pila,123);
	//agregar_elemento(&p2,43);
	//mostrar_pila(pila);
	return 0;
}
