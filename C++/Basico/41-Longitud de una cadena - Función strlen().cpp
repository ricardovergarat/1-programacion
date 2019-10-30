# include <iostream>
# include <string.h>

using namespace std;

int main(){
	char x[] = "holiwis  ";
	int y;
	y = strlen(x);
	// recordar que los espacios tambien son comtados como caracteres
	cout << "tiene de largo: " << y;
	return 0;
}