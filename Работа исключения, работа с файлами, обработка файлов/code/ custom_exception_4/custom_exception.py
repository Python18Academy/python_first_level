day = 32
try:
    if day > 31:
        raise ValueError("Неправильное число")
except ValueError as msg:
    print("программа нашла", msg)
finally:
    print(" Но сегодня ведь классный денечек, не правда ли? ")