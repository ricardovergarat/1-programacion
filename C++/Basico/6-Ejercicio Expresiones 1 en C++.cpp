# include <iostream>

using namespace std;

int main(){
	float a,b;
	cout << "ingrese el valorde a: "; cin >> a;
	cout << "ingrese el valor de b. "; cin >> b;
	float c;
	c = a / b + 1;
	// cout.precision(2) esto mostrala solo dos numeros despues del decimal
	cout << "El resusltado es: " << c;
	return 0;
}