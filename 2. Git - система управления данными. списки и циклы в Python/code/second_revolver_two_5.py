# дополнительная программа Python 
import random

flag = input("Вы хотите поиграть в русскую рулетку? Введите да/нет: ")
baraban = [0, 0, 0, 0, 0, 0]
bullet_amount = 1


def try_play(bullet_amount):
    # print("В револьвере " + str(bullet_amount) + " патрон")
    print(bullet_amount)
    for i in range(1, bullet_amount):
        baraban[i] = 1
    random.shuffle(baraban)

    if baraban[0] == 1:

        print(baraban)
        print("Бабах")
    else:
        print("щелчок")
        second_flag = input("Вы хотите поиграть ещё? Введите да/нет: ")
        if second_flag == "да":
            bullet_amount += 1
            try_play(bullet_amount)
        else:
            return


if (flag == "да"):
    try_play(bullet_amount)
else:
    print("Ну и ладно")
