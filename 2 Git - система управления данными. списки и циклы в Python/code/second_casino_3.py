import random

guess_number = input("Выберите любое число: ")
limit = input("введите пределе рандома: ")
limit = int(limit)
random_number = random.randint(0, limit)
if random_number == int(guess_number):
    print("могу вас поздравить, вы выйграли!")
else:
    print("сегодня вам не везет")
    print("выйгрышное число на самом деле", random_number)
