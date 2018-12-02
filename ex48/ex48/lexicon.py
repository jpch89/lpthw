# -*- coding: utf-8 -*-
# @Author: jpch89
# @Email:  jpch89@outlook.com
# @Time:   2018/7/28 21:14

glossary = {}

glossary['direction'] = ('north',
                         'south',
                         'east',
                         'west',
                         'down',
                         'up',
                         'left',
                         'right',
                         'back')

glossary['verb'] = ('go',
                    'stop',
                    'kill',
                    'eat')

glossary['stop'] = ('the',
                    'in',
                    'of',
                    'from',
                    'at',
                    'it')

glossary['noun'] = ('door',
                    'bear',
                    'princess',
                    'cabinet')


def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None


def scan(stuff):
    words = stuff.split()
    sentence = []
    for word in words:
        item = ()
        if convert_number(word):
            item = ('number', convert_number(word))
            sentence.append(item)

        for key, value in glossary.items():
            if word in value:
                item = (key, word)
                sentence.append(item)

        if item == ():
            sentence.append(('error', word))

    return sentence
