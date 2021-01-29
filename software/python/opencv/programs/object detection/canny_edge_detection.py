import cv2
import numpy as np
from matplotlib import pyplot as plt
path = 'C:/users/mike/desktop/creative cloud files/coding/python/opencv/files/'
img = cv2.imread(path+"messi5.jpg", cv2.IMREAD_GRAYSCALE)
imgblurred = cv2.GaussianBlur(img, (5, 5), 1)
cannyafterblur = cv2.Canny(imgblurred, threshold1=100, threshold2=200)
canny = cv2.Canny(img, threshold1=100, threshold2=200)
titles = ['image', 'blurred image', 'canny', 'cannyafterblur']
images = [img, imgblurred, canny, cannyafterblur]
for i in range(0, len(images)):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])

plt.show()