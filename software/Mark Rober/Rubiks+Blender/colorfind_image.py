from PIL import Image, ImageDraw
from picamera import PiCamera
from time import sleep
#import board
from adafruit_crickit import crickit
from adafruit_seesaw.neopixel import NeoPixel


def get_average_color(xy, n, image):
    """ Returns a 3-tuple containing the RGB value of the average color of the
    given square bounded area of length = n whose origin (top left corner) 
    is (x, y) in the given image"""
    (x,y) = xy
    r, g, b = 0, 0, 0
    count = 0
    for s in range(x, x+n+1):
        for t in range(y, y+n+1):
            pixlr, pixlg, pixlb = image[s, t]
            r += pixlr
            g += pixlg
            b += pixlb
            count += 1
    return ((r/count), (g/count), (b/count))

def nearest_color( subjects, query ):
    return min( subjects, key = lambda subject: sum( (s - q) ** 2 for s, q in zip( subject, query ) ) )


colors = ( (255,255,255, "white"),
           (247, 128, 187, "red"),
           (101, 200, 102, "green"),
           (143,238 , 169, "blue"),
	   (40,178,162,"yellow"),
	   (14,196,151,"orange")
)

num_pixels = 16

pixels = NeoPixel(crickit.seesaw, 20, num_pixels, bpp=4, auto_write=True, pixel_order=(0,1,2,3))

side1 = ((190,116),
         (258,85),
	     (247,150),
	     (317,64),
	     (327,111),
	     (327,175),
	     (386,83),
	     (395, 144),
	     (450,106))

side2 = ((149,180),
         (160,255),
         (175,319),
         (207,206),
         (220,292),
         (228,359),
         (285,252),
         (290, 336),
         (290,410))

side3 = ((366,253),
         (365,345),
         (365,412),
         (440,205),
         (434,293),
         (425,360),
         (495,168),
         (485, 247),
         (476,319))


cam = PiCamera()
#cam.shutter_speed = 1000000
cam.iso = 400
cam.resolution = (800, 600)
pixels.fill((255,255,255,255))
cam.start_preview()
sleep(1)
cam.exposure_mode = 'off'
cam.capture('cube.jpg')
image = Image.open('cube.jpg')
cam.stop_preview()
pixels.fill((0,0,0,0))
image = image.resize((800,600))
image = image.convert('HSV')
#image = image.rotate(90)
pix = image.load()

#.load()
draw = ImageDraw.Draw(image)
x = 380
y = 240
n = 20

avgr = 0
avgb = 0
avgg = 0

completedCube = 1
lastColor = "white"

for i in range(0, 9):
    x1 = side1[i][0]
    y1 = side1[i][1]
    n1 = 10
    red,green,blue = get_average_color(side1[i], n1, pix)
    avgr += int(red)
    avgg += int(green)
    avgb += int(blue)

    red = int(red)
    blue = int(blue)
    green = int(green)
    #print(red,green,blue)
    dcolor = nearest_color(colors,(red,green,blue))
    currentColor = dcolor[3]
    if (i>0):
        if(currentColor != lastColor):
            completedCube = 0
    lastColor = currentColor
    print(dcolor[3])
    draw.rectangle((x1, y1, x1+n1, y1+n1), fill = ((dcolor[0], dcolor[1], dcolor[2])), outline = (255, 255, 255))

avgr = avgr/9
avgb = avgb/9
avgg = avgg/9

print ("Average of 9 squares")
print (int(avgr), int(avgg), int(avgb))

avgr = 0
avgb = 0
avgg = 0


for i in range(0, 9):
    x1 = side2[i][0]
    y1 = side2[i][1]
    n1 = 10
    red,green,blue = get_average_color(side2[i], n1, pix)
    avgr += int(red)
    avgg += int(green)
    avgb += int(blue)

    red = int(red)
    blue = int(blue)
    green = int(green)
    #print(red,green,blue)
    dcolor = nearest_color(colors,(red,green,blue))
    currentColor = dcolor[3]
    if (i>0):
        if(currentColor != lastColor):
            completedCube = 0
    lastColor = currentColor
    print(dcolor[3])
    draw.rectangle((x1, y1, x1+n1, y1+n1), fill = ((dcolor[0], dcolor[1], dcolor[2])), outline = (255, 255, 255))

avgr = avgr/9
avgb = avgb/9
avgg = avgg/9

print ("Average of 9 squares")
print (int(avgr), int(avgg), int(avgb))

avgr = 0
avgb = 0
avgg = 0


for i in range(0, 9):
    x1 = side3[i][0]
    y1 = side3[i][1]
    n1 = 10
    red,green,blue = get_average_color(side3[i], n1, pix)
    avgr += int(red)
    avgg += int(green)
    avgb += int(blue)

    red = int(red)
    blue = int(blue)
    green = int(green)
    #print(red,green,blue)
    dcolor = nearest_color(colors,(red,green,blue))
    currentColor = dcolor[3]
    if (i>0):
        if(currentColor != lastColor):
            completedCube = 0
    lastColor = currentColor
    print(dcolor[3])
    draw.rectangle((x1, y1, x1+n1, y1+n1), fill = ((dcolor[0], dcolor[1], dcolor[2])), outline = (255, 255, 255))

avgr = avgr/9
avgb = avgb/9
avgg = avgg/9

print ("Cube is ")
if not (completedCube):
    print ("NOT")
print ("Completed.")
print ("Average of 9 squares")
print (int(avgr), int(avgg), int(avgb))
#r, g, b = get_average_color((x,y), n, pix)
#r = int(r)
#g = int(g)
#b = int(b)
#draw.rectangle((x,y,x+n,y+n), fill = (r,g,b), outline=(255,255,255))
image.show()
sleep(5)
#print(r,g,b)
cam.stop_preview()
