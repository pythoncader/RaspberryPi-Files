//Light_Monitor

const int phototransistor = A0;
int Val = 0;

void setup() {                     
 Serial.begin(9600);                       //Open terminal window
 pinMode(phototransistor, INPUT);  
}

void loop() {
 Val = analogRead(A0);                     //Measure light value

 Serial.print("Measured light value = ");  //Print text
 Serial.println(Val);                      //Print light value
 delay(250);
}

