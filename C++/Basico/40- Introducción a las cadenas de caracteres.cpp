# include <iostream>
# include <string.h>

using namespace std;

int main(){
	char x[] = "un string";
	char y[] = {'i','z','i'};
	// las dos lineas anteriores dan como resultado lo mismo
	cout << x << "\n";
	cout << y << "\n";
	// cin NO es recomendable para guardar string con espacios
	char z[30];
	cout << "ingrese su nombre: ";
	gets(z);
	cout << z << "\n";
	// el gets() sirve para recuperar todo lo ingresado aunque no coincida con el espacio del arreglo
	// PERO su desventaja es que usa la mmemoria su gusto con tal de almacenar el string
	cout << "ingrese su nombre: ";
	cin.getline(z,20,'\n');
	// cin.getline(variable donde almacenar, cantidad de espacios, caracter final o que no sera registrado)
	// getline() es mas estricto con la cantidad de espacio que almacenara
	// DATO IMPORTANTE EL ULTIMO CARACTER DEBE SER EN COMILLAS SIMPLES DEBIDO A QUE DEBE DE SER UN VARIABLE DE TIPO CHAR
	cout << z << "\n"; 
	return 0;
}
