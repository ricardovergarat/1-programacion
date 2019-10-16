# include <iostream>

using namespace std;

int main(){
	int x;
	cout << "ingrese su edad: ", cin >> x;
	if (x > 25 || x < 18){
		cout << "no esta dentro del rango";
	} else {
		cout << "esta dentro del rango";
	}
	return 0;
}