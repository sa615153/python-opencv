# -*- coding: utf-8 -*-

import numpy as np
import cv2

# 矩
img = cv2.imread('../../bounding_rec3.png',0)
img3 = cv2.imread('../../bounding_rec3.png',3)

ret,thresh = cv2.threshold(img,100,255,0)
img_copy = thresh.copy()
contours,hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
M = cv2.moments(cnt)

# 长宽比 Aspect Ratio
x,y,w,h = cv2.boundingRect(cnt)
aspect_ratio = float(w)/h
print aspect_ratio

# 轮廓面积与边界矩形面积的比 Extent
area = cv2.contourArea(cnt)
x,y,w,h = cv2.boundingRect(cnt)
rect_area = w*h
extent = float(area)/rect_area
print extent

# 轮廓面积与凸包面积的比 Solidity

area = cv2.contourArea(cnt)
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area
print solidity


# 与轮廓面积相等的圆形的直径 Equivalent Diameter

area = cv2.contourArea(cnt)
equi_diameter = np.sqrt(4*area/np.pi)

# 方向 Orientation
(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)


# 掩模和像素点 Mask and Pixel Points

# 有时我们需要构成对象的所有像素点，我们可以这样做：
mask = np.zeros(img3.shape,np.uint8)
cv2.imshow('mask',mask)
cv2.waitKey(0)

# 这里一定要使用参数-1, 绘制填充的的轮廓,,若为3，则厚度为3，不会填充
cv2.drawContours(mask,[cnt],0,255,-1)
cv2.imshow('drawContours',mask)
cv2.waitKey(0)

# Returns a tuple of arrays, one for each dimension of a,
# containing the indices of the non-zero elements in that dimension.
# The result of this is always a 2-D array, with a row for
# each non-zero element.
# To group the indices by element, rather than dimension, use:
# transpose(nonzero(a))
# >>> x = np.eye(3)
# >>> x
# array([[ 1., 0., 0.],
# [ 0., 1., 0.],
# [ 0., 0., 1.]])
# >>> np.nonzero(x)
# (array([0, 1, 2]), array([0, 1, 2]))
# >>> x[np.nonzero(x)]
# array([ 1., 1., 1.])
# >>> np.transpose(np.nonzero(x))
# array([[0, 0],
# [1, 1],
# [2, 2]])

pixelpoints = np.transpose(np.nonzero(mask))
#pixelpoints = cv2.findNonZero(mask)