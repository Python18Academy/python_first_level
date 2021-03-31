# теперь мы можем сделать это с yandex
# хотя вся история SEO это война роботов с роботами
import requests

# c  полным набором регионов можно ознакомиться
# здесь https://yandex.ru/dev/xml/doc/dg/reference/regions-docpage/

payload = {'text': 'ozon', 'lr': 187}
r = requests.get('https://yandex.ru/search/', params=payload)

print(r.text)


# все работет вполне корректно, только результат у нас выглядит нечитабельно
