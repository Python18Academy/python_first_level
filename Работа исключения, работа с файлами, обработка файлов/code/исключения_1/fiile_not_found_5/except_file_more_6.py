#теперь мы можем попробовать считать файл с except
# filename = 'file.txt'
filename = 'file1.txt'

try:
    with open(filename) as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    message = "Извиняйте, файл " + filename + " не существует"
    print(message)
