#!/usr/bin/env python3
# Author Zuxing Gu

def print_sorted(collection):
    try:
        collection.sort()
    except AttributeError:
        print("wrong type")
    print(collection)


print_sorted([1, 3, 2])
print_sorted('123')
