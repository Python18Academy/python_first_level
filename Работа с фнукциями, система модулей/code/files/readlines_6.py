filename = 'auth.txt'

with open(filename) as file:
    lines = file.readlines()
    for line in lines:
        print(line.rstrip())
print(len(lines))
#да, у нас есть 4 строки