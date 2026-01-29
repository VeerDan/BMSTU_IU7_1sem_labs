'''
Автор: Андреев Игорь Николаевич
Группа: ИУ7-14Б
Задание 7. Срез трёхмерного массива.
'''
from matrix import params_check, int_check, matrix_print

x = input("Введите размерность x массива: ")
if t := params_check(x):
    print(t)
    exit()
x = int(x)

y = input("Введите размерность y массива: ")
if t := params_check(y):
    print(t)
    exit()
y = int(y)

z = input("Введите размерность z массива: ")
if t := params_check(z):
    print(t)
    exit()
z = int(z)

m = [[[0] * z for _ in range(y)] for _ in range(x)]
for i in range(x):
    for j in range(y):
        for k in range(z):
            t = input("Введите {}-й элемент {}-ого столбца {}-ого слоя: ".format(j + 1, k + 1, x + 1))
            if not int_check(t):
                print("Введён неверный тип данных!")
                exit()
            m[i][j][k] = int(t)

t = max(x, y, z)
if t == x:
    t = int(t / 2)
    matrix_print(m[t])
elif t == y:
    t = int(t / 2)
    for i in range(x):
        for j in m[i]:
            print("|{:^10}".format(j), end="")
        print("|")
else:
    t = int(t / 2)
    for i in range(x):
        for j in range(y):
            for k in m[i][j]:
                print("|{:^10}".format(k), end="")
            print("|")

