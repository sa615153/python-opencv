# -*- coding: utf-8 -*-
import numpy as np

objp = np.zeros((6*7,3),np.float32)
print objp
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

# print np.mgrid[0:7,0:6]
#  两排墙，第一排：7摞，每一摞6个数，0一摞，1一摞，2一摞，3一摞，4一摞，5一摞，6一摞        看输出：正常取7行，6列
#          第二排：也是共7摞，每一摞6个数，都是[0,1,2,3,4,5]                                看输出：转置取7行，6列
# print np.mgrid[0:7,0:6].T
# print '---------'
# print np.mgrid[0:7,0:6].T.reshape(-1,2)
print '-'
print objp
