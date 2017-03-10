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
# 方框不变，将原来每个方框的值是相等的，现在里面的值是符合高斯分布的，方框中心的值最大，其余方框根据
# 距离中心元素的距离递减，构成一个高斯小山包
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
# 特点:模糊的同时保留边界
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

