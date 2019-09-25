#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from com.luhanlin.object.extend import *

a = User('Mr.ming')
vip = UserVip('vip')
general = UserGeneral('general')
b = a.printUser()

print(type(123))
print(type('test'))
print(type(a))
print(type(b))
print(type(abs))
print(type(None))
# print out:
# <class 'int'>
# <class 'str'>
# <class 'com.luhanlin.object.extend.User'>
# <class 'NoneType'>
# <class 'builtin_function_or_method'>
# <class 'NoneType'>

print(isinstance(vip, UserVip))     # True
print(isinstance(vip, User))        # True












