//Alternating_Lights

int delay1 = 50;         //Set delay value. 
int greenlightnum = 0;
int redlightnum = 0;
int greenlighton = 9;
int redlight1on = 10;
int redlight2on = 11;
int yellowlighton = 12;
void setup()
{
  pinMode(greenlighton, OUTPUT);     //Set digital pin 9 as an output. 
  pinMode(redlight1on, OUTPUT);    //Set digital pin 10 as an output. 
  pinMode(yellowlighton, OUTPUT);
  pinMode(redlight2on, OUTPUT);
  Serial.begin(9600);
}
void yellowlight(){
  digitalWrite(yellowlighton, HIGH);
  delay(1000);
  digitalWrite(yellowlighton, LOW);
}
void redlight2(){
  digitalWrite(redlight2on, HIGH);
  delay(1000);
  digitalWrite(redlight2on, LOW);
}
void loop() 
{
  if(greenlightnum == 100){
    Serial.println("Green light has flashed 100 times since the last time the yellow light was on! Yellow light should be on!");
    greenlightnum = 0;
    yellowlight();
  } 
  if(redlightnum == 25){
    Serial.println("Red light 1 has flashed 25 times since red light 2 was on! Red light 2 should be on!");
    redlightnum = 0;
    redlight2();
  }
  digitalWrite(9, HIGH); //Turn green LED on. 
  delay(delay1);          //Wait for the delay value.
  digitalWrite(9,LOW);   //Turn green LED off. 
  greenlightnum++;
  digitalWrite(10, HIGH); //Turn red LED on. 
  delay(delay1);          // Wait for the delay value. 
  digitalWrite(10,LOW);   //Turn red LED off.
  Serial.print("greenlightnum = ");
  Serial.println(greenlightnum);
  Serial.print("redlightnum = ");
  Serial.println(redlightnum);
  redlightnum++;
  }
