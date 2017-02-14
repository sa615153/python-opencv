import numpy as np
import cv2

img = cv2.imread('C:/Users/JPang3/Desktop/beijing/opencv/opencv_projects/python-opencv/messi5.jpg')

ball = img[280:340,330:390]
img[273:333,100:160] = ball


cv2.imshow('img3',img)
cv2.waitKey(0)