# -*- coding: utf-8 -*-
# 可能由于阈值设置问题，不是很理想，100,200 时边比较少

# waitkey(5)时只有第一次的阈值0,0保存下来，后续更改无效，waitkey(100)时更改延迟生效

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

def draw_edges(event,x,y,flags,param):
    global l,h
    l = cv2.getTrackbarPos('L', 'edges')
    h = cv2.getTrackbarPos('H', 'edges')
    print "change"
    print l,h


cv2.namedWindow('edges', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('frame', cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('L', 'edges', 0, 255, nothing)
cv2.createTrackbar('H', 'edges', 0, 255, nothing)
cv2.setMouseCallback('edges', draw_edges)
l,h = 100,200
while(1):

    # Take each frame
    _, frame = cap.read()

    cv2.imshow('frame',frame)
    # print l,h
    edges = cv2.Canny(frame, l, h)
    cv2.imshow('edges',edges)
    k = cv2.waitKey(1000) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()