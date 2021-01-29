from PIL import Image, ImageDraw, ImageOps, ImageEnhance
import numpy
from picamera import PiCamera
from time import sleep
from adafruit_crickit import crickit
from adafruit_seesaw.neopixel import NeoPixel

num_pixels = 16

pixels = NeoPixel(crickit.seesaw, 20, num_pixels, bpp=4, auto_write=True, pixel_order=(0,1,2,3))



polyfile = open("corner_coords.txt", "r")
polynumlist = polyfile.readlines()

polyNums = []
polyX = []
polyY = []

#polygon = ((0,0),(0,0),(0,0),(0,0),(0,0),(0,0))

for line in polynumlist:
    polyNums += line.strip().split(" ") # get a list containing 
    
for num in range(6*2):
    
    if(num % 2) == 0:
        polyX.append(int(polyNums[num]))
    else:
        polyY.append(int(polyNums[num]))

print(polyX,polyY)


polygon = [(polyX[0],polyY[0]),(polyX[1],polyY[1]),(polyX[2],polyY[2]),(polyX[3],polyY[3]),(polyX[4],polyY[4]),(polyX[5],polyY[5])]

cam = PiCamera()
#cam.shutter_speed = 1000000
cam.iso = 400
cam.resolution = (800, 600)
pixels.fill((0,0,0,255))
#sleep(1)
cam.start_preview()
sleep(2)
cam.exposure_mode = 'off'
cam.capture('cube.jpg')
cam.stop_preview()
pixels.fill((0,0,0,0))
image = Image.open('cube.jpg')

mask = Image.new("L", image.size, 0)
draw = ImageDraw.Draw(mask)
draw.polygon(polygon, fill=255, outline=None)
black =  Image.new("RGBA", image.size, 0)
result = Image.composite(image, black, mask)
resultcrop = result.crop((min(polyX), min(polyY), max(polyX), max(polyY)))
final = resultcrop.convert('RGB')



final.save("cube_cropped.jpg")


image.show()
result.show()
final.show()

#image = image.resize((800,600))
#image = image.convert('HSV')
#image = image.rotate(90)
#pixels = image.load()

#.load()
#draw = ImageDraw.Draw(image)



