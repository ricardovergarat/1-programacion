# include <iostream>
# include <string.h>

using namespace std;

int main(){
	char x[] = "mensaje";
	strupr(x);
	// este metodo tambien hace el cambio en la variable dadao por lo que hay que ser cuidado con este metodo
	cout << x;
	return 0;
}
