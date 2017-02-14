import numpy as np
import cv2

img1 = cv2.imread('C:/Users/JPang3/Desktop/beijing/opencv/opencv_projects/python-opencv/img3.jpg')
# ----------------------#
cv2.imshow('tmp',img1)  #
cv2.waitKey(0)          #
# ----------------------#
e1 = cv2.getTickCount()
for i in xrange(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print t

# ----------------------#
cv2.imshow('tmp',img1)  #
cv2.waitKey(0)          #
# ----------------------#



# check if optimization is enabled
print cv2.useOptimized()

cv2.setUseOptimized(False)
print cv2.useOptimized()

e1 = cv2.getTickCount()
for i in xrange(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print t