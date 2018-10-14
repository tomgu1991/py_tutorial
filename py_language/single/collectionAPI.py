#!/usr/bin/env python3
# Author Zuxing Gu

list1 = [1, 3, 5, 7, 9, 9]
list2 = [2, 4, 5, 6, 8, 10]

set1 = set(list1)
set2 = set(list2)
print(set1, set2)

print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))
