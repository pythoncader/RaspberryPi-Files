import numpy as np
import cv2

def nothing(argument):
    print('Switch Position:', argument)

#img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow("image")

switch = "Color/Gray"
cv2.createTrackbar(switch, "image", 0, 1, nothing)
img = cv2.imread("alligator.png")
height, width, channels = img.shape
img = cv2.resize(img, (int(width/2.5), int(height/2.5)))
cv2.imwrite("smalligator.png", img)
img = cv2.imshow("image", img)
while True:
    img = cv2.imread("smalligator.png")
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

    s = cv2.getTrackbarPos(switch, "image")

    if s == 0:
        pass
        #img[:] = [b, g, r]
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.imshow("image", img)
cv2.destroyAllWindows()