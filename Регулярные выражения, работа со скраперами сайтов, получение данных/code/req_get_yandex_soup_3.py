from bs4 import BeautifulSoup
import requests

# c  полным набором регионов можно ознакомиться
# здесь https://yandex.ru/dev/xml/doc/dg/reference/regions-docpage/

payload = {'text': 'ozon', 'lr': 187}
#я думаю нам нужно развиваться В Украине
r = requests.get('https://yandex.ru/search/', params=payload)

result = r.text

soup = BeautifulSoup(result, 'html.parser')
print(soup.prettify()) #у нас отдается более красивая страница, которую можно прочитать.
# положим, нас интересуют  только ссылочки, с которыми мы можем поработать:

with open("result.txt", 'a') as file:
    for link in soup.find_all("a"):
        file.write(link.get('href')+'\n')