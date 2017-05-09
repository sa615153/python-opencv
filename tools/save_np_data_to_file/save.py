# -*- coding: utf-8 -*-
import numpy as np

l1 = [1,2,3,4,5]
l2 = ['a','b','c','d','e']
t1 = (1,2,3,4,5,6,7)

np.savez_compressed('test.npz',t1=t1,l1=l1)

np.savez('test2',l1=l1)