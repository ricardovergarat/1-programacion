# include <stdlib.h>
# include <stdbool.h>

typedef struct nodo{
	int dato_arbol;
	struct nodo *izquierda;
	struct nodo *derecha;
}nodo;

int determinar_lado(int a,int b){
	if (a <= b){
		return 0;
	}
	return 1;
}

bool nodo_valido_para_agregar(nodo *nodo_arbol,int dato){
	if ( (nodo_arbol -> izquierda == NULL) || (nodo_arbol -> derecha == NULL) ){
		int lado = determinar_lado(nodo_arbol -> dato_arbol,dato);
		if ( ( (lado == 0) && (nodo_arbol -> izquierda == NULL) ) || ( (lado == 1) && (nodo_arbol -> derecha == NULL) ) ){
			return true;
		}
		return false;
	}
	return false;
}

int cambio_de_nodo(nodo *nodo_arbol,int dato){
	int lado = determinar_lado(nodo_arbol -> dato_arbol,dato);
	if (lado == 0){
		return nodo_arbol -> izquierda;
	}else{
		return nodo_arbol -> derecha;
	}
}

int agregar(nodo *arbol,int dato){
	if (arbol == NULL){
		nodo *nuevo_nodo = (nodo*) malloc(sizeof(nodo));
		nuevo_nodo -> dato_arbol = dato;
		nuevo_nodo -> izquierda = NULL;
		nuevo_nodo -> derecha = NULL;
		return nuevo_nodo;
	}else{ // implica que tenemos almenos un elemento
		if ( (arbol -> izquierda == NULL) && (arbol -> derecha == NULL) ){ // solo existe un elemento
			int lado = determinar_lado(arbol -> dato_arbol, dato);
			if (lado == 0){ // lado izquierda
				nodo *nuevo_nodo = (nodo*) malloc(sizeof(nodo));
				nuevo_nodo -> dato_arbol = dato;
				nuevo_nodo -> izquierda = NULL;
				nuevo_nodo -> derecha = NULL;
				arbol -> izquierda = nuevo_nodo;
			}else{ // lado derecho
				nodo *nuevo_nodo = (nodo*) malloc(sizeof(nodo));
				nuevo_nodo -> dato_arbol = dato;
				nuevo_nodo -> izquierda = NULL;
				nuevo_nodo -> derecha = NULL;
				arbol -> derecha = nuevo_nodo;
			}
			return arbol;
		}else{ // tenemos 2 o mas elementos
			nodo *nivel_arbol = arbol;
			bool valido = nodo_valido_para_agregar(nivel_arbol,dato);
			while ( valido != true ){
				nivel_arbol = cambio_de_nodo(nivel_arbol,dato);
				valido = nodo_valido_para_agregar(nivel_arbol,dato);
			}
			int lado = determinar_lado(nivel_arbol -> dato_arbol,dato);
			if (lado == 0){
				nodo *nuevo_nodo = (nodo*) malloc(sizeof(nodo));
				nuevo_nodo -> dato_arbol = dato;
				nuevo_nodo -> izquierda = NULL;
				nuevo_nodo -> derecha = NULL;
				nivel_arbol -> izquierda = nuevo_nodo;
			}else{
				nodo *nuevo_nodo = (nodo*) malloc(sizeof(nodo));
				nuevo_nodo -> dato_arbol = dato;
				nuevo_nodo -> izquierda = NULL;
				nuevo_nodo -> derecha = NULL;
				nivel_arbol -> derecha = nuevo_nodo;
			}
			return arbol;
		}	
	}
}

int main(){
	nodo *arbol = NULL;
	arbol = agregar(arbol,40);
	return 0;
}
