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


# Default values are evaluated when the function is defined,
# not when it is called. This can be problematic when using mutable types
# (e.g. dictionary or list) and modifying them in the function body,
# since the modifications will be persistent across invocations of the function.
def double_it(x=2):
    return x * 2


# *args:any number of positional arguments packed into a tuple
# **kwargs:any number of keyword arguments packed into a dictionary
def variable_args(*args, **kwargs):
    print('args is', args)
    print('kwargs is', kwargs)

strResult = printName("Tom")
print(strResult)

testargs(1, [{1: 2}, {'a': 'b'}])
testkwargs(name='tom', age='8', gender='M')

print(add(-1, 2, f))

print(double_it())

x = 5


def setx(y):
    x = y
    print(x)


setx(10)  # 10
print(x)


# x is 5

def setgx(y):
    global x
    x = y
    print(x)


setgx(10)  # 10
# x is 10
print(x)
