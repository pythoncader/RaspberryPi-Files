//Capacitor Monitor

const int output = 10;
int cval;
int val;
int timer;

void setup() {
  pinMode(output,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  cval = analogRead(0);
  Serial.println(cval);
  if(cval < 10){
    val = 1;
    }
  if(cval > 1000){
    val = 0;
    }
  if(val == 1){
    digitalWrite(output,HIGH);
    }
  if(val == 0){
    digitalWrite(output,LOW);
    }
  delay(100);
}

