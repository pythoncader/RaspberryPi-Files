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
        cv2.circle(img, (x, y), n, (255,255,255),1)
        cv2.imshow('image', img)
        buf = str(x) + " " + str(y) + ("\n")
        file.write(buf)

    # checking for right mouse clicks      
    if event==cv2.EVENT_RBUTTONDOWN: 
  
        # displaying the coordinates 
        # on the Shell 
        print(x, ', ', y) 
        n = 5
        cv2.circle(img, (x, y), n, (255,255,255),1)
        cv2.imshow('image', img) 
  
# driver function 





if __name__=="__main__":
    
    file = open("corner_coords.txt", 'w')

    # reading the image 
    img = cv2.imread('cube.png', 1) 

    # displaying the image 
    cv2.imshow('image', img)
  
    # setting mouse hadler for the image 
    # and calling the click_event() function 
    cv2.setMouseCallback('image', click_event) 
    print ("Click the 6 corners of the cube and press exit.")
    
  
    # wait for a key to be pressed to exit 

    cv2.waitKey(0) 
  
    # close the window 
    file.close()
    cv2.destroyAllWindows()
