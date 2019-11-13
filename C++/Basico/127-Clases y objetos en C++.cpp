# include <iostream>


using namespace std;

// crear una clase
class persona{
	//atributos
	private:
		// estos son sus atributos y son de tipo privado
		int edad;
		string nombre;
	// metodos
	public:
		// el metodo contructor le dan valores a los atributos
		// y suele tener el mismo nombre de la clase
		// ejemplo:
		// persona(int,string); --------> este seria el metodo contructor
		persona(int,string);
		void leer();
		void corre();
};

// aqui inicializamos la clase con valores
persona::persona(int _edad, string _nombre){
	edad = _edad;
	nombre = _nombre;
}

void persona::leer(){ // el tipo de retorno | la clase a la que pernece :: metodo
	cout << "mi nombre es: "<< nombre << endl;
}

void persona::corre(){
	cout << nombre << " empezo a correr" << endl;
}

int main(){
	persona p1 = persona(18,"daniela");
	p1.leer();
	// otra forma de inicializar una clase
	persona p2(23,"tamara");
	p2.corre();
	return 0;
}
