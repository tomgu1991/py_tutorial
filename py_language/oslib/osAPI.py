#!/usr/bin/env python3
# Author Zuxing Gu

import os

os.system("pwd")
print(os.getcwd())
print(os.pardir)

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
