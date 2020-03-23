# include <iostream>
# include <stdlib.h> // es para importar el new

using namespace std;

struct nodo{
	int dato;
	nodo *sgt; // ubicacion del siguietne elemento
};

void mostrar_pila(nodo *pila){ // el elemento mas a la izquierda es el tope de la pila
	nodo *pila_actual = pila;
	if ( pila_actual == NULL ){
		cout << "[]" << endl;
	}else{
		cout << "[";
		while ( pila_actual -> sgt != NULL ){
			cout << pila_actual -> dato << ",";
			pila_actual = pila_actual -> sgt;
		}
	cout << "]" << endl;
	}
}

void agregar_elemento(nodo *&pila, int numero){
	nodo *nuevo_espacio = new nodo(); // reservamos espacio en la memoria
	nuevo_espacio -> dato = numero; // inicializamos el elemento que queriamos poner en la pila
	nuevo_espacio -> sgt = pila; // ubicacion de la pila anterior
	//cout << "Elemento: " << nuevo_espacio -> dato << "		apuntador anterior: " << nuevo_espacio -> sgt << endl;
	pila = nuevo_espacio; // por que nuestra nueva pila ahora le agregamos un nuevo elemento, es decir actualizamo la pila
}

void quitar_elemento(nodo *&pila){
	cout << "El elemento a quitar es: " << pila -> dato << "	ubicacion de la pila anterior es: " << pila -> sgt << endl;
	pila = pila -> sgt;
}

void obtener_tope(nodo *pila){// cambiar a tipo de retorno si queremos el tope en una variable
	if ( pila == NULL ){
		cout << "Esta pila esta vacia" << endl;
		// return 0; // esto por si queremos retornar el tope
	}
	// tipo tope = pila -> dato;
	int tope = pila -> dato;
	cout << "Esto es el tope: " << tope << endl;
}

void obtener_largo(nodo *pila){
	if ( pila == NULL ){
		cout << "0" << endl;
		//return 0;
	}
	int x = 0;
	nodo *pila_actual = pila;
	while ( pila_actual -> sgt != NULL ){
		x = x + 1;
		pila_actual = pila_actual -> sgt;
	}
	cout << "La pila tiene largo: " << x << endl;
}

int main(){
	nodo *pila = NULL; // pila = []
	mostrar_pila(pila);
	agregar_elemento(pila,5);
	agregar_elemento(pila,3);
	agregar_elemento(pila,8);
	mostrar_pila(pila);
	agregar_elemento(pila,13);
	agregar_elemento(pila,17);
	agregar_elemento(pila,19);
	agregar_elemento(pila,27);
	agregar_elemento(pila,65);
	agregar_elemento(pila,132);
	mostrar_pila(pila);
	quitar_elemento(pila);
	obtener_tope(pila);
	obtener_largo(pila);
	return 0;
}
