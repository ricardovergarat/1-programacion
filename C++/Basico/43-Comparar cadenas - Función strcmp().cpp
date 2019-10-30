# include <iostream>
# include <string.h>

using namespace std;

int main(){
	char x[] = "holiwis";
	char y[] = "holi";
	// si son iguales retorna 0
	// si son diferentes retorna 1
	if (strcmp(x,y) == 0){
		cout << "los string son liguales";
	}else{
		cout << "vale 1 por ende son distintas";
	}
	return 0;
}
