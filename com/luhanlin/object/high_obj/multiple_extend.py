#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class Animal(object):
    pass

# 大类:
# 哺乳类
class Mammal(Animal):
    pass

# 鸟类
class Bird(Animal):
    pass

# 各种动物:
# class Dog(Mammal):
#     pass
#
# class Bat(Mammal):
#     pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

# 具有的功能类
class RunnableMaxIn(object):
    def run(self):
        print('Running...')

class FlyableMaxIn(object):
    def fly(self):
        print('Flying...')

# 以下为多重继承
class Dog(Mammal, RunnableMaxIn):
    pass

class Bat(Mammal, FlyableMaxIn):
    pass

dog = Dog()

dog.run();


































