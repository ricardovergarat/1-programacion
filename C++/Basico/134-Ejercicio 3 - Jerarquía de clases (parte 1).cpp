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
	cout << "nombre: " << nombre << endl;
	cout << "edad: " << edad << endl;
}

class empleado : public persona{
	private:
		int sueldo;
	public:
		empleado(string , int , int);
		void mostrar_empleado();
};

empleado::empleado(string _nombre, int _edad, int _sueldo ) : persona(_nombre, _edad){ // le digo que ya tengo los datos _nombre y _edad
	sueldo = _sueldo;
}

void empleado::mostrar_empleado(){
	mostrar_persona();
	cout << "sueldo: " << sueldo << endl;
}

class estudiante : public persona{
	private:
		float nota;
	public:
		estudiante(string , int , float);
		void mostrar_estudiante();
};

estudiante::estudiante(string _nombre, int _edad, float _nota) : persona(_nombre, _edad){
	nota = _nota;
}

void estudiante::mostrar_estudiante(){
	mostrar_persona();
	cout << "nota: " << nota << endl;
}

class universitario : public estudiante{
	private:
		string carrera;
	public:
		universitario(string , int , float, string);
		void mostrar_universitario();
};

universitario::universitario(string _nombre , int _edad, float _nota, string _carrera) : estudiante(_nombre, _edad, _nota){
	carrera = _carrera;
}

void universitario::mostrar_universitario(){
	mostrar_estudiante();
	cout << "carrera: " << carrera << endl;
}

int main(){
	empleado e("ricardo",20,150000);
	e.mostrar_empleado();
	estudiante a("levi",19,4.0);
	a.mostrar_estudiante();
	universitario u("nati",19,5.3,"informatica");
	u.mostrar_universitario();
	return 0;
}
