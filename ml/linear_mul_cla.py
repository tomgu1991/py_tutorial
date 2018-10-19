#!/usr/bin/env python3
# Author Zuxing Gu

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.svm import LinearSVC

X, y = make_blobs(random_state=42)
co = ['ro', 'y^', 'bv']
for a, b, c in zip(X[:, 0], X[:, 1], y):
    plt.plot(a, b, co[c])

linear_svm = LinearSVC().fit(X, y)
print("Coefficient shape: {}".format(linear_svm.coef_.T))
print("Intercept shape: {}".format(linear_svm.intercept_.T))
'''
Coefficient shape: [[-0.17492497  0.47621415 -0.18914147]
 [ 0.2314118  -0.06937507 -0.20400561]]
Intercept shape: [-1.07745203  0.13140457 -0.08605001]
'''

line = np.linspace(-15, 15)
for coef, intercept, color in zip(linear_svm.coef_, linear_svm.intercept_,
                                  ['b', 'r', 'y']):
    plt.plot(line, -(line * coef[0] + intercept) / coef[1], c=color)
plt.ylim(-10, 15)
plt.xlim(-10, 8)
plt.xlabel("Feature 0")
plt.ylabel("Feature 1")
plt.legend(['Class 0', 'Class 1', 'Class 2', 'Line class 0', 'Line class 1',
            'Line class 2'], loc=(1.01, 0.3))
plt.show()
