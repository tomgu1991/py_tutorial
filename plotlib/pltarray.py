#!/usr/bin/env python3
# Author Zuxing Gu

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3, 20)
y = np.linspace(0, 9, 20)
plt.plot(x, y)  # line plot
plt.show()
plt.plot(x, y, 'o')  # dot plot
plt.show()

image = np.random.rand(30, 30)
plt.imshow(image, cmap=plt.cm.hot)  # hot plot
plt.colorbar()
plt.show()

np.random.seed(12)
x = np.linspace(0, 1, 20)
y = np.cos(x) + 0.3 * np.random.rand(20)
p = np.poly1d(np.polyfit(x, y, 3))
t = np.linspace(0, 1, 200)
plt.plot(x, y, 'o', t, p(t), '-')
plt.show()
