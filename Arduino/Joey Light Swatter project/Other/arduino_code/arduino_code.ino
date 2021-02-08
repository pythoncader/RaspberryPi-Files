/*

PIR HCSR501 

modified on 5 Feb 2019
by Saeed Hosseini @ ElectroPeak
https://electropeak.com/learn/guides/

*/
 
int ledPin = 13;                // LED 
int pirPin = 2;                 // PIR Out pin 
int pirStat = 0;                   // PIR status
int isLEDon = 0;
 
void setup() {
  pinMode(ledPin, OUTPUT);     
  pinMode(pirPin, INPUT);     
 
  Serial.begin(9600);
}
 
void loop(){
  
  pirStat = digitalRead(pirPin); 
  if (pirStat == 1 && isLEDon == 0) {            // if motion detected
    //digitalWrite(ledPin, HIGH);  // turn LED ON
    Serial.println("Motion Detected...");
    isLEDon = 1;
    int mylooptime = 0;
    while(mylooptime <= 5000){
      delay(1);
      pirStat = digitalRead(pirPin);
      mylooptime++;
    }
    Serial.println("Sensor Ready!");
  }
  else if(pirStat == LOW && isLEDon == 1){
    //digitalWrite(ledPin, LOW); // turn LED OFF if we have no motion
    Serial.println("Motion Not Detected...");
    isLEDon = 0;
  }
}
