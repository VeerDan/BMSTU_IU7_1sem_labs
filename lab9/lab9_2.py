'''
Автор: Андреев Игорь НИколаевич
Группа: ИУ7-14Б
Задание 2. Поворот матрицы.
'''
from matrix import square_matrix, matrix_print

# Ввод данных
m = square_matrix()
n = len(m)

# Печать исходной матрицы
print("\nИсходная матрица:")
matrix_print(m)

# Поворот матрицы на 90 градусов по часовой стрелке
for i in range(n // 2):
    for j in range(i, n - i - 1):
        ti, tj = i, j
        t = m[ti][tj]
        for k in range(4):
            t, m[tj][n - ti - 1] = m[tj][n - ti - 1], t
            ti, tj = tj, n - ti - 1

# Вывод повернутой матрицы
print("\nПовернутая матрица на 90 градусов по часовой стрелки:")
matrix_print(m)

# Поворот матрицы на 90 градусов против стрелки
for i in range(n // 2):
    for j in range(i, n - i - 1):
        ti, tj = i, j
        t = m[ti][tj]
        for k in range(4):
            t, m[n - tj - 1][ti] = m[n - tj - 1][ti], t
            ti, tj = n - tj - 1, ti

# Вывод итоговой матрицы
print("\nПовёрнутая матрица на 90 градусов против часовой стрелки")
matrix_print(m)
