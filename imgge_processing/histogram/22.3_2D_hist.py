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


# print hsv
h,s,v = cv2.split(hsv)
hist, xbins, ybins = np.histogram2d(h.ravel(),s.ravel(),[180,256],[[0,180],[0,256]])


# --------------------------draw-----------------------------
cv2.imshow('2d_hist',hist)
cv2.waitKey(0)


# # X axis shows S values and Y axis shows Hue.
# plt.imshow(hist,interpolation = 'nearest')
# plt.show()


# opencv
# https://github.com/opencv/opencv/blob/master/samples/python/color_histogram.py
hsv_map = np.zeros((180, 256, 3), np.uint8)  # still a bgr img
# cv2.imshow('ori_bgr',hsv_map)
# cv2.waitKey(0)

print hsv_map
print hsv_map.shape[:2]
h, s = np.indices(hsv_map.shape[:2])
print "----------h----------------"
print h
print "----------s----------------"
print s

print "-------------hsv[:,:,0]----"
print hsv_map[:,:,0]

hsv_map[:,:,0] = h
hsv_map[:,:,1] = s
hsv_map[:,:,2] = 255

hsv_map = cv2.cvtColor(hsv_map, cv2.COLOR_HSV2BGR)

cv2.imshow('h=row,s=col,color is',hsv_map)
# cv2.waitKey(0)