# Самое наивное решение, каждый случай - независимая ветка
for x in range(1, 100):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz", end=' ')
    elif x % 3 == 0:
        print("Fizz", end=' ')
    elif x % 5 == 0:
        print("Buzz", end=' ')
    else:
        print(x, end=' ')

# Чуть более лаконичное решение - в нем столько же строк, сколько и в предыдущем
# но оно более изящно и содержит меньше повторов кода
for x in range(1, 100):
    s = ''
    if x % 3 == 0:
        s += 'Fizz'
    if x % 5 == 0:
        s += "Buzz"
    if s == '':
        s = x
    print(s, end=' ')
