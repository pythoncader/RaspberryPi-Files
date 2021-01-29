import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
pwm = GPIO.PWM(17, 50) #set the pwm to the 17th gpio pin and to 50 Hz
pwm.start(0)
def set_angle(angle, runtime, hold=False):

    if angle >= 0 and angle <= 180:
        dutycycle = (angle / 180)* 10 + 2.5
#divide the angle by 180 to get the percent, then translate that into a range of 0 to 10, then add 2.5 because the servo's duty cycle ranges from 2.5 to 12.5
        GPIO.output(17, True)
        pwm.ChangeDutyCycle(dutycycle)
        time.sleep(runtime)
        if hold == False:
            GPIO.output(17, False)
            pwm.ChangeDutyCycle(0)
try:
    while True:
        servoangle = float(input("Angle of Rotation: "))
        holdstr = str(input("Hold? "))
        if "y" in holdstr or "t" in holdstr or "T" in holdstr or "Y" in holdstr:
            holdbool = True
        else:
            holdbool = False
        set_angle(servoangle, 1, holdbool)
except KeyboardInterrupt:
    print("\nProgram Stopped...\n")
    set_angle(servoangle, 0.1)
    GPIO.cleanup()
