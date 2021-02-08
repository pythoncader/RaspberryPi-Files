//Constants
const int pResistor = A0; // Photoresistor at Arduino analog pin A0
const int ledPin = 9;       // Led pin at Arduino pin 9
int pirPin = 2;                 // PIR Out pin 
int pirPin2 = 7;
int pirPin3 = 12;

int pirStat = 0;                   // PIR status
int pirStat2 = 0;
int pirStat3 = 0;
int speaker = 11; // speaker Pin

int red_light_pin = 3;
int green_light_pin = 5;
int blue_light_pin = 6;
int delay_value = 175;
char color = 'r';
int i;

bool motion1detected = false;
bool motion2detected = false;
bool motion3detected = false;

//Variables
int value;          // Store value from photoresistor (0-1023)

void setup(){
  pinMode(ledPin, OUTPUT);  // Set lepPin - 9 pin as an output
  pinMode(pResistor, INPUT); // Set pResistor - A0 pin as an input (optional) 
  pinMode(ledPin, OUTPUT);     
  pinMode(pirPin, INPUT);
  pinMode(pirPin2, INPUT);
  Serial.begin(9600);
}

/*void siren() {                             //This function produces the 4th siren(POLICE) sound with led transition.
  for(int hz = 440; hz < 1000; hz++){
    tone(speaker, hz, 50);
    delay(4);
  }
  for(int hz = 1000; hz > 440; hz--){
    tone(speaker, hz, 50);
    delay(4);
  }
}*/
void siren1() {                             //This function produces the 4th siren(POLICE) sound with led transition.
  for(int hz = 440; hz < 1000; hz++){
    tone(speaker, hz, 50);
    delay(4);
  }
  for(int hz = 1000; hz > 440; hz--){
    tone(speaker, hz, 50);
    delay(4);
  }
}
void siren2() {                             //This function produces the 4th siren(POLICE) sound with led transition.
  for(int hz = 850; hz < 1200; hz++){
    tone(speaker, hz, 50);
    delay(2);
  }
  for(int hz = 1200; hz < 1500; hz++){
    tone(speaker, hz, 50);
    delay(2);
  }
  for(int hz = 1500; hz > 1200; hz--){
    tone(speaker, hz, 50);
    delay(5);
  }
  for(int hz = 1200; hz > 850; hz--){
    tone(speaker, hz, 50);
    delay(5);
  }
}
void siren3() {                             //This function produces the 4th siren(POLICE) sound with led transition.
  for(int hz = 550; hz < 1000; hz++){
    tone(speaker, hz, 50);
    delayMicroseconds(1900);
  }
  for(int hz = 1000; hz < 1250; hz++){
    tone(speaker, hz, 50);
    delayMicroseconds(1900);
  }
  for(int hz = 1250; hz > 1000; hz--){
    tone(speaker, hz, 50);
    delay(4);
  }
  for(int hz = 1000; hz > 550; hz--){
    tone(speaker, hz, 50);
    delay(4);
  }
}

void checkvalues() {
  value = analogRead(pResistor);
  pirStat = digitalRead(pirPin);
  pirStat2 = digitalRead(pirPin2);
  pirStat3 = digitalRead(pirPin3);
}

void RGB_color(int red_light_value, int green_light_value, int blue_light_value){
  analogWrite(red_light_pin, red_light_value);
  analogWrite(green_light_pin, green_light_value);
  analogWrite(blue_light_pin, blue_light_value);
}

void policelights(){
  if (color == 'w'){
    RGB_color(0, 0, 255); // Blue
    delay(delay_value);
    color = 'b';
  }else if(color == 'b'){
    RGB_color(255, 0, 0); // Red
    delay(delay_value);
    color = 'r';
  }else if (color == 'r'){
    RGB_color(255, 255, 255); // White
    delay(delay_value);
    color = 'w';
  }
}
void policelightsoff(){
  RGB_color(0, 0, 0);
}

void loop(){
  checkvalues(); //Update the sensor values

  //You can change value "25"
  while (value > 200){ //While the light is on
    checkvalues(); //Update the sensor values
    digitalWrite(ledPin, LOW);  //Turn led off
    Serial.println(pirStat);
    if (pirStat == 1) { // if motion is detected by the first sensor
      motion1detected = true; //Set the motion1detected variable to true
      
      //When loop is broken by first motion detected
      while(motion1detected){

        while(value > 200){ //While the light is on
          Serial.println(pirStat);
          checkvalues(); //Update the sensor values
          Serial.println("First motion detected"); //Let the user know that the first motion sensor has been tripped

          if(pirStat2 == 1){ //If the second motion sensor detects motion, then go into another loop
            Serial.println("Second motion detected"); //Let the user know that the second motion sensor has been tripped
            motion2detected = true; //set the motion2detected variable to true

            while(value > 200 && motion2detected){ //While the light is on and motion2detected is true
              policelights(); //turn on the police lights
              checkvalues(); //Update the sensor values again
              Serial.println("Police Lights on"); //Let the user know where the program is

              if (pirStat3 == 1){ //If the third motion sensor detects motion
                Serial.println("Third Motion Detected"); //let the user know that the third motion sensor detected motion
                motion3detected = true;
                policelightsoff(); //turn off the police lights

                while (value > 200){ //While the light is on
                  Serial.println("Siren on"); //Let the user know where the program is
                  siren3(); //blare the siren
                  checkvalues(); //Keep updating the sensor values
                }
              }
            }
          }
        } //End of "light on" loop

        while (value < 200){ //while the light is off
          policelightsoff(); //turn the police lights off
          checkvalues(); //Update the sensor values
          Serial.println("Light off (line 126)"); //let the user know that the light is off
          motion1detected = false; //Reset the loops
          motion2detected = false; //Reset the loops
          motion3detected = false; //Reset the loops
          digitalWrite(ledPin, HIGH); //Turn on the led
        }
      }   
    } else if (pirStat == 0){ //If the first motion detector has not detected motion
      Serial.println("First Motion Not Detected..."); //Let the user know
      checkvalues(); //Update the sensor values
      motion1detected = false; //Reset the loops
      motion2detected = false; //Reset the loops
      motion3detected = false; //Reset the loops
    }
  } while (value < 200){ //While the light is off
    policelightsoff(); //turn off the police lights
    checkvalues(); //update the sensor values
    Serial.println("Light Off (line 142)"); //Let the user know where the program is
    motion1detected = false; //Reset the loops
    motion2detected = false; //Reset the loops
    motion3detected = false; //Reset the loops
    digitalWrite(ledPin, HIGH); //Turn led on
  }

  delay(100); //Small delay so the program doesn't use all of the resources
}
