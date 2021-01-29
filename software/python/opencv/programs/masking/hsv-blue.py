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
while True:
    frame = cv2.imread(path+'smarties.png')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    """l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")
    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, l_b, u_b)"""

    upperBlue = [137, 255, 255]
    lowerBlue = [86, 157, 188]
    
    lower_bounds = np.array(lowerBlue)
    upper_bounds = np.array(upperBlue)
    mask = cv2.inRange(hsv, lower_bounds, upper_bounds)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord("s"):
        print("lower bounds:", lower_bounds)
        print("upper bounds:", upper_bounds)
        break


cv2.destroyAllWindows()
if key == ord("s"):
        l_b = np.array(lower_bounds)
        u_b = np.array(upper_bounds)
        mask = cv2.inRange(hsv, l_b, u_b)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        res = cv2.putText(res, str(l_b), (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 4)
        res = cv2.putText(res, str(u_b), (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 4)
        cv2.imshow("Result:", res)
        key = cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite("programs/masking/Result.png", res)