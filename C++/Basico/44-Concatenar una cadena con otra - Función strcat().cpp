# include <iostream>
# include <string.h>

using namespace std;

int main(){
	char x[] = "NA";
	char y[] = "NI";
	strcat(x,y);
	// strcat(variable a la que se va a juntar, que lo que juntara al la variable anterior)
	cout << x;
	return 0;
}
