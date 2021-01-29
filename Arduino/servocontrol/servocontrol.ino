 /*
 * Original sourse: https://github.com/adafruit/Adafruit-PWM-Servo-Driver-Library
 * 
 * This is the Arduino code PAC6985 16 channel servo controller
 * watch the video for details (V1) and demo http://youtu.be/y8X9X10Tn1k
 *  This code is #1 for V2 Video Watch the video :https://youtu.be/bal2STaoQ1M
 *  I have got 3 codes as follow:
   #1-Arduino Code to run one by one all servos from 0 to 180°   
   #2-Arduino Code to control specific servos with specific angle
   #3-Arduino Code to run 2 or all servos at together
   
 * Written/updated by Ahmad Shamshiri for Robojax Video channel www.Robojax.com
 * Date: Dec 16, 2017, in Ajax, Ontario, Canada
 * Permission granted to share this code given that this
 * note is kept with the code.
 * Disclaimer: this code is "AS IS" and for educational purpose only.
 * this code has been downloaded from http://robojax.com/learn/arduino/
 
 * Get this code and other Arduino codes from Robojax.com
Learn Arduino step by step in structured course with all material, wiring diagram and library
all in once place. Purchase My course on Udemy.com http://robojax.com/L/?id=62

****************************
Get early access to my videos via Patreon and have  your name mentioned at end of very 
videos I publish on YouTube here: http://robojax.com/L/?id=63 (watch until end of this video to list of my Patrons)
****************************

or make donation using PayPal http://robojax.com/L/?id=64

 *  * This code is "AS IS" without warranty or liability. Free to be used as long as you keep this note intact.* 
 * This code has been download from Robojax.com
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

/*************************************************** 
  This is an example for our Adafruit 16-channel PWM & Servo driver
  Servo test - this will drive 16 servos, one after the other

  Pick one up today in the adafruit shop!
  ------> http://www.adafruit.com/products/815

  These displays use I2C to communicate, 2 pins are required to  
  interface. For Arduino UNOs, thats SCL -> Analog 5, SDA -> Analog 4

  Adafruit invests time and resources providing this open source code, 
  please support Adafruit and open-source hardware by purchasing 
  products from Adafruit!

  Written by Limor Fried/Ladyada for Adafruit Industries.  
  BSD license, all text above must be included in any redistribution
 ****************************************************/

#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

// called this way, it uses the default address 0x40
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
// you can also call it with a different address you want
//Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x41);

// Depending on your servo make, the pulse width min and max may vary, you 
// want these to be as small/large as possible without hitting the hard stop
// for max range. You'll have to tweak them as necessary to match the servos you
// have!
// Watch video V1 to understand the two lines below: http://youtu.be/y8X9X10Tn1k
#define SERVOMIN  125 // this is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  575 // this is the 'maximum' pulse length count (out of 4096)

// our servo # counter
uint8_t servonum = 0;
int myrandom = 0;
int pass = 0;
int top3 = 0;
int top1 = 1;
int bottom3 = 2;
int top4 = 3;
int bottom4 = 4;
int bottom2 = 5;
int bottom1 = 6;
int top2 = 7;

int min0 = 30;
int max0 = 100;
int min1 = 30;
int max1 = 80;
int min2 = 85;
int max2 = 180;

int min3 = 95;
int max3 = 180;
int min4 = 40;
int max4 = 100;

int min5 = 85;
int max5 = 180;
int min6 = 25;
int max6 = 110;
int min7 = 5;
int max7 = 80;
int currentAngles[] = {0, 0, 0, 0, 0, 0, 0, 0};

void setup() {
  Serial.begin(9600);
  Serial.println("16 channel Servo test!");

  pwm.begin();
  
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates

  //yield();
}

int angleToPulse(int ang){
   int pulse = map(ang,0, 180, SERVOMIN,SERVOMAX);// map angle of 0 to 180 to Servo min and Servo max 
   return pulse;
}
void set_angle(int channel, int myangle, float servowait=1){
  currentAngles[channel] = myangle;
  pwm.setPWM(channel, 0, angleToPulse(myangle));
  Serial.print("servowait: ");
  Serial.println(servowait*1000);
  delay(servowait*1000);
}
int pickrandom(int channel){
  switch (channel) {
  case 0:
    myrandom = random(min0, max0);
    return myrandom;
  case 1:
    myrandom = random(min1, max1);
    return myrandom;
  case 2:
    myrandom = random(min2, max2);
    return myrandom;
  case 3:
    myrandom = random(min3, max3);
    return myrandom;
  case 4:
    myrandom = random(min4, max4);
    return myrandom;
  case 5:
    myrandom = random(min5, max5);
    return myrandom;
  case 6:
    myrandom = random(min6, max6);
    return myrandom;
  case 7:
    myrandom = random(min7, max7);
    return myrandom;
}
}
int settorandom(int channel, float servowait=0){
  set_angle(channel, pickrandom(channel), servowait);
}

// the code inside loop() has been updated by Robojax
void loop() {
  
  /*set_angle(0, min0);
  set_angle(1, min1);
  set_angle(2, min2);
  set_angle(3, min3);
  set_angle(4, min4);
  set_angle(5, min5);
  set_angle(6, min6);
  set_angle(7, min7);
  delay(1000);
  set_angle(0, max0);
  set_angle(1, max1);
  set_angle(2, max2);
  set_angle(3, max3);
  set_angle(4, max4);
  set_angle(5, max5);
  set_angle(6, max6);
  set_angle(7, max7);
  delay(1000);*/
  /*for(int i=0; i<8; i++){
    settorandom(i);
    delay(random(0, 300));
  }*/
  set_angle(0, 0);
  set_angle(0, 60);
  /*
  set_angle(1, 180, 0);
  set_angle(2, 180, 0);
  set_angle(3, 180, 0);
  set_angle(4, 180, 0);
  set_angle(5, 180, 0);
  delay(1000);
  set_angle(0, 90, 0);
  set_angle(1, 90, 0);
  set_angle(2, 90, 0);
  set_angle(3, 90, 0);
  set_angle(4, 90, 0);
  set_angle(5, 90, 0);
  delay(1000);
  set_angle(0, 0, 0);
  set_angle(1, 0, 0);
  set_angle(2, 0, 0);
  set_angle(3, 0, 0);
  set_angle(4, 0, 0);
  set_angle(5, 0, 0);
  delay(1000);*/
  
}

/*
/* angleToPulse(int ang)
 * @brief gets angle in degree and returns the pulse width
 * @param "ang" is integer represending angle from 0 to 180
 * @return returns integer pulse width
 * Usage to use 65 degree: angleToPulse(65);
 * Written by Ahmad Shamshiri on Sep 17, 2019. 
 * in Ajax, Ontario, Canada
 * www.Robojax.com 
 */
