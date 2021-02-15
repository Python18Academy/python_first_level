import shutil
import os
print("Запущена программа бекапа")
second = input("Введите название папки для бекапа")
file = input("Введите название файла")
os.mkdir(second)
src = 'first/' + file
dist = second
shutil.copy(src, dist)