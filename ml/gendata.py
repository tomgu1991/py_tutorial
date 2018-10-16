#!/usr/bin/env python3
# Author Zuxing Gu

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer

import mglearn

# generate dataset
X, y = mglearn.datasets.make_forge()

mglearn.discrete_scatter(X[:, 0], X[:, 1], y)

# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html
# Place a legend on the axes. Loc=location
plt.legend(["Class 0", "Class 1"], loc=4)
plt.xlabel("First feature")
plt.ylabel("Second feature")
plt.show()
print("X.shape:", X.shape)

X, y = mglearn.datasets.make_wave(n_samples=40)
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html?highlight=plot#matplotlib.pyplot.plot
# Plot y versus x as lines and/or markers. 'color-marker-line'
plt.plot(X, y, 'ro')
plt.ylim(-3, 3)
plt.xlabel("Feature")
plt.ylabel("Target")
plt.show()

# cancer data
cancer = load_breast_cancer()
print("cancer.keys():\n", cancer.keys())
# dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names', 'filename'])
# bincount: Count number of occurrences of each value in array of non-negative ints.
# zip: [1,2,3] [4,5,6] -> [(1,2),(3,4),(5,6)]
print("Sample counts per class:\n",
      {n: v for n, v in zip(cancer.target_names, np.bincount(cancer.target))})
# {'malignant': 212, 'benign': 357}
