# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Create some random colors
def randint():
    color = np.random.randint(0,255,(100,3))
    print color
    print len(color)

def enumerate_():
    print enumerate(['a','b','c','d','e'])
    for i,s in enumerate(['a','b','c','d','e']):
        print i
        print s
        print '-----'



if __name__ == '__main__':
    # enumerate_()
    pass


