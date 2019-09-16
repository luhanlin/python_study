# -*- coding: UTF-8 -*-

# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
else:
    print('for ... else test')
# output:
# cat 3
# window 6
# defenestrate 12

for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
print(words)
# output:
# ['defenestrate', 'cat', 'window', 'defenestrate']

sum = 0
for x in range(101):
    sum = sum + x
print(sum)
# output:
# 5050

# 裴波那契数列
a, b = 0, 1
while a < 100:
    print(a, end=',')
    a, b = b, a + b
else:
    print('\nwhile ... else test')
# 0,1,1,2,3,5,8,13,21,34,55,89,
# while ... else test

# beak test
for x in range(100001):
    if x > 1000:
        print(x)
        break
# 1001

# continue test
for y in range(1, 5):
    if y % 2 == 0:
        print('continue test ', y)
        continue
    print('normal print ', y)
# normal print  1
# continue test  2
# normal print  3
# continue test  4

