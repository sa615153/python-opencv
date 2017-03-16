# -*- coding: utf-8 -*-

import numpy as np
import cv2

# 矩
img = cv2.imread('../../bounding_rec3.png',0)
img3 = cv2.imread('../../bounding_rec3.png',3)

ret,thresh = cv2.threshold(img,100,255,0)
img_copy = thresh.copy()
img,contours,hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
M = cv2.moments(cnt)
print cnt
print M
print M['m00']

# 重心
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print cx,cy

# area 面积 m00
area = cv2.contourArea(cnt)
print area


#周长
perimeter = cv2.arcLength(cnt,True)
print perimeter

# Contour Approximation, 更少的点 Douglas-Peucker algorithm 首尾点，最远点（大则留，小则弃），留点与首点重做，留点与尾点重做
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)

# 凸包，
# Convex Hull, 找到一个凸边形，包含object
# Python: cv2.convexHull(points[, hull[, clockwise[, returnPoints]]]) → hull
# points 我们要传入的轮廓
# • hull 输出，通常不需要
# • clockwise 方向标志。如果设置为 True，输出的凸包是顺时针方向的。
# 否则为逆时针方向。
# • returnPoints By default, True. Then it returns the coordinates of the hull points.
# If False, it returns the indices of contour points corresponding to the hull points.

hull = cv2.convexHull(cnt)

# Checking Convexity
# True or False
k = cv2.isContourConvex(cnt)

# 7. 边框Bounding Rectangle
# Straight Bounding Rectangle
x,y,w,h = cv2.boundingRect(cnt)
print "img type"
print type(img)
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
print type(img)

# Rotated Rectangle
# Here, bounding rectangle is drawn with minimum area, so it considers the rotation also.
# The function used is cv2.minAreaRect().
# It returns a Box2D structure which contains following detals-(top-left corner(x,y),(width,height),angle of rotation).
#  But to draw this rectangle, we need 4 corners of the rectangle. It is obtained by the function cv2.boxPoints()

rect = cv2.minAreaRect(cnt)
# cv3
box = cv2.boxPoints(rect)
# cv2
# box = cv2.cv.BoxPoints(rect)
box = np.int0(box)
print '--------'
print box

# cv2
n = cv2.drawContours(img3,[box],0,(0,0,255),2)

cv2.imshow('bounding_rec',img3)
cv2.waitKey(0)


# 外接圆 Minimum Enclosing Circle

(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)


# img3 = cv2.circle(img3,center,radius,(0,255,0),2)
# cv2
n = cv2.circle(img3,center,radius,(0,255,0),2)
cv2.imshow('circle',img3)
cv2.waitKey(0)


# 椭圆,旋转的边界矩形内切圆

ellipse = cv2.fitEllipse(cnt)
print "ellipse"
print ellipse
print type(ellipse) # tuple
# cv2
n = cv2.ellipse(img3,ellipse,(0,255,0),2)
cv2.imshow('ellipse',img3)
cv2.waitKey(0)


# 直线拟合
rows,cols = img3.shape[:2]
# cv3
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
# cv2
# [vx,vy,x,y] = cv2.fitLine(cnt, cv2.cv.CV_DIST_L2,0,0.01,0.01)

lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
#cv3
# img = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)
#cv2
cv2.line(img3,(cols-1,righty),(0,lefty),(0,255,0),2)
cv2.imshow('line',img3)
cv2.waitKey(0)

