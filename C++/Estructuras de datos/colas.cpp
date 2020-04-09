# include <iostream>
# include <stdlib.h>

using namespace std;

struct nodo{
	int dato;
	nodo *sgt; // ubicacion del siguietne elemento
};

void mostrar_cola(nodo *frente, nodo *fin){
	if ( ( frente && fin ) == NULL ){
		cout << "[]" << endl;
	}else{
		nodo *cola_actual = frente;
		cout << "primer elemento de la cola: " << cola_actual -> dato << "		y su ubicacion es: " << cola_actual << endl;
		cout << "[";
		while ( cola_actual -> sgt != NULL ){
			cout << cola_actual -> dato << ",";
			cola_actual = cola_actual -> sgt;
			cout << "ubicacion del siguietne nodo: " << cola_actual << endl;
		}
	}
}

void agregar_elemento(nodo *&frente, nodo *&fin,int n){
	nodo *nuevo_espacio = new nodo();
	nuevo_espacio -> dato = n;
	nuevo_espacio -> sgt = NULL;
	if ( frente == NULL ){
		// impica que la cola estaba vacia antes de crear este nuevo nodo
		frente = nuevo_espacio;
	}else{
		fin -> sgt = nuevo_espacio;
	}
	fin = nuevo_espacio;
	cout << "dato es: " << nuevo_espacio -> dato << "		y su siguietne apuntador es: " << nuevo_espacio -> sgt << endl;
}


int main(){
	nodo *frente = NULL;
	nodo *fin = NULL;
	cout << "ubicacion del puntero: " << &frente << endl;
	mostrar_cola(frente,fin);
	agregar_elemento(frente,fin,10);
	cout << "nueva cola "<< fin << endl;
	agregar_elemento(frente,fin,15);
	cout << "nueva cola "<< fin << endl;
	agregar_elemento(frente,fin,20);
	cout << "nueva cola "<< fin << endl;
	agregar_elemento(frente,fin,25);
	cout << "nueva cola "<< fin << endl;
	mostrar_cola(frente,fin);

	return 0;
}
