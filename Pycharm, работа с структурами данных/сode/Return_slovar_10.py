person = {'names':[], 'surnames': []}

def create_person(name, surname):
    """Возвращает словарь с информацией о человеке"""
    person['names'].append(name)
    person['surnames'].append(surname)
    return person


user_size = int(input("Введите количество пользователей, которые должны появиться в  этом словаре: "))
for user in range(user_size):
    name = input("Введите имя пользователя")
    surname = input("Введите фамилию пользователя")
    create_person(name, surname)

print(person)


