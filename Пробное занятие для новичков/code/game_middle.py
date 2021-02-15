import random
# нам потребуется random для работы нашего приложения
#программа спрашивает нас, является

print("Привет! Давай поиграем в простую программу, которая является угадайкой")
rand = random.randint(1, 30)

def game():
    count = 0
    while True:
        data = int(input("Введите число: \n"))
        if data == rand:
            result = input("Прекрасно, вы отгадали, хотите поиграть еще? Y/N - для решения: \n")
            if result == "Y":
                game()
            elif result == "N":
                break
            else:
                break
        elif count > 5:
            print("Game Over")
            break
        elif data < rand:
            print("Вам нужно взять побольше")
            count = count + 1
        elif data > rand:
            print("Вам нужно взять поменьше")
            count = count + 1

game()