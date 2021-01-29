from PIL import Image, ImageDraw, ImageEnhance
from picamera import PiCamera
from time import sleep
from time import time
from adafruit_crickit import crickit
from adafruit_seesaw.neopixel import NeoPixel
from num2words import num2words
from subprocess import call
from subprocess import Popen
from math import sqrt
import colorsys
ss = crickit.seesaw

DOOR = crickit.SIGNAL1
ONOFF = crickit.SIGNAL2
TIMER = crickit.SIGNAL3

ss.pin_mode(DOOR, ss.INPUT_PULLUP)
ss.pin_mode(ONOFF, ss.INPUT_PULLUP)
ss.pin_mode(TIMER, ss.INPUT_PULLUP)

num_pixels = 16
pixels = NeoPixel(crickit.seesaw, 20, num_pixels, bpp=4, auto_write=True, pixel_order=(0,1,2,3))

cam = PiCamera()

colors = ( (485,200,230, "white"),
               (976, 993, 195, "red"),
               (399, 999, 106, "green"),
               (582, 999 , 232, "blue"),
               (166, 991, 245,"yellow"),
	           (74,1000,210,"orange"))
                



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

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        sleep(wait)


def get_average_color_hsv(x,y,n,image):
    """ Returns a 3-tuple containing the RGB value of the average color of the
    given square bounded area of length = n whose origin (top left corner) 
    is (x, y) in the given image"""
    #(x,y) = xy
    ch,cs,cv = 0, 0, 0
    count = 0
    for s in range(x-n, x+n+1):
        for t in range(y-n, y+n+1):
            pixr, pixg, pixb = image.getpixel((s,t))
            h, s, v = colorsys.rgb_to_hsv(pixr, pixg, pixb)
            h = int(h * 1000)
            s = int(s * 1000)
            #print(h, s, v)
            #pixlr, pixlg, pixlb = image[s, t]
            ch += h
            cs += s
            cv += v
            count += 1
    return ((ch/count), (cs/count), (cv/count))
    
    
def get_average_color_hsv_squares(x,y,n,image):
    """ Returns a 3-tuple containing the RGB value of the average color of the
    given square bounded area of length = n whose origin (top left corner) 
    is (x, y) in the given image"""
    #(x,y) = xy
    ch,cs,cv = 0, 0, 0
    count = 0
    for px in range(x-n, x+n+1):
        for py in range(y-n, y+n+1):

            pixr, pixg, pixb = image.getpixel((px,py))
            h, s, v = colorsys.rgb_to_hsv(pixr, pixg, pixb)
            h = int(h * 1000)
            s = int(s * 1000)
            
            #pixlr, pixlg, pixlb = image[s, t]
            ch += h * h
            cs += s * s
            cv += v * v
            count += 1

    return (sqrt(ch/count), sqrt(cs/count), sqrt(cv/count))

def get_average_color(x, y, n, image):
    """ Returns a 3-tuple containing the RGB value of the average color of the
    given square bounded area of length = n whose origin (top left corner) 
    is (x, y) in the given image"""
    #(x,y) = xy
    r, g, b = 0, 0, 0
    count = 0
    for s in range(x, x+n+1):
        for t in range(y, y+n+1):
            pixlr, pixlg, pixlb = image.getpixel((x,y))
            #pixlr, pixlg, pixlb = image[s, t]
            r += pixlr
            g += pixlg
            b += pixlb
            count += 1
    return ((r/count), (g/count), (b/count))


def closest_color(rgb):
    r, g, b = rgb
    color_diffs = []
    for color in colors:
        cr, cg, cb,name = color
        color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
        
        color_diffs.append((color_diff, color))
        #print (int(color_diff), color)
    return min(color_diffs)[1]

def nearest_color( subjects, query ):
    return min( subjects, key = lambda subject: sum( (s - q) ** 2 for s, q in zip( subject, query ) ) )

def close_door():
    servoOpen = 50
    servoClose = 150
    print("Close Door!")
    speak_words("Close Door To Continue")   
    crickit.servo_1.angle = servoOpen
    while not ss.digital_read(DOOR):
        print("Waiting for door")
        sleep(1)

    print("Wait for Servo")
    if ss.digital_read(DOOR):
        crickit.servo_1.angle = servoClose
        sleep(1)
        crickit.servo_1._pwm_out.duty_cycle = 0
    
    return ss.digital_read(DOOR)
    
def open_door():
    servoOpen = 50
    servoClose = 150
    crickit.servo_1.angle = servoOpen
    sleep(5)
    speak_words("Close the door")
    crickit.servo_1.angle = 60
    while not ss.digital_read(DOOR):
        print("Waiting for door")
        sleep(1)
        
    print("Wait for Servo")
    if ss.digital_read(DOOR):
        crickit.servo_1.angle = servoClose
        sleep(1)
        crickit.servo_1._pwm_out.duty_cycle = 0
    #door_status = ss.digital_read(DOOR)
    return ss.digital_read(DOOR)
    
def speak_words(words):
    cmd_beg= 'espeak -ven+m4 '
    cmd_end= ' 2>/dev/null' # To dump the std errors to /dev/null
    words = words.replace(' ', '_')
    call([cmd_beg+words+cmd_end], shell=True)
    
def play_mp3(mp3file):
    playing_audio = Popen(["mpg123", mp3file])
    return playing_audio

def cube_check():
    
    cam.iso = 400
    cam.resolution = (800, 600)
    pixels.fill((0,0,0,255))
    cam.start_preview()
    sleep(2)
    cam.exposure_mode = 'off'
    cam.capture('cube.jpg')
    image = Image.open('cube.jpg')
    cam.stop_preview()
    pixels.fill((0,0,0,0))
    
    polyfile = open("corner_coords.txt", "r")
    polynumlist = polyfile.readlines()

    polyNums = []
    polyX = []
    polyY = []

    for line in polynumlist:
        polyNums += line.strip().split(" ") # get a list containing 
        
    for num in range(6*2):
        
        if(num % 2) == 0:
            polyX.append(int(polyNums[num]))
        else:
            polyY.append(int(polyNums[num]))

    print(polyX,polyY)

    polygon = [(polyX[0],polyY[0]),(polyX[1],polyY[1]),(polyX[2],polyY[2]),(polyX[3],polyY[3]),(polyX[4],polyY[4]),(polyX[5],polyY[5])]

    
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.polygon(polygon, fill=255, outline=None)
    black =  Image.new("RGBA", image.size, 0)
    result = Image.composite(image, black, mask)
    resultcrop = result.crop((min(polyX), min(polyY), max(polyX), max(polyY)))
    image = resultcrop.convert('RGB')
    
    #image = ImageEnhance.Contrast(image).enhance(1.5)    
    image = ImageEnhance.Color(image).enhance(2)
    image.save("cube_cropped.jpg") 
    #image.show()
    #image = image.convert('HSV')
    pix = image
    #pix = image.load()
    draw = ImageDraw.Draw(image)
    x = 380
    y = 240
    n = 20

    avgr = 0
    avgb = 0
    avgg = 0

    #Get Coordinates from File 

    file = open("color_coords.txt", "r")
    numlist = file.readlines()

    allNums = []
    x = []
    y = []

    for line in numlist:
        allNums += line.strip().split(" ") # get a list containing 
        #print(line)
    for num in range(27*2):
        
        if(num % 2) == 0:
            x.append(allNums[num])
        else:
            y.append(allNums[num])
            
    file.close()

    #Check Cube with Coordinates
    completedCube = 1
    lastColor = "white"
    n1 = 10
    for i in range(0, 9):
        x1 = x[i]
        y1 = y[i]
        x1 = int(x1)
        y1 = int(y1)

        
        red,green,blue = get_average_color_hsv_squares(x1, y1, n1, pix)
        avgr += int(red)
        avgg += int(green)
        avgb += int(blue)

        red = int(red)
        blue = int(blue)
        green = int(green)
        #print(red,green,blue)
        dcolor = nearest_color(colors,(red,green,blue))
        close_color = closest_color((red,green,blue))
        currentColor = close_color[3]
        if (i>0):
            if(currentColor != lastColor):
                completedCube = 0
        lastColor = currentColor
        print(dcolor[3], red,green,blue, close_color)
        draw.rectangle((x1-n1, y1-n1, x1+n1, y1+n1), fill = ((dcolor[0], dcolor[1], dcolor[2])), outline = (255, 255, 255))

    avgr = avgr/9
    avgb = avgb/9
    avgg = avgg/9

    print ("Average of 9 squares")
    print (int(avgr), int(avgg), int(avgb))

    avgr = 0
    avgb = 0
    avgg = 0


    for i in range(9, 18):
        x1 = x[i]
        y1 = y[i]
        x1 = int(x1)
        y1 = int(y1)
        

        red,green,blue = get_average_color_hsv_squares(x1, y1, n1, pix)
        avgr += int(red)
        avgg += int(green)
        avgb += int(blue)

        red = int(red)
        blue = int(blue)
        green = int(green)
        #print(red,green,blue)
        dcolor = nearest_color(colors,(red,green,blue))
        close_color = closest_color((red,green,blue))
        currentColor = close_color[3]
        if (i>9):
            if(currentColor != lastColor):
                completedCube = 0
        lastColor = currentColor
        print(dcolor[3], red,green,blue, close_color)
        draw.rectangle((x1-n1, y1-n1, x1+n1, y1+n1), fill = ((dcolor[0], dcolor[1], dcolor[2])), outline = (255, 255, 255))

    avgr = avgr/9
    avgb = avgb/9
    avgg = avgg/9

    print ("Average of 9 squares")
    print (int(avgr), int(avgg), int(avgb))

    avgr = 0
    avgb = 0
    avgg = 0


    for i in range(18, 27):
        x1 = x[i]
        y1 = y[i]
        x1 = int(x1)
        y1 = int(y1)

        red,green,blue = get_average_color_hsv_squares(x1, y1, n1, pix)
        avgr += int(red)
        avgg += int(green)
        avgb += int(blue)

        red = int(red)
        blue = int(blue)
        green = int(green)
        #print(red,green,blue)
        dcolor = nearest_color(colors,(red,green,blue))
        close_color = closest_color((red,green,blue))
        currentColor = close_color[3]
        if (i>18):
            if(currentColor != lastColor):
                completedCube = 0
        lastColor = currentColor
        print(dcolor[3], red,green,blue, close_color)
        draw.rectangle((x1-n1, y1-n1, x1+n1, y1+n1), fill = ((dcolor[0], dcolor[1], dcolor[2])), outline = (255, 255, 255))

    avgr = avgr/9
    avgb = avgb/9
    avgg = avgg/9

    print ("Average of 9 squares")
    print (int(avgr), int(avgg), int(avgb))

    image.show()
    #print(r,g,b)
    
    return completedCube


if not (ss.digital_read(DOOR)):
    close_door()

completed = cube_check()

if (completed):
    speak_words("Scramble cube and restart")
else:
    speak_words("Cube is Scrambled")
    
    speak_words("Ready to start timer")
    while (ss.digital_read(TIMER)):
        sleep(1) 
    speak_words("three")   
    speak_words("two")   
    speak_words("one")
    
    jeopardy = play_mp3("audio/jeopardy.mp3")
    startTime = time()
    while not (ss.digital_read(TIMER)):
        sleep(1)
    solveTime = time() - startTime
    print (int(solveTime))
    jeopardy.kill()
    
    print ("Cube is ")
    if not (cube_check()):
        print ("NOT Completed")
        loser = play_mp3("audio/price_is_right_loser.mp3")
    else:
        zelda = play_mp3("audio/zelda_secret.mp3")
        sleep(2)
        #rainbow_cycle(1)
        open_door()
        
        print ("Completed.")
        speak_words("Your time was")
        speak_words(num2words(int(solveTime)))
        speak_words("Seconds")
while not (ss.digital_read(ONOFF)):
    sleep(1)

#r, g, b = get_average_color((x,y), n, pix)
#r = int(r)
#g = int(g)
#b = int(b)
#draw.rectangle((x,y,x+n,y+n), fill = (r,g,b), outline=(255,255,255))

