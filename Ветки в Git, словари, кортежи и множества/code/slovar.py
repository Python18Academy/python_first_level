slovar = {'book': 'книга', 'bear': 'медведь'}

print(slovar['book'])

if 'book' not in slovar.keys():
    print("а перевода этого у нас и нет")

user = {
    'name': 'Petr',
    'surname': 'Ivanov'
}

for key, value in user.items():
    print('\nKey: ' + key)
    print('\nValue: ' + value)

for key in user.keys():
    print(key.title())

# и абсолютно точно также работающий код
for key in user:
    print(key.title())

for key in user.keys():
    print(user[key])
