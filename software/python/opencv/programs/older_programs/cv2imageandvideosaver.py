import cv2
from time import sleep

filesdirectory = 'C:/users/mike/desktop/opencv/files/'
img = cv2.imread(filesdirectory+"IMG_0919.JPG", 1)
print(img)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
key = cv2.waitKey(0) & 0xFF

if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite(filesdirectory+'alligator.png', img)
    cv2.destroyAllWindows()
videofilename = 'MVI_4715'
videoextension = '.MOV'
video = cv2.VideoCapture(filesdirectory+videofilename+videoextension)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
outgray = cv2.VideoWriter(filesdirectory+videofilename+'-output(gray).mp4', fourcc, 25.0, (1280, 720), 0)
out = cv2.VideoWriter(filesdirectory+videofilename+'-output.mp4', fourcc, 25.0, (1280, 720))
while video.isOpened():
    ret, frame = video.read()
    if ret == True:
        print(video.get(cv2.CAP_PROP_FPS))
        print(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

        grayscl = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(frame)
        outgray.write(grayscl)
        cv2.imshow('frame:', frame)
        cv2.imshow('gray: ', grayscl)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break
video.release()
out.release()
cv2.destroyAllWindows()