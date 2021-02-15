how = int(input("Сколько вы хотите пользователей в списке: "))
names_spi = []
for i in range(how):
    new_name = input("Введите имя пользователя: ")
    names_spi.append(new_name)


def filter_data(spisok):
    spisok_dubl = spisok[:]
    for name in spisok_dubl:
        if len(name) <= 1:
            spisok_dubl.remove(name)
    return spisok_dubl

print(filter_data(names_spi))
print(names_spi)
# у нас есть неизменный список




