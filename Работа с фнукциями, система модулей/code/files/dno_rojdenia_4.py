filename = 'pi_million_digits.txt'
with open(filename) as file:
    lines = file.readlines()
pi_string = ''
for line in lines:
    pi_string += line

birthday = input("Введите дату вашего рождения: ")
if birthday in pi_string:
    print("Вот здорово! Ваш день рождения оказался в PI")
else:
    print("В числе Пи не рождаются. Числом Пи не становятся")
