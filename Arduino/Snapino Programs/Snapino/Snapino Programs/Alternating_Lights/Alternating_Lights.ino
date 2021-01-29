//Alternating_Lights

int delay1 = 100;         //Set delay value. 

void setup()
{
  pinMode(9, OUTPUT);     //Set digital pin 9 as an output. 
  pinMode(10, OUTPUT);    //Set digital pin 10 as an output. 
}

void loop()
{
  digitalWrite(9, HIGH); //Turn green LED on. 
  digitalWrite(10,LOW);   //Turn red LED off.
  delay(delay1);          //Wait for the delay value.
  digitalWrite(9,LOW);   //Turn green LED off. 
  digitalWrite(10, HIGH); //Turn red LED on. 
  delay(delay1);          // Wait for the delay value. 
  }
