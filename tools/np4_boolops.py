# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import cv2

a = np.arange(10)
b = a > 5
print b


a = np.array(([1,2,3,6,5],[2,3,6,4,3],[2,6,3,3,3],[6,2,2,2,2],[2,2,2,2,6]),dtype=int)
print '---a---这是个二维'
print a
b = a > 5
print '---b=a>5---'
print '---b---'
print b

print '---a[b]---这是个视图,一维'
print a[b]
a[b] = 100
print 'a[b] = 100  print a'
print a

c = np.where(a >= 10)
print "-----c=np.where(a >= 5)---"
print c
print "---type(c)-----------------"
print type(c)
print "--c[::-1]------------------"
print c[::-1]
print "-------zip(*c[::-1])-------"
print zip(*c[::-1])
# zip(*  内部zip




img = cv2.imread('../2Dhist.png')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# cv2.imshow('img',img)
# cv2.waitKey(0)
print "------------hsv[...,2]---------------"
print hsv[...,2]  # 这其实是个二维数组,hsv[...,2]类比a
dark = hsv[...,2] < 32  # 二维bool数组，，，hsv[...,2]类比a
print "---------------dark------------二维bool数组----"
print dark
print"----------hsv[...,2][dark]----------这是个视图,一维"
print hsv[...,2][dark]  #hsv[...,2][dark]类似于用坐标取原hsv[...,2]的某些值

print "-------------- hsv[dark] = 0---------dark始终是一个二维坐标，所以得到一维视图，每个元素有三个数h,s,v（所以其实是个二维数组）"
print hsv[dark]

hsv[dark] = 0
print "------hsv[dark]=0----print hsv[dark]---------每个元素的三个数都变为0"
print hsv[dark]
print "----------hsv----------------hsv中的一些元素（hsv中v<32的）已被置(0,0,0)"
print hsv


# newaxis

'''
 x1 = np.array([1, 2, 3, 4, 5])
 x2 = np.array([5, 4, 3])

 In [2]: x1_new = x1[:, np.newaxis]    全取第一维（只有这一维），升为行数，，，，元素变为[元素，]
# now, x1_new is (5, 1) 五行一列
'''




print "----------newaxis----------"
a = np.arange(0,25).reshape(5,5)
print a


d = a[:,:,np.newaxis]
print "----------a[:,:,np.newaxis]----------底层墙，但只有这一层，俯视图为原二维数组  / 元素变为[元素，]"
print d