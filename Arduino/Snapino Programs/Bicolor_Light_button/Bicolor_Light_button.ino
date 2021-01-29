//Bicolor_Light
int red = 9;
int yellow = 10;
int button = 11;
int button_val = 0;
int pressed = 0;

void setup() {
  pinMode(red,OUTPUT);
  pinMode(yellow,OUTPUT);
  pinMode(button, INPUT);
  Serial.begin(9600);
}

void loop() {
  button_val = digitalRead(button);
  Serial.println(button_val);
  if (button_val == pressed){
    digitalWrite(yellow, 0);
    digitalWrite(red, 1);
  }
  else {
    digitalWrite(yellow, 1);
    digitalWrite(red, 0);
  }
}
