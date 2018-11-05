#!/usr/bin/env python3
# Author Zuxing Gu

list1 = [1, 3, 5, 7, 9, 9]
list2 = [2, 4, 5, 6, 8, 10]

# set
set1 = set(list1)
set2 = set(list2)
print(set1, set2)
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))

# list
colors = ['red', 'blue', 'green', 'black', 'white']
print(colors[-2])
print(colors[2:4])
print(colors[::2])
colors.append('pink')
colors.pop()
colors.extend(['pink', 'purple'])
colors = colors[:-2]
a = [i ** 2 for i in range(4)]
# reverse
rcolors = colors[::-1]
rcolors2 = list(colors)
rcolors2.reverse()
# repeat
t1 = rcolors2 + colors
t2 = rcolors * 2
# sort
t3 = sorted(rcolors)

# map
tel = {'emmanuelle': 5752, 'sebastian': 5578}
tel['francis'] = 5915
tel.keys()
tel.values()
