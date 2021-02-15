import os
import shutil

while True:
    move = input("Что вы собираетесь сделать, создать или удалить папку? Y - создать, N - удалить,  q - прекратить: ")
    if move == 'Y':
        make_dir = input("Введите название папки: ")
        os.mkdir(make_dir)
    elif move == 'N':
        del_dir = input("Введите название папки: ")
        shutil.rmtree(del_dir)
    elif move == 'q':
        exit()


