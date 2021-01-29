import cv2
filesdirectory = 'C:/users/mike/desktop/coding/python/opencv/files/'
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