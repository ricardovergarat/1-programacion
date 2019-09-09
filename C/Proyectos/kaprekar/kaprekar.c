//Constante de Kaprekar

#include<stdio.h>
#include<string.h>
#include<stdlib.h>


void abrir_archivo(){
	FILE *archivo;
	char caracteres[5];
	archivo = fopen("entrada.txt","r");
	fgets(caracteres,3,archivo);
	printf("%s",caracteres);
	fgets(caracteres,3,archivo);
	printf("%s",caracteres);
	/*
	if (archivo == NULL)
 		exit(1);
 	else
        {
 	    printf("\nEl contenido del archivo de prueba es \n\n");
 	    while (feof(archivo) == 0)
 	    {
 		fgets(caracteres,3,archivo);
 		printf("%s",caracteres);
 	    }
            system("PAUSE");
        }
        fclose(archivo);
    */
}


int main(){
	abrir_archivo();
	return 0;
}
