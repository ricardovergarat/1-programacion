# include <stdlib.h>

//forma 1
/*
struct animal{
	char nombre[30];
	int edad;
	float peso;
};

int main(){
	struct animal perro = {"atila",10,3.5};
	printf("El nombre del animal es: %s\n",perro.nombre );
	printf("El peso del animal es: %.2f\n",perro.peso );
	printf("La edad del animal es: %i\n", perro.edad);
	return 0;
}
*/

// forma 2
/*
typedef struct animal{
	char nombre[30];
	int edad;
	float peso;
}animal;

int main(){
	animal perro = {"atila",10,3.5};
	printf("El nombre del animal es: %s\n",perro.nombre );
	printf("El peso del animal es: %.2f\n",perro.peso );
	printf("La edad del animal es: %i\n", perro.edad);
	return 0;
}
*/

// forma 3
/*
typedef struct{
	char nombre[30];
	int edad;
	float peso;
}animal;

int main(){
	animal perro = {"atila",10,3.5};
	printf("El nombre del animal es: %s\n",perro.nombre );
	printf("El peso del animal es: %.2f\n",perro.peso );
	printf("La edad del animal es: %i\n", perro.edad);
	return 0;
}
*/


