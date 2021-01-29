#Help from https://learn.adafruit.com/adafruit-crickit-hat-for-raspberry-pi-linux-computers
import time
from adafruit_crickit import crickit

# For signal control, we'll chat directly with seesaw, use 'ss' to shorted typing!
ss = crickit.seesaw

# Two buttons are pullups, connect to ground to activate
BUTTON_1 = crickit.SIGNAL1  # button #1 connected to signal port 1 & ground
BUTTON_2 = crickit.SIGNAL2  # button #2 connected to signal port 2 & ground
BUTTON_3 = crickit.SIGNAL3

ss.pin_mode(BUTTON_1, ss.INPUT_PULLUP)
ss.pin_mode(BUTTON_2, ss.INPUT_PULLUP)
ss.pin_mode(BUTTON_3, ss.INPUT_PULLUP)

button1last = 0
button2last = 0
button3last = 0

while True:
    button1state =  ss.digital_read(BUTTON_1)
    button2state =  ss.digital_read(BUTTON_2)
    button3state =  ss.digital_read(BUTTON_3)
    if (button1state != button1last):
        print("Button 1:", button1state)
        button1last = button1state
    if (button2state != button2last):
        print("Button 2:", button2state)
        button2last = button2state
    if (button3state != button3last):
        print("Button 3:", button3state)
        button3last = button3state
