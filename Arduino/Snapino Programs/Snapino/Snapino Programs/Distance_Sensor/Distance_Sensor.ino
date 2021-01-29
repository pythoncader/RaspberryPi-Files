//Distance Sensor

const int redLED = 11;
const int yellowLED = 10;
const int greenLED = 9;
const int phototransistor = A0;
int Val = 0;

void setup() {                      //Declare which variables are outputs or inputs
    pinMode(redLED,OUTPUT);
    pinMode(yellowLED,OUTPUT);
    pinMode(greenLED,OUTPUT);
    pinMode(phototransistor,INPUT);
}

void loop() {
  Val = analogRead(phototransistor); //Read the value of the A2 pin and assign that value to Val
  
  delay(50);
      
      if (Val >= 750){
      digitalWrite(redLED,HIGH);
      digitalWrite(yellowLED,LOW);  //If the value is very high, just turn on the red LED
      digitalWrite(greenLED,LOW);
        
      }if ((Val < 750) && (Val > 150)){
      digitalWrite(redLED,LOW);
      digitalWrite(yellowLED,HIGH); //If the value is not high or low, just turn on the yellow LED
      digitalWrite(greenLED,LOW);
        
      }if (Val <= 150){
      digitalWrite(redLED,LOW);
      digitalWrite(yellowLED,LOW);  //If the value is low, just turn on the green LED
      digitalWrite(greenLED,HIGH);
        
       }
      }

