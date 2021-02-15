name_of_user = input("Можете ввести свое имя: ")
surname_of_user = input("Можете ввести свою фамилию: ")


def get_name(name, surname):
    print("Добрый день", name.strip().title() + " " + surname.strip().title())


get_name(surname=surname_of_user, name=name_of_user)
