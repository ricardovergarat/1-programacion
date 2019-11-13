# include <iostream>

using namespace std;

class auto{
	// atributos
	// si no establesco el encapsulamiento es privado
	public:
		int creacion;
		int matricula;
		char color;
	// metodos
		void encender_motor(){
			cout << "se encendio el motor..." << endl;
		}
		void acelerar(){
			cout << "el auto aranco" << endl;
		}
		void frenar(){
			cout << "el aut ofreno" << endl;
		}
};

int main(){

	return 0;
}