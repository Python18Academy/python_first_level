import os
data_file = input("Введите название файлика вместе с его расширением: ")
#  Если файл существует, тогда мы его удалим
if os.path.isfile(data_file):
	os.remove(data_file)
else: print(f'Error: {data_file} неправильное имя файла или его нет в этой директории')
