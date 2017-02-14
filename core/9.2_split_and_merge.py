# -*- coding: utf-8 -*-
import numpy as np
import cv2

img = cv2.imread('C:/Users/JPang3/Desktop/beijing/opencv/opencv_projects/python-opencv/messi5.jpg')

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

b = img[:,:,0]
# all red to zero
img[:,:,2] = 0





# 能用ｎｕｍｐｙ的索引就用索引，不要用ｓｐｌｉｔ

