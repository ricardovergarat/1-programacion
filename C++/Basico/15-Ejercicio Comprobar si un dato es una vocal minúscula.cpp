# include <iostream>

using namespace std;

int main(){
	char x;
	cout << "ingrese un caracter: "; cin >> x;
	// el switch en char debe ser en comilla simple si o si
	switch(x){
		case 'a':
		case 'e':
		case 'i':
		case 'o':
		case 'u': cout << "es una vocal minuscula "; break;
		default: cout << "es una vocal mayuscula";
	}
	return 0;
}