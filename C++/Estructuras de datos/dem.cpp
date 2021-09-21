# include <iostream>
# include <stdlib.h> // es para importar el new
# include "lista.cpp"
//# include "diccionarios.cpp"

using namespace std;

int main(){
	//nodo_diccionario *diccionario = NULL;
	//agregar_elemento_diccionario(diccionario,"hola","primero.html");
	//mostrar_diccionario(diccionario);
	nodo_lista *lista = NULL;
	agregar_elemento_lista(lista,"hola");
	mostrar_lista(lista);
}
