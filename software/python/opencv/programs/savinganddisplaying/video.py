import cv2
import os
import shutil

filesdirectory = '/home/pi/Desktop/RaspberryPi-Files/software/python/opencv/files/'
directorylist = os.listdir(filesdirectory)
filenames = []
extension = '.MOV'
path = '/home/pi/Desktop/RaspberryPi-Files/software/python/opencv/files/output-video/'

if os.path.exists(path):
    shutil.rmtree(path)

os.mkdir(path)

for i in range(0, len(directorylist)):
    if directorylist[i].endswith('.MOV'):
        newlist = list(directorylist[i])
        
        del newlist[-1]
        del newlist[-1]
        del newlist[-1]
        del newlist[-1]
        newstring = ''.join(newlist)
        print(newstring)
        filenames.append(newstring)

for i in range(0, len(filenames)):
    cap = cv2.VideoCapture(filesdirectory+filenames[i]+extension)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    path += str(filenames[i])
    
    if os.path.exists(path):
        print('The path exists!')
    else:    
        os.mkdir(path)

    out = cv2.VideoWriter(path+'/'+filenames[i]+'-output.mp4', fourcc, 25.0, (1280, 720))
    outgray = cv2.VideoWriter(path+'/'+filenames[i]+'-outputgray.mp4', fourcc, 25.0, (1280, 720), 0)


    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            outgray.write(gray)
            out.write(frame)
            cv2.namedWindow(filenames[i]+extension, cv2.WINDOW_NORMAL)
            cv2.imshow(filenames[i]+extension, frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()