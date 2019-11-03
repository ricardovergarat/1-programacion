# include <iostream>
# include <stdlib.h>

using namespace std;

/*
1- crear espacio de memoria
2- cargar el valor dentro del nodo
3 - cargar el puntero pila dentro del nodo
4 - asignar el nuevo nodo
*/

// los nuemros indicaran el orden que considero neseario para entederlo
// 1 agregar la libreria <stdlib.h> para usar new que reservara espacio en memoria

// 2 crear un estructura que tenga datos y  un puntero 
struct nodo{
	int numero;
	nodo *sgt;
}; 

void agregar_pila(nodo *&pila, int n){
	// 4- crearemos un nuevo nodo llamado "nuevo" de tipo puntero y tendra un espacio reservador por el new de tipo "nodo", otra forma seria como de tipo int,float,char, etc
	nodo *nuevo = new nodo();
	// 5- ahora asignaremos el valor de el "atributo" numero de tipo "nodo"---- (recordar que en funciones se debe usar -> en vez de . para las estructuras)
	nuevo -> numero = n;
	cout << "n vale: " << nuevo -> numero << endl;
	// 6- igual que el paso anterior asignaremos el puntero
	nuevo -> sgt = pila;
	cout << "esto es sgt: " << nuevo -> sgt << endl;
	// 7- aqui actulizamos nuestra pila, es decir de estar vacia agregamos el elemento "n" , esto ocure efectivamente por que pasamos la variable pila por referencia-- es decir =====*&pila===0 por esa parte del codigo
	pila = nuevo; 
	cout << "la pila es: " << pila << endl;
	// la pila ahora que esta actualizada tiene otra direcion de memoria a la que apunta 
	// cabe aclarar que siempre el ultimo es la cabeza de la pila 
	//cout << "se actualizo la pila" << endl;

}

int main(){
	// 3- creamos una pila que apunta a nada ya que no tiene nada que es lo mismo que decir apunta a nada o NULL
	nodo *pila = NULL;
	for (int x = 0; x < 10; x++){
		agregar_pila(pila,x);
	}
	agregar_pila(pila,34);


	return 0;

}
