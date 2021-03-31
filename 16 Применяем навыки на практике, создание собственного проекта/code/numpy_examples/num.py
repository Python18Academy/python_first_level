import numpy as np
#создание одномерного массива
vertor_row = np.array([1, 2, 3])

#многомерного массива
matrix = np.array([[1,2,3],
                   [2,3,4],
                   [4, 2,5]])
matrix2 = np.array([[2,4,5],
                   [5,6,4],
                   [5, 9,2]])

#пример сложения
matrix3 = matrix + matrix2
#пример умножения
matrix4 = np.dot(matrix, matrix2)