# -*- coding: utf-8 -*-
'''
2017.1.30
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)



while(True):
    # capture frame by frame
    ret, frame = cap.read()

    print 'ret = '+ str(ret)
    # #operations on frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #
    # display result frame
    plt.imshow(color)

    plt.xticks([])
    plt.yticks([])
    plt.show()
    # plt.pause(5)

cap.release()
cv2.destroyAllWindows()
