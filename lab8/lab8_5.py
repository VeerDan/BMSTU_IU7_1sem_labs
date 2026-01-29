'''
Автор: Андреев Игорь Николаевич
Группа: ИУ7-14Б
Задание 5.
'''
# импорт модуля для ввода и вывода матрицы
from matrix import matrix_input, matrix_print

# Ввод матрицы
m = matrix_input(square=True)
n = len(m)

# Решение
maximum = None
minimum = None
for i in range(n - 1):
    for j in range(i + 1, n):
        if maximum is None or m[i][j] > maximum:
            maximum = m[i][j]

for i in range(n - 1):
    for j in range(n - i - 1):
        if minimum is None or m[i][j] < minimum:
            minimum = m[i][j]

# Печать исходной матрицы
print("\nИсходная матрица:")
matrix_print(m)

# Вывод полученных значений
if maximum is None:
    print("Введена матрица размерности 1, нет элементов выше и ниже диагоналей!")
else:
    print(f"\nМаксимальное значение над главной диагональю: {maximum:.7g}")
    print(f"\nМинимальное значение над побочной диагональю: {minimum:.7g}")
