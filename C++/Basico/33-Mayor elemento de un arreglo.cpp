# include <iostream>

using namespace std;

int main(){
	int x[] = {1,3,6,23,123,415,123};
	int y = 0;
	for (int z = 0; z != 7 ; z++){
		if (x[z] > y){
			y = x[z];
		}

	}
	cout << "el numero mayoe es: " << y;

	return 0;
}