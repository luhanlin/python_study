#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""__slots__ 允许对当前实例类的变量做限制，但对子类不生效"""

__author__ = 'Mr.lu'

class Slot(object):
    __slots__ = ('name', 'age')

s = Slot()

s.name = 'Mr.lu'
s.age = 12

# s.score = 55      # AttributeError: 'Slot' object has no attribute 'score'


class Test(Slot):
    pass

t = Test()
t.score = 55        # 此处可以动态定义实例属性


