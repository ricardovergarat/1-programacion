#include <stdio.h>
#include <stdlib.h>

typedef struct arista{
    int u;
    int v;
    int peso;
}arista;

vertice crear_arista(int u,int v){
    arista una_arista;
    una_arista.u = u;
    una_arista.v = v;
    una_arista.peso = 0;
}