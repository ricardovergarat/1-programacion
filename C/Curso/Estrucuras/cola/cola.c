# include <stdlib.h>

typedef struct nodo{
	int dato_cola;
	struct nodo *atras;
}nodo;

int encolar(nodo *cola,int dato){
	if (cola == NULL){
		nodo *nuevo_nodo = (nodo*) malloc(sizeof(nodo));
		nuevo_nodo -> dato_cola = dato;
		nuevo_nodo -> atras = NULL;
		return nuevo_nodo;
	}else{
		nodo *nodo_actual = cola;
		while (nodo_actual -> atras != NULL){
			nodo_actual = nodo_actual -> atras;
		}
		nodo *nuevo_nodo = (nodo*) malloc(sizeof(nodo));
		nuevo_nodo -> dato_cola = dato;
		nuevo_nodo -> atras = NULL;
		nodo_actual -> atras = nuevo_nodo;
		return cola;
	}
}

int desencolar(nodo *cola){
	if (cola == NULL){
		return NULL;
	}
	return cola -> atras;
}

void mostrar_cola(nodo *cola){
	if (cola == NULL){
		printf("[]\n");
	}else{
		printf("[");
		int x = 0;
		while (cola != NULL){
			if (x > 0){
				printf(",");
			}
			x = x + 1;
			printf("%i",cola -> dato_cola );
			cola = desencolar(cola);
		}
		printf("]\n");
	}
}

int largo_cola(nodo *cola){
	int largo = 0;
	while (cola != NULL){
		largo = largo + 1;
		cola = cola -> atras;
	}
	return largo;
}

int main(){
	printf("Hola mundo\n");
	nodo *cola = NULL;
	cola = encolar(cola,1);
	cola = encolar(cola,2);
	mostrar_cola(cola);
	cola = encolar(cola,3);
	cola = encolar(cola,4);
	cola = desencolar(cola);
	mostrar_cola(cola);
	int x = largo_cola(cola);
	printf("%i\n",x );
	cola = desencolar(cola);
	cola = desencolar(cola);
	cola = desencolar(cola);
	mostrar_cola(cola);
	cola = desencolar(cola);
	mostrar_cola(cola);
	//int x = largo_cola(cola);
	//printf("%i\n",x );
	return 0;
}
