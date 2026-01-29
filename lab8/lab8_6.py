'''
Автор: Андреев Игорь Николаевич
Группа: ИУ7-14Б
Задание 6.
'''
# импорт модуля для ввода и вывода матрицы
from matrix import matrix_input, matrix_print

# Ввод матрицы
m = matrix_input(square=True)
n = len(m)

# Печать исходной матрицы
print("\nИсходная матрица:")
matrix_print(m)


# Решение
for i in range(n):
    for j in range(i + 1, n):
        m[i][j], m[j][i] = m[j][i], m[i][j]

# Вывод данных
print("\nТранспонированная матрица:")
matrix_print(m)
