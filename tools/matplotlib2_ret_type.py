# -*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../img3.jpg',0)
ret = plt.hist(img.ravel(),256,[0,256])
print type(ret)
print ret


# cv2.imshow('plt',ret)
# cv2.waitKey(0)
# TypeError: mat is not a numerical tuple


fig = plt.figure()
fig.add_subplot(111)
# If we haven't already shown or saved the plot, then we need to
# draw the figure first...
fig.canvas.draw()

# Now we can save it to a numpy array.
data = np.fromstring(ret.canvas.tostring_rgb(), dtype=np.uint8, sep='')
# data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))

cv2.imshow('t',data)
cv2.waitKey(0)