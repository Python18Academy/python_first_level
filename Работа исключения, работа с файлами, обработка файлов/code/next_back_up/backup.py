import random
import os
import shutil
# path = os.getcwd()
print("Программа автоматического бекапа")
name_of_folder = input("введите имя папки для бекапа")
name_folder_second = random.randint(len(name_of_folder),len(name_of_folder) )

second_name = name_of_folder + str(name_folder_second)
os.mkdir(second_name)
shutil.copytree(name_of_folder, second_name)
