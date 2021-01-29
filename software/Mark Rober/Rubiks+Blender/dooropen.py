#Help from https://learn.adafruit.com/adafruit-crickit-hat-for-raspberry-pi-linux-computers

import time
from adafruit_crickit import crickit

ss = crickit.seesaw

servoOpen = 50
servoClose = 150
print("Close Door!")

DOOR = crickit.SIGNAL1

ss.pin_mode(DOOR, ss.INPUT_PULLUP)

crickit.servo_1.angle = servoOpen

while not ss.digital_read(DOOR):
    print("Waiting for door")
    time.sleep(1)

print("Wait for Servo")
if ss.digital_read(DOOR):
    crickit.servo_1.angle = servoClose
    time.sleep(1)
    crickit.servo_1._pwm_out.duty_cycle = 0

time.sleep(5)

crickit.servo_1.angle = servoOpen
