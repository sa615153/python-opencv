# -*- coding: utf-8 -*-
import cv2

#  BGR <-> Gray and BGR <-> HSV
# HSV可以更具体的知道颜色信息
# cv2.cvtColor(input_image, flag)
# flags
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print flags

