# -*- coding: utf-8 -*-
# @Author: jpch89
# @Email:  jpch89@outlook.com
# @Time:   2018/7/28 20:29

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
