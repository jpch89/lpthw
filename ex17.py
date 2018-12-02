# -*- coding: utf-8 -*-
# @Author: jpch89
# @Email:  jpch89@outlook.com
# @Date:   2018-07-01 12:25:25
# @Last Modified by:   jpch89
# @Last Modified time: 2018-07-01 16:42:22

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Coping from {from_file} to {to_file}")

# we could do these two on one line, how?
# in_file = open(from_file)
in_file = open(from_file, encoding = 'utf-16')
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()