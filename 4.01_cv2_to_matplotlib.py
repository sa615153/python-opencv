import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img2.jpg',0)
# plt.imshow(img,cmap='gray',interpolation='bicubic')
# plt.xticks([]),plt.yticks([]) #hide x,y values
# plt.show()

# ------------------------------------------------------------------
img2 = cv2.imread('img2.jpg',cv2.IMREAD_COLOR)
plt.imshow(img2)
# plt.imshow(img2,cmap='color',interpolation='bicubic')
plt.show()