#add a button on gpio 21 and ground, then add "sudo python3 /home/pi/Desktop/coding/CadePiProjects/raspberrypistuff/CadeShutdown.py &" (edit this directory as necessary) to end of /etc/rc.local (before exit 0)This runs this
#program on startup, and makes a shutdown button. Hold the button for 5 seconds to shutdown the raspberry pi.
#https://www.quartoknows.com/page/raspberry-pi-shutdown-button
import time
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = 21

GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)
current_state = "NULL"
while True:
    button_state = GPIO.input(button)
    if button_state == GPIO.LOW and current_state != "LOW":
        print ("LOW")
        counter = 0
        while GPIO.input(button) == GPIO.LOW: #while the button is pressed
            if counter != 50:
              current_state = "LOW"
              time.sleep(0.1)
              counter += 1
            else:
                print("shutting down...")
                os.system("sudo shutdown now -h")
              
    if button_state == GPIO.HIGH and current_state != "HIGH":
      print ("HIGH")
      current_state = "HIGH"
      time.sleep(0.5)