#Program always runs to check to see if the blender power switch is flipped to "ON"
#Help from https://stackoverflow.com/questions/34149547/when-press-button-python-script-runs-automatically-on-raspberry-pi

import time
from adafruit_crickit import crickit
import subprocess

# For signal control, we'll chat directly with seesaw, use 'ss' to shorted typing!
ss = crickit.seesaw

# Two buttons are pullups, connect to ground to activate

ONOFF = crickit.SIGNAL2  # FALSE IS ON, TRUE IS OFF



ss.pin_mode(ONOFF, ss.INPUT_PULLUP)




running = False

print("Program Running")

while True:

    ONOFFstate =  ss.digital_read(ONOFF)
    if (ONOFFstate == False):
        print("Switched ON!")
        program = subprocess.call(["python3 check_cube.py"], shell=True)        
