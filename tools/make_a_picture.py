# -*- coding: utf-8 -*-

import numpy as np
import cv2

i = cv2.imread('../img3.jpg',3)

row = i.shape[0]
col = i.shape[1]


img=np.zeros((row,col,3),np.uint8)

cv2.imshow('new picture',img)
k = cv2.waitKey(0)
if k == 27: # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('new_picture.jpg',img)
    cv2.destroyAllWindows()