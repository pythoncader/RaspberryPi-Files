//Light_Monitor

const int phototransistor = A5;
int Val = 0;
const int LED = 11;

void setup() {                     
 Serial.begin(9600);                       //Open terminal window
 pinMode(phototransistor, INPUT);
 pinMode(11, OUTPUT);  
}

void loop() {
 Val = analogRead(A5);                     //Measure light value

 Serial.print("Measured light value = ");  //Print text
 Serial.println(Val);                      //Print light value
 delay(1000);
}
void turn() {
  if (Val>=400){
   digitalWrite(11,HIGH); 
    }if ((Val <=399)){
   digitalWrite(11,LOW);
      }
  }
