import numpy as np
import cv2

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
#events = [i  for i in dir(cv2) if 'EVENT' in i]
#print(events)
font = cv2.FONT_HERSHEY_SIMPLEX
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 20, (0, 0, 0), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 20, (0, 0, 0), -1)
        points.clear()
        points.append((x, y))
        cv2.imshow('image', img)

#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('alligator.png')
cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
