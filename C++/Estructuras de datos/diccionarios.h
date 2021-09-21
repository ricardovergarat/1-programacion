# include <iostream>
# include <stdlib.h> // es para importar el new
# include "lista.cpp"

using namespace std;

// modificar lineas 10,15,26(atencion clave y elemento)

struct nodo_diccionario{
	string clave;
	nodo_lista *lista;
	nodo_diccionario *sgt;
};

bool existe_clave(nodo_diccionario *diccionario,string busqueda){
	nodo_diccionario *diccionario_actual = diccionario;
	while (diccionario_actual != NULL){
		if (diccionario_actual -> clave == busqueda){
			return true;
		}
		diccionario_actual = diccionario_actual -> sgt;
	}
	return false;
}

void agregar_elemento_diccionario(nodo_diccionario *&diccionario,string clave,string elemento){
	if (diccionario == NULL){
		nodo_diccionario *nuevo_espacio = new nodo_diccionario();
		nuevo_espacio -> clave = clave;
		nuevo_espacio -> lista = NULL;
		agregar_elemento_lista(nuevo_espacio -> lista,elemento);
		nuevo_espacio -> sgt = NULL;
		diccionario = nuevo_espacio;
	}else{
		bool clave_existe = existe_clave(diccionario,clave);
		if (clave_existe == true){
			nodo_diccionario *nodo_coincidente = diccionario;
			while ( nodo_coincidente -> clave != clave){
				nodo_coincidente = nodo_coincidente -> sgt;
			}
			agregar_elemento_lista(nodo_coincidente -> lista,elemento);
		}else{
			nodo_diccionario *ultimo_nodo = diccionario;
			whiel (ultimo_nodo -> sgt != NULL){
				ultimo_nodo = ultimo_nodo -> sgt;
			}
			nodo_diccionario *nuevo_espacio = new nodo_diccionario();
			nuevo_espacio -> lista = NULL;
			agregar_elemento_lista(nuevo_espacio -> lista,elemento);
			nuevo_espacio -> sgt = NULL;
			ultimo_nodo -> sgt = nuevo_espacio;
		}
	}
}

void mostrar_diccionario(nodo_diccionario *diccionario){
	if (diccionario == NULL){
		cout << "[]" << endl;
	}else{
		cout << "[";
		nodo_diccionario *diccionario_actual = diccionario;
		while (diccionario_actual != NULL){
			cout << "{" << diccionario_actual -> clave << " : ";
			mostrar_lista(diccionario_actual -> lista);
			cout << "}";
			if (diccionario_actual -> sgt != NULL){
				cout << ",";
			}
			diccionario_actual = diccionario_actual -> sgt;
		}
		cout << "]" << endl;
	}
}
