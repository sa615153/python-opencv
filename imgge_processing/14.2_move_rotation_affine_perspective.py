# -*- coding: utf-8 -*-

#  https://www.zhihu.com/question/20666664
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../messi5.jpg',0)
rows,cols = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 这里的第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
# 可以通过设置旋转中心，缩放因子，以及窗口大小来防止旋转后超出边界的问题
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)

# 第三个参数是输出图像的尺寸中心
dst = cv2.warpAffine(img,M,(cols,rows))

# ----------------------#
cv2.imshow('tmp',dst)   #
cv2.waitKey(0)          #
# ----------------------#


# affine transformation,仿射，一个线性变换加一个位移
# https://www.zhihu.com/question/20666664
# 三个点
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('affine Input')
plt.subplot(122),plt.imshow(dst),plt.title('affine Output')
plt.show()



# perspective transformation
# 四个点

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('perspective Input')
plt.subplot(122),plt.imshow(dst),plt.title('perspective Output')
plt.show()