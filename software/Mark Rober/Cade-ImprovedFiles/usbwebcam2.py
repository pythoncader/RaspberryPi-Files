import cv2
import numpy as np

cam = cv2.VideoCapture(0)

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
    else:
        cv2.imshow("frame", frame)
        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = f"opencv_frame_{img_counter}.png"
            cv2.imwrite(img_name, frame)
            print(f"{img_name} written!")
            img_counter += 1
cv2.destroyAllWindows()