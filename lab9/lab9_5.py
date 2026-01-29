'''
Автор: Андреев Игорь Николаевич
Группа: ИУ7-14Б
Задание 5. Умножение матриц.
'''
from matrix import matrix_input, matrix_print, params_check

# Ввод данных
n = input("Введите количество столбцов матрицы А и количество строк матрицы B: ")
if t := params_check(n):
    print(t)
    exit()
n = int(n)
a = matrix_input(name="A", columns=n)
n_a, m_a = len(a), len(a[0])
b = matrix_input(name="B", rows=n)
n_b, m_b = len(b), len(b[0])

# Решение
c = [[0] * m_b for _ in range(n_a)]
for i in range(n_a):
    for j in range(m_b):
        for q in range(m_a):
            c[i][j] += (a[i][q] * b[q][j])

# Вывод данных
print("\nМатрица  A:")
matrix_print(a)
print("\nМатрица B:")
matrix_print(b)
print("\nМатрица C:")
matrix_print(c)
