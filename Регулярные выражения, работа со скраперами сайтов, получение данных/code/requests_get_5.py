#сначала мы потренируемся на специально
#созданном ресурсе httpbin
#который возвращает нам наши введеные данные
import requests

payload  = {'page': 2,'count': 25}
r = requests.get('https://httpbin.org/get',params=payload)

print(r.text)

# как видите, у нас все работает вполне корректно