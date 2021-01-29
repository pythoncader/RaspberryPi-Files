import cv2
import numpy as np
path = "C:/users/mike/desktop/creative cloud files/coding/python/opencv/files/"
def nothing(x):
    pass
"""
#Hue range is [0,255], Saturation range is [0,255] and Value range is [0,255]
cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)
"""

def selectROI_CADE(yourimg):
        myroi = cv2.selectROI(yourimg)
    
        y1 = int(myroi[1])
        y2 = int(myroi[1]+myroi[3])
        x1 = int(myroi[0])
        x2 = int(myroi[0]+myroi[2])

        roi_area = res[y1:y2, x1:x2]
        cv2.imshow("cropped", roi_area)
        key = cv2.waitKey(0)
        print(f"y1= {y1}\ny2= {y2}\nx1= {x1}\nx2= {x2}\n")
        return [y1, y2, x1, x2]
myfiles = ["skystonesmall.jpg", "skystonepic.jpg", "skystonestack.jpg", "skystonestack2.jpg", "skystonestack3.jpg"]

for i in range(0, len(myfiles)):
    frame = cv2.imread(path+myfiles[i])

    dimensions = frame.shape #get the dimensions of the image

    myblackframe = np.zeros((dimensions[0], dimensions[1]), np.uint8) #create a black image that is the same shape as the original image

    blur = cv2.blur(frame, (8, 8)) #blur the image to refine the selection process
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV) #convert the image to hsv for easy thresholding.

    """
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")
    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")
    """

    upperYellow = [35, 255, 255] #give upper HSV values
    lowerYellow = [20, 150, 155] #give lower HSV values
    
    lower_bounds = np.array(lowerYellow) #make a numpy array of the lower HSV values
    upper_bounds = np.array(upperYellow) #make a numpy array of the upper HSV values
    mask = cv2.inRange(hsv, lower_bounds, upper_bounds) #calculate a mask with the range of color values

    res = cv2.bitwise_and(frame, frame, mask=mask) #compares the original image to itself, then applies a mask, which we have calculated above
    #above code actually provides no purpose other than to show the masked area in the original image. We do not need this to perform our calculations.



    print("lower bounds:", lower_bounds)
    print("upper bounds:", upper_bounds)

    cv2.imshow("Original Image", frame)
    cv2.imshow("Result:", res)
    cv2.waitKey(0)


    #roi_dimensions = selectROI_CADE(mask) #select an ROI

    #set ROI values based on which image it is
    w = i+1
    if (w == 1):
        y1 = 107
        y2 = 276
        x1 = 301
        x2 = 558
        
    elif (w == 2):
        y1 = 73
        y2 = 388
        x1 = 240
        x2 = 640
        
    elif (w == 3):
        y1 = 55
        y2 = 472
        x1 = 106
        x2 = 628
        
    elif (w == 4):
        y1 = 7
        y2 = 720
        x1 = 312
        x2 = 799
        
    elif (w == 5):
        y1 = 11
        y2 = 720
        x1 = 166
        x2 = 1251
        


    #or set an ROI manually
    '''
    y1= 64 #define the values of a rectangle where the stack will always be.
    y2= 398
    x1= 328
    x2= 581
    '''

    #get an roi of the mask matrix
    roi = mask[y1:y2, x1:x2]
    
    myblackframe[y1:y2, x1:x2] = roi #add the roi of the mask to the blank black image to get the right rectangle coordinates to draw on the original image.
    x,y,w,h = cv2.boundingRect(myblackframe) #get a bounding rectangle of the un-masked area
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) #draw the above rectangle in green on the original image


    cv2.imshow("cropped", roi)
    cv2.imshow("Final image:", frame)
    cv2.waitKey(0)

    print(f"Height is {h} pixels")
    print(f"Percent of image height: {int((h/dimensions[0])*100)}%")


    cv2.destroyAllWindows()
    

cv2.destroyAllWindows()
