import shutil
import os

print("Запущена программа для бекапа")

folder = input("Введите название папки для бекапа")
file = input("Введите название файла, который нужно откопировать")

os.mkdir(folder)

shutil.copy(file, folder)
