# -*- coding: utf-8 -*-

import cv2
import numpy as np

'''
green = np.uint8([0,255,0])
hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)

modules/imgproc/src/color.cpp:3541:
error: (-215) (scn == 3 || scn == 4) && (depth == CV_8U || depth == CV_32F)
in function cvtColor
#scn (the number of channels of the source),
#i.e. self.img.channels(), is neither 3 nor 4.
#
#depth (of the source),
#i.e. self.img.depth(), is neither CV_8U nor CV_32F.
# 所以不能用 [0,255,0]，而要用 [[[0,255,0]]]
# 这里的三层括号应该分别对应于 cvArray， cvMat， IplImage
'''

green=np.uint8([[[0,255,0]]])
hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print hsv_green

'''
 take [H-10, 100,100] and [H+10, 255, 255] as lower bound and upper bound respectively.
 Apart from this method, you can use any image editing tools like GIMP or any online converters to find these values,
 but don’t forget to adjust the HSV ranges
'''