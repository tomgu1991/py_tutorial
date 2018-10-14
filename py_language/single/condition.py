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
