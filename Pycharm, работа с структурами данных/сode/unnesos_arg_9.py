def get_full_info(name, otchestvo, surname):
    """Возвращает аккуратно отформатированное полное имя."""
    if otchestvo:
        full_name = name.strip().title() + ' ' + otchestvo.strip().title() + ' ' + surname.strip().title()
    else:
        full_name = name.strip().title() + ' ' + surname.strip().title()
    return full_name


name_of_user = input("Введите ваше имя: ")
othestvo = input("Введите ваше отчество: ")
surname_of_user = input("Введите вашу фамилию: ")


print(get_full_info(name_of_user, othestvo, surname_of_user))




