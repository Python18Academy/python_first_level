from bs4 import BeautifulSoup

with open("index.html") as html_doc:
    content = html_doc.read()
    # print(content)



soup = BeautifulSoup(content, 'html.parser')

print(soup.title)
# Выведет title нашего приложения

print(soup.title.string)
# выведет контент title

print(soup.title.parent.name)
#Выведет контент родителя

print(soup.p)
# выведет все теги p, если они у вас есть

print(soup.p['class'])
# выведет класс первого элемента с классом

print(soup.a)
#  Выведет первую ссылку, если она есть в вашем документе.

print(soup.find_all('a'))
# выведете все ссылки, которые есть в ваше документе. Достаточно полезый метод, если вы пытаетесь написать парсер.

