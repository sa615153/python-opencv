# -*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('../water_coins.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU) # 反转（灰度低转变为255）+ otsu

# cv2.imshow('thresh',thresh)
# cv2.waitKey(0)


# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
# cv2.imshow('opening',opening)
# cv2.waitKey(0)


# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)
# cv2.imshow('sure_bg',sure_bg)
# cv2.waitKey(0)


# Finding sure foreground area
# 距离变换的基本含义是计算一个图像中非零像素点到最近的零像素点的距离，也就是到零像素点的最短距离
# 个最常见的距离变换算法就是通过连续的腐蚀操作来实现，腐蚀操作的停止条件是所有前景像素都被完全
# 腐蚀。这样根据腐蚀的先后顺序，我们就得到各个前景像素点到前景中心呗Ⅵ像素点的
# 距离。根据各个像素点的距离值，设置为不同的灰度值。这样就完成了二值图像的距离变换
#cv2.distanceTransform(src, distanceType, maskSize)
# 第二个参数 0,1,2 分别表示 CV_DIST_L1, CV_DIST_L2 , CV_DIST_C
dist_transform = cv2.distanceTransform(opening,1,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)  # 0.7*dist_transform.max() 最大灰度*0.7
# cv2.imshow('sure_fg',sure_fg)
# cv2.waitKey(0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
cv2.imshow('unknown',unknown)
cv2.waitKey(0)


# -----------------------------------------------------------------
# Marker labelling

# 由试验得知，markers1每个连通域分别标值0,1,2,3。。。背景为0
ret, markers1 = cv2.connectedComponents(sure_fg)

# cv2.imshow('markers1',markers1)
# cv2.waitKey(0)
# #######################################
# img_copy = img.copy()
# img_copy[markers1==4] = [0,0,255]
# cv2.imshow('img_copy',img_copy)
# cv2.waitKey(0)
# #######################################

# Add one to all labels so that sure background is not 0, but 1
markers = markers1+1
# #######################################
# img_copy = img.copy()
# img_copy[markers==1] = [0,0,255]
# cv2.imshow('img_copy',img_copy)
# cv2.waitKey(0)
# #######################################

# Now, mark the region of unknown with zero
markers[unknown==255] = 0
# #######################################
# img_copy = img.copy()
# img_copy[markers==1] = [0,0,255]  # 0 是unknown，1是背景
# cv2.imshow('img_copy',img_copy)
# cv2.waitKey(0)
# #######################################


markers3 = cv2.watershed(img,markers)
img[markers3 == -1] = [255,0,0]
cv2.imshow('img', img)
cv2.waitKey(0)

for i in range(-3,10):
    print i
    img[markers3 == 0] = [255, 0, 0]
    cv2.imshow('img',img)
    cv2.waitKey(1000)
