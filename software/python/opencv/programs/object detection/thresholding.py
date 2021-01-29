import cv2
from matplotlib import pyplot as plt
path = "c:/users/mike/desktop/creative cloud files/coding/python/opencv/files/"
img = cv2.imread(path+"gradient.png", -1)

threshold = 127
ret, th1 = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY) #if the value of the pixel is between the threshold and 255, then set it to white, otherwise it is black.  
ret, th2 = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY_INV) #if the value of the pixel is between the threshold and 255, then it is set to black, otherwise it is set to white
ret, th3 = cv2.threshold(img, threshold, 255, cv2.THRESH_TRUNC) #if the value of the pixel is lower than the threshold, then the pixel does not change, but after the threshold value, then the value is set to the threshold. 
ret, th4 = cv2.threshold(img, threshold, 255, cv2.THRESH_TOZERO) #if the value of the pixel is lower than the threshold, then the pixel is 0 or black.
ret, th5 = cv2.threshold(img, threshold, 255, cv2.THRESH_TOZERO_INV) #if the value of the pixel is higher than the threshold, then the pixel is 0 or black

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, th1, th2, th3, th4, th5]


'''
for i in range(0, 6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])'''
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", img)
cv2.imshow("th1", th1)
cv2.imshow("th2", th2)
cv2.imshow("th3", th3)
cv2.imshow("th4", th4)
cv2.imshow("th5", th5)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
