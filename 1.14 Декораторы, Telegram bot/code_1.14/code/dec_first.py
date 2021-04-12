from datetime import datetime
# положим, что нам надо написать

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            print("Я вам запрещаю работать по ночам")
    return wrapper

def say_whee():
    print("Вполне можно и покодить в данном время")

say_whee = not_during_the_night(say_whee)
say_whee()
