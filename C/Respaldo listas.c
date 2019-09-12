#include <stdio.h>
#include <stdlib.h>

typedef struct _nodo
{
	int valor;
	struct _nodo * pNext;
}_Nodo;

typedef _Nodo * _pNodo;

_pNodo CrearLista(int valor)
{
	_pNodo Lista;

	Lista = (_pNodo) malloc (sizeof(_Nodo));
	Lista->valor = valor;
	Lista->pNext = NULL;

	return Lista;
}
_pNodo InsertarElementoAlFinal(int valor, _pNodo ListaInicial)
{
    _pNodo NuevoNodo;
    _pNodo Auxiliar = ListaInicial;
    NuevoNodo =  malloc(sizeof(_Nodo));
 
    NuevoNodo->valor = valor;
    NuevoNodo->pNext = NULL;
 
    if (ListaInicial->pNext == NULL)
    {
        ListaInicial->pNext = NuevoNodo;
    }
    else
    {
        while(Auxiliar->pNext != NULL)
        {
            Auxiliar =  Auxiliar->pNext;
        }
        Auxiliar->pNext = NuevoNodo;
    }
 
    return NuevoNodo; 
}
_pNodo InsertarElementoAlInicio(int valor, _pNodo ListaInicial)
{
    _pNodo NuevoNodo;
    NuevoNodo = malloc(sizeof(_Nodo));
    NuevoNodo->valor = valor;
    NuevoNodo->pNext = ListaInicial;
 
    return NuevoNodo; 
}
_pNodo InsertarElementoPosterior(int valor, _pNodo ElementoAnterior)
{
    _pNodo NuevoNodo;
    NuevoNodo = malloc(sizeof(_Nodo));
 
    NuevoNodo->valor = valor;
    NuevoNodo->pNext = ElementoAnterior->pNext;
 
    ElementoAnterior->pNext = NuevoNodo;
 
    return NuevoNodo; 
}
_pNodo EliminarPrimerElemento(_pNodo Lista)
{
    _pNodo Auxiliar;
    Auxiliar = Lista;
 
    if (Auxiliar->pNext == NULL)
    {
        return Lista; 
    }
    Lista = Auxiliar->pNext;
    free(Auxiliar);
 
    return Lista; 
}
int EliminarElemento(_pNodo Elemento, _pNodo Lista)
{
    _pNodo Auxiliar;
    Auxiliar = Lista;
    while (Auxiliar != NULL)
    {
        if (Auxiliar->pNext == Elemento)
        {
            break;
        }
        Auxiliar = Auxiliar->pNext;
    }
    if (Auxiliar == NULL)
    {
        return 0;
    }
    else
    {
        if (Elemento->pNext == NULL)
        {
            Auxiliar->pNext = NULL;
        }
        else
        {
            Auxiliar->pNext = Elemento->pNext;
        }
 
        free(Elemento);
        return 1;
    }
}
_pNodo BuscarElemento(int valor, _pNodo Lista)
{
    _pNodo Auxiliar;
 
    Auxiliar = Lista;
    while(Auxiliar != NULL)
    {
        if (Auxiliar->valor == valor)
        {
            break;
        }
        Auxiliar = Auxiliar->pNext;
    }
    return Auxiliar; // Retornamos dirección del elemento encontrado
}
_pNodo ImprimirLista(_pNodo lista){
	 _pNodo Auxiliar = lista;
	 while (Auxiliar != NULL){
	 	printf("El valor es: %d\n",Auxiliar->valor);
        Auxiliar = Auxiliar -> pNext;

	 }
}
int main()
{
	_pNodo miLista;

	miLista = CrearLista(43);

	printf("El primer elemento en miLista es: %d\n", miLista->valor);
	printf("La dirección del siguiente elemento en miLista es: %p\n", miLista->pNext);
	InsertarElementoAlFinal(5,miLista);
    miLista = InsertarElementoAlInicio(3,miLista);
    InsertarElementoPosterior(9,miLista);
    miLista = EliminarPrimerElemento(miLista);
    EliminarElemento(miLista->pNext,miLista);
    BuscarElemento(9,miLista);
	ImprimirLista(miLista);
	printf(
		"\n"
		"\nTAREA"
		"\nPara la proxima clase traer implementado el código para probar cada una de las funciones de manipulción de la lista."
		"\nAdemás crear una nueva función, llamada \"ImprimirLista\", para mostrar por pantalla todos los elementos de la lista"
		"\n"
	);
}
