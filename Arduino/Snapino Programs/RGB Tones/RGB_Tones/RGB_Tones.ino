//RGB Tones

const int strobe = 6;
const int blue = 11;
const int green = 10;
const int red = 9;
int counter = 1;

void setup() {
  pinMode(blue,OUTPUT);
  pinMode(green,OUTPUT);
  pinMode(red,OUTPUT);
  pinMode(strobe,OUTPUT);
}

void loop() {
  
  if(counter == 1){
    analogWrite(strobe,900);
    digitalWrite(blue,HIGH);
    digitalWrite(green,LOW);
    digitalWrite(red,LOW);
    }
  if(counter == 2){
    analogWrite(strobe,300);
    digitalWrite(blue,LOW);
    digitalWrite(green,HIGH);
    digitalWrite(red,LOW);
    }
  if(counter == 3){
    analogWrite(strobe,30);
    digitalWrite(blue,LOW);
    digitalWrite(green,LOW);
    digitalWrite(red,HIGH);
    }
  if(counter >= 3){
    counter = 0;
    }

  ++counter;
  delay(1500);

}

