#попробуем теперь обернуть это в конструкцию try/catch

try:
    print(5/0)
except ZeroDivisionError:
    print("вы отдаете себе отчет в своих математических операциях?")