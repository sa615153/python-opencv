# -*- coding: utf-8 -*-
import numpy as np
import cv2

img=np.zeros((512,512,3),np.uint8)


cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.imshow('512',img)
cv2.waitKey(0)
##################################################

img2 = cv2.imread('img3.jpg',cv2.IMREAD_COLOR)

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.line(img2,(0,0),(511,511),(255,0,0),5)
cv2.rectangle(img2,(384,0),(510,128),(0,255,0),3)
cv2.circle(img2,(447,63), 63, (0,0,255), -1)
cv2.ellipse(img2,(256,256),(100,50),0,0,180,255,-1)



cv2.imshow('image',img2)
cv2.waitKey(0)

pts=np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts=pts.reshape((-1,1,2))
cv2.polylines(img2,[pts],True,(0,255,255))

cv2.imshow('image',img2)
cv2.waitKey(0)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img2,'opencv',(10,500), font, 4,(255,255,255),2)

cv2.imshow('image',img2)
cv2.waitKey(0)
