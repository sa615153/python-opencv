import cv2
from matplotlib import pyplot as plt

img = cv2.imread('first_frame.png',3)

print img.shape
target = img[438:452,198:206]
# r = 432
# c = 190
# w = 20
# h = 26

r = 438
c = 198
w = 8
h = 14
cv2.imshow('first frame',img)
cv2.imshow('target',target)



cv2.waitKey(0)
