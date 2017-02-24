# -*- coding: utf-8 -*-
import numpy as np
import cv2

img = cv2.imread('../../bounding_rec3.png',0)
img3 = cv2.imread('../../bounding_rec3.png',3)

ret,thresh = cv2.threshold(img,100,255,0)
img_copy = thresh.copy()
thresh,contours,hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]

# 凸缺陷

# 找凸包
hull = cv2.convexHull(cnt,returnPoints = False)
# 计算缺陷
defects = cv2.convexityDefects(cnt,hull)  # [[[]]],三维数组

for i in range(defects.shape[0]):  # shape(0)行数
    s,e,f,d = defects[i,0]  # defeats 每一行都是一个defeat，defeats[i]是一个[[]],defeats[i,0]是双标里边的[],单维数组
    start = tuple(cnt[s][0])  # cnt 也是[[[]]]三维数组,cnt[s]中s是目标点在cnt中的索引，cnt[s]即为[[]](第s行),cnt[s][0]即为单维数组--点坐标
    end = tuple(cnt[e][0])  # 同上
    far = tuple(cnt[f][0])  # 同上
    cv2.line(img3,start,end,[0,255,0],2)  # 画线
    cv2.circle(img3,far,5,[0,0,255],-1)  # 画点

cv2.imshow('img',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

# print cnt
# print 'defects'
# print defects
# print 'range'
# print range(defects.shape[0])
# print 'img'
# print img
# print 'img3'
# print img3
# print type(img3)



#  Point Polygon Test 点多边形测试
# 求解图像中的一个点到一个对象轮廓的最短距离
# 内正外负边0

# 此函数的第三个参数是 measureDist。如果设置为 True，就会计算最
# 短距离。如果是 False，只会判断这个点与轮廓之间的位置关系（返回值为
# +1， -1， 0）。
# time consuming process. So, making it False gives about 2-3X speedup.
dist = cv2.pointPolygonTest(cnt,(50,50),True)
print dist


# 形状匹配 match shapes

img1 = cv2.imread('../../img1.jpg',0)
img2 = cv2.imread('../../j.png',0)
black1 = np.zeros(img1.shape,np.uint8)
black2 = np.zeros(img2.shape,np.uint8)




ret, thresh = cv2.threshold(img1, 127, 255,0)
ret, thresh2 = cv2.threshold(img2, 127, 255,0)
# cv2.imshow('thresh',thresh)
# cv2.waitKey(0)
# cv2.imshow('thresh2',thresh2)
# cv2.waitKey(0)


thresh,contours,hierarchy = cv2.findContours(thresh,2,1)
cnt1 = contours[0]
thresh2,contours,hierarchy = cv2.findContours(thresh2,2,1)
cnt2 = contours[0]

# black1 = cv2.drawContours(black1,[cnt1],0,(0,255,0),3)
# cv2.imshow('black1',black1)
# cv2.waitKey(0)
black2 = cv2.drawContours(black2,[cnt2],0,255,1)
cv2.imshow('black2',black2)
cv2.waitKey(0)
print 1
print 'cnt1---------------'  #  [[[ 49 123]]]
print cnt1
print 'cnt2---------------'
print cnt2
print 'end of cnt2--------'

ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
print ret



