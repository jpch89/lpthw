# -*- coding: utf-8 -*-
# @Author: jpch89
# @Email:  jpch89@outlook.com
# @Time:   2018/7/29 9:07

from nose.tools import *
from ex48 import parser

# test subject(noun) verb noun
def test_svn():
    x = parser.parse_sentence([('noun', 'Angel'), ('verb', 'kill'), ('noun', 'monster')])
    assert_equals(x.subject, 'Angel')
    assert_equals(x.verb, 'kill')
    assert_equals(x.object, 'monster')

# test subject(noun) verb direction
def test_svd():
    x = parser.parse_sentence([('stop', 'the'), ('noun', 'bear'), ('verb', 'run'), ('direction', 'south')])
    assert_equals(x.subject, 'bear')
    assert_equals(x.verb, 'run')
    assert_equals(x.object, 'south')

# test verb verb noun
def test_vvn():
    assert_raises(parser.ParserError, parser.parse_sentence, [('verb', 'kill'), ('verb', 'kill'), ('noun', 'monster')])
