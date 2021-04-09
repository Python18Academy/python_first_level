x = 10

def print_x():
    x = 12
    print(x)

print(x)
print_x()
#сначала у нас появится 10, затем 12
#здесь все довольно просто

y = 12

def print_y():
    global y
    y = 14
    print(y)
print(y)
print_y()
#попробуйте теперь закомментировваться перменную y на 12 строчке
#и поменять функцию print_y и просто print местами

