import random

# попробуем написать простую программу, которая выдает смешные приветствия
# если пользователь появился на нашем ресурсе, или, к примеру, как это происходит в дискорде

person = {'names': [], 'surnames': []}
funny_words = ['прикольный', 'смешной', 'очень позитивный']


def create_person(name, surname):
    """Возвращает словарь с информацией о человеке"""
    person['names'].append(name)
    person['surnames'].append(surname)
    return person


def speech_funny(slovar):
    for i in range(len(slovar['names'])):
        rand_word = random.choice(funny_words)
        greet = rand_word + " " + slovar['names'][i] + " " + slovar['surnames'][i]
        print(greet)


user_size = int(input("Введите количество пользователей, которые должны появиться в  этом словаре: "))
for user in range(user_size):
    name = input("Введите имя пользователя: ")
    surname = input("Введите фамилию пользователя: ")
    create_person(name, surname)

speech_funny(person)
