#!/usr/bin/env python3
# Author Zuxing Gu

import os
import sys

print(sys.argv)

print(sys.path)

# run first, save the result
cmd_str = os.system("ls -l")
print("ls -l: \n", cmd_str)

print("make a new dir: test_dir")
os.mkdir("test_dir")

print("make a new dir: test_dir_root/test_dir_leaf")
os.makedirs("test_dir_root/test_dir_leaf")
