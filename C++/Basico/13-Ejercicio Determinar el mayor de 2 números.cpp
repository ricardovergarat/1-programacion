# include <iostream>

using namespace std;

int main(){
	float x,y;
	cout << "ingrese elvalor del primer numero: "; cin >> x;
	cout << "ingrese el sgundo numero: "; cin >> y;
	if (x > y){
		cout << "el x es mayor que y";
	}else{
		if (x < y){
			cout << "el x es mejor que y";
		}else{
			cout << "los numeros son iguales";
		}
	}
	return 0;
}