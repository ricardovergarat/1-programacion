# include <iostream>

using namespace std;
 int main(){
 	int x;
 	cout << "ingrese la cantidad de elemtos: "; cin >> x;
 	int y[x];
 	int a;
 	for (int z = 0; z != x;z++){
 		cout << "ingrese el elemento del indice " << z << ":"; cin >> a;
 		y[z] = a;
 	}
 	for (int z = 0; z != x; z++){
 		cout << y[z];
 	}
 	return 0;
 }
