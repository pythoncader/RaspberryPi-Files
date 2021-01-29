//Program Blinking_Light
void setup() {
   pinMode(13,OUTPUT);      // Set digital pin 13 as an output.
}
void loop() {
   digitalWrite(13,HIGH);   // Set the LED on.
  delay(500);              // Delay half a second.
   digitalWrite(13,LOW);    // Set the LED off.
  delay(500);              // Delay half a second. 
}
