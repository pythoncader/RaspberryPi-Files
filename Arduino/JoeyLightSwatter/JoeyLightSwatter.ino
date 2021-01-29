/* Use a photoresistor (or photocell) to turn on an LED in the dark
   More info and circuit schematic: http://www.ardumotive.com/how-to-use-a-photoresistor-en.html
   Dev: Michalis Vasilakis // Date: 8/6/2015 // www.ardumotive.com */
   

//Constants
const int pResistor = A0; // Photoresistor at Arduino analog pin A0
const int ledPin=9;       // Led pin at Arduino pin 9
int pirPin = 2;                 // PIR Out pin 
int pirStat = 0;                   // PIR status
int isLEDon = 0;

//Variables
int value;          // Store value from photoresistor (0-1023)

void setup(){
 pinMode(ledPin, OUTPUT);  // Set lepPin - 9 pin as an output
 pinMode(pResistor, INPUT); // Set pResistor - A0 pin as an input (optional) 
 pinMode(ledPin, OUTPUT);     
 pinMode(pirPin, INPUT);     
 Serial.begin(9600);
}

void loop(){
  //You can change value "25"
  while (value > 200){ //While the light is on
    value = analogRead(pResistor);
    Serial.println(value);
    digitalWrite(ledPin, LOW);  //Turn led off
    pirStat = digitalRead(pirPin);
    if (pirStat == 1) { // if motion detected
      //digitalWrite(ledPin, HIGH);  // turn LED ON
      Serial.println("Motion Detected...");
      //isLEDon = 1;
      /*int mylooptime = 0;
      while(mylooptime <= 5000){
        delay(1);
        pirStat = digitalRead(pirPin);
        mylooptime++;
      }
      Serial.println("Sensor Ready!");*/
    }
    else if(pirStat == LOW){
      //digitalWrite(ledPin, LOW); // turn LED OFF if we have no motion
      Serial.println("Motion Not Detected...");
      //isLEDon = 0;
    }
  }
  while (value < 200){
    value = analogRead(pResistor);
    Serial.println(value);
    digitalWrite(ledPin, HIGH); //Turn led on
  }

  delay(500); //Small delay
}
