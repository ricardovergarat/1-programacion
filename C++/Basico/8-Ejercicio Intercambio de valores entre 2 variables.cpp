# include <iostream>

using namespace std;

int main(){
	float x,y,z;
	cout << "ingrese el valor de x: ", cin >> x;
	cout << "ingrese el valor de y: ", cin >> y;
	z = x;
	x = y;
	y = z;
	cout << "x ahora vale: " << x << "\n";
	cout << "y ahora vale: " << y;
	return 0;
}