func = lambda x, y: x + y
print(func(1, 2))
#3
print(func('a', 'b'))
# 'ab'
print((lambda x, y: x + y)(1, 2))
# 3
print((lambda x, y: x + y)('a', 'b'))
# 'ab'