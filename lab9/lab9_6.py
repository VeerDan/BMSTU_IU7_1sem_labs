'''
Автор: Анреев Игорь Николаевич
Группа: ИУ7-14Б
Задание 6. Преобразование матрицы символов
'''
from matrix import str_matrix_input, str_matrix_print

a = str_matrix_input()
n, m = len(a), len(a[0])
print("\nМатрица до преобразований:")
str_matrix_print(a)

for i in range(n):
    for j in range(m):
        k = a[i][j]
        l = k.lower()
        if 'a' < l < 'z' and l not in "aeuio":
            a[i][j] = l.capitalize()

print("\nПреобразованная матрица:")
str_matrix_print(a)
