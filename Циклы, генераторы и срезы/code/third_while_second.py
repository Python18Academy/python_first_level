#кроме того, нам нужнно посмотреть на возможность обрыва, если вдруг пользователь захочет остановиться
prompt = "\n Скажи мне какое-либо число, и я верну его степень"
prompt += "\a Введите 0 чтобы закончить программу: "
#создаем пустую переменную
message = ''
while message != '0':
    message = input(prompt)
    print(int(message) ** 2)
