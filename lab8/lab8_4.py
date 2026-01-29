'''
Автор: Андреев Игорь Николаевич
Группа: ИУ7-14Б
Задание 4.
'''
# импорт модуля для ввода и вывода матрицы
from matrix import matrix_input, matrix_print

# Ввод матрицы
m = matrix_input()

# Решение
s_min = None
j_s_min = None
s_max = None
j_s_max = None
x, y = len(m), len(m[0])
for j in range(y):
    s = 0
    for i in range(x):
        s += m[i][j]
    if s and (s_min is None or s_min > s):
        s_min = s
        j_s_min = j
    if s_max is None or s_max <= s:
        s_max = s
        j_s_max = j

# Печать исходной матрицы
print("\nИсходная матрица:")
matrix_print(m)

# Вывод данных
if s_min == s_max:
    print("\nМаксимальная и минимальная сумма столбца в матрице совпадают!")
else:
    print("\nИзменённая матрица:")
    for i in range(x):
        m[i][j_s_min], m[i][j_s_max] = m[i][j_s_max], m[i][j_s_min]
    matrix_print(m)
