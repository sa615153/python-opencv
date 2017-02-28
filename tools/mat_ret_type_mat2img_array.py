# -*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt
from cStringIO import StringIO

img = cv2.imread('../img3.jpg',0)
ret = plt.hist(img.ravel(),256,[0,256])
print type(ret)
# print ret


# cv2.imshow('plt',ret)
# cv2.waitKey(0)
# TypeError: mat is not a numerical tuple



# plt.show()  # show 完之后就没办法后续显示了

buffer_ = StringIO()
plt.savefig( buffer_, format = "png", bbox_inches = 'tight', pad_inches = 0 )
buffer_.seek(0)

img_array = np.asarray(bytearray(buffer_.read()), dtype=np.uint8)

# new = cv2.imdecode(buffer_,0)  #  TypeError: buf is not a numpy array, neither a scalar


new = cv2.imdecode(img_array,3)
cv2.imshow('buffer_',new)
cv2.waitKey(0)


















'''

import cv2
import numpy as np
from urllib2 import urlopen
from cStringIO import StringIO

def create_opencv_image_from_stringio(img_stream, cv2_img_flag=0):
    img_stream.seek(0)
    img_array = np.asarray(bytearray(img_stream.read()), dtype=np.uint8)
    return cv2.imdecode(img_array, cv2_img_flag)

def create_opencv_image_from_url(url, cv2_img_flag=0):
    request = urlopen(url)
    img_array = np.asarray(bytearray(request.read()), dtype=np.uint8)
    return cv2.imdecode(img_array, cv2_img_flag)

    '''