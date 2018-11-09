#!/usr/bin/env python3
# Author Zuxing Gu

import matplotlib.pyplot as plt
import numpy as np

plt.rc('text', usetex=False)
a = np.outer(np.arange(0, 1, 0.01), np.ones(10))
plt.figure(figsize=(10, 5))
plt.subplots_adjust(top=0.8, bottom=0.05, left=0.01, right=0.99)
maps = [m for m in plt.cm.datad if not m.endswith("_r")]
maps.sort()
l = len(maps) + 1
for i, m in enumerate(maps):
    plt.subplot(1, l, i + 1)
    plt.axis("off")
    plt.imshow(a, aspect='auto', cmap=plt.get_cmap(m), origin="lower")
    plt.title(m, rotation=90, fontsize=10, va='bottom')
plt.show()


# line
def linestyle(ls, i):
    X = i * .5 * np.ones(11)
    Y = np.arange(11)
    plt.plot(X, Y, ls, color=(.0, .0, 1, 1), lw=3, ms=8,
             mfc=(.75, .75, 1, 1), mec=(0, 0, 1, 1))
    plt.text(.5 * i, 10.25, ls, rotation=90, fontsize=15, va='bottom')


linestyles = ['-', '--', ':', '-.', '.', ',', 'o', '^', 'v', '<', '>', 's',
              '+', 'x', 'd', '1', '2', '3', '4', 'h', 'p', '|', '_', 'D', 'H']
n_lines = len(linestyles)
size = 20 * n_lines, 300
dpi = 72.0
figsize = size[0] / float(dpi), size[1] / float(dpi)
fig = plt.figure(figsize=figsize, dpi=dpi)
plt.axes([0, 0.01, 1, .9], frameon=False)
for i, ls in enumerate(linestyles):
    linestyle(ls, i)
plt.xlim(-.2, .2 + .5 * n_lines)
plt.xticks(())
plt.yticks(())
plt.show()


# marker
def marker(m, i):
    X = i * .5 * np.ones(11)
    Y = np.arange(11)
    plt.plot(X, Y, lw=1, marker=m, ms=10, mfc=(.75, .75, 1, 1),
             mec=(0, 0, 1, 1))
    plt.text(.5 * i, 10.25, repr(m), rotation=90, fontsize=15, va='bottom')


markers = [0, 1, 2, 3, 4, 5, 6, 7, 'o', 'h', '_', '1', '2', '3', '4',
           '8', 'p', '^', 'v', '<', '>', '|', 'd', ',', '+', 's', '*',
           '|', 'x', 'D', 'H', '.']
n_markers = len(markers)
size = 20 * n_markers, 300
dpi = 72.0
figsize = size[0] / float(dpi), size[1] / float(dpi)
fig = plt.figure(figsize=figsize, dpi=dpi)
plt.axes([0, 0.01, 1, .9], frameon=False)
for i, m in enumerate(markers):
    marker(m, i)
plt.xlim(-.2, .2 + .5 * n_markers)
plt.xticks(())
plt.yticks(())
plt.show()
