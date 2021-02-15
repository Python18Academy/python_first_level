print("Давай сюда два числа, и я разделю их")
print("Введите q первым числом чтобы завершить выполнение программы")
while True:
    first_number = input("\n Введите первое число: ")
    if first_number == 'q':
        break
    second_number = input("\n Введите второе число: ")

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Подумайте о вашем поведении")
    else:
        print(answer)
