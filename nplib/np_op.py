#!/usr/bin/env python3
# Author Zuxing Gu

import numpy as np

# Elementwise operations
a = np.array([1, 2, 3, 4])
print(a + 1)  # array([2, 3, 4, 5])
c = np.ones((3, 3))
# matrix
print(c.dot(c))  # all 3
print(c * c)  # all 1

a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
print(a == b)  # array([False, True, False, True], dtype=bool)
print(a > b)  # array([False, False,  True, False], dtype=bool)

a = np.array([1, 1, 0, 0], dtype=bool)
b = np.array([1, 0, 1, 0], dtype=bool)
np.logical_or(a, b)
# array([ True, True, True, False], dtype=bool)
np.logical_and(a, b)
# array([ True, False, False, False], dtype=bool)

a = np.triu(np.ones((3, 3)), 1)  # upper triangle of matrix
'''
array([[ 0., 1., 1.],
       [ 0., 0., 1.],
       [ 0.,  0.,  0.]])
'''
a.T
'''
array([[ 0., 0., 0.],
       [ 1.,  0.,  0.],
       [ 1.,  1.,  0.]])
'''

# reduction
x = np.array([1, 2, 3, 4])
print(np.sum(x))  # 10
print(x.sum())  # 10

x = np.array([[1, 1], [2, 2]])
x.sum(axis=0)  # array([3, 3])
x.sum(axis=1)  # rows (second dimension) array([2, 4])
x = np.array([1, 3, 2])
x.min()
x.max()
print(x.argmax())  # index of max, 1

np.all([True, True, False])
# False
np.any([True, True, False])
# True
a = np.zeros((100, 100))
np.any(a != 0)
# False
np.all(a == a)
# True
a = np.array([1, 2, 3, 2])
b = np.array([2, 2, 3, 2])
c = np.array([6, 4, 4, 5])
((a <= b) & (b <= c)).all()
# True

x = np.array([1, 2, 3, 1])
y = np.array([[1, 2, 3], [5, 6, 1]])
x.mean()
# 1.75
np.median(x)
# 1.5
np.median(y, axis=-1)  # last axis array([ 2., 5.])
x.std()  # full population standard dev. 0.82915619758884995

# broadcasting It’s also possible to do operations on arrays of different sizes if NumPy can transform
# these arrays so that they all have the same size: this conversion is called broadcasting.
a = np.tile(np.arange(0, 40, 10), (3, 1))  # repeat 3x4
a = a.T  # 4*3
'''
array([[ 0,  0,  0],
       [10, 10, 10],
       [20, 20, 20],
       [30, 30, 30]])
'''
a = np.arange(0, 40, 10)
print(a.shape)  # (4,) 1D
a = a[:, np.newaxis]  # (4, 1) 2D
b = np.array([0, 1, 2])
print(a + b)  # 4*3
'''

'''
x, y = np.ogrid[0:5, 0:5]
'''
((5, 1), (1, 5))
'''
x, y = np.mgrid[0:4, 0:4]
'''
>>> x
array([[0, 0, 0, 0],
       [1, 1, 1, 1],
       [2, 2, 2, 2],
       [3, 3, 3, 3]])
>>> y
array([[0, 1, 2, 3],
       [0, 1, 2, 3],
       [0, 1, 2, 3],
       [0, 1, 2, 3]])
'''

# shape
a = np.array([[1, 2, 3], [4, 5, 6]])
a.ravel()  # array([1, 2, 3, 4, 5, 6])
a = np.arange(4 * 3 * 2).reshape(4, 3, 2)
a.shape  # 4, 3, 2
a = np.arange(4)
a.resize((8,))  # array([0, 1, 2, 3, 0, 0, 0, 0])

# sort
a = np.array([[4, 3, 5], [1, 2, 1]])
b = np.sort(a, axis=1)  # 3 4 5 , 1 1 2
a = np.array([4, 3, 1, 2])
j = np.argsort(a)  # 2 3 1 0
print(a[j])  # 1 2 3 4

# type
a = np.array([1.7, 1.2, 1.6])
b = a.astype(int)  # <-- truncates to integer
a = np.array([1.2, 1.5, 1.6, 2.5, 3.5, 4.5])
b = np.around(a)  # still floating-point array([ 1., 2., 2., 2., 4., 4.])

samples = np.zeros((6,), dtype=[('sensor_code', 'S4'), ('position', float), ('value', float)])
samples.ndim  # 1
samples.shape  # 6,
samples.dtype.names  # ('sensor_code', 'position', 'value')
samples[:] = [('ALFA', 1, 0.37), ('BETA', 1, 0.11), ('TAU', 1, 0.13), ('ALFA', 1.5, 0.37), ('ALFA', 3, 0.11),
              ('TAU', 1.2, 0.13)]
samples['sensor_code']
# array(['ALFA', 'BETA', 'TAU', 'ALFA', 'ALFA', 'TAU'], dtype='|S4')
samples['value']
# array([ 0.37, 0.11, 0.13, 0.37, 0.11, 0.13])
samples[0]
# ('ALFA', 1.0, 0.37)
samples[0]['sensor_code'] = 'TAU'
samples[0]
# ('TAU', 1.0, 0.37)


# poly
# 3x2 +2x −1:
p = np.poly1d([3, 2, -1])
print(p(0))  # -1
print(p.roots)  # array([-1. ,  0.33333333])
p.order  # 2
