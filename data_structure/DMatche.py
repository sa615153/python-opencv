# -*- coding: utf-8 -*-
import cv2


# arg1:比较距离方法  arg2:若为true，则match(i,j),j是i的最佳匹配，i也是j的最佳匹配
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance.  ascend, small distance first
matches = sorted(matches, key = lambda x:x.distance)
# DMatch.distance - Distance between descriptors. The lower, the better it is.
# DMatch.trainIdx - Index of the descriptor in train descriptors
# DMatch.queryIdx - Index of the descriptor in query descriptors
# DMatch.imgIdx - Index of the train image.
