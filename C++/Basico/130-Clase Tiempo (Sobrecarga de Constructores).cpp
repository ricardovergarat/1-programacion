# include <iostream>

using namespace std;

class tiempo{
	private:
		int hora,minuto,segundo;
	public:
		tiempo(int,int,int);
		tiempo(int);
		void mostrar_hora();
};

tiempo::tiempo(int _hora, int _minuto, int _segundo){
	hora = _hora;
	minuto = _minuto;
	segundo = _segundo;
}

tiempo::tiempo(int numero){
	int m,s;
	hora = numero / 3600;
	minuto = numero / 60;
	segundo = numero % 60;
	cout << hora << ":" << minuto << ":" << segundo << endl;
}

void tiempo::mostrar_hora(){
	cout << hora << ":" << minuto << ":" << segundo << endl;
}

int main(){
	tiempo x(14,40,32);
	x.mostrar_hora();
	tiempo y(1370);


	return 0;
}
