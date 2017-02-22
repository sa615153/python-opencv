# -*- coding: utf-8 -*-

import numpy as np
import cv2

# 矩
img = cv2.imread('../bounding_rec3.png',0)
img3 = cv2.imread('../bounding_rec3.png',3)

ret,thresh = cv2.threshold(img,100,255,0)
# cv2.imshow('thresh',thresh)
# cv2.waitKey(0)

image,contours,hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]

(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
n = cv2.circle(img3,center,radius,(0,255,0),2)

print type(n)