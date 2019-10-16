# include <iostream>
# include <math.h>

using namespace std;

int main(){
	float x,y;
	cout << "ingrese el valor de x: "; cin >> x;
	cout << "ingrese el valor de y: "; cin >> y;
	float r;
	r = (sqrt(x)) / (pow(y,2) - 1); // pow = potencia o elevado ----- (variable , numero a elevar)
	cout << "el resusltado es: " << r;
	return 0;
}