# include <iostream>
# include <stdlib.h> // es para importar el new

using namespace std;

// modificar lineas 9,13,39

struct nodo_cola{
	int dato;
	nodo_cola *anterior;
};

void agregar_elemento_cola(nodo_cola &*cola,int elemento){
	if (cola == NULL){
		nodo_cola *nuevo_espacio = new nodo_cola();
		nuevo_espacio -> dato = elemento;
		nuevo_espacio -> anterior = NULL;
		cola = nuevo_espacio;
	}else{
		nodo_cola *ultimo_nodo = cola;
		while (ultimo_nodo -> anterior != NULL){
			ultimo_nodo = ultimo_nodo -> anterior;
		}
		nodo_cola *nuevo_espacio = new nodo_cola();
		nuevo_espacio -> dato = elemento;
		nuevo_espacio -> anterior = NULL;
		ultimo_nodo -> anterior = nuevo_espacio;
	}
}

void quitar_elemento_cola(nodo_cola &*cola){
	if (cola == NULL){
		cola = NULL;
	}else{
		cola = cola -> anterior;
	}
}

int obtener_cabeza(nodo_cola *cola){
	if (cola == NULL){
		return NULL;
	}
	return cola -> dato;
}

void mostrar_cola(nodo_cola *cola){
	if (cola == NULL){
		cout << "[]" << endl;
	}else{
		nodo_cola *cola_actual = cola;
		cout << "[";
		while (cola_actual != NULL){
			cout << cola_actual -> dato;
			if (cola_actual -> anterior != NULL){
				cout << ",";
			}
			quitar_elemento_cola(cola_actual);
		}
		cout << "]" << endl;
	}
}