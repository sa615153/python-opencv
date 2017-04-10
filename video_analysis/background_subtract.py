# -*- coding: utf-8 -*-
import numpy as np
import cv2

# cv2.createBackgroundSubtractorMOG()出错，改为了MOG2
# 问题：
# 变化大的是前景，这个原则会导致前景刚刚离开的位置，像素变为背景，这个变化也很大，被高亮显示，但是其实这个高亮属于背景

cap = cv2.VideoCapture('../a.mp4')
# fgbg = cv2.createBackgroundSubtractorMOG() # 不可用
fgbg = cv2.createBackgroundSubtractorMOG2()
while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()



# 不可用
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorGMG()
while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
