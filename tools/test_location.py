import cv2
from matplotlib import pyplot as plt

img = cv2.imread('first_frame.png',3)

print img.shape
target = img[432:458,190:210]
r = 432
c = 190
w = 20
h = 26
cv2.imshow('first frame',img)
cv2.imshow('target',target)



cv2.waitKey(0)
