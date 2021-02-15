alive = True
while alive:
    health = input('Введите ваш статус по здоровью: ')
    if health.lower() == 'covid':
        print("бывает")
        alive = False
    else:
        print("Прекрасно! Приступайте к работе!")
