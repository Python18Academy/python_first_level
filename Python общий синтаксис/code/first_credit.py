# stroka = "Gvatemala 'strana' s teplim klimatom"

name1 = input("Введите имя первого человека: ")
name2 = input("Введите имя второго человека: ")
name3 = input("Введите имя третьего человека: ")

salary1 = input("зп первого: ")
salary2 = input("зп второго: ")
salary3 = input("зп третьего: ")

сredit = input("введите сумму кредита")
how_long = input("на какой срок кредит в месяцах")
procent = input("введите процент")

pay_per_month = (int(сredit) / int(how_long) )+ ((int(сredit)/100 * int(procent))/ 12)

print("Платеж за месяц", pay_per_month)

mean = (int(salary1) + int(salary2) + int(salary3)  - pay_per_month)/3
# mean = mean - pay_per_month
mean = str(mean)
print(name1 + " может потратить " + mean)
print(name2+ " может потратить " + mean)
print(name3+ " может потратить " + mean)






# print("privet User!")
# name = input("Введите ваше имя!: ")
# name = name.strip()
# print("Добро пожаловать " + name.title())
# entry1 = input("введите первое число: ")
# entry2 = input("введите второе число: ")
# print(int(entry1) + int(entry2))