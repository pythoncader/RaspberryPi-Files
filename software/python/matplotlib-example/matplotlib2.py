from matplotlib import pyplot as plt
import cv2
import numpy as np

img = cv2.imread('alligator.png', -1)
cv2.imshow("image", img)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(rgb)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()