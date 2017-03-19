# -*- coding: utf-8 -*-
# meidong

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('fly.png',0)
# Create SURF object. You can specify params here or later.
# Here I set Hessian Threshold to 400
surf = cv2.xfeatures2d.SURF_create(400)
# Find keypoints and descriptors directly
kp, des = surf.detectAndCompute(img, None)
print len(kp)

'''在一幅图像中显示699 个关键点太多了。我们把它缩减到50 个再绘制到
图片上。在匹配时，我们可能需要所有的这些特征，不过现在还不需要。所以
我们现在提高Hessian 的阈值。'''
# Check present Hessian threshold
print surf.hessianThreshold
# We set it to some 50000. Remember, it is just for representing in picture.
# In actual cases, it is better to have a value 300-500
surf.hessianThreshold = 50000
# Again compute keypoints and check its number.
kp, des = surf.detectAndCompute(img,None)
print len(kp)

img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
plt.imshow(img2),plt.show()


# 现在我们试一下U-SURF，它不会检测关键点的方向。
# Check upright flag, if it False, set it to True
print surf.upright
surf.upright = True
# Recompute the feature points and draw it
kp = surf.detect(img,None)
img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
plt.imshow(img2),plt.show()

'''所有的关键点的朝向都是一致的。它比前面的快很多。如果你
的工作对关键点的朝向没有特别的要求（如全景图拼接）等，这种方法会更快。'''

# 最后我们再看看关键点描述符的大小，如果是64 维的就改成128 维。

# Find size of descriptor
print surf.descriptorSize()

# That means flag, "extended" is False.
print surf.extended

# So we make it to True to get 128-dim descriptors.
surf.extended = True
kp, des = surf.detectAndCompute(img,None)
print surf.descriptorSize()
print des.shape









