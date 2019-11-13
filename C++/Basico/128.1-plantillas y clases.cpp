# include <iostream>

using namespace std;

template <class numero>
class rectangulo{
	public:
		numero largo;
		numero ancho;
	public:
		rectangulo(numero,numero);
		void perimetro();
		void area();	
};

template <class numero>
rectangulo<numero>::rectangulo(numero _largo, numero _ancho){
	largo = _largo;
	ancho = _ancho;
}

template <class numero>
void rectangulo<numero>::perimetro(){
	numero resultado;
	resultado = largo + ancho;
	cout << "el perimetro es: " << resultado << endl;
}

template <class numero>
void rectangulo<numero>::area(){
	numero resultado;
	resultado = largo * ancho;
	cout << "el area es: " << resultado << endl;
}
template <class numero>
int main(){
	rectangulo <numero> f1(23,4);
	f1.perimetro();
	f1.area();
	return 0;
}
