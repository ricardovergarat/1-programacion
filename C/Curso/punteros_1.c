# include <stdlib.h>

int main(){
	int x = 23;
	int *u = &x;
	printf("%i\n",u ); // esto es la ubicacion
	printf("%i\n",*u); // esto es el contenido
	return 0;
}
