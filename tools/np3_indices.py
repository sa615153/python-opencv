# -*- coding: utf-8 -*-
import numpy as np

y = np.arange(10,1,-1)
print y
b = y[[3,3,1,8]]  # [ [] ]  整数数列，就是一个数组
print b

# c = y[[1,2],[3,4]]
# print c  # IndexError: too many indices for array








a = np.array(([1,2,3],[4,5,6]),dtype=int)
print a
print a.shape
print "--------------a[[0,1],[1,2]]-------------"
print a[[0,1],[1,2]]   # 多个数组（两个数组），做zip  坐标01  坐标12      a[]里的东西叫组元
print a[(0,1),(1,2)]   # 同上
# In Python, x[(exp1, exp2, ..., expN)] is equivalent to x[exp1, exp2, ..., expN];
# the latter is just syntactic sugar for the former.
# a[3:,[0,2,5]]  # 3行0列，3行2列，3行5列   4行0列，4行2列，4行5列   5行0列，5行2列，5行5列

grid = np.indices(a.shape)
print grid.shape
print grid[0]  # row indices
print grid[1]  # column indices


x = np.arange(20).reshape(5,4)
print x
row, col = np.indices((2, 3))
print "------------row--------------"
print row
print "------------col--------------"
print col

print "-----------------x[row]------------------"
print x[row]
print "---------------x[row,col]----------------"
print x[row,col]
'''
------------row--------------
[[0 0 0]
 [1 1 1]]
------------col--------------
[[0 1 2]
 [0 1 2]]
---------------x[row,col]----------------
[[0 1 2]
 [4 5 6]]
 类似x[[0,0,0,1,1,1],[0,1,2,0,1,2]]做zip，但是是二维结果，有行列信息

'''

print "-------x[[0,0,0,1,1,1],[0,1,2,0,1,2]]-------"
print x[[0,0,0,1,1,1],[0,1,2,0,1,2]]
'''-------x[[0,0,0,1,1,1],[0,1,2,0,1,2]]-------
[0 1 2 4 5 6]'''


print x[1,2]  # 第1行第2列   → 一个数
print x[[1,2],[1,3]]  # 第1行第1列，第2行第3列    → 一维结果
print x[[[1,2],[1,3]]] # 多加一对[]，结果不变，同上

# x[row,col]
print "等效于将两个二维数组做了大zip  \n print x[ [[0, 0, 0], [1, 1, 1]], [[0, 1, 2], [0, 1, 2]] ]"
print x[ [[0, 0, 0], [1, 1, 1]], [[0, 1, 2], [0, 1, 2]] ]
print "等效于横纵切片  print x[:2,:3]"
print x[:2,:3]



'''indices 函数结果类似于取片'''