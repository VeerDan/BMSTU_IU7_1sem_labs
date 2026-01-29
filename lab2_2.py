'''
Автор: Андреев Игорь Николаевич
Группа: ИУ7-14Б
Вариант 3
'''
# Импорт необходимых библиотек
from math import sqrt

# Ввод данных
x = input("Введите значение x: ")
y = input("Введите значение y: ")

# Проверка введённых данных (x)
al = "0123456789+-eE."
is_a_number_x = True
dot_count = 0
e_count = 0
for i in range(len(x)):
    if x[i] == ".":
        dot_count += 1
    if dot_count > 1:
        is_a_number = False
        break
    if x[i] in "eE":
        e_count += 1
        if i == 0 or i == len(x) - 1 or e_count > 1:
            is_a_number = False
            break
    if x[i] not in al:
        is_a_number_x = False
        break
    if x[i] in "+-" and (i > 0 and x[i - 1] != "e" or i == len(x) - 1):
        is_a_number_x = False
        break

# Проверка введённых данных (y)
al = "0123456789+-eE."
is_a_number_y = True
dot_count = 0
e_count = 0
for i in range(len(y)):
    if y[i] == ".":
        dot_count += 1
    if dot_count > 1:
        is_a_number_y = False
        break
    if y[i] in "eE":
        e_count += 1
        if i == 0 or i == len(y) - 1 or e_count > 1:
            is_a_number = False
            break
    if y[i] not in al:
        is_a_number_y = False
        break
    if y[i] in "+-" and (i > 0 and y[i - 1] != "e" or i == len(y) - 1):
        is_a_number_y = False
        break

if is_a_number_x and is_a_number_y:
    # Решение
    x = float(x)
    y = float(y)
    f = False
    if y >= x ** 2 - 6 and (-1) * ((x < 0) + 1) <= y <= sqrt(9 - x ** 2) + 3:
        f = True
    else:
        f = False

    # Вывод
    if f:
        print(f"Точка ({x:.7g}, {y:.7g}) принадлежит заданной области!")
    else:
        print(f"Точка ({x:.7g}, {y:.7g}) не принадлежит заданной области!")
else:
    print("Введённые значения не являются числом!")
