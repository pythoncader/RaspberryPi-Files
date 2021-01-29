//Button_Stoplight

const int redLED = 11;
const int yellowLED = 10;
const int greenLED = 9;
const int button = A0;
int Val;
int oldVal;
int counter = 3;

void setup() {
  pinMode(redLED,OUTPUT);
  pinMode(yellowLED,OUTPUT);
  pinMode(greenLED,OUTPUT);
  pinMode(button,INPUT);
}

void loop() {
  Val = digitalRead(button);             //Read the value from the button
  if((Val == HIGH) && (oldVal == LOW)){  //If Val is HIGH and oldVal is LOW then 
    ++counter;                           //Add to the counter when the button is pressed
  }
  oldVal = Val;
  delay(10);
                                         //When the counter variable = 1, turn on the red LED
      if (counter == 1){
      digitalWrite(redLED,HIGH);
      digitalWrite(yellowLED,LOW);
      digitalWrite(greenLED,LOW);
                                         //When the counter variable = 2, turn on the yellow LED
      }if (counter == 2){
      digitalWrite(redLED,LOW);
      digitalWrite(yellowLED,HIGH);
      digitalWrite(greenLED,LOW);
                                         //When the counter variable = 3, turn on the green LED
      }if (counter == 3){
      digitalWrite(redLED,LOW);
      digitalWrite(yellowLED,LOW);
      digitalWrite(greenLED,HIGH);
                                         //Set the counter variable back to 1 if it equals 4
      }if (counter == 4){
        counter = 1;
        }
}

