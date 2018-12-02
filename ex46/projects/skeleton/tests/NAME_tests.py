# -*- coding: utf-8 -*-
# @Author: jpch89
# @Email:  jpch89@outlook.com
# @Time:   2018/7/28 17:35

from nose.tools import *
import NAME

def setup():
    print('SETUP!')

def teardown():
    print('TEAR DOWN!')

def test_basic():
    print('I RAN!')
