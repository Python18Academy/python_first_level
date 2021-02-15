name_of_user = input("Можете ввести свое имя: ")
surname_of_user = input("Можете ввести свою фамилию: ")


def get_name(name='Anonim', surname='Anonimov'):
    print("Добрый день", name.strip().title() + " " + surname.strip().title())


get_name()
get_name(name_of_user, surname_of_user)

