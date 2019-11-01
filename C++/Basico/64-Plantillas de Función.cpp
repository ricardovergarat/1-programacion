# include <iostream>

using namespace std;


template <class tipon>
void mostrar(tipon x){
	cout << x << "\n";
}

template <class tipon>
void suma(tipon x,tipon y){
	tipon z = x + y;
	mostrar(z);
}
template <class tipon>
void resta(tipon x , tipon y){
	tipon z = x - y;
	mostrar(z);

}
/*
tipon mul(tipon x, tipon y){
	tipon z = x * y;
	mostrar(z);
	return z;
}

tipon divi(tipon x , tipon y){
	tipon z = x / y;
	mostrar(z);
	return z;
}
*/



int main(){
	int n1,n2;
	n1 = 3;
	n2 = 6;
	suma(n1,n2);
	resta(n1,n2);
	/*
	b = resta(n1,n2);
	c = mul(n1,n2);
	d = divi(n1,n2);
	*/
	return 0;
}
