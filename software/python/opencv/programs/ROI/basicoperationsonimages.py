import numpy as np
import cv2

filesdirectory = 'C:/users/mike/desktop/Creative Cloud Files/coding/CadePiProjects/software/python/opencv/files/'
filesdirectorylinux = '/home/pi/Desktop/CadePiProjects/software/python/opencv/files/'
try:
	img = cv2.imread(filesdirectorylinux+'messi5.jpg')
	height, width, channels = img.shape
except:
	img = cv2.imread(filesdirectory+'messi5.jpg')
	height, width, channels = img.shape
print('height:', height)
print('width:', width)
print('channels:', channels)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.namedWindow('ball:',cv2.WINDOW_NORMAL)
print(img.shape) #returns a tuple of the height, width, and then channels
#print(img.size) #returns the total number of pixels in the image- height * width * channels
#print(img.dtype) #returns the data type of the image

b, g, r = cv2.split(img)

img = cv2.merge((b, g, r))


y1 = 63 #the y of the top left corner of the ROI
y2 = 130 #the y of the bottom right of the ROI
x1 = 203 #the x of the top left of the ROI
x2 = 264 #the x of the bottom right of the ROI
myROI = img[y1:y2, x1:x2] #get the rectangle of the ROI
img[80:147, 393:454] = myROI #set the pixel values of another, equal rectangle to the values of the ROI

y1 = 129 #the y of the top left corner of the ROI
y2 = 157 #the y of the bottom right of the ROI
x1 = 208 #the x of the top left of the ROI
x2 = 269 #the x of the bottom right of the ROI
myROI2 = img[y1:y2, x1:x2] #get the rectangle of the ROI
img[11:39, 21:82] = myROI2 #set the pixel values of another, equal rectangle to the values of the ROI


y1 = 298 #the y of the top left corner of the ROI
y2 = 333 #the y of the bottom right of the ROI
x1 = 436 #the x of the top left of the ROI
x2 = 538 #the x of the bottom right of the ROI
myROI3 = img[y1:y2, x1:x2] #get the rectangle of the ROI
img[197:232, 162:264] = myROI3 #set the pixel values of another, equal rectangle to the values of the ROI


ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

cv2.imwrite(filesdirectory+"ball.png", ball)

cv2.imshow('ball:', ball)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#image[y, x] = pixel values at point (x, y)
