# include <iostream>
# include <conio.h>

using namespace std;

int main(){
	int x[] = {2,7,3};
	int y;
	for (int z = 0; z != 3; z++){
		y = y + x[z];
	}
	cout << "la suma es: " << y;
	getch();
	return 0;
}