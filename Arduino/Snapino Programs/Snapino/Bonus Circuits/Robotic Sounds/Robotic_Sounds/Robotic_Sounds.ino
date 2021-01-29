//Robotic Sounds

int sound;
void setup() {
}

void loop() {  
  sound  = random(31,1500); //Pick a random number between 31 and 1500.
  tone(10,sound);           //Output a tone at the frequency of the random number selected.
  delay(100);
}


