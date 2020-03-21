# include <stdlib.h>

size_t obtener_size(float *puntero){
	return sizeof(puntero);
}

int main(){
	float v[5];
	long unsigned y = sizeof(v);
	printf("El tamaño en bytes es: %lu\n",y);
	unsigned x = obtener_size(&v);
	printf("El numero de bytes retornado es: %i\n",x );
	return 0;
}
