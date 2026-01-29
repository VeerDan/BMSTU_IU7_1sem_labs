'''
Автор: Андреев Игорь Николаевич
Группа: ИУ7-14Б
Задание 1. Формирование матрицы.
'''
from matrix import matrix_print, list_input, list_print

# Ввод данных
a = list_input("A")
b = list_input("B")

# Печать входных данных
print("\nСписок A:")
list_print(a)
print("\nСписок B:")
list_print(b)

# Решение
m = [[0] * len(b) for _ in range(len(a))]
for i in range(len(a)):
    for j in range(len(b)):
        m[i][j] = a[i] * b[j]

# Печать сформированной матрицы
print("\nСформированная матрица:")
matrix_print(m)

