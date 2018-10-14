#!/usr/bin/env python3
# Author Zuxing Gu

# import XXX - __init__.py can be used
# import XXX.YYY - YYY can be used as XXX.YYY
# from XXX import YYY - YYY can be used as YYY


from .RoleClass import Role

from .school import Student


class Dog(object):
    def __init__(self, name):
        self.name = name

    @staticmethod  # 把eat方法变为静态方法
    def eat(self):
        print("%s is eating" % self.name)

    def __str__(self):
        return "str"


d = Dog("ChenRocha")
d.eat(d)
print(d)

r1 = Role('Tom', 'AK47')
r1.shot()

s1 = Student("Tsinghua", 24, "Python S12", 1483)
s1.tell()
