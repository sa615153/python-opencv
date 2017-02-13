# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt
print 1
img = cv2.imread('img1.jpg',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('img3.jpg',cv2.IMREAD_GRAYSCALE)

# cv2.namedWindow('image',cv2.WINDOW_NORMAL)
# cv2.imwrite('flower.jpg',img)
what1 = cv2.imshow('image',img)
what2 = cv2.imshow('image2',img2)
# show 两个窗口
print type(what1)
print type(what2)

k = cv2.waitKey(0)

print 'aft waitkey'  # 要等esc后才执行
cv2.destroyWindow(what1)  # 没用，因为waitKey是同步函数


if k == 27: # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()



# cv2.destroyAllWindows()