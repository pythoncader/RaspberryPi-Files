//www.elegoo.com

//    Left motor truth table
//  ENA         IN1               IN2         Description  
//  LOW   Not Applicable    Not Applicable    Motor is off
//  HIGH        LOW               LOW         Motor is stopped (brakes)
//  HIGH        HIGH              LOW         Motor is on and turning forwards
//  HIGH        LOW               HIGH        Motor is on and turning backwards
//  HIGH        HIGH              HIGH        Motor is stopped (brakes)

//    Right motor truth table
//  ENB         IN3             IN4         Description  
//  LOW   Not Applicable   Not Applicable   Motor is off
//  HIGH        LOW             LOW         Motor is stopped (brakes)
//  HIGH        LOW             HIGH        Motor is on and turning forwards
//  HIGH        HIGH            LOW         Motor is on and turning backwards
//  HIGH        HIGH            HIGH        Motor is stopped (brakes)  

//    The direction of the car's movement
//  Left motor    Right motor     Description  
//  stop(off)     stop(off)       Car is stopped
//  forward       forward         Car is running forwards
//  forward       backward        Car is turning right
//  backward      forward         Car is turning left
//  backward      backward        Car is running backwards

//define the L298n IO pin
//www.elegoo.com

#include <IRremote.h>

////////// IR REMOTE CODES //////////
#define F 16736925  // FORWARD
#define B 16754775  // BACK
#define L 16720605  // LEFT
#define R 16761405  // RIGHT
#define S 16712445  // STOP
#define UNKNOWN_F 5316027     // FORWARD
#define UNKNOWN_B 2747854299  // BACK
#define UNKNOWN_L 1386468383  // LEFT
#define UNKNOWN_R 553536955   // RIGHT
#define UNKNOWN_S 3622325019  // STOP
#define KEY1 16738455
#define KEY2 16750695
#define KEY3 16756815
#define KEY4 16724175
#define KEY5 16718055
#define KEY6 16743045
#define KEY7 16716015
#define KEY8 16726215
#define KEY9 16734885
#define KEY0 16730805
#define KEY_STAR 16728765
#define KEY_HASH 16732845

#define RECV_PIN  12

#define ENA 5
#define ENB 6
#define IN1 7
#define IN2 8
#define IN3 9
#define IN4 11
#define LED 13

#include <Servo.h>

Servo head;
int Echo = A4;  
int Trig = A5;

IRrecv irrecv(RECV_PIN);
decode_results results;
unsigned long val;
unsigned long preMillis;

void setup() {
  pinMode(LED, OUTPUT); 
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(Echo, INPUT);
  pinMode(Trig, OUTPUT);
  digitalWrite(ENA, HIGH);  
  digitalWrite(ENB, HIGH);
  Serial.begin(9600);
  int minAngle = 700;//the pulse width, in microseconds, corresponding to the minimum (0-degree) angle on the servo (defaults to 700)
  int maxAngle = 2400;//the pulse width, in microseconds, corresponding to the maximum (180-degree) angle on the servo (defaults to 2400)
  head.attach(3,minAngle,maxAngle);//setting the servo IO pin and the steering range.
  irrecv.enableIRIn();
}
void LED_on(){
  digitalWrite(LED, HIGH);  
}
void LED_off(){
  digitalWrite(LED, LOW);
}
void go_forward(int delay_value=0) { //the combination of in1 = 1 and in2 = 0 or in3 = 1 and in4 = 0 makes the motors go forward
  digitalWrite(IN1, HIGH);      
  digitalWrite(IN2, LOW); 
  digitalWrite(IN3, LOW);      
  digitalWrite(IN4, HIGH);  //go forward
  delay(delay_value);
}
void left_forward(int delay_value=0){
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  delay(delay_value);
}
void right_forward(int delay_value=0){
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  delay(delay_value);
}
void go_backward(int delay_value=0){ // the combination of in1 = 0 and in2 = 1 or in3 = 0 and in4 = 1 makes the motors go backward
  digitalWrite(IN1, LOW);      
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);      
  digitalWrite(IN4, LOW);   //go back 
  delay(delay_value);
}
void left_backward(int delay_value=0){
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  delay(delay_value);
}
void right_backward(int delay_value=0){
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  delay(delay_value);
}
void stop_driving(int delay_value=0){
  digitalWrite(IN1, LOW);      
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);      
  digitalWrite(IN4, LOW);   //stop
  delay(delay_value);
}
float find_distance() {
  digitalWrite(Trig, LOW);   
  delayMicroseconds(2);
  digitalWrite(Trig, HIGH);  
  delayMicroseconds(20);
  digitalWrite(Trig, LOW);   
  float Fdistance = pulseIn(Echo, HIGH);  
  Fdistance= Fdistance / 58;       
  return Fdistance;
}

void print_distance() {
  while (true){
    float found_distance = find_distance();
    Serial.println(found_distance);
    delay(200);
  }
}
void count() {
 for (int x=0; x<=255; x=x+1) {
    Serial.println(x);
    delay(0);
  }
}
void getBluetooth_messages(){
  while(true){
    if(Serial.available())
    {
      char getstr = Serial.read();
      switch(getstr){
        case 'f': go_forward(); break;
        case 'b': go_backward();   break;
        case 'l': left_backward(); right_forward(); break;
        case 'r': right_backward(); left_forward(); break;
        case 's': stop_driving();   break;
        case 'n': LED_on(); break;
        case 'o': LED_off(); break;
        default:  break;
      }
    }
  }
}
void getIR_control(){
  while (true){
   if (irrecv.decode(&results)){ 
    preMillis = millis();
    val = results.value;
    Serial.println(val);
    irrecv.resume();
    switch(val){
      case F: 
      case UNKNOWN_F: go_forward(); break;
      case B: 
      case UNKNOWN_B: go_backward(); break;
      case L: 
      case UNKNOWN_L: left_backward(); right_forward(); break;
      case R: 
      case UNKNOWN_R: right_backward(); left_forward(); break;
      case S: 
      case UNKNOWN_S: stop_driving(); break;
      default: break;
    }
   } else{
        if(millis() - preMillis > 500){
          stop_driving();
          preMillis = millis();
        }
     }
  }
}
void loop() {
  go_forward(5000);
  stop_driving(5000);
  
  left_forward(1000);
  stop_driving(1000);
  
  right_forward(1000);
  stop_driving(1000);
  
  left_backward(2000);
  stop_driving(1000);
  
  right_backward(2000);
  stop_driving(1000);
  
  go_backward(3000);
  stop_driving(1000);
  head.write(180);
  delay(1000);
  head.write(135);
  delay(1000);
  head.write(90);
  delay(1000);
  head.write(45);
  delay(1000);
  head.write(0);
  delay(1000);
  head.write(90);
  count();
  //print_distance();
  getIR_control();
  //getBluetooth_messages();
  
}
