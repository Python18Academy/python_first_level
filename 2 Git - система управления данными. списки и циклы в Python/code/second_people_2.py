
#
data_arr = []
salary_arr = []
amount = 0

for i in range(3):
    data_arr.append(input("Имя " + str(i + 1) + " человека: "))

# вызывать каждый раз какую то функцию и класть в массив эти данные, уже обработанные
for i in range(3):
    salary_arr.append(input("Доход " + str(i + 1) + " человека"))

for salary in salary_arr:
    amount += int(salary)
mean = amount / 3

mean = str(mean)

for name in data_arr:
    print(name.title() + " Может тратить: " + mean)
