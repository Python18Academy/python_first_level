print("Сейчас вы будете иметь возможность внести любые слова в ваш словарик")
print("Когда заходите остановиться, просто введите в виде ключа stop")

slovar = {}
while True:
    key = input(
        "Введите слово на английском, или stop, что бы прекратить\n:").strip().lower()
    if key == "stop":
        break
    value = input("Введите слово на русском\n:").strip().lower()
    slovar[key] = value
print(slovar)

print(
    "Теперь у вас будет возможность проверить ваши знания по только что занесенным словам")
print("Если вы ошибетесь больше трех раз, тогда проверка у нас прекратится")

errors = 0
bonus = 0

for key in slovar:
    print("Введите значение слова", key, ": ")
    answer = input(
        "Вы считаете, что это слово переводится как: ").strip().lower()
    if slovar[key] == answer:
        bonus += 1
        print("Отлично! Ваш счет составляет:", bonus)
    elif errors > 3:
        print(" ВЫ проиграли")
        break
    else:
        errors += 1
        print("Ваше количество ошибок", errors)
