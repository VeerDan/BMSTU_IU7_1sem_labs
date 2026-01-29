'''
Автор: Андреев Игорь Николаевич
Группа: ИУ7-14Б
Задание 3. Вариант: 4.
'''
# импорт модуля для ввода и вывода матрицы
from matrix import matrix_input, matrix_print
EPS = 1e-9

# Ввод матрицы
m = matrix_input()

# Решение
x, y = len(m), len(m[0])
j_max = None
j_c_max = None
for j in range(y):
    c = 0
    for i in range(x):
        if abs(m[i][j]) <= EPS:
            c += 1
    if j_c_max is None or j_c_max <= c:
        j_c_max = c
        j_max = j

# Печать исходной матрицы
print("\nИсходная матрица:")
matrix_print(m)

# Вывод данных
if j_c_max:
    m = [[m[i][j_max]] for i in range(x)]
    print("\nСтолбец с наибольшим количеством нулевых элементов:")
    matrix_print(m)
else:
    print("\nВ матрице нет нулевых элементов!")
