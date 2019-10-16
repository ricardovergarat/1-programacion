# include <iostream>

using namespace std;

int main(){
	float x,y,z,a,b,c;
	cout << "ingrese el valor de x: ", cin >> x;
	cout << "ingrese el valor de y: ", cin >> y;
	cout << "ingrese el valor de z: ", cin >> z;
	cout << "ingrese el valor de a: ", cin >> a;
	cout << "ingrese el valor de b: ", cin >> b;
	cout << "ingrese el valor de c: ", cin >> c;
	float r;
	r = (x + y/z ) / (a + b/ c);
	cout << "el resultado es: " << r;

	return 0;
}