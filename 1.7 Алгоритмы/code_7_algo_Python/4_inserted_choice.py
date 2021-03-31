def insertion_sort(array):

    #Мы начинаем единицы
    for index in range(1, len(array)):
        currentValue = array[index] # получаем текущее значение в массиве
        currentPosition = index # получаем текущую позицию

        # Пока мы не достигнем начала и пока у нас есть элемент который больше
        # того которого мы пытаемся вставить этот элемент направо
        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            array[currentPosition] = array[currentPosition -1]
            currentPosition = currentPosition - 1


        # Мы должны либо достигнуть начала нашего или мы найдем
        # элемент нашего отсортированного массива который меньше чем элемент к
        # который мы пытаемся вставть на index currentPosition - 1.
        # В другом случае мы пытаемся вставить элемент на currentPosition
        array[currentPosition] = currentValue

array = [4, 22, 41, 40, 27, 30, 36, 16, 42, 37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47]
insertion_sort(array)
print("sorted array: " + str(array))