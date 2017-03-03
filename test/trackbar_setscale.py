# -*- coding: utf-8 -*-

import cv2
import numpy as np
hsv_map = np.zeros((180, 256, 3), np.uint8)
cv2.namedWindow('hist',0)
hist_scale = 10


def set_scale(val):
    global hist_scale
    hist_scale = val
cv2.createTrackbar('scale','hist',hist_scale,32,set_scale)  # 一次创建，即使hist_scale以后会变，trackbar的样子也不会变

while(1):
    print hist_scale
    cv2.imshow('hist',hsv_map)
    cv2.waitKey(500)