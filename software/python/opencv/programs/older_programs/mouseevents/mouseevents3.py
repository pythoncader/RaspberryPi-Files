import numpy as np
import cv2

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
#events = [i  for i in dir(cv2) if 'EVENT' in i]
#print(events)
font = cv2.FONT_HERSHEY_SIMPLEX
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        mycolorImage = np.zeros((512, 512, 3), np.uint8)

        mycolorImage[:] = [blue, green, red]
        strrgb = str(red) + ', ' + str(green) + ', ' + str(blue)
        print('color: ' + strrgb)
        cv2.putText(mycolorImage, strrgb, (85, 256), font, 2, (0, 0, 255), 3)
        cv2.imshow('color', mycolorImage)

img = np.zeros((512, 512, 3), np.uint8)
#img = cv2.imread('alligator.png')
height, width, channels = img.shape
print('height:', height)
print('width:', width)
cv2.imshow('image', img)

points = []
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
