x = int(input("Please enter an integer: "))

## TypeError: can only concatenate str (not "int") to str
# print("输入的值为：" + x) -- 使用str()函数
print('输入的值为：' + str(x))

if x < 0:
    x = 0
    print('输入数字不可以小于0')
elif x == 0:
    print('zero')
elif x == 1:
    print('one')
else:
    print('other')
