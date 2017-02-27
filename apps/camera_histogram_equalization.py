# -*- coding: utf-8 -*-
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(gray)

    res = np.hstack(( gray, equ))
    cv2.imshow('res',res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

# inrange
# For every element of a single-channel input array:
# dst(I) = lowerb(I) <= src(i) <= upperb(I)   符合为1（白），不符合为0（黑）



