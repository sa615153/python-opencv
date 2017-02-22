# -*- coding: utf-8 -*-

import numpy as np
import cv2

# 矩
img = cv2.imread('../../bounding_rec3.png',0)
img3 = cv2.imread('../../bounding_rec3.png',0)

ret,thresh = cv2.threshold(img,100,255,0)
img_copy = thresh.copy()
thresh,contours,hierarchy = cv2.findContours(thresh, 1, 2)
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

# 从黑图制模
mask = np.zeros(img3.shape,np.uint8)
cv2.imshow('mask',mask)
cv2.waitKey(0)

# 这里一定要使用参数-1, 绘制填充的的轮廓,,若为3，则厚度为3，不会填充
mask = cv2.drawContours(mask,[cnt],0,255,-1)
cv2.imshow('drawContours_mask',mask)
cv2.waitKey(0)

# Returns a tuple of arrays, one for each dimension of matrix,
# containing the 索引indices of the non-zero elements in that dimension.
# The result of this is always a 2-D array, with a row for
# each non-zero element.
# To group the indices by element, rather than dimension, use:
# transpose(nonzero(a))
# >>> x = np.eye(3)
# >>> x
# array([[ 1., 0., 0.],
#        [ 0., 1., 0.],
#        [ 0., 0., 1.]])
# >>> np.nonzero(x)

# 横维012是1，零行一行二行       纵维012是1，零列一列二列
# (array([0, 1, 2]), array([0, 1, 2]))
# >>> x[np.nonzero(x)]
# array([ 1., 1., 1.])
# >>> np.transpose(np.nonzero(x))
# array([[0, 0],
# [1, 1],
# [2, 2]])

# 获得像素点
pixelpoints = np.transpose(np.nonzero(mask))
# pixelpoints = cv2.findNonZero(mask)


# Maximum Value, Minimum Value and their locations

cv2.imshow('img',img)
cv2.waitKey(0)

# 这里出的问题，img已经被改变，不能用，img3原来是3通道，也不能用，总之，保证是没被修改过的0通道图
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img3,mask = mask)
print min_val,max_val,min_loc,max_loc


# 平均颜色及平均灰度

img = cv2.imread('../../tmp.jpg',0)
img3 = cv2.imread('../../tmp.jpg',3)

# 做黑图
mask = np.zeros(img.shape,np.uint8)
# 画1
mask = cv2.drawContours(mask,[cnt],0,255,-1)
cv2.imshow('tmp_mask',mask)
cv2.waitKey(0)

# mask为1的像素才被考虑在内
mean_val = cv2.mean(img ,mask = mask)
print mean_val

# 极点
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])




