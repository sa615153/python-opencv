# -*- coding: utf-8 -*-
import cv2
import numpy as np
import time

cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
cap = cv2.VideoCapture('../../calibration_img/后置大格.mp4')
print cap.isOpened()
while(cap.isOpened()):
    ret, frame = cap.read()



    # # rotate
    # rows, cols, depth= frame.shape
    # print rows,cols,depth
    # M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
    # dest = cv2.warpAffine(frame, M, (cols, rows))
    # rows, cols, depth = dest.shape
    # print rows, cols, depth




    cv2.imshow('frame', frame)
    k = cv2.waitKey(0)
    if k & 0xFF == ord('q') or k==27:
        break
    if k == ord('s'):
        cv2.imwrite('./output/{0}.png'.format(str(time.time())[0:-3]), frame)

cap.release()
cv2.destroyAllWindows()