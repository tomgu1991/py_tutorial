#!/usr/bin/env python3
# Author Zuxing Gu

print(all([1, 0]))
print(any([1, 0]))
print(ascii([1, 2, '3', '古']))
print(bin(6))
print(chr(98))
print(ord('b'))

a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]
zipped = zip(a, b)
print(tuple(zipped))
zipped = zip(a, c)
print(tuple(zipped))
