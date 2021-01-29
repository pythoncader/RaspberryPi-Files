//Copy_Cat_Light

const int LED = 9;
const int pt = A0;
int pVal;
double counter = 0;
double rcounter = 0;
void setup() {
 pinMode(LED,OUTPUT);
}
void loop() {
  pVal = analogRead(pt);
  if(pVal >= 300){                     //Add to the counter every 10 milliseconds if the phototransistor is covered
    ++counter;      
    delay(10);          }
    if((pVal < 300) && (counter > 0)){
      digitalWrite(LED,HIGH);          //Turn on LED for as long as the phototransistor was covered
      delay(counter * 10);
      counter = 0;
      }
  digitalWrite(LED,LOW);               //Turn the LED off
}

