# -*- coding: utf-8 -*-
# @Author: jpch89
# @Email:  jpch89@outlook.com
# @Date:   2018-07-01 15:05:15
# @Last Modified by:   jpch89
# @Last Modified time: 2018-07-01 15:08:30

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes on arguments
def print_none():
    print("I got nohthin'.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()