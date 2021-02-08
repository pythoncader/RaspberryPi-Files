/*This is my Arduino project on making diffent Siren Sound with their LED scnc/transitions. You can get the this code from my Github 
 * repository named "Siren", You can watch its working on my Youtube Channel and the complete tutorial is explained in my Aruino Create account
 * named coding_killer. Now it's your turn to make some cool tone using my Project and explore all the possibilities.
 */
boolean lastbutton=LOW;
boolean currentbutton=LOW;
int input=0;
int speaker=11; // speakerer Pin
int j=3;
int k=12;
void setup() {
  pinMode(2,INPUT);
}
boolean debounce(boolean last){                 //Function to solve the problem of button debouncing
  boolean current=digitalRead(2);
  if(last!=current)
  {
    delay(5);
    current=digitalRead(2);
    }
  return current;
  }
void loop() {
  //one();
  //two();
  //three();
  four();
}


void one() {         //This function produces the 1st siren sound with ON/OFF led transition.
  // Whoop up
  for(int hz = 440; hz < 1000; hz+=25){
    tone(speaker, hz, 50);
    delay(5);
  }
  // Whoop down
  for(int hz = 1000; hz > 440; hz-=25){
    tone(speaker, hz, 50);
    delay(5);
  }
  }
  
void oneA() {                //This function produces differnt transition on 1st siren.
  
  // Whoop up
  for(int hz = 440; hz < 1000; hz+=25){
    tone(speaker, hz, 50);
    delay(5);
  }
  // Whoop down
  for(int hz = 1000; hz > 440; hz-=25){
    tone(speaker, hz, 50);
    delay(5);
  }
  }
void two() {                   //This function produces the 2nd siren sound with progressive led transition.
  // Whoop up
  for(int hz = 440; hz < 1000; hz+=25){
    tone(speaker, hz, 50);
    delay(2);
  }
  // Whoop down
  for(int hz = 1000; hz > 440; hz-=25){
    tone(speaker, hz, 50);
    delay(2);
  }
  }
void twoA() {                  //This function produces differnt transition on 2nd siren.
  // Whoop up
  for(int hz = 440; hz < 1000; hz+=25){
    tone(speaker, hz, 50);
    delay(5);
  }
  for(int hz = 1000; hz > 440; hz-=25){
    tone(speaker, hz, 50);
    delay(5);
  }
  }
  void three() {              //This function produces the 3rd siren(AMBULANCE) sound with led transition.
  tone(speaker,440,200);
    delay(300);
  for(int i=3;i<=6;i++)
  digitalWrite(i,HIGH);
  noTone(speaker);
  tone(speaker,494,500);
  delay(300);
  for(int i=3;i<=6;i++){
  digitalWrite(i,LOW);
  digitalWrite(i+6,HIGH);
  }
  noTone(speaker);
  tone(speaker,523,300);
   delay(200);
  digitalWrite(7,HIGH);
  delay(50);
  digitalWrite(8,HIGH);
  delay(50);
  noTone(speaker);
}
  void threeA() {              //This function produces differnt transition on 3rd siren.
  tone(speaker,440,200);
  noTone(speaker);
  tone(speaker,494,500);
  delay(300);
  tone(speaker,523,300);
  delay(300);
  noTone(speaker);
}
void four() {                             //This function produces the 4th siren(POLICE) sound with led transition.
  for(int hz = 440; hz < 1000; hz++){
    tone(speaker, hz, 50);
    delay(4);
  }
  for(int hz = 1000; hz > 440; hz--){
    tone(speaker, hz, 50);
    delay(4);
    }
  }
