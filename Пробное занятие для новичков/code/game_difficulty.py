# Давайте напишием с вами простую программу, которая
# является угайдкой просто
# это позволит нам немного поменять наше отношение
# к логике

import random
# нам потребуется random для работы нашего приложения
#программа спрашивает нас, является

print("Привет! Давай поиграем в простую программу, которая является угадайкой")
rand = random.randint(1, 30)

def game():
    count = 0
    while True:
        data = int(input("Введите число: \n"))
        if data == rand:
            result = input("Прекрасно, вы отгадали, хотите поиграть еще? Y/N - для решения: \n")
            if result == "Y":
                game()
            elif result == "N":
                break
            else:
                break
        elif count > 5:
            print("Game Over")
            break
        elif data < rand:
            print("Вам нужно взять побольше")
            count = count + 1
        elif data > rand:
            print("Вам нужно взять поменьше")
            count = count + 1

game()


#
#
#
# print('\tДобро пожаловать в игру "Отгадай число!"')
# print('Я загадал натруальное число из диапазона от 0 до 100')
# print('Попробуйте отгадать его за меньшее количество попыток')
#
# level_tries = {1:12, 2:9, 3:6} #какому уровню сколько попыток соответствует
#
# level = 0
# while level not in range(1, 4):
#     print(
#         """
#         Уровни сложности:
#         1 - низкий
#         2 - средний
#         3 - высокий
#         """
#     )
#     try:
#         level = int(input("Пожалуйста, выберите уроверь сложности: "))
#     except ValueError:
#         print("Выберите уровень из значений ниже")
#
# max_tries = level_tries[level]
# the_number = random.randint(0, 100)
# guess = int(input('Ваше предположение: '))
# tries = 1
#
# while tries != max_tries: #число попыток по уровню
#     if guess == the_number:
#         break
#     elif guess > the_number:
#         print('Меньше..')
#     else:
#         print('Больше..')
#     guess = int(input('Еще попытка: '))
#     tries += 1
#
# if guess == the_number:
#     print('Поздравляю! Это действительно число',the_number)
#     print('Вам удалось отгадать его за',tries, 'попыток.')
#     input('Press Enter to exit')
# if guess != the_number:
#     print('К сожалению, число попыток исчерпано. Better luck next time, buddy!')
#



