# -*- coding: utf-8 -*-
import numpy as np

x = np.eye(3)
x = np.array([[0, 0, 0, 1],[1, 0, 0, 0], [0, 0, 1, 0]])


print x

y = np.nonzero(x)
# 横纵维非零坐标数据,,,零行一行二行，三列零列二列
print y

print x[y]

# 二行三列变成三行二列，二列即坐标
print np.transpose(np.nonzero(x))


