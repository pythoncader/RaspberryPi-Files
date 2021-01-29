import cv2
import os
directorylist = os.listdir()
filenames = []
extension = '.MOV'
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
    cap = cv2.VideoCapture(filenames[i]+extension)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    path = 'C:/users/mike/desktop/outputvideo/'+filenames[i]
    if os.path.exists(path):
        print('The path exists!')
    else:    
        os.mkdir(path)

    out = cv2.VideoWriter(os.path.join(path, filenames[i]+'-output.mp4'), fourcc, 25.0, (1280, 720))
    outgray = cv2.VideoWriter(os.path.join(path, filenames[i]+'-outputgray.mp4'), fourcc, 25.0, (1280, 720), 0)


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