# -*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../messi5.jpg')
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (50,50,450,290)
# 函数的返回值是更新的 mask, bgdModel, fgdModel
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

# cv2.GC_BGD, cv2.GC_FGD, cv2.GC_PR_BGD, cv2.GC_PR_FGD
# 0 2 → 0， 1 3 → 1
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img),plt.colorbar(),plt.show()

#

# manual part

# 使用图像编辑软件打开输入图像，添加一个图层，使用笔刷工具在需要的地方使用白色绘制（比如头发，鞋子，球等）；
# 使用黑色笔刷在不需要的地方绘制（比如， logo，草地等）。然后将其他地方用灰色填充，保存成新的掩码图像。
# 在 OpenCV 中导入这个掩模图像，根据新的掩码图像对原来的掩模图像进行编辑。

# newmask is the mask image I manually labelled
newmask = cv2.imread('newmask.png',0)

# whereever it is marked white (sure foreground), change mask=1
# whereever it is marked black (sure background), change mask=0
mask[newmask == 0] = 0
mask[newmask == 255] = 1

mask, bgdModel, fgdModel = cv2.grabCut(img,mask,None,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_MASK)

mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask[:,:,np.newaxis]
plt.imshow(img),plt.colorbar(),plt.show()