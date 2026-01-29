'''
Автор: Андреев Игорь Николаевич
Группа: ИУ7-14Б
Задание 3. Работа с двумя матрицами
'''
from matrix import matrix_input, matrix_print, params_check

# Ввод данных
m = input("Введите количество столбцов в матрицах A и B: ")
if t := params_check(m):
    print(t)
    exit()
m = int(m)
a = matrix_input(columns=m, name="A")
b = matrix_input(columns=m, name="B")

# Вывод изначальных данных
print("\nМатрица А:")
matrix_print(a)
print("\nМатрица B:")
matrix_print(b)

# Решение
n_b = len(b)
n_a = len(a)
for j in range(m):
    s = 0
    c = 0
    for i in range(n_b):
        s += b[i][j]
        c += 1
    sr = s / c
    c = 0
    for i in range(n_a):
        if a[i][j] > sr:
            c += 1
    print(f"Количество значений {j + 1} столбца А больших стреднего арифметического {j + 1} столбца B: {c}")
    if c != 0:
        for i in range(n_b):
            b[i][j] *= c

# Вывод преобразованной матрицы B
print("\nПреобразованная матрица B:")
matrix_print(b)
