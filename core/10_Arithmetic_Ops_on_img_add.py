import numpy as np
import cv2

x = np.uint8([250])
y = np.uint8([10])

print cv2.add(x,y)
print x+y

#Both images should be of same depth and type, or second image can just be a scalar value. size have to be same


img1=cv2.imread('C:/Users/JPang3/Desktop/beijing/opencv/opencv_projects/python-opencv/opencv_logo1.png')
img2=cv2.imread('C:/Users/JPang3/Desktop/beijing/opencv/opencv_projects/python-opencv/img3.png')

dst1 = cv2.add(img1,img2)
cv2.imshow('dst',dst1)
cv2.waitKey(0)

dst=cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()