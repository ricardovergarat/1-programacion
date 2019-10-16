# include <iostream>

using namespace std;

int main(){
	int x;
	cout << "ingrese un nuemro entre 1 y 5: "; cin >> x;
	switch(x){
		case 1: cout << "es el numero 1"; break;
		case 2: cout << "es el numero 2"; break;
		case 3: cout << "es el numero 3"; break;
		case 4: cout << "es el numero 4"; break;
		case 5: cout << "es el numero 5"; break;
		default : cout << "no esta en el rango"; 
	}
	return 0;
}
