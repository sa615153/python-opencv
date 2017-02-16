# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread('../j.png',0)

ret,bi_img = cv2.threshold(img,10,255,cv2.THRESH_BINARY)

# # -----------------------------------------
# cv2.namedWindow('1',cv2.WINDOW_NORMAL)    #
# cv2.namedWindow('2',cv2.WINDOW_NORMAL)    #
# cv2.imshow('1',img)                       #
# cv2.imshow('2',bi_img)                    #
# cv2.waitKey(0)                            #
# # -----------------------------------------


kernel = np.ones((5,5),np.uint8)


# 腐蚀
erosion = cv2.erode(bi_img,kernel,iterations = 1)

kernel2 = np.ones((3,3),np.uint8)
erosion2 = cv2.erode(bi_img,kernel,iterations = 1)

# # -----------------------------------------
# cv2.namedWindow('1',cv2.WINDOW_AUTOSIZE)    #
# cv2.namedWindow('2',cv2.WINDOW_AUTOSIZE)    #
# cv2.namedWindow('3',cv2.WINDOW_AUTOSIZE)    #
# cv2.imshow('1',bi_img)                    #
# cv2.imshow('2',erosion)                   #
# cv2.imshow('3',erosion2)                  #
# cv2.waitKey(0)                            #
# # -----------------------------------------

# 膨胀
dilation = cv2.dilate(img,kernel,iterations = 1)

# # -----------------------------------------
# cv2.namedWindow('1',cv2.WINDOW_AUTOSIZE)    #
# cv2.namedWindow('2',cv2.WINDOW_AUTOSIZE)    #
# cv2.namedWindow('3',cv2.WINDOW_AUTOSIZE)    #
# cv2.imshow('1',bi_img)                    #
# cv2.imshow('2',erosion)                   #
# cv2.imshow('3',dilation)                  #
# cv2.waitKey(0)                            #
# # -----------------------------------------

# 开运算，先腐蚀再膨胀,降白噪音

bi_img = cv2.imread('../j_noise.png',0)
opening = cv2.morphologyEx(bi_img, cv2.MORPH_OPEN, kernel)

# # -----------------------------------------
# cv2.namedWindow('1',cv2.WINDOW_NORMAL)    #
# cv2.namedWindow('2',cv2.WINDOW_NORMAL)    #
# cv2.imshow('1',bi_img)                    #
# cv2.imshow('2',opening)                   #
# cv2.waitKey(0)                            #
# # -----------------------------------------

# 闭运算
bi_img = cv2.imread('../j_noise_2.png',0)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# -----------------------------------------
cv2.namedWindow('1',cv2.WINDOW_NORMAL)    #
cv2.namedWindow('2',cv2.WINDOW_NORMAL)    #
cv2.imshow('1',bi_img)                    #
cv2.imshow('2',opening)                   #
cv2.waitKey(0)                            #
# -----------------------------------------




# -----------------------------------------------------------------------------------------------------
# 形态学梯度,like outline of the object
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# 礼帽 原始图像与进行开运算之后得到的图像的差。下面的例子是用一个 9x9 的核进行礼帽操作的结果

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# 黑帽
# 进行闭运算之后得到的图像与原始图像的差

blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
# -----------------------------------------------------------------------------------------------------




#结构化元素

'''在前面的例子中我们使用 Numpy 构建了结构化元素，它是正方形的。但
有时我们需要构建一个椭圆形/圆形的核。为了实现这种要求，提供了 OpenCV
函数 cv2.getStructuringElement()。你只需要告诉他你需要的核的形状
和大小。
# Rectangular Kernel
>>> cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
array([[1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]], dtype=uint8)

# Elliptical Kernel
>>> cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
array([[0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0]], dtype=uint8)

# Cross-shaped Kernel
>>> cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
array([[0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0]], dtype=uint8)'''