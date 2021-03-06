# -*- coding: utf-8 -*-
import numpy as np

a = np.arange(16).reshape(2, 2, 2, 2)

'''
numpy.clip

numpy.clip(a, a_min, a_max, out=None)[source]
Clip (limit) the values in an array.

Given an interval, values outside the interval are clipped to the interval edges. For example, if an interval of [0, 1]
 is specified, values smaller than 0 become 0, and values larger than 1 become 1.

Parameters:
a : array_like
Array containing elements to clip.
a_min : scalar or array_like
Minimum value.
a_max : scalar or array_like
Maximum value. If a_min or a_max are array_like, then they will be broadcasted to the shape of a.
out : ndarray, optional
The results will be placed in this array. It may be the input array for in-place clipping. out must be of the right shape to hold the output. Its type is preserved.
Returns:
clipped_array : ndarray
An array with the elements of a, but where values < a_min are replaced with a_min, and those > a_max with a_max.
See also
numpy.doc.ufuncs
Section “Output arguments”
Examples

>>>
>>> a = np.arange(10)
>>> np.clip(a, 1, 8)
array([1, 1, 2, 3, 4, 5, 6, 7, 8, 8])
>>> a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> np.clip(a, 3, 6, out=a)
array([3, 3, 3, 3, 4, 5, 6, 6, 6, 6])
>>> a = np.arange(10)
>>> a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> np.clip(a, [3,4,1,1,1,4,4,4,4,4], 8)
array([3, 4, 2, 3, 4, 5, 6, 7, 8, 8])'''









a[...,2]

'''The ellipsis is used to slice higher-dimensional data structures.

It's designed to mean at this point, insert as many full slices (:) to extend the multi-dimensional slice to all dimensions.

Example:

>>> from numpy import arange
>>> a = arange(16).reshape(2,2,2,2)
Now, you have a 4-dimensional matrix of order 2x2x2x2. To select all first elements in the 4th dimension, you can use the ellipsis notation

>>> a[..., 0].flatten()
array([ 0,  2,  4,  6,  8, 10, 12, 14])
which is equivalent to

>>> a[:,:,:,0].flatten()
array([ 0,  2,  4,  6,  8, 10, 12, 14])
In your own implementations, you're free to ignore the contract mentioned above and use it for whatever you see fit.'''