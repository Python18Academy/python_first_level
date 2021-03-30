# Поиск элемента в массиве
# На самом деле это легко может быть сделано с помощью in  оператора
# Пример:
# if x in arr:
#   print arr.index(x)

# Смотрим на пример, как это может выглядеть

# Linearly search x in arr[]
# If x is present then return its location
# else return -1

def search(arr, x):
    for i in range(len(arr)):

        if arr[i] == x:
            return i

    return -1
