# -*- coding: utf-8 -*-
# gradients_edge
# 求边界，即求离散倒数，边界存在导致边界边缘两侧高度明显不同，导数较大
# 一阶将上坡区数值改为斜率（较大值），别处平坦的地方为0（较小）  00000123333333333 3 2 10000
# 二阶姜上坡区的开始处标为二阶导，后续上坡区为0                  00000110000000000 0-1-10000
# 二阶导更靠近边缘，更细
# 详见dell书签learning，http://blog.csdn.net/xiaowei_cqu/article/details/7829481

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('../dave.jpg',0)
#cv2.CV_64F 输出图像的深度（数据类型），可以使用-1, 与原图像保持一致 np.uint8
laplacian=cv2.Laplacian(img,cv2.CV_64F)
# 参数 1,0 为只在 x 方向求一阶导数，最大可以求 2 阶导数。
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
# 参数 0,1 为只在 y 方向求一阶导数，最大可以求 2 阶导数。
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)


plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()


# -----------------------------------------------------------------------
# 在查看上面这个例子的注释时不知道你有没有注意到：当我们可以通过参
# 数 -1 来设定输出图像的深度（数据类型）与原图像保持一致，但是我们在代
# 码中使用的却是 cv2.CV_64F。这是为什么呢？想象一下一个从黑到白的边界
# 的导数是整数，而一个从白到黑的边界点导数却是负数。如果原图像的深度是
# np.int8 时，所有的负值都会被截断变成 0，换句话说就是把把边界丢失掉。


img = cv2.imread('../boxs.png',0)
# Output dtype = cv2.CV_8U
sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)
# 也可以将参数设为-1
#sobelx8u = cv2.Sobel(img,-1,1,0,ksize=5)
# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)
plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])
plt.show()