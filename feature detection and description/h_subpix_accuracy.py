# -*- coding: utf-8 -*-

import cv2
import numpy as np

filename = '../subpix_accuracy.png'
# filename = '../subpix_accuracy2.png'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# find Harris corners
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)

# find centroids
# connectedComponentsWithStats(InputArray image, OutputArray labels, OutputArray stats,
# OutputArray centroids, int connectivity=8, int ltype=CV_32S)
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)

# Python: cv2.cornerSubPix(image, corners, winSize, zeroZone, criteria)
# zeroZone – Half of the size of the dead region in the middle of the search zone
# over which the summation in the formula below is not done. It is used sometimes
# to avoid possible singularities of the autocorrelation matrix. The value of (-1,-1)
# indicates that there is no such a size.
# 返回值由角点坐标组成的一个数组（而非图像）
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

print centroids
print '-------------------'
print corners

# Now draw them

res = np.hstack((centroids,corners))  # stacking images side-by-side
# np.int0 可以用来省略小数点后面的数字（非四舍五入）。
res = np.int0(res)

print "-----------res----------"
print res

img[res[:,1],res[:,0]]=[0,0,255]  # img 是先取行后取列，即点的纵坐标，点的横坐标
img[res[:,3],res[:,2]] = [0,255,0]

cv2.namedWindow('subpix',cv2.WINDOW_NORMAL)
cv2.imshow('subpix',img)
cv2.waitKey(0)