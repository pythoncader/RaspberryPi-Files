#include <Servo.h>
Servo head_servo;
int servo_position = 0;
int servo_pin = 3;

void setup() {
  // put your setup code here, to run once:
  head_servo.attach(servo_pin)
}

void loop() {
  // put your main code here, to run repeatedly:
  head_servo.write(180)
  delay(1000)
  head_servo.write(135)
  delay(1000)
  head_servo.write(90)
  delay(1000)
  head_servo.write(45)
  delay(1000)
  head_servo.write(0)
  delay(1000)
  
}
