//Bicolor_Light

int delay1 = 10; 

void setup() {
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
}

void loop() {
  digitalWrite(9,HIGH);
  digitalWrite(10,LOW);
  delay(delay1);
  digitalWrite(9,LOW);
  digitalWrite(10,HIGH);
  delay(delay1);
}
