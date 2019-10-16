# include <iostream>

using namespace std;

int main(){
	float x,y,z;
	cout << "ingrese el x: "; cin >> x ;
	cout << "ingrese el y: "; cin >> y ;
	cout << "ingrese el z: "; cin >> z ;
	x = x * 0.3;
	y = y * 0.6;
	z = z * 0.1;
	float r;
	r = x + y + z;
	cout << "la nota final es: " << r;
	return 0;
}
