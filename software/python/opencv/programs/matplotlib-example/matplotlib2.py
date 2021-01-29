from matplotlib import pyplot as plt
import cv2
import numpy as np
path = "C:/users/mike/desktop/creative cloud files/coding/python/opencv/files/"
img = cv2.imread(path+'alligator.png', -1)
cv2.imshow("image", img)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(rgb)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()