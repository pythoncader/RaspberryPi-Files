import cv2
import numpy as np 
img = cv2.imread('cube_cropped.jpg')  #read image from system
#cv2.imshow('original', img)    #Displaying original image

gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)  #Convert to grayscale image
gamma = 1.2
invGamma = 1.0 / gamma
table = np.array([((i / 255.0) ** invGamma) * 255
    for i in np.arange(0, 256)]).astype("uint8")

# apply gamma correction using the lookup table
gray = cv2.LUT(gray, table)
gray = cv2.equalizeHist(gray)
blur = cv2.GaussianBlur(gray, (5,5),0)
cv2.imshow('gray',blur)

edged = cv2.Canny(blur, 50, 150,apertureSize = 3)            #Determine edges of objects in an image
cv2.imshow('edged', edged)    #Displaying original image


ret,thresh = cv2.threshold(blur,30,255,cv2.THRESH_BINARY)  
#th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
ret3,th3 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
(contours,_) = cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #Find contours in an image
cv2.imshow('threshold', th3) 
cv2.imshow('lines', img)    #Displaying original image
cv2.waitKey(0) 

def detectShape(c):          #Function to determine type of polygon on basis of number of sides
       shape = 'unknown' 
       peri=cv2.arcLength(cnt,True) 
       vertices = cv2.approxPolyDP(cnt, 0.2 * peri, True)
       sides = len(vertices) 
       if (sides == 3): 
            shape='triangle' 
       elif(sides==4): 
             x,y,w,h=cv2.boundingRect(cnt)
             aspectratio=float(w)/h 
             if (aspectratio==1):
                   shape='square'
             else:
                   shape="rectangle" 
       elif(sides==5):
            shape='pentagon' 
       elif(sides==6):
            shape='hexagon' 
       elif(sides==8): 
            shape='octagon' 
       elif(sides==10): 
            shape='star'
       else:
           shape='circle' 
       return shape 
       
for cnt in contours:
    moment=cv2.moments(cnt) 
    if(moment['m00'] > 0):
        cx = int(moment['m10'] / moment['m00']) 
        cy = int(moment['m01'] / moment['m00']) 
    area = cv2.contourArea(cnt)
    if(area > 50):
        shape=detectShape(cnt)     
        cv2.drawContours(img,[cnt],-1,(0,255,0),2)
    #cv2.putText(img,shape,(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)  #Putting name of polygon along with the shape 
    cv2.imshow('polygons_detected',img) 
cv2.waitKey(0) 
cv2.destroyAllWindows()