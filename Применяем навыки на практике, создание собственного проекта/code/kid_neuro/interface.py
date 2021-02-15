from kinder import *

epoch = int(input("Эпохи: \n"))
lr = float(input("Введите скорость обучения: \n"))
accur = float(input("Введите допустимую точность от 0.1 до 0.05: \n"))

kid_neuro(epoch, lr, accur)