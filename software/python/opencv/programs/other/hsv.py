import cv2
import numpy as np

def nothing(x):
    pass
#Hue range is [0,255], Saturation range is [0,255] and Value range is [0,255]
cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    frame = cv2.imread('opencv-logo.png')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")
    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord("s"):
        print("lower bounds:", l_b)
        print("upper bounds:", u_b)
        break


cv2.destroyAllWindows()
if key == ord("s"):
        l_b = np.array(l_b)
        u_b = np.array(u_b)
        mask = cv2.inRange(hsv, l_b, u_b)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        res = cv2.putText(res, str(l_b), (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 4)
        res = cv2.putText(res, str(u_b), (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 4)
        cv2.imshow("Result:", res)
        key = cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite("Result.png", res)