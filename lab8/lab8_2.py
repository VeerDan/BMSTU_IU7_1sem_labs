'''
Автор: Андреев Игорь Николаевич
Группа: ИУ7-14Б
Задание 2.
'''
# импорт модуля для ввода и вывода матрицы
from matrix import matrix_input, matrix_print

# Ввод матрицы
m = matrix_input()

# Решение
min_neg = None
max_neg = None
i_min_neg = None
i_max_neg = None
x, y = len(m), len(m[0])
for i in range(x):
    c = 0
    for j in range(y):
        if m[i][j] < 0:
            c += 1
    if c and (min_neg is None or min_neg > c):
        min_neg = c
        i_min_neg = i
    if max_neg is None and c or max_neg is not None and max_neg <= c:
        max_neg = c
        i_max_neg = i

# Печать исходной матрицы
print("\nИсходная матрица:")
matrix_print(m)

# Вывод данных
if min_neg is None:
    print("\nНет строк с отрицательными элементами, матрица не менялась!")
elif min_neg == max_neg:
    print("\nНаибольшее и наименьшее количество отрицательных элементов в строках совпадают!")
else:
    for j in range(y):
        m[i_min_neg][j], m[i_max_neg][j] = m[i_max_neg][j], m[i_min_neg][j]
    print("\nОтредактированная матрица:")
    matrix_print(m)
