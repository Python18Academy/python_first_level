amount_of_words = input("Как мног слов вы собираетесь занести в словарь?")
aow = int(amount_of_words)

slovar = {}

for i in range(aow):
    key = input("Введите слово на английском\n:")
    value = input("Введите слово на русском\n:")
    slovar[key] = value

for key in slovar.keys():
    print("Введите значение слова", key, ": ")
    answer = input("Вы считаете, что это слово переводится как: ")
    if slovar[key] == answer:
        print("Отлично! Лев сыт")
    else:
        print("Ничего! В следующий раз сможете запомнить")
