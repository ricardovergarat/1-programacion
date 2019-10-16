# include <iostream>

using namespace std;

int main(){
	int x;
	cout << "ingrese el primer numero: ";
	cin >> x;
	int y;
	cout << "ingrese el segundo numero: ";
	cin >> y;
	int a,b,c,d;
	a = x + y;
	b = x - y;
	c = x * y;
	d = x / y;
	cout << a << " " << b << " " << c << " " << d;
	return 0;
}