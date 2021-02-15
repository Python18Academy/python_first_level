import random

print("Привет! Давай поиграем в игру угадайка!")
rand = random.randint(1, 20)
# TODO только три попытки

count = 0
while True:
  data = int(input("Введите число: "))
  if data == rand:
     print("Поздравляем! Вы выйграли!")
     break
  elif count == 2:
    print("Game over")
    break
  elif data < rand:
    print("У вас получилось маловато! Нужно взять побольше")
    count = count + 1;
  elif data > rand:
    print("У вас получилось многовато! Нужно взять поменьше")
    count = count + 1;

# i = 0;
# while i < 100:
#   print("I will not waste chalk!")
#   i=i+1




# x = int(input("Введите первое значение"))
# y = int(input("Введите второе значение"))
# print(x+y)
