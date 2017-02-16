# -*- coding: utf-8 -*-


import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('../tmp.jpg')

# 平均
blur = cv2.blur(img,(5,5))

# -----------------------------------------------------------
plt.subplot(121),plt.imshow(img),plt.title('Original')      #
plt.xticks([]), plt.yticks([])                              #
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')      #
plt.xticks([]), plt.yticks([])                              #
plt.show()                                                  #
# -----------------------------------------------------------

# 高斯
blur = cv2.GaussianBlur(img,(5,5),0)

# -----------------------------------------------------------
plt.subplot(121),plt.imshow(img),plt.title('Original')      #
plt.xticks([]), plt.yticks([])                              #
plt.subplot(122),plt.imshow(blur),plt.title('gaussian_blur')#
plt.xticks([]), plt.yticks([])                              #
plt.show()                                                  #
# -----------------------------------------------------------

# 中值模糊/滤波
# 窗口中的某个像素取代中心值，中值
median = cv2.medianBlur(img,5)

# -----------------------------------------------------------
plt.subplot(121),plt.imshow(img),plt.title('Original')      #
plt.xticks([]), plt.yticks([])                              #
plt.subplot(122),plt.imshow(median),plt.title('median blur')#
plt.xticks([]), plt.yticks([])                              #
plt.show()                                                  #
# -----------------------------------------------------------

# 双边过滤
# only those pixels with intensities similar to that of the central pixel (‘intensity neighbors’) are included to compute the blurred intensity value
# http://people.csail.mit.edu/sparis/bf_course/

blur = cv2.bilateralFilter(img,9,75,75)

# -----------------------------------------------------------
plt.subplot(121),plt.imshow(img),plt.title('Original')      #
plt.xticks([]), plt.yticks([])                              #
plt.subplot(122),plt.imshow(blur),plt.title('bilateral')#
plt.xticks([]), plt.yticks([])                              #
plt.show()                                                  #
# -----------------------------------------------------------

