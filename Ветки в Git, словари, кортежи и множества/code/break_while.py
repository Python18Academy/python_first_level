# теперь можно использовать break для того чтобы выйти из цикла
while True:
    health = input('Введите ваш статус по здоровью: ')
    if health.lower() == 'covid':
        print("бывает(")
        break
    else:
        print("Прекрасно! Приступайте к работе!")