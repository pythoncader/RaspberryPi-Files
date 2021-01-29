import cv2
import datetime

filesdirectory = 'C:/users/mike/desktop/opencv/files/'
cap = cv2.VideoCapture(0)
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3, 3000)
cap.set(4, 3000)
print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

       font = cv2.FONT_HERSHEY_SIMPLEX
       text = 'Width: '+ str(cap.get(3)) + ' Height:' + str(cap.get(4))
       datet = str(datetime.datetime.now())
       frame = cv2.putText(frame, text, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
       frame = cv2.putText(frame, datet, (10, 100), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
       cv2.imshow('frame', frame)

       if cv2.waitKey(1) & 0xFF == 27:
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()