# include <iostream>

using namespace std;

class persona{
	private:
		string nombre;
		int edad;
	public:
		persona(string , int);
		virtual void mostrar(); // virtual es la palabrea reservada para polimosfismo
};

persona::persona(string _nombre, int _edad){
	nombre = _nombre;
	edad = _edad;
}

void persona::mostrar(){
	cout << "nombre: " << nombre << endl;
	cout << "edad: " << edad << endl;
}

class alumno : public persona{
	private:
		float nota;
	public:
		alumno(string , int ,float);
		void mostrar();
};

alumno::alumno(string _nombre, int _edad, float _nota) : persona(_nombre, _edad){
	nota = _nota;
}

void alumno::mostrar(){
	persona::mostrar();
	cout << "nota: " << nota << endl;
}

class profesor : public persona{
	private:
		string ramo;
	public:
		profesor(string , int , string);
		void mostrar();
};

profesor::profesor(string _nombre, int _edad, string _ramo) : persona(_nombre,_edad){
	ramo = _ramo;
}

void profesor::mostrar(){
	persona::mostrar();
	cout << "ramo: " << ramo << endl;
}

int main(){
	persona *vector[3];
	vector[0] = new alumno("izi",19,3.9);
	vector[0] -> mostrar();
	vector[1] = new alumno("ella",18,4.1);
	vector[1] -> mostrar();
	vector[2] = new profesor("hugo",43,"cagarte la vida");
	vector[2] -> mostrar();
	return 0;
}
