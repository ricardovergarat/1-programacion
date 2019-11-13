# include <iostream>
# include <fstream>
# include <string.h>

using namespace std;

void lectura(){
	ifstream archivo; // i = input esto es para la lectura de archivos
	string text;
	archivo.open("dos.txt",ios::in);
	if (archivo.fail()){
		cout << "ese archivo no existe";
	}
	while (!archivo.eof()){ // mientras no sea el final del archivo
		getline(archivo,text); // estamos recuperando lo escrito en el texto y lo estamos guardando el la variable texto
		// ahora vamos a imprimir en consola el texto del archivo
		cout << text << endl;
	}
	
}

int main(){
	lectura();
	return 0;
}
