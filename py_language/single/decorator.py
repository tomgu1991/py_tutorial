#!/usr/bin/env python3
# Author Zuxing Gu

import time


def timer(f):
    def wrap():
        print("in wrap")
        start = time.time()
        f()
        end = time.time()
        print("time run %s " % (end - start))

    return wrap


@timer
def testSleep():
    print("before sleep")
    time.sleep(2)
    print("in test Sleep")


testSleep()

x = 0


def grandpa():
    x = 1

    def dad():
        x = 2

        def son():
            x = 3
            print(x)

        son()

    dad()


grandpa()


def deco(f):
    def wrapper(x):
        print("in wrapper run f")
        f(x)
        print("end wrapper")

    return wrapper


def hello(x):
    print("hello: %s" % (x))


newHello = deco(hello)
newHello('Tom')
