# -*- coding: utf-8 -*-

# Hough变换的原理是将特定图形上的点变换到一组参数空间上，根据参数空间点的累计结果找到一个极大值对应的解，那么这个解就对应着要寻找的几何形状的参数
# 直线 → rho theta
import cv2
import numpy as np

img = cv2.imread('dave.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
# 第一个参数是一个二值化图像，所以在进行霍夫变换之前要首先进行二值化，或者进行Canny 边缘检测。
# 第二和第三个值分别代表 ρ 和 θ 的精确度。
# 第四个参数是阈值，只有累加其中的值高于阈值时才被认为是一条直线，也可以把它看成能
# 检测到的直线的最短长度（以像素点为单位）。
lines = cv2.HoughLines(edges,1,np.pi/180,200)
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imwrite('houghlines3.jpg',img)




# ------------------------Probabilistic Hough Transform---------------------

img = cv2.imread('dave.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 10

# minLineLength - 线的最短长度。比这个短的线都会被忽略。
# MaxLineGap - 两条线段之间的最大间隔，如果小于此值，这两条直线就被看成是一条直线。

# 返回值就是直线的起点和终点
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    cv2.imwrite('houghlines5.jpg',img)