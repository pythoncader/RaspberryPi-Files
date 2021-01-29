# Help from https://learn.adafruit.com/adafruit-crickit-hat-for-raspberry-pi-linux-computers


import time
from adafruit_crickit import crickit
#import neopixel
from adafruit_seesaw.neopixel import NeoPixel

num_pixels = 16  # Number of pixels driven from Crickit NeoPixel terminal
#ORDER = neopixel.GRBW

# The following line sets up a NeoPixel strip on Seesaw pin 20 for Feather
pixels = NeoPixel(crickit.seesaw, 20,  num_pixels,bpp=4, pixel_order=(0,1,2,3))

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0,0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0,0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3,0)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3,0)
 
def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)
 
def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

BRIGHTWHITE=(255,255,255,255)
WHITE = (0,0,0,255)
RED = (255, 0, 0,0)
YELLOW = (255, 150, 0,0)
GREEN = (0, 255, 0,0)
CYAN = (0, 255, 255,0)
BLUE = (0, 0, 255,0)
PURPLE = (180, 0, 255,0)
 
while True:
    print("fill")
    pixels.fill(WHITE)
    pixels.show()
    time.sleep(1)
    # Increase or decrease to change the speed of the solid color change.
    time.sleep(1)
    pixels.fill(BRIGHTWHITE)
    pixels.show()
    time.sleep(1)
    pixels.fill(BLUE)
    pixels.show()
    time.sleep(1)
 
    print("chase")
    color_chase(RED, 0.1)  # Increase the number to slow down the color chase
    color_chase(YELLOW, 0.1)
    color_chase(GREEN, 0.1)
    color_chase(CYAN, 0.1)
    color_chase(BLUE, 0.1)
    color_chase(PURPLE, 0.1)
 
    print("rainbow")
    rainbow_cycle(0)  # Increase the number to slow down the rainbow
