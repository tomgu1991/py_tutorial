#!/usr/bin/env python3
# Author Zuxing Gu

import os

os.system("pwd")
print(os.getcwd())
print(os.pardir)
print(os.listdir(os.curdir))

# os.rename(old, new)
# os.rmdir(name)

# path
# os.path.abspath/split/dirname/basename/splittext/exists/isfile/isdir(name)

for dirpath, dirnames, filenames in os.walk(os.curdir):
    for fp in filenames:
        print(os.path.abspath(fp))

strdir = './newDir'
strMulDir = './mul1/mul2/mul3'
strPath = strdir + "/newFile.txt"
if os.path.isdir(strdir):
    pass
else:
    os.mkdir(strdir)

if os.path.isdir(strMulDir):
    pass
else:
    os.makedirs(strMulDir)
