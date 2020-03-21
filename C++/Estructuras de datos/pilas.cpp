# include <iostream>
# include <stdlib.h> // es para importar el new

using namespace std;

struct nodo{
	int dato;
	nodo *sgt; // ubicacion del ssiguietne elemento
};

void mostrar_pila(nodo *&pila){
	cout << "El dato es: " << pila -> dato << endl;
	cout << "apuntador anterior es: " << pila -> sgt << endl;
	cout << pila -> sgt << endl;
	nodo *anterior = pila -> sgt;
	//cout << "Esto es anterior: " << anterior << endl;
	
}

void agregar_elemento(nodo *&pila, int numero){
	nodo *nuevo_espacio = new nodo(); // reservamos espacio en la memoria
	nuevo_espacio -> dato = numero; // inicializamos el elemento que queriamos poner en la pila
	nuevo_espacio -> sgt = pila; // esto el elemento que esta debajo por que es una pila, es decir nuevo espacio es ahora la cima
	pila = nuevo_espacio; // por que nuestra nueva pila ahora le agregamos un nuevo elemento
}


int main(){
	nodo *pila = NULL; // pila = []
	agregar_elemento(pila,5);
	mostrar_pila(pila);
	agregar_elemento(pila,3);
	mostrar_pila(pila);
	agregar_elemento(pila,8);
	mostrar_pila(pila);
	return 0;
}
