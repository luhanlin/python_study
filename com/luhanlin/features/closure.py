# -*- coding: utf-8 -*-

# 闭包测试
def createCounter():
    def gen():
        n = 0
        while True:
            n = n + 1
            yield n

    x = gen()

    def counter():
        return next(x)

    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


