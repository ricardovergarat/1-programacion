# include <iostream>

using namespace std;

class rectangulo{
	public:
		float largo;
		float ancho;
	public:
		rectangulo(float,float);
		void perimetro();
		void area();	
};

rectangulo::rectangulo(float _largo, float _ancho){
	largo = _largo;
	ancho = _ancho;
}

void rectangulo::perimetro(){
	float resultado;
	resultado = 2 * largo + 2 * ancho;
	cout << "el perimetro es: " << resultado << endl;
}

void rectangulo::area(){
	float resultado;
	resultado = largo * ancho;
	cout << "el area es: " << resultado << endl;
}

int main(){
	rectangulo f1(23.32,4.8);
	f1.perimetro();
	f1.area();
	return 0;
}