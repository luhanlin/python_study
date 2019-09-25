# -*-coding:UTF-8-*-
import functools


def log01(func):
    # wraps 可以将被装饰的函数的名称服务装饰器
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('test log, call {}()'.format(func.__name__))
        return func(*args, **kw)
    return wrapper

@log01
def test01():
    print('this is a test')

test01()
print(test01.__name__)
# print out:
# test log, call test()
# this is a test
# test01

def log02(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log02('execute')
def test02():
    print('this is a test')

test02()
print(test02.__name__)
# print out:
# execute test02():
# this is a test
# wrapper


