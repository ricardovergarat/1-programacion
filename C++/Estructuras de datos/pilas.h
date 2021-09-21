# include <iostream>
# include <stdlib.h> // es para importar el new

using namespace std;

// modificar lineas 9,13,24

struct nodo_pila{
	int dato;
	nodo_pila *anterior;
};

void agregar_elemento_pila(nodo_pila &*pila,int elemento){
	nodo_pila *nuevo_espacio = new nodo_pila();
	nuevo_espacio -> dato = elemento;
	nuevo_espacio -> anterior = pila;
	pila = nuevo_espacio;
}

void quitar_elemento_pila(nodo_pila &*pila){
	if (pila == NULL){
		pila = NULL;
	}else{
		pila = pila -> anterior;
	}
}

int obtener_tope(nodo_pila *pila){
	return pila -> dato;
}

int obtener_largo_pila(nodo_pila *pila){
	if (pila == NULL){
		return 0;
	}else{
		int largo = 0;
		nodo_pila *pila_actual = pila;
		while (pila_actual != NULL){
			largo = largo + 1;
			pila_actual = pila -> anterior;
		}
		return largo;
	}
}

nodo_pila* obtener_pila_inversa(nodo_pila *pila){
	int largo = obtener_largo_pila(pila);
	nodo_pila *pila_inversa = NULL;
	for (int i = 0; i < largo;i++){
		int tope = obtener_tope(pila);
		quitar_elemento_pila(pila);
		agregar_elemento_pila(pila_inversa);
	}
	return pila_inversa;
}

void mostrar_pila(nodo_pila *pila){
	if (pila == NULL){
		cout << "[]" << endl;
	}else{
		nodo_pila *pila_inversa = obtener_pila_inversa(pila);
		cout << "[";
		while (pila_inversa != NULL){
			cout << pila -> dato;
			if (pila_inversa -> anterior != NULL){
				cout << ",";
			}
			quitar_elemento_pila(pila_inversa);
		}
		cout << "]" << endl;
	}
}