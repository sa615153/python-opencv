# -*- coding: utf-8 -*-
'''
2017.1.30
'''

import numpy as np
import cv2

# cap = cv2.VideoCapture('C:/Users/JPang3/Desktop/beijing/opencv/opencv_projects/python-opencv/wildlife.wmv')
cap = cv2.VideoCapture('I:\USTC\PycharmProjects\opencv-python-book/a.mp4')
print cap.isOpened()
while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.imwrite('first_frame.png',frame)
        break

cap.release()
cv2.destroyAllWindows()
