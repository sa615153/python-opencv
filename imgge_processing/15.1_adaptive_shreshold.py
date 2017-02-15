import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../img1.jpg',0)
img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in xrange(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv2.namedWindow('h',cv2.WINDOW_NORMAL)
cv2.imshow('h',th3)
cv2.waitKey(0)

h2=cv2.resize(th3,None,fx=0.25,fy=0.25,interpolation=cv2.INTER_CUBIC)
cv2.imshow('h',h2)
cv2.waitKey(0)
cv2.imwrite('img1.1.jpg',h2)
