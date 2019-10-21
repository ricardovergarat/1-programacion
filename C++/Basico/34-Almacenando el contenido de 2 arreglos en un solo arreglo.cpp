# include <iostream>

using namespace std;

int main(){
	char x[] = {'a','b','c','d','e'};
	char y[] = {'f','g','h','i','j'};
	char z[2];
	z[0] = x;
	z[1] = y;
	for (int a = 0; a != 2; a++){
		cout << z[a];
	}

	return 0;
}
