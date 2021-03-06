# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt
from cStringIO import StringIO

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(gray)


    plt.hist(frame.ravel(), 256, [0, 256])
    buffer_ = StringIO()
    plt.savefig(buffer_, format="png", bbox_inches='tight', pad_inches=0)
    buffer_.seek(0)
    img_array = np.asarray(bytearray(buffer_.read()), dtype=np.uint8)
    hist = cv2.imdecode(img_array, 0)

    cv2.imshow('hist',hist)

    res = np.hstack(( gray, equ))  # stacking images side-by-side
    cv2.imshow('res',res)

    k = cv2.waitKey(1000) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

# inrange
# For every element of a single-channel input array:
# dst(I) = lowerb(I) <= src(i) <= upperb(I)   符合为1（白），不符合为0（黑）



