# -*- coding: utf-8 -*-

# 相同的颜色或者灰度(intensity) 轮廓在形状分析和物体的检测和识别中很有用


import numpy as np
import cv2
from matplotlib_1 import pyplot as plt


# how to find contours of a binary image:
im = cv2.imread('../../boxs.png')

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)


ret,thresh = cv2.threshold(imgray,127,255,0)
thresh_store = thresh.copy()
#cv3
# image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cv2
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# cv2.RETR_TREE 检索模式
# cv2.CHAIN_APPROX_SIMPLE 近似方法，cv2.CHAIN_APPROX_NONE ---所有点 | cv2.CHAIN_APPROX_SIMPLE 简化




# draw contours
'''
To draw all the contours in an image:
img = cv2.drawContours(img, contours, -1, (0,255,0), 3)

To draw an individual contour, say 4th contour:
img = cv2.drawContours(img, contours, 3, (0,255,0), 3)

But most of the time, below method will be useful:
cnt = contours[4]
img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)
'''

to_draw = cv2.imread('../../draw_contours.jpg')
to_draw_store = to_draw.copy()
# cv3
# new_img = cv2.drawContours(to_draw, contours,-1, (0,255,0), 3)
# cv2 new_img is None
cv2.drawContours(to_draw, contours,-1, (0,255,0), 3)


# ----------------------------------------------------------------------------
plt.subplot(231),plt.imshow(im,cmap='gray'),plt.title('Original')      #
plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(imgray,cmap='gray'),plt.title('imgray')      #
plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(thresh_store,cmap='gray'),plt.title('thresh_store')      #
plt.xticks([]), plt.yticks([])
plt.subplot(234),plt.imshow(thresh,cmap='gray'),plt.title('thresh')      #
plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(to_draw_store,cmap='gray'),plt.title('to_draw_store')      #
plt.xticks([]), plt.yticks([])
plt.subplot(236),plt.imshow(to_draw,cmap='gray'),plt.title('to_draw')      #
plt.xticks([]), plt.yticks([])

plt.show()