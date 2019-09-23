# -*- coding: utf-8 -*-

def findMinAndMax(L):

    if len(L) == 0:
        return None, None
    if len(L) == 1:
        return L[0], L[0]

    v_min = L[0]
    v_max = L[len(L) - 1]

    for x in L:
        if x < v_min:
            v_min = x
        if x > v_max:
            v_max = x

    return v_min, v_max

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
