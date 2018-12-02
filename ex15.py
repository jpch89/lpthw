# -*- coding: utf-8 -*-
# @Author: jpch89
# @Email:  jpch89@outlook.com
# @Date:   2018-07-01 11:40:12
# @Last Modified by:   jpch89
# @Last Modified time: 2018-07-01 11:49:40

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

txt.close()

print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()