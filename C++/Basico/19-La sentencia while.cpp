# include <iostream>
# include <conio.h> // biblioteca usada para linea 12 que nesesita presionar un boton para terminar el programa

using namespace std;

int main(){
	int x = 0;
	while (x != 99){
		cout << x << "\n";
		x = x + 1;
	}
	getch();
	return 0;
}