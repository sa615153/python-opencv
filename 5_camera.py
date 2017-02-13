# -*- coding: utf-8 -*-
'''
2017.1.30
'''

import numpy as np
import cv2

cap = cv2.VideoCapture(0)



while(True):
    # capture frame by frame
    ret, frame = cap.read()

    # print cap.get(3)
    # print cap.get(4)
    #
    # cap.set(3,100)
    # cap.set(4,100)

    print 'ret = '+ str(ret)
    # #operations on frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #
    # display result frame
    cv2.imshow('frame',gray)

    # cv2.waitKey()

    if cv2.waitKey(1000)&0xFF ==ord('q'):  # ka yi miao
        break
    #
cap.release()
cv2.destroyAllWindows()
