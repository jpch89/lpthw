# -*- coding: utf-8 -*-
# @Author: jpch89
# @Email:  jpch89@outlook.com
# @Time:   2018/7/27 15:24

class Parent(object):

    def override(self):
        print('PARENT override()')

    def implicit(self):
        print('PARENT implicit()')

    def altered(self):
        print('PARENT altered()')

class Child(Parent):

    def override(self):
        print('CHILD override()')

    def altered(self):
        print('CHILD, BEFORE PARENT altered()')
        super(Child, self).altered()
        print('CHILD, AFTER PARENT altered()')

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
