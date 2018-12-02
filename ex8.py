# -*- coding: utf-8 -*-
# @Author: jpch89
# @Email:  jpch89@outlook.com
# @Date:   2018-06-27 23:59:30
# @Last Modified by:   jpch89
# @Last Modified time: 2018-06-28 00:02:38

formatter = '{} {} {} {}'
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a peom",
    "Or a song about fear"
))