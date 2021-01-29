//Click_Counter

const int button = 9;
int Val = 0;
int oldVal = HIGH;
int counter = 0;

void setup() {
  Serial.begin(9600);
  pinMode(button, INPUT);
}

void loop() {
    Val = digitalRead(button);          //Check the button
  if((Val == HIGH) && (oldVal == LOW)){ 
    ++counter;
    Serial.print("The button has been pressed ");
    Serial.print(counter);
    Serial.println(" times");
    //Add to the counter when the button is pressed and display it on the screen
  }
  oldVal = Val;
  delay(10);
}

