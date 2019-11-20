# include <iostream>

using namespace std;

class animal{
	private:
		int edad;
	public:
		animal(int);
		virtual void comer();
};

animal::animal(int _edad){
	edad = _edad;
}

void animal::comer(){
	cout << "comer en el suelo" << endl;
}

class humano : public animal{
	private:
		string nombre;
	public:
		humano(int, string);
		void comer();
};

humano::humano(int _edad, string _nombre) : animal(_edad){
	nombre = _nombre;
}

void humano::comer(){
	cout << "comer en la mesa" << endl;
}

class perro : public animal{
	private:
		string nombre;
		string raza;
	public:
		perro(int, string, string);
		void comer();
};

perro::perro(int _edad, string _nombre, string _raza) : animal(_edad){
	nombre = _nombre;
	raza = _raza;
}

void perro::comer(){
	cout << "comer en el plato del suelo" << endl;
}

int main(){
	animal *animales[2];
	animales[0] = new perro(5,"atila","pastor aleman");
	animales[1] = new humano(20,"ricardo");
	animales[0] -> comer();
	animales[1] -> comer();
	return 0;
}