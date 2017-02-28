# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
import cv2


# ---------------
# opencv
# ---------------
img = cv2.imread('../../2Dhist.png')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])


# -------------
# numpy
# -------------

img = cv2.imread('../../2Dhist.png')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

print hsv
h,s,v = cv2.split(hsv)
hist, xbins, ybins = np.histogram2d(h.ravel(),s.ravel(),[180,256],[[0,180],[0,256]])


# --------------------------draw-----------------------------
# cv2.imshow('2d_hist',hist)
# cv2.waitKey(0)


# # X axis shows S values and Y axis shows Hue.
# plt.imshow(hist,interpolation = 'nearest')
# plt.show()


