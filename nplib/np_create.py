#!/usr/bin/env python3
# Author Zuxing Gu

import numpy as np

'''
https://docs.scipy.org/doc/
Memory-efficient container that provides fast numerical operations.
'''
a = np.array([0, 1, 2, 3])
print(a.ndim)  # 1, dimensions
print(a.shape)  # (4,) Tuple of array dimensions
print(len(a))  # 4

b = np.array([[0, 1, 2], [3, 4, 5]])
print(b.ndim)  # 2
print(b.shape)  # (2, 3)
print(len(b))  # 2, return the size of the first dimension

# creating array
a = np.arange(10)  # 0-n-1
b = np.arange(1, 9, 2)  # 1 3 5 7
c = np.linspace(0, 1, 6)  # start, end, num-points
d = np.linspace(0, 1, 5, endpoint=False)  # array([ 0. , 0.2, 0.4, 0.6, 0.8])

a = np.ones((3, 3))  # all 1
b = np.zeros((2, 2))  # all 0
c = np.eye(3)  # 100 010 001
d = np.diag(np.array([1, 2, 3, 4]))  # build a 2d array
e = np.diag(c, k=0)  # [1, 1, 1] extract from 2d by level k
f = np.diag(np.arange(1, 10).reshape(3, 3), k=1)  # [2, 6]
print(f)
g = np.random.rand(4)  # uniform in [0, 1]
h = np.random.randn(4)  # Gaussian

c = np.array([1, 2, 3], dtype=float)
d = np.array([1 + 2j, 3 + 4j, 5 + 6 * 1j])
e = np.array([True, False, False, True])
f = np.array(['Bonjour', 'Hello', 'Hallo', ])  # dtype('S7'), strings containing max 7 letters

# indexing and slicing
a = np.arange(10)
print(a[0])  # 0
print(a[::-1])  # reverse
a = np.diag(np.arange(3))
print(a[1, 1])  # 1
a[2, 1] = 10
print(a[2])  # [ 0 10  2]
a = np.arange(10)
a[5:] = 10  # array([ 0, 1, 2, 3, 4, 10, 10, 10, 10, 10])
b = np.arange(5)
a[5:] = b[::-1]  # array([0, 1, 2, 3, 4, 4, 3, 2, 1, 0])
'''
A slicing operation creates a view on the original array, which is just a way of accessing array data. 
'''
a = np.arange(10)
b = a[::2]
print(np.may_share_memory(a, b))  # True
c = a[::2].copy()
print(np.may_share_memory(a, c))  # False

# fancy indexing
a = np.random.randint(0, 21, 15)
extract_from_a = a[(a % 3 == 0)]  # 0 0 6 0
a[a % 3 == 0] = -1  # assign to -1
a = np.arange(0, 100, 10)
print(a[[2, 3]])  # array([20, 30])
