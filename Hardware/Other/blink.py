#blink.py
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
light = 4
button = 26
GPIO.setup(light, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.output(light, False)
oldinput = False
lightdelay = 0.05
try:
    while True:
        buttoninput = GPIO.input(button)
        if buttoninput != True:
            print("Button is pressed")
            while GPIO.input(button) == False:
                GPIO.output(light, True)
                time.sleep(lightdelay)
                GPIO.output(light, False)
                time.sleep(lightdelay)
        else:
            print("Button is not pressed")
            while GPIO.input(button) == True:
                time.sleep(lightdelay)

except KeyboardInterrupt:
    print("\nEnding program...")
    GPIO.output(light, False)
    GPIO.cleanup()
