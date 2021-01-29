
int wallLights = A0;
int doorbell = 9;
int fan = 11;
int red = 5;
int green = 6;
int blue = 4;


void setup() {
pinMode(wallLights, OUTPUT);
pinMode(doorbell, OUTPUT); 
pinMode(fan, OUTPUT);     
pinMode(red, OUTPUT); 
pinMode(green, OUTPUT);
pinMode(blue, OUTPUT);
}

void loop() {
/*
digitalWrite(wallLights, HIGH); 
digitalWrite(doorbell, HIGH); 
digitalWrite(fan, HIGH); 
digitalWrite(red, HIGH); 
digitalWrite(green, HIGH); 
digitalWrite(blue, HIGH); 

digitalWrite(wallLights, LOW); 
digitalWrite(doorbell, LOW); 
digitalWrite(fan, LOW); 
digitalWrite(red, LOW); 
digitalWrite(green, LOW); 
digitalWrite(blue, LOW); 
*/
digitalWrite(wallLights, HIGH); 
digitalWrite(doorbell, HIGH); 
digitalWrite(fan, LOW); 
digitalWrite(red, LOW); 
digitalWrite(green, HIGH); 
digitalWrite(blue, HIGH); 
delay(1000);
digitalWrite(red, HIGH); 
digitalWrite(green, LOW); 
digitalWrite(blue, HIGH);
delay(1000);
digitalWrite(doorbell, LOW);
digitalWrite(red, HIGH); 
digitalWrite(green, HIGH); 
digitalWrite(blue, LOW);
delay(1000);
digitalWrite(red, LOW); 
digitalWrite(green, LOW); 
digitalWrite(blue, LOW);
delay(1000);
digitalWrite(fan, HIGH); 
digitalWrite(red, HIGH); 
digitalWrite(green, HIGH); 
digitalWrite(blue, HIGH); 
delay(3000);
digitalWrite(wallLights, LOW); 
delay(2000);
digitalWrite(wallLights, HIGH); 
delay(2000);

}


