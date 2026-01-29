'''
Автор: Андреев Игорь Николаевич
Группа: ИУ7-14Б
'''
# Импорт необходимых библиотек
from math import sqrt

# Ввод данных
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))

# Решение
if a == 0:
    if b == 0:
        if c == 0:
            print("x = (-∞, +∞)")
        else:
            print("x = ø")
    else:
        x = -c / b
        print(f"x = {x:.7g}")  # Вывод данных
else:
    d = b ** 2 - 4 * a * c
    if d <= 0:
        if d == 0:
            x = -b / (2 * a)
            print(f"x = {x:.7g}")  # Вывод данных
        else:
            print("x = ø")
    else:
        x1 = (-b - sqrt(d)) / (2 * a)
        x2 = (-b + sqrt(d)) / (2 * a)
        print(f"x1 = {x1:.7g}")  # Вывод данных
        print(f"x2 = {x2:.7g}")  # Вывод данных
