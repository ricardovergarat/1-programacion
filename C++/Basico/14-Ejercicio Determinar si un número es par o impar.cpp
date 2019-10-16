# include <iostream>

using namespace std;

int main(){
	int x;
	cout << "ingrese un numero: "; cin >> x;
	x = x % 2;
	if (x == 0){
		cout << "el numero es par";
	}else{
		cout << "el nuemro es impar";
	}
	return 0;
}