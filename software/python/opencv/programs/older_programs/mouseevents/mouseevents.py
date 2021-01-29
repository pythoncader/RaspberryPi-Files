import numpy as np
import cv2

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
#events = [i  for i in dir(cv2) if 'EVENT' in i]
#print(events)
font = cv2.FONT_HERSHEY_SIMPLEX
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(str(x)+',' ,y)
        strxy = str(x) +', ' + str(y)
        cv2.putText(img, strxy, (x, y), font, .5, (255, 255, 0), 1)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        strrgb = str(red) + ', ' + str(green) + ', ' + str(blue)
        print('color: ' + strrgb)
        cv2.putText(img, strrgb, (x, y), font, .5, (0, 0, 255), 1)
        cv2.imshow('image', img)
img = np.zeros((512, 512, 3), np.uint8)
#img = cv2.imread('messi5.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()



