//Stoplight

int delay1 = 1000;          //Set delay value
int red = 11;               //Set up red as a constant 
int yellow = 10;            //Set up yellow as a constant
int green = 9;              //Set up green as a constant

void setup() {
pinMode(red, OUTPUT);       //Set digital pin red as an output
pinMode(green, OUTPUT);     //Set digital pin green as an output
pinMode(yellow, OUTPUT);    //Set digital pin yellow as an output
}

void loop() {

digitalWrite(green, HIGH);  //Turn the green light on
delay(delay1);              //Wait 1000 ms

digitalWrite(green, LOW);   //Turn the green light off
digitalWrite(yellow, HIGH); //Turn the yellow light on
delay(delay1 / 2);          //Wait 500 ms

digitalWrite(yellow, LOW);  //Turn the yellow light off
digitalWrite(red, HIGH);    //Turn the red light on
delay(delay1);              //Wait 1000 ms

digitalWrite(red, LOW);     //Turn the red light off
}
