'''
Автор: Андреев Игорь Николаевич
Группа: ИУ7-14Б
Задание 4. Среднее арифметическое строк.
'''
from matrix import matrix_input, list_input, matrix_print, list_print

# Ввод данных
d = matrix_input(name="D")
n = len(d)
m = len(d[0])
il = list_input(name="I", max_el=n)

# Решение
r = [0] * len(il)
s = 0
for i in range(n):
    maximum = -1e100
    for j in il:
        t = d[i][j - 1]
        if maximum < t:
            maximum = t
    r[i] = maximum
    s += maximum

# Вычисление среднего арифметического
sr = s / n

# Вывод данных
print("\nМатрица  D:")
matrix_print(d)
print("\nМассив I:")
list_print(il)
print("\nМассив R:")
list_print(r)
print(f"\nСреднее арифметическое полученных значений: {sr:.7g}")
