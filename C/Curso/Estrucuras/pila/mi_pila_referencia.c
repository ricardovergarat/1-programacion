# include <stdlib.h>

typedef struct nodo{
	int dato_pila;
	struct nodo *anterior;
}nodo;

int apilar(nodo *pila,int dato){
	//printf("Reservaremos: %i bytes\n",sizeof(nodo) );
	nodo *nuevo_nodo = (nodo*) malloc(sizeof(nodo));
	nuevo_nodo -> dato_pila = dato;
	nuevo_nodo -> anterior = pila;
	//printf("El dato de la pila es: %i     La ubicaion del nodo anterior es: %i          Ubicaion actual de la pila es: %i      \n",nuevo_nodo -> dato_pila,nuevo_nodo -> anterior,nuevo_nodo);
	return nuevo_nodo;
}

int desapilar(nodo *pila){
	if (pila == NULL){
		return NULL;
	}
	return pila -> anterior;
}

void mostrar_cima(nodo *pila){
	printf("La cima es: %i\n",pila -> dato_pila );
}

int pila_inversa(nodo *pila){
	nodo *pila_inversa = NULL;
	while (pila != NULL){
		pila_inversa = apilar(pila_inversa,pila -> dato_pila);
		pila = desapilar(pila);
	}
	return pila_inversa;
}

void mostrar_pila(nodo *pila){
	pila = pila_inversa(pila);
	if (pila == NULL){
		printf("[]\n" );
	}else{
		printf("[");
		int x = 0;
		while (pila != NULL){
			if (x > 0){
				printf(",");
			}
			x = x + 1;
			printf("%i",pila -> dato_pila );
			pila = desapilar(pila);
		}
		printf("]\n");
	}
}

int largo_pila(nodo *pila){
	int largo = 0;
	while (pila != NULL){
		largo = largo + 1;
		pila = pila -> anterior;
	}
	return largo;
}

int main(){
	nodo *pila = NULL;
	pila = apilar(pila,1);
	pila = apilar(pila,2);
	pila = apilar(pila,3);
	pila = apilar(pila,4);
	pila = apilar(pila,5);
	pila = apilar(pila,6);
	pila = desapilar(pila);
	mostrar_pila(pila);
	pila = desapilar(pila);
	mostrar_pila(pila);
	int x = largo_pila(pila);
	printf("%i\n",x );
	return 0;
}
