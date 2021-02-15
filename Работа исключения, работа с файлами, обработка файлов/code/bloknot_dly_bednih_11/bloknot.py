# для того, чтобы данные могли оставаться неизменяемыми, мы возьмем модуль pickle
import os, pickle

if not os.path.isfile('diary.dat'):
    data = [0, 1]
    data[0] = input("Введите тему: ")
    data[1] = input("Введите описание вашего дела: ")
    # теперь мы может открыть наш файл
    file = open('diary.dat', 'wb')
    pickle.dump(data, file)
    file.close()
else:
    file = open("diary.dat", 'rb')
    data = pickle.load(file)
    file.close()
print('Список ваших дел: ' + data[0] + ", " + data[1])
