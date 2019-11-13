# include <iostream>
# include <fstream>
# include <string.h>

using namespace std;

void agregar(){
	ofstream archivo;
	archivo.open("uno.txt",ios::app); // queremos agregar texto al archivo
	if (archivo.fail()){
		cout << "hubo algun problema";
	}
	archivo << "1";// es importante aclarar que se escribe despues de donde se puso por ultima vez el coso de escribir
	archivo.close();
}

int main(){
	agregar();
	return 0;
}
