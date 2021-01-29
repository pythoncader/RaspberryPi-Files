import numpy as np
import cv2

def Blue(argument):
    print('Blue trackbar Position: ', argument)
def Green(argument):
    print('Green trackbar Position: ', argument)
def Red(argument):
    print('Red trackbar Position: ', argument)


img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow("image")

cv2.createTrackbar("Blue", "image", 0, 255, Blue)
cv2.createTrackbar("Green", "image", 0, 255, Green)
cv2.createTrackbar("Red", "image", 0, 255, Red)

while True:
    cv2.imshow("image", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    BluePos = cv2.getTrackbarPos("Blue", "image")
    GreenPos = cv2.getTrackbarPos("Green", "image")
    RedPos = cv2.getTrackbarPos("Red", "image")

    img[:] = [BluePos, GreenPos, RedPos]

cv2.destroyAllWindows()