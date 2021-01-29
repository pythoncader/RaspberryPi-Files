import cv2
import numpy as np
from matplotlib import pyplot as plt
path = 'C:/users/mike/desktop/creative cloud files/coding/python/opencv/files/'
img = cv2.imread(path+"sudoku.png", cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0) #dx is 1 if you use x direction, and dy is 0.
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1) #dy is 1 if you use y direction, and dx is 0.


lap = np.uint8(np.absolute(lap))
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY) #if either pixel is white, then it will be white in the next one.

titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombined']
images = [img, lap, sobelX, sobelY, sobelCombined]
for i in range(0, len(images)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])

plt.show()