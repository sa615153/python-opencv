# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../img3.jpg',0)
img2 = cv2.imread('../CLAHE.png',0)

plt.hist(img.ravel(),256,[0,256])
plt.hist(img2.ravel(),256,[0,256])
plt.show()