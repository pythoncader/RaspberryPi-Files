import cv2
import numpy as np
path = "C:/users/mike/desktop/coding/python/opencv/files/"
img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread(path+"image_1.png")

bitAnd = cv2.bitwise_and(img2, img1) #if both are white, then it will be white
bitOr = cv2.bitwise_or(img2, img1) #if either is white, then it will be white
bitXor = cv2.bitwise_xor(img2, img1) #if both are white, it will be black, if one is white and the other is black, it will be white, otherwise black
bitNot = cv2.bitwise_not(img1) #bitNot is the opposite of the source
bitNot2 = cv2.bitwise_not(img2) #bitNot is the opposite of the source

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("bitAnd", bitAnd)
cv2.imshow("bitOr", bitOr)
cv2.imshow("bitxOr", bitXor)
cv2.imshow("bitNot", bitNot)
cv2.imshow("bitNot2", bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()