#!/usr/bin/env python3
# Author Zuxing Gu
import time


def printName(x):
    time_format = "%Y-%m-%d %X"
    time_current = time.strftime(time_format)
    print("{0}: hello {1}".format(time_current, x))
    return "hello " + x


def testargs(x, *a):
    print(x)
    print(a)


def testkwargs(**kwargs):
    print(kwargs)


def add(x, y, f):
    return f(x) + f(y)


def f(x):
    return abs(x)


strResult = printName("Tom")
print(strResult)

testargs(1, [{1: 2}, {'a': 'b'}])
testkwargs(name='tom', age='8', gender='M')

print(add(-1, 2, f))
