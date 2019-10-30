# include <iostream>

using namespace std;

int main(){
	int x[] = {4,31,54,2,3};
	int i,j,aux;
	for (i = 0 ; i < 5; i++){
		for (j = 0; j < 5; j++){
			if (x[j] > x[j + 1]){
				aux = x[j];
				x[j] = x[j + 1];
				x[j + 1] = aux;
			}
		}
	}

	cout << "ascendente";
	for (i = 0; i < 5; i++){
		cout << x[i] << "\n";
	}
	return 0;
}
