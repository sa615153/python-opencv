# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import cv2
import numpy as np

# ---------------
img=np.zeros((500,500,3),np.uint8)
print img

# ---------------
pts=np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)  # 二维数组，并不是点
pts=pts.reshape((-1,1,2))      # ？行1列，每个点两个数据，点
# cv2.polylines(img2,[pts],True,(0,255,255))

# 四个点
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])