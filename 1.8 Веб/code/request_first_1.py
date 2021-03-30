import requests


r = requests.get("https://ru.wikipedia.org/wiki/Python")
print(r)
print(r.text)

print(type(r))
print(dir(r))
print(help(r))
