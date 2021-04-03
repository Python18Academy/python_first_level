def get_formatted_name(first, last, otch=''):
    """Возвращает нам правильно созданное имя человека"""
    if otch:
        full_name = f"{first.title()} {last.title()} {otch.title()}"
    else:
        full_name = f"{first.title()} {last.title()}"
    return full_name.title()