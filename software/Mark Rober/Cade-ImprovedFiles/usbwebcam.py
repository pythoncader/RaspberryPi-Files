#!/usr/bin/env python3

import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")



ret, frame = cam.read()
if not ret:
    print("Failed to grab frame")
else:
    print("\nCapturing Image...\n")
    myimage = frame.copy()
    # Using cv2.putText() method 
    image = cv2.putText(myimage, 'Image Preview', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA) 
    cv2.imshow("test", myimage)
    cv2.waitKey(0)

    print("Successfully captured image... Save to File?\n")
    yesorno = str(input())
    if "y" in yesorno or "s" in yesorno:
        cv2.imwrite("OpenCV-Capture.png", frame)
        print("Completed!")
    else:
        print("Discarding File...")
cv2.destroyAllWindows()