# -*- coding: utf-8 -*-
# @Author: jpch89
# @Email:  jpch89@outlook.com
# @Date:   2018-07-17 08:53:33
# @Last Modified by:   jpch89
# @Last Modified time: 2018-07-17 08:56:23

i = 0
numbers = []

while i < 6:
    print(f'At the top is {i}')
    numbers.append(i)

    i = i + 1
    print('Numbers now:', numbers)
    print(f'At the bottom i is {i}')


    print('The numbers:')

for num in numbers:
    print(num)