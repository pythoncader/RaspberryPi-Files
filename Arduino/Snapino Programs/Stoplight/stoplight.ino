int greenandred_delay = 3000;
int yellow_delay = 1000;
int greenled = 9;
int yellowled = 10;
int redled = 11;
void setup() {
  // put your setup code here, to run once:
  pinMode(greenled, OUTPUT);
  pinMode(yellowled, OUTPUT);
  pinMode(redled, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(greenled, HIGH);
  delay(greenandred_delay);
  digitalWrite(greenled, LOW);
  digitalWrite(yellowled, HIGH);
  delay(yellow_delay);
  digitalWrite(yellowled, LOW);
  digitalWrite(redled, HIGH);
  delay(greenandred_delay);
  digitalWrite(redled, LOW);
}
