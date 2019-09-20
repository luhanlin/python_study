# -*-coding:UTF-8-*-

name_list = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# [0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
print(name_list[0:3])
# 如果第一个索引是 0, 还可以省略
print(name_list[:3])


# 不使用strip()
# 实现strip 忽略前后空格功能
def trim(s):
    count = 0
    l = []   # 用于记录非' '的位置
    for i in s:
        count += 1
        if i != ' ':
            l.append(count)
    if l:
        s = s[(l[0]-1):l[-1]]
    else:
        s = ''
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

