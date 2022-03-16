#include <stdio.h>
#include <stdlib.h>

typedef struct vertice{
    int id;
    float latitud;
    float longuitud;
}vertice;

vertice crear_vertice(int id,float latitud,float longuitud){
    vertice un_vertice;
    un_vertice.id = id;
    un_vertice.latitud = latitud;
    un_vertice.longuitud = longuitud;
}