# include <iostream>
# include <string.h>
// esta es la biblioteca que permite usar los sgt metodos y no string.h
# include <stdlib.h>

using namespace std;

int main(){
	char x[] = "2019";
	int y;
	y = atoi(x);
	// el metodo atof() es lo mismo pero para flotantes
	cout << y;
	return 0;
}