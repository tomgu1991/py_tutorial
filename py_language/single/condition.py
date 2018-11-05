#!/usr/bin/env python3
# Author Zuxing Gu


for i in range(0, 10, 2):
    print(i)

number = int(input("input a number:"))
while True:
    if number == 5:
        print("yes")
        break
    else:
        print("no, continue")
        number = int(input("input a number:"))

a = 10
if a == 1:
    print(1)
elif a == 2:
    print(2)
else:
    print('A lot')

words = ('cool', 'powerful', 'readable')
for index, item in enumerate(words):
    print((index, item))

d = {'a': 1, 'b': 1.2, 'c': 1j}
for key, val in sorted(d.items()):
    print('Key: %s has value: %s' % (key, val))
