// evitar el uno de hugito

#include<stdio.h>
#include <stdlib.h>


int main(){
	FILE *datos;
	char leer[10];
	int eso;
	int i = 0;
	datos = fopen("rondas.txt", "r");
	eso = feof(datos);
	while (eso == 0){
		eso = feof(datos);
		if (eso != 0){
			break;
		}
		else{
			printf("EOF = %d",eso);
			printf("\n");
			fscanf(datos, " %[^\n]", &leer);
			printf("se leyo: %s",&leer);
			printf("\n");
			i = i + 1;
		}
	}
	printf("I = %d\n",i);
	char conjuto[i];
	
	fclose(datos);


	return 0;
}
