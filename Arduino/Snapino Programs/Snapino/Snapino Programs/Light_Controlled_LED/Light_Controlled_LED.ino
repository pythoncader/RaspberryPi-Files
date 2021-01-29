//Light_Controlled_LED

const int phototransistor = A0;
int lightval;

void setup() {
  pinMode(9, OUTPUT);
}

void loop() {
  lightval = analogRead(phototransistor); //Read the value from the phototransistor
  analogWrite(9,lightval/16);             //Turn on the LED at a certain brightness
  delay(5);                               //Wait 5 milliseconds
}

