#!/usr/bin/env python3
# Author Zuxing Gu

import copy

objs = [1, 2, 3, 4]
print(objs[1:])
print(objs[1:3])
print(objs[-2:])
print(objs[-3:-1])

objs.insert(1, 1.5)
print(objs)

names = ['a', 'b', 'c', ['c1', 'c2'], 'd']
print(names)
names2 = names.copy()
print(names2)
names[0] = 'a1'
names2[3][0] = 'c11'
print(names)
print(names2)

names = ['a', 'b', 'c', ['c1', 'c2'], 'd']
names2 = copy.deepcopy(names)
names[0] = 'a1'
names2[3][0] = 'c11'
print(names)
print(names2)
