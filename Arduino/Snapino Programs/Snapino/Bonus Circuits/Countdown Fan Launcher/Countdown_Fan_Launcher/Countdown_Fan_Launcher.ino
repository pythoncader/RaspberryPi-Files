//Countdown Fan Launcher 

const int LED = 10;
const int motor = 9;
const int bswitch = A0;
int button;
int oldbutton;
int buttonval;
int motorstate;
int speakerrate;
int startup;

void setup() {
  pinMode(LED,OUTPUT);
  pinMode(motor,OUTPUT);
  pinMode(bswitch,INPUT);
}

void loop() {
  
  button = digitalRead(bswitch);
  if((button == HIGH) && (oldbutton == LOW)){
    speakerrate = 300;
    startup = 1;
    }
    oldbutton = button;
  
  if((speakerrate > 25) && (motorstate == 0)){
    tone(11,500,speakerrate);
    digitalWrite(LED,HIGH);
    delay(speakerrate);
    digitalWrite(LED,LOW);
    noTone(11);
    delay(speakerrate);
    speakerrate = speakerrate/1.1;
    }
  if((speakerrate <= 25) && (startup == 1)) { 
    motorstate = 1;
    noTone(11);
    }
  if(motorstate == 1){
    digitalWrite(motor,HIGH);
    delay(3000);
    digitalWrite(motor,LOW);
    delay(1000);
    motorstate = 0;
    startup = 0;
    }
    delay(5);
}

