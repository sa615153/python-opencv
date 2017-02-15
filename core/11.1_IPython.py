'''
pip install ipython


import cv2
import numpy as np
In [10]: x = 5
In [11]: %timeit y=x**2
10000000 loops, best of 3: 73 ns per loop
In [12]: %timeit y=x*x
10000000 loops, best of 3: 58.3 ns per loop
In [15]: z = np.uint8([5])
In [17]: %timeit y=z*z
1000000 loops, best of 3: 1.25 us per loop
In [19]: %timeit y=np.square(z)
1000000 loops, best of 3: 1.16 us per loop

http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_core/py_optimization/py_optimization.html#additional-resources
'''
