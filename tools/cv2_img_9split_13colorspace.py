# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img1.jpg')
b,g,r = cv2.split(img)

img2 = cv2.merge([r,g,b])

##
plt.subplot(121);plt.imshow(img) # expects distorted color
plt.subplot(122);plt.imshow(img2) # expect true color
plt.show()

cv2.imshow('bgr image',img) # expects true color
cv2.imshow('rgb image',img2) # expects distorted color
cv2.waitKey(0)
cv2.destroyAllWindows()




img3 = img[:,:,::-1]
img4 = img[..., ::-1]
img5 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

rows,cols = img.shape[:2]
print rows, cols



'''
img3 = cv2.imread('../../bounding_rec3.png',3)
[[[0 0 0]
  [0 0 0]
  [0 0 0]
  ...,
  [0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]
  ...,
  [0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]
  ...,
  [0 0 0]
  [0 0 0]
  [0 0 0]]

 ...,
 [[0 0 0]
  [0 0 0]
  [0 0 0]
  ...,
  [0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]
  ...,
  [0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]
  ...,
  [0 0 0]
  [0 0 0]
  [0 0 0]]]

（行列可能相反）
每个[[]]是一行像素，行内每个元素都有三个值，类似于树立起来的一排墙
多个[[]]就是多个墙，最后变成一个，大平面，大平面每个元素都有3值高


img = cv2.imread('../../bounding_rec3.png',0)
[[0 0 0 ..., 0 0 0]
 [0 0 0 ..., 0 0 0]
 [0 0 0 ..., 0 0 0]
 ...,
 [0 0 0 ..., 0 0 0]
 [0 0 0 ..., 0 0 0]
 [0 0 0 ..., 0 0 0]]

（行列可能相反）
每个[]是一行像素，每个值是灰度，是一条线
多个[]就是多条线，最后变成一个大平面，大平面每个元素只有1值高


range(defects.shape[0])
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]








'''