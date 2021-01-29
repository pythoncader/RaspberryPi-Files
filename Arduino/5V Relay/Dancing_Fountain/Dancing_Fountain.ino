void setup() {    // initialize digital pin 1,2,3 as an output.
pinMode(1, OUTPUT);
pinMode(2, OUTPUT);
pinMode(3, OUTPUT);
}

void loop() {             //continuously loop the program
digitalWrite(1, HIGH);   //Turn pins 1,2&3 on & off in sequnce for two rounds
delay(3000);
digitalWrite(1, LOW);
delay(3000);
}   
