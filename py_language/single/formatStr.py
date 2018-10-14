#!/usr/bin/env python3
# Author Zuxing Gu

print("hello world")

name = "A"
name2 = name
print(name, name2)

name = "B"
print(name, name2)

name = "谷祖兴"
print(name)
age = 26

info = '''
--- info ---
name = %s
age = %s
''' % (name, age)

print(info)

info2 = '''
--- info2 ---
name:{_name}
age:{_age}
'''.format(_name=name,
           _age=age)
print(info2)

name = input("name:")
info3 = '''
--- info3 {0} ---
name:{0}
age:{1}
'''.format(name,
           age)
print(info3)
