# -*- coding: utf-8 -*-

'''OpenCV 提供了函数： cv2.goodFeaturesToTrack()。这个函数可以
帮我们使用 Shi-Tomasi 方法获取图像中 N 个最好的角点（如果你愿意的话，
也可以通过改变参数来使用 Harris 角点检测算法）。通常情况下，输入的应该
是灰度图像。然后确定你想要检测到的角点数目。再设置角点的质量水平， 0
到 1 之间。它代表了角点的最低质量，低于这个数的所有角点都会被忽略。最
后在设置两个角点之间的最短欧式距离。
根据这些信息，函数就能在图像上找到角点。所有低于质量水平的角点都
会被忽略。然后再把合格角点按角点质量进行降序排列。函数会采用角点质量
最高的那个角点（排序后的第一个），然后将它附近（最小距离之内）的角点都
删掉。按着这样的方式最后返回 N 个最佳角点'''

import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('../subpix_accuracy.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 找出10个最佳角点
corners = cv2.goodFeaturesToTrack(gray,10,0.01,10)
# 返回的结果是 [[ 311., 250.]] 两层括号的数组。

# np.int0 可以用来省略小数点后面的数字（非四舍五入）。
corners = np.int0(corners)
for i in corners:
    print i,i.ravel()
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)
plt.imshow(img),plt.show()

