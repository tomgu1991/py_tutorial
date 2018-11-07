#!/usr/bin/env python3
# Author Zuxing Gu

import matplotlib.pyplot as plt

img = plt.imread('../resource/elephant.png')
print(img.shape, img.dtype)

plt.imshow(img)
plt.show()

plt.imsave('red_elephant.png', img[:, :, 0], cmap=plt.cm.gray)  # red chanel only
