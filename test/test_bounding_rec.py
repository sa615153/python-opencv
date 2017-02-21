# -*- coding: utf-8 -*-

import numpy as np
import cv2

# 矩
# 最后一个参数必须是0，不能是3
img = cv2.imread('../bounding_rec3.png',0)
img3 = cv2.imread('../bounding_rec3.png',3)
ret,thresh = cv2.threshold(img,100,255,0)

# cv2.imshow('1',thresh) 若参数为3，这里没问题，但是findContour会报错
cv2.waitKey(0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
M = cv2.moments(cnt)
print cnt
print M
print M['m00']
# cv2.imshow('img_copy', img_copy)
# cv2.waitKey(0)

x,y,w,h = cv2.boundingRect(cnt)
print "x,y,w,h"
print x,y,w,h

cv2.rectangle(img3,(x,y),(x+w,y+h),(0,255,0),3)

# cv2.rectangle(img, (ix, iy), (x, y), color, -1)
cv2.imshow('boundingRect', img3)
cv2.waitKey(0)


rect = cv2.minAreaRect(cnt)
# cv2
box = cv2.cv.BoxPoints(rect)
box = np.int0(box)
print '--------'
print box

n = cv2.drawContours(img3,[box],0,(0,0,255),2)
cv2.imshow('minAreaRect',img3)
cv2.waitKey(0)


