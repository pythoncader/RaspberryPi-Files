//Multitune

const int sound1 = 9;
const int sound2 = 10;
const int sound3 = 11;
const int sound4 = 12;
const int sound5 = A0;
int counter = 1;

void setup() {
  //Declare which variables are outputs or inputs
  pinMode(sound1,OUTPUT);
  pinMode(sound2,OUTPUT);
  pinMode(sound3,OUTPUT);
  pinMode(sound4,OUTPUT);
  pinMode(sound5,OUTPUT);
}

void loop() {

      counter = random(1,6);    
      //Assign the counter vairable to a random number from 1 to 5

      if (counter == 1){
      digitalWrite(sound1,LOW);
      digitalWrite(sound2,HIGH);
      digitalWrite(sound3,LOW);
      digitalWrite(sound4,LOW);
      digitalWrite(sound5,LOW);

      }if (counter == 2){
      digitalWrite(sound1,HIGH);
      digitalWrite(sound2,LOW);
      digitalWrite(sound3,LOW);
      digitalWrite(sound4,LOW);
      digitalWrite(sound5,LOW);

      }if (counter == 3){
      digitalWrite(sound1,LOW);
      digitalWrite(sound2,LOW);
      digitalWrite(sound3,HIGH);
      digitalWrite(sound4,LOW);
      digitalWrite(sound5,LOW);

      }if (counter == 4){
      digitalWrite(sound1,HIGH);
      digitalWrite(sound2,LOW);
      digitalWrite(sound3,LOW);
      digitalWrite(sound4,HIGH);
      digitalWrite(sound5,LOW);

      }if (counter == 5){
      digitalWrite(sound1,HIGH);
      digitalWrite(sound2,LOW);
      digitalWrite(sound3,LOW);
      digitalWrite(sound4,LOW);
      digitalWrite(sound5,HIGH);
      }
        delay(4000);
}
