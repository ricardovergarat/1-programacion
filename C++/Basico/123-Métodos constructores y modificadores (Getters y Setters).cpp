# include <iostream>

using namespace std;

class punto{
	private:
		int x,y;
	public:
		punto();
		void setpunto(int , int); // dar punto ----------> setters
		int getpuntox(); // -----------> getters
		int getpuntoy();
};

// setters permite asignar valores a los atributos desde el main
// getters perimte aceder a los valores de los atributos desde el main

punto::punto(){

}

void punto::setpunto(int _x, int _y){
	x = _x;
	y = _y;
}

int punto::getpuntox(){
	return x;
}

int punto::getpuntoy(){
	return y;
}

int main(){
	punto p1;
	p1.setpunto(10,20);
	cout << p1.getpuntox() << endl;
	cout << p1.getpuntoy() << endl;
	return 0;
}