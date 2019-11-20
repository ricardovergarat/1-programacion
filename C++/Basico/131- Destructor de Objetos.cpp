# include <iostream>

using namespace std;

class perro{
	private:
		string nombre, raza;
	public:
		perro(string,string);
		~perro(); // recordar que los destrucotres tienen el mismo nombre de la clase pero comienza con ~
		void mostrar_datos();
		void jugar();
};

perro::perro(string _nombre, string _raza){
	nombre = _nombre;
	raza = _raza;
}

// la siguiente linea es el destructor
perro::~perro(){
}

void perro::mostrar_datos(){
	cout << "el perro se llama: " << nombre << " y su raza es: " << raza << endl;
}

void perro::jugar(){
	cout << "el perro comenzo a jugar" << endl;
}

int main(){
	perro p1("atila","pastor aleman");
	p1.mostrar_datos();
	p1.jugar();
	p1.~perro();
	// aqui ya se elimino el objeto
	return 0;
}
