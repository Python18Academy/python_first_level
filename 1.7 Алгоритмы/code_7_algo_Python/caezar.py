
def encrypt(text, shift):

    encryption = ""

    for symbol in text:

        # check if character is an uppercase letter
        if symbol.isupper():

            # find the position in 0-25
            c_unicode = ord(symbol)

            c_index = ord(symbol) - ord("A")

            # perform the shift
            new_index = (c_index + shift) % 26

            # convert to new character
            new_unicode = new_index + ord("A")

            new_character = chr(new_unicode)

            # Добавляем зашифрованную строку
            encryption = encryption + new_character
        else:
            # since character is not uppercase, leave it as it is
            encryption += symbol
    return encryption


print(encrypt("HELLO WORLD", 3))
