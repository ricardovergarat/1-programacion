# include <stdlib.h>

typedef struct nodo{
	int dato_lista;
	struct nodo *anterior;
	struct nodo *siguiente;
}nodo;

int agregar(nodo *lista,int dato){
	//printf("Reservaremos: %i bytes\n",sizeof(nodo) );
	nodo *nuevo_nodo = (nodo*) malloc(sizeof(nodo));
	nuevo_nodo -> dato_lista = dato;
	nuevo_nodo -> siguiente = NULL;
	if (lista != NULL){
		lista -> siguiente = nuevo_nodo;
	}
	nuevo_nodo -> anterior = lista;
	return nuevo_nodo;
}

void mostrar_lista(nodo *lista){
	if (lista == NULL){
		printf("[]\n");
	}else{
		while (lista -> anterior != NULL){
			lista = lista -> anterior;
		}
		printf("[");
		int x = 0;
		while (lista != NULL){
			if (x > 0){
				printf(",");
			}
			x = x + 1;
			printf("%i",lista -> dato_lista );
			lista = lista -> siguiente;
		}
		printf("]\n");
	}
}

int largo_lista(nodo *lista){
	int largo = 0;
	while (lista != NULL){
		largo = largo + 1;
		lista = lista -> anterior;
	}
	return largo;
}

int eliminar(nodo *lista){
	nodo *nodo_anterior = lista -> anterior;
	nodo_anterior -> siguiente = NULL;
	return nodo_anterior;
}

int main(){
	nodo *lista = NULL;
	lista = agregar(lista,1);
	lista = agregar(lista,2);
	lista = agregar(lista,3);
	lista = agregar(lista,4);
	mostrar_lista(lista);
	int x = largo_lista(lista);
	printf("%i\n",x );
	lista = eliminar(lista);
	mostrar_lista(lista);
	return 0;
}
