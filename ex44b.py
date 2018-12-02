# -*- coding: utf-8 -*-
# @Author: jpch89
# @Email:  jpch89@outlook.com
# @Time:   2018/7/27 15:19

class Parent(object):

    def override(self):
        print('PARENT override()')


class Child(Parent):

    def override(self):
        print('CHILD override()')

dad = Parent()
son = Child()

dad.override()
son.override()
