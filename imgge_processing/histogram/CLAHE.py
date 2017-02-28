# -*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt


'''对每一个小块分别进行直方图均衡化（跟前面类似）。
所以在每一个的区域中，直方图会集中在某一个小的区域中（除非有噪声干
扰）。

如果有噪声的话，噪声会被放大。
为了避免这种情况的出现要使用对比度限制。对于每个小块来说，如果直方图中的 bin 超过对比度的上限的话，就把
其中的像素点均匀分散到其他 bins 中，然后在进行直方图均衡化。

最后，为了去除每一个小块之间“人造的”（由于算法造成）边界，再使用双线性差值，对小块进行缝合。'''

img = cv2.imread('../../CLAHE.png',0)
# img_copy = img.copy()

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

cv2.imshow('ori',img)
cv2.imshow('CLACHE',cl1)
cv2.waitKey(0)