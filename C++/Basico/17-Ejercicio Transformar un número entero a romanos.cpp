# include <iostream>

using namespace std;

int main(){
	int x,u,d,c,m;
	cout << "ingrese un numero: "; cin >> x;
	u = x % 10;
	cout << u;
	x = x / 10;
	cout << "\n" << x;
	return 0;
}
