# include <iostream>

using namespace std;

class persona{
	private:
		string nombre;
		int edad;
	public:
		persona(string, int);
		void mostrar_persona();
};

persona::persona(string _nombre, int _edad){
	nombre = _nombre;
	edad = _edad;
}

void persona::mostrar_persona(){
	cout << "la persona se llama: " << nombre << " y su edad es:  " << edad << endl;
}

class alumno : public persona{  // esta es la synntasis para la herencia     se pude leer como alumno es herencia publica de la clase persona
	private:
		string carrera;
		int ano_ingreso;
	public:
		alumno(string , int , string, int); // contructor de alumno
		void mostrar_alumno();
};

alumno::alumno(string _nombre, int _edad, string _carrera, int _ano_ingreso):persona(_nombre, _edad){ // :persona(_nombre, _edad) esa parte es para decir que recuperamos esos datos 
	carrera = _carrera;
	ano_ingreso = _ano_ingreso;
}

void alumno::mostrar_alumno(){
	mostrar_persona();
	cout << "carrera: " << carrera << endl;
	cout << "ano de ingreso: " << ano_ingreso << endl;
}


int main(){
	alumno levi("levi",20,"informatica",2018);
	levi.mostrar_alumno();
	return 0;
}