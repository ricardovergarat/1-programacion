# include <iostream>
# include <string.h>

using namespace std;

int main(){
	char x[] = "gaming";
	strrev(x);
	// la misma variable es la que esta al reves no es guarda en otra varibla asi que es recomendable un respaldo en caso especificos
	cout << x;
	return 0;
}
