import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../messi5.jpg',0)
rows,cols = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(500,500))
# ---------------------------------------------------------

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,400]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst2 = cv2.warpPerspective(img,M,(500,500))
# ---------------------------------------------------------

pts1 = np.float32([[56,65],[368,52],[28,387],[375,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst3 = cv2.warpPerspective(img,M,(500,500))
# ---------------------------------------------------------



plt.subplot(221),plt.imshow(img),plt.title('perspective Input')
plt.subplot(222),plt.imshow(dst),plt.title('Output1')
plt.subplot(223),plt.imshow(dst2),plt.title('Output2')
plt.subplot(224),plt.imshow(dst3),plt.title('Output3')
plt.show()

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()