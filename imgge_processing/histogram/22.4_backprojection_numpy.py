# -*- coding: utf-8 -*-

'''1、原理
图像的反向投影图是用输入图像的某一位置上像素值（多维或灰度）对应在直方图的一个bin上的值来代替该像素值，所以得到的反向投影图是单通的。'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

#roi is the object or region of object we need to find
roi = cv2.imread('rose_red.png')
hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

#target is the image we search in
target = cv2.imread('rose.png')
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)

# Find the histograms using calcHist. Can be done with np.histogram2d also
M = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
I = cv2.calcHist([hsvt],[0, 1], None, [180, 256], [0, 180, 0, 256] )

'''计算比值： R = M/I 。反向投影 R，也就是根据 R 这个”调色板“创建一
副新的图像，其中的每一个像素代表这个点就是目标的概率。例如 B (x, y) =
R [h (x, y) , s (x, y)]，其中 h 为点（x， y）处的 hue 值， s 为点（x， y）处的
saturation 值。最后加入再一个条件 B (x, y) = min [B (x, y) , 1]。'''
h,s,v = cv2.split(hsvt)
B = R[h.ravel(),s.ravel()]
B = np.minimum(B,1)
B = B.reshape(hsvt.shape[:2])

# 现在使用一个圆盘算子做卷积， B = D × B，其中 D 为卷积核
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.filter2D(B,-1,disc,B)
B = np.uint8(B)
cv2.normalize(B,B,0,255,cv2.NORM_MINMAX)

ret,thresh = cv2.threshold(B,50,255,0)

