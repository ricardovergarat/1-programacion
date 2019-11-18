# include <iostream>

using namespace std;

// la sobrecarga de contructores son para distintos casos para iniciar los atributos
// es decir mas de un metodo constructor

class fecha{
	private:
		int dia,mes,ano;
	public:
		fecha(int,int,int);
		fecha(long);
		void mostrar_fecha();
};

fecha::fecha(int _dia, int _mes, int _ano){
	dia = _dia;
	mes = _mes;
	ano = _ano;
}

fecha::fecha(long dato){
	ano = int(dato / 10000);
	mes = int((dato - ano * 10000) / 100);
	dia = int(dato - ano * 10000 - mes * 100);
}

void fecha::mostrar_fecha(){
	cout << "la fecha es: " << dia << "/" << mes << "/" << ano << endl;
}

int main(){
	fecha hoy(14,11,2019);
	fecha ayer(20191114);
	hoy.mostrar_fecha();
	ayer.mostrar_fecha();

	return 0;
}
