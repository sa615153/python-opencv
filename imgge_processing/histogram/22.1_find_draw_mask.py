# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

# ----------
# find
# ----------
# ####cv
# cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])

# images: 原图像（图像格式为 uint8 或 float32）。当传入函数时应该用中括号 [] 括起来，例如： [img]。
# channels: 如果输入图像是灰度图，它的值就是 [0];如果是彩色图像的话，传入的参数可以是 [0]，[1]，[2]它们分别对应着通道BGR
# mask: 掩模图像。要统计整幅图像的直方图就把它设为 None
# histSize:BIN 的数目。也应该用中括号括起来，例如： [256]
# ranges: 像素值范围，通常为 [0， 256]

img = cv2.imread('../../img1.jpg',0)
hist = cv2.calcHist([img],[0],None,[256],[0,256]) #  256*1 二维数组，[[],[],[],[],,,]
# print hist
# print img


# ##numpy
#img.ravel() 将图像转成一维数组，这里没有中括号。
hist,bins = np.histogram(img.ravel(),256,[0,256])
'''np.bincount()，它的运行速度是np.histgram的十倍。所以对于一维直方图，我们最好使用这个函数。使用np.bincount时别忘了设置minlength=256。例如，
hist=np.bincount(img.ravel()， minlength=256)'''

'''OpenCV function is more faster than (around 40X) than np.histogram(). So stick with OpenCV function.'''


# ---------------
# plot绘制直方图
# ---------------

# 一、matplotlib
# 直接find and plot
img = cv2.imread('../../img3.jpg',0)
plt.hist(img.ravel(),256,[0,256]); plt.show()

# hist → plot
img = cv2.imread('../../img3.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()


# 二、opencv 比较麻烦


# -------------------
# mask
# -------------------

img = cv2.imread('../../img3.jpg',0)
# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)
# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])
plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask,color='g')
plt.xlim([0,256])
plt.show()

