import random # импортируем рандом, для того

print('Привет! Давай поиграем в игру!')
print('Угадай числа от 1 до 30!')

def game():
  dif = input("Выберите уровень сложности, 1 - легкий, 2 - сложный")
  if dif == '1':
    counter_limit = 8
  elif dif == '2':
    counter_limit = 4
  
  rand = random.randint(1, 30)
  count = 0
  while True:
    data = int(input("Введите число \n"))
    if data == rand:
      result = input("Молодец! Ты угадал! Просто красавчик!")
      if result == "Y":
        game()
        break
      elif result == "N":
        break
      else:
        break
    elif count > counter_limit:
      print("Game Over")
      break
    elif data < rand:
      print("Вам нужно взять побольше! ")
      count = count + 1
    elif data > rand:
      print("Вам нужно взять поменьше! ")
      count = count + 1

game()