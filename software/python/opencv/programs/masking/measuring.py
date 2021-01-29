import cv2
path = "C:/users/mike/desktop/creative cloud files/coding/python/opencv/files/"
# Load image, grayscale, Gaussian blur, Otsu's threshold
image = cv2.imread(path+"1.jpg") #get the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert to grayscale.
blur = cv2.GaussianBlur(gray, (5,5), 0) #blur the image
ret, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY_INV) #THRESH_OTSU uses the optimal threshold value.

# Find bounding box
x,y,w,h = cv2.boundingRect(thresh)
cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
cv2.putText(image, "w={},h={}".format(w,h), (x,y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (36,255,12), 2)

cv2.imshow("thresh", thresh)
cv2.imshow("gray", gray)
cv2.imshow("blur", blur)
cv2.imshow("image", image)
cv2.waitKey()