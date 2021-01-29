import numpy as np
import cv2
filesdirectory = 'C:/users/mike/desktop/opencv/files/'
img = cv2.imread(filesdirectory+'messi5.jpg')
img2 = cv2.imread(filesdirectory+'opencv-logo.png')

print(img.shape)
print(img.size)
print(img.dtype)
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# dst = cv2.add(img, img2) #the images need to be the same size
# the images need to be the same size
dst = cv2.addWeighted(img, .9, img2, .1, 0)
cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
for i in range(0, 6):
    print('Hello world!')
    x = 'My name is Cade'
    print('Hello, '+x)
    print('Hello world!')
    x = 'My name is Cade'
    print('Hello, '+x)
    print('Hello world!')
    x = 'My name is Cade'
    print('Hello, '+x)
    print('Hello world!')
    x = 'My name is Cade'
    print('Hello, '+x)
