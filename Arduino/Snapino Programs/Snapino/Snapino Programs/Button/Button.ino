//Button 

const int ledPin =  10;
const int button = 11;   
int buttonState = 0;      

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(button, INPUT);     
}

void loop(){
   buttonState = digitalRead(button);  //Read the value from the button and assign it to a variable
   
  if (buttonState == 0) {     
    digitalWrite(ledPin, 1);         //If the value is high (button is pressed) turn on the LED
  } 
  else {
    digitalWrite(ledPin, 0);          //If anything else happens turn the LED off
  }
}
