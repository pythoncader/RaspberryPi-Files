import numpy as np
import cv2
filesdirectory = 'C:/users/mike/desktop/opencv/files/'
img = cv2.imread(filesdirectory+'alligator.png', 1)
#img = np.zeros([1728, 2304, 3], np.uint8)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)

height, width, channels = img.shape
print (height, width, channels)


img = cv2.line(img, (width, 0), (0, height), (0, 255, 255), 10, cv2.LINE_AA)
img = cv2.line(img, (0, 0), (width, height), (0, 255, 255), 10, cv2.LINE_AA)

img = cv2.circle(img, (1152, 864), 20, (255, 255, 255), -1)
img = cv2.rectangle(img, (0, 0), (width, height), (0, 0, 255), 5)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'center', (1300, 950), font, 4, (255, 255, 255), 10, cv2.LINE_AA)
img = cv2.arrowedLine(img, (1275, 915), (1170, 875), (16, 69, 139), 8, cv2.LINE_AA)
cv2.imshow('image', img)
key = cv2.waitKey(0) & 0xFF

if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite(filesdirectory+'newimage.jpg', img)
    cv2.destroyAllWindows()