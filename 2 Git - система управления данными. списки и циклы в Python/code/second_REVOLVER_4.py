# мне она нравится тем, что существует огромная масса вариантов, как это можно написать и сделать
# давайте напишем несложнуую программу русской рулетки
# к примеру:
import random

amount_of_bullets = input(
    'Сколько патронов вы собираетесь вставить в револьвер?')
aob = int(amount_of_bullets)
baraban = [0, 0, 0, 0, 0, 0]

for i in range(aob):
    baraban[i] = 1

print("Посмотрите на барабан", baraban)

How_much = input("сколько раз вы собираетесь нажимать на курок?")
hm = int(How_much)
for i in range(hm):
    random.shuffle(baraban)
    print(baraban[0])
