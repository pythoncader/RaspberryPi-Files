//Photo_Stop

int val = 0;
const int red = 11;
const int yellow = 10;
const int green = 9;

void setup() {
pinMode(red, OUTPUT);
pinMode(yellow, OUTPUT);
pinMode(green, OUTPUT);
}

void loop() {
val = analogRead(2);         //Read light on phototransistor

digitalWrite(red, HIGH);     //Light red LED
delay(val);                  //Delay based on light value
digitalWrite(red, LOW);      //Turn off red LED
digitalWrite(yellow, HIGH);  //Turn on yellow LED
delay(val);                  //Delay based on light value
digitalWrite(yellow, LOW);   //Turn off yellow LED
digitalWrite(green, HIGH);   //Turn on green LED
delay(val);                  //Delay based on light value
digitalWrite(green, LOW);    //Turn off green LED
}

