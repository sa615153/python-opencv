import numpy as np
list = ['a','b','c','d']
what = enumerate(list)
print what
for i,str in what:
    print i, str


l1 = ['a','b','c','d']
l2 = ['A','B','C','D']
print zip(l1,l2)



color = np.random.randint(0,255,(100,3))
print color
print "lenth = {}".format(len(color))
print color[0]
print type(color[0])