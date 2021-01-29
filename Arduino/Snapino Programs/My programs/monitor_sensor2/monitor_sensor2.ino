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
 turn();
 delay(0);
}
void turn() {
  if (Val >= 800){
   digitalWrite(11,LOW); 
   Serial.println("It's bright!");
    }if ((Val <= 799)){
   digitalWrite(11,HIGH);
      }
  }
