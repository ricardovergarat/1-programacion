# include <iostream>
# include <stdlib.h> // es para importar el new

using namespace std;

// modificar lineas 9,13

struct nodo_lista{
	string dato;
	nodo_lista *sgt;
};

void agregar_elemento_lista(nodo_lista *&lista,string elemento){
	if (lista == NULL){
		nodo_lista *nuevo_espacio = new nodo_lista();
		nuevo_espacio -> dato = elemento;
		nuevo_espacio -> sgt = NULL;
		lista = nuevo_espacio;
	}else{
		nodo_lista *ultimo_nodo = lista;
		while (lista -> sgt != NULL){
			ultimo_nodo = lista -> sgt;
		}
		nodo_lista *nuevo_espacio = new nodo_lista();
		nuevo_espacio -> dato = elemento;
		nuevo_espacio -> sgt = NULL;
		ultimo_nodo -> sgt = nuevo_espacio;
	}
}

void mostrar_lista(nodo_lista *lista){
	if (lista == NULL){
		cout << "[]" << endl;
	}else{
		nodo_lista *lista_actual = lista;
		cout << "[";
		while (lista_actual != NULL){
			cout << lista_actual -> dato;
			if (lista_actual -> sgt != NULL){
				cout << ",";
			}
			lista_actual = lista_actual -> sgt;
		}
		cout << "]" << endl;
	}
}
