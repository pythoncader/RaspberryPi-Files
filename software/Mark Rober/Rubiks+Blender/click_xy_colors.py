# Help from https://www.geeksforgeeks.org/displaying-the-coordinates-of-the-points-clicked-on-the-image-using-python-opencv/
# This program lets you click on the locations of the cube where to take color readings
# Each click will create a box for the color averaging. 9 clicks for each color (do each color individually)
# Once 27 boxes are on the cube press the escape key. It will save to a file "color_coords.txt"

import cv2 
   
# function to display the coordinates of 
# of the points clicked on the image  
def click_event(event, x, y, flags, params): 
  
    # checking for left mouse clicks 
    if event == cv2.EVENT_LBUTTONDOWN: 
  
        # displaying the coordinates 
        # on the Shell 
        print(x, y) 
        n = 5
        cv2.rectangle(img, (x-n, y-n), (x+n,y+n), (255,255,255),1)
        cv2.imshow('image', img)
        buf = str(x) + " " + str(y) + ("\n")
        file.write(buf)

    # checking for right mouse clicks      
    if event==cv2.EVENT_RBUTTONDOWN: 
  
        # displaying the coordinates 
        # on the Shell 
        print(x, ', ', y) 
        n = 5
        cv2.rectangle(img, (x-n, y-n), (x+n,y+n), (255,255,255),1)
        cv2.imshow('image', img) 
  
# driver function 





if __name__=="__main__":
    
    file = open("color_coords.txt", 'w')

    # reading the image 
    img = cv2.imread('cube_cropped.jpg', 1) 

    # displaying the image 
    cv2.imshow('image', img)
  
    # setting mouse hadler for the image 
    # and calling the click_event() function 
    cv2.setMouseCallback('image', click_event) 
    print ("Click the 9 color boxes for each side then press Escape Key")
    
  
    # wait for a key to be pressed to exit 

    cv2.waitKey(0) 
  
    # close the window 
    file.close()
    cv2.destroyAllWindows() 