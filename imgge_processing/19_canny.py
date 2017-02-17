# -*- coding: utf-8 -*-

#
# 1,除噪声 - Noise Reduction,                           5*5 gaussian blur filter
# 2,计算梯度-Finding Intensity Gradient of the Image    用sobel的Gx和Gy
# 3,非极大值抑制 - Non-maximum Suppression
#   So point A is checked with point B and C to see if it forms a local maximum.
#   If so, it is considered for next stage, otherwise, it is suppressed ( put to zero)
# 4,滞后阈值 - Hysteresis Thresholding  ?

# cv2.Canny()
# 第一个参数是输入图像。第二和第三
# 个分别是 minVal 和 maxVal。第三个参数设置用来计算图像梯度的 Sobel
# 卷积核的大小，默认值为 3。最后一个参数是 L2gradient，它可以用来设定
# 求梯度大小的方程。如果设为 True，就会使用我们上面提到过的方程，否则
# 使用方程： Edge−Gradient(G) = |G2 x| + |G2 y| 代替，默认值为 False

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('../messi5.jpg',0)
edges = cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()