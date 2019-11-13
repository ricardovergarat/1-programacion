# include <iostream>
# include <fstream>
// esta libreria es para los archivos

using namespace std;

void escribir(){
	ofstream archivo; // creamos una variable llamada archivo de tipo archivo txt,py,etc
	archivo.open("almas.txt",ios::out); // aqui abrimos el archivo y que tipo de lectura r,w,rw ------> la sintasis es la sgt: nombre variable.open(nombre archivo,ios:: entrada(in) o saliad(out) )
	// archivo.open("C:\\Users\\Intel\\Desktop\\almas.txt",ios::out);
	// si se usa el linea anterior se creara el archivo en ese directorio
	if (archivo.fail()){ // esto ocurre si hay un problema apara abrir el archivo
		cout << "no se pudo abiri el archivo";
		exit(1); // esto es un mensaje para nosotros para decirnos que algo salio mal
	}

	archivo << "hola a todos los weones";
	archivo << "una segunda linea en el archivo";
	// se pondra efectivamente ambos mensajes pero sedido a que falta \n se vera junto por lo que se debe recordar como siempre

	archivo.close();
}

int main(){
	escribir();
	return 0;
}
