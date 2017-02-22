# -*- coding: utf-8 -*-
import numpy as np
import cv2

img = cv2.imread('../../bounding_rec3.png',0)
img3 = cv2.imread('../../bounding_rec3.png',3)

ret,thresh = cv2.threshold(img,100,255,0)
img_copy = thresh.copy()
thresh,contours,hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]

# 凸缺陷

# 找凸包
hull = cv2.convexHull(cnt,returnPoints = False)
# 计算缺陷
defects = cv2.convexityDefects(cnt,hull)

print 'defects'
print defects
print 'range'
print range(defects.shape[0])
print 'img'
print img
print 'img3'
print img3
print type(img3)
