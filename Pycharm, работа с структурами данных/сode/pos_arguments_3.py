name_of_user = input("Можете ввести свое имя: ")
surname_of_user = input("Можете ввести свою фамилию: ")

def get_name(name, surname):
    print("Добрый день", name.title() +"  "+ surname.title())

get_name(name_of_user, surname_of_user)