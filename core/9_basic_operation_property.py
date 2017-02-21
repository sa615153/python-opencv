# -*- coding: utf-8 -*-
import cv2
import numpy as np
img = cv2.imread('C:/Users/JPang3/Desktop/beijing/opencv/opencv_projects/python-opencv/img3.jpg')

px = img[100,100]
print px
# [ 93 144 140]
blue = img[100,100,0]
print blue
# 93
blue2 = img[100,100][0]
print blue2
# 93

# img[100,100]=[255,255,255]
# print img[100,100]

################################
#better way

# accessing RED value
print img.item(100,100,2)
# modifying RED value
img.itemset((100,100,2),100)
print img.item(100,100,2)

# -------------------------------------------------------------------------
# property
# -------------------------------------------------------------------------
print img.shape
# Total number of pixels
print img.size
print img.shape[0]*img.shape[1]
print "img.shape[0]*img.shape[1]*3"
print img.shape[0]*img.shape[1]*3
print img.dtype


# cv2.imshow('img3',img)
# cv2.waitKey(0)

# img[] 平面坐标，坐标值为[b,g,r]
# 修改ｐｉｘ能用ｎｕｍｐｙ矩阵运算就不要用循环
# 如果图像是灰度图，返回值仅有行数和列数。所以通过检查这个返回值就可以知道加载的是灰度图还是彩色图
