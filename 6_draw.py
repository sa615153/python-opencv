import numpy as np
import cv2

img=np.zeros((512,512,3),np.uint8)


cv2.line(img,(0,0),(511,511),(255,0,0),5)
# cv2.imshow('512',img)
# cv2.waitKey(0)
##################################################

img2 = cv2.imread('img3.jpg',cv2.IMREAD_COLOR)

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.line(img2,(0,0),(511,511),(255,0,0),5)
cv2.rectangle(img2,(384,0),(510,128),(0,255,0),3)
cv2.circle(img2,(447,63), 63, (0,0,255), -1)
cv2.imshow('512',img2)
cv2.waitKey(0)