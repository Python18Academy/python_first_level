# Python 3 программа для бинарного поиска

# Возвращает index  x  в массиве, если он в нем присутствует
def binary_search(arr, low, high, x):
    # Проверяем базовый случай
    if high >= low:

        mid = (high + low) // 2

        # Если элемент у нас присутвует прямо в середине
        if arr[mid] == x:
            return mid

        # Если элемент у нас маеньше, тогда он точно должен находится в левой части
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # В другом случае мы изем элемент справа
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Элемент не притсвует слева? Тогда возвращаем отрицательное значение, чтобы возвращение не работало
        return -1


#  Тестируем эту историю
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Элемент приствует в массиве", str(result))
else:
    print("Элемента в этом массиве нет")
