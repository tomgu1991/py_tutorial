#!/usr/bin/env python3
# Author Zuxing Gu

f = open("fileTest.txt", 'w')

f.write("hello1\n")
f.write("hello2\n")

f.close()

f = open("fileTest.txt", 'a')
f.write("hello3\n")
f.close()

f = open("fileTest.txt", 'r')
for index, content in enumerate(f.readlines()):
    print(index, content.strip())

f.seek(0)
print(f.tell())
print(f.read(5))
print(f.tell())
f.close()
