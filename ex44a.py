# -*- coding: utf-8 -*-
# @Author: jpch89
# @Email:  jpch89@outlook.com
# @Time:   2018/7/27 15:17

class Parent(object):

    def implicit(self):
        print('PARENT implicit()')


class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
