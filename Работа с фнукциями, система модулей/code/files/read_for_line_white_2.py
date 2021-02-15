filename = 'auth.txt'

with open(filename) as file:
    for line in file:
        print(line.rstrip())
