import random


def get_name():
    name = input("Введите ваше имя: ")
    return name.strip().title()


def generate_number(name_length):
    name_length = len(name_length)
    rand_str = ''
    for i in range(name_length):
        rand_num = random.randint(1, name_length)
        rand_str += str(rand_num)
    return rand_str


def get_full_data():
    name = get_name()
    number = generate_number(name)
    return name + str(number)


print(get_full_data())
