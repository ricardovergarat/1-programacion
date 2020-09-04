// Usaremos esta clase para hacer uso de las clases y metodos
# include <DallasTemperature.h> 
# include <OneWire.h>
// DIO ERROR DE COMPILACION AL PONER BIBLIOTECAS AL REVES, ASI QUE RESPETAR ESTE ORDEN

#define Puerto_temperatura 6 // damos valor al puerto al cual estamos usando

OneWire dato_recuperado(Puerto_temperatura); // usamos la clase OneWire para recuperar los datos en el puerto n
DallasTemperature Sensor_temperatura(&dato_recuperado); // funciona similar a scanf de los lenguaje de nivel medio

void setup() {
  Sensor_temperatura.begin(); // iniciamos el objeto
  Serial.begin(9600); // sincronizamos el envio de datos
}

void loop() {
  Sensor_temperatura.requestTemperatures(); // solicitamos la temperatura con el metodo
  float celsius = Sensor_temperatura.getTempCByIndex(0); // recuperamos los grados en medidas de celcius
  String c;
  c = String(celsius) + "\n";
  Serial.print(c);
  
  //Serial.print(celsius);
  //Serial.print("\ncelsius\n");
  delay(1000);
}
