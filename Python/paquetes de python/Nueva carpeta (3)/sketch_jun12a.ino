int estado = 0;
int estadoAnterior = 0;
int salida = 0;

void setup() {
  pinMode(8, INPUT);
  pinMode(4, OUTPUT);
}
void loop(){
  estado = digitalRead(8);
  if ((estado == HIGH) && (estadoAnterior == LOW)) {
    salida = 1 - salida;
  }
  estadoAnterior = estado;
  if(salida == 1){
    digitalWrite(4, HIGH);
  }
  else {
    digitalWrite(4,LOW);
  }
  
}   
