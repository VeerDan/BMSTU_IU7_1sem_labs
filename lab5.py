'''
Автор: Андреев Игорь Николаевич
Группа: ИУ7-14Б
Вариант 26
'''
# Импорт необходимых библиотек
from math import sqrt, cos, pi

# Ввод данных
z0 = float(input("Введите начальное значение: "))  # начальное значение
zn = float(input("Введите конечное значение: "))  # конечное значение
if z0 > zn:
    print("Начальное больше конечного!")
    exit()
elif z0 == zn:
    print("Начальное равно конечному!")
    exit()
h = float(input("Введите шаг: "))  # Шаг
if h <= 0:
    print("Неверный шаг!")
    exit()
k = int(round((zn - z0) / h, 0))  # количество шагов
c = 0  # количество перемен знака функции p2
sign = -2  # Знак предыдущего слагаемого
# Максимальное и минимальное значение функции p2 на отрезке
max_value = None
min_value = None

# Печать заголовка таблицы
print("-" * 64)
print("|{:^20}|{:^20}|{:^20}|".format("z", "p1", "p2"))
print("-" * 64)
for i in range(k + 1):
    # Вычисление текущего значения z
    z = z0 + h * i
    # Вычисление z и его степеней
    z_2 = z * z
    z_3 = z_2 * z
    z_4 = z_3 * z
    # Вычисление значения функции p1
    p1 = z_4 - 3 * z_3 + 8 * z_2 - 5
    # Определение максимального/минимального
    if max_value is None:
        max_value = p1
    else:
        max_value = max(max_value, p1)
    if min_value is None:
        min_value = p1
    else:
        min_value = min(min_value, p1)
    # Проверка области определения функции p2
    if z < 0:
        p2 = "-"
    else:
        # Вычисление p2, если определена
        cosine = cos(pi / 2 * z)
        z_sqrt = sqrt(z)
        p2 = 10.125 * z_sqrt - 20.15 * cosine
    # Проверка на перемену знака функции p2
    if p2 != "-":
        if sign == -2:
            if p2 < 0:
                sign = -1
            else:
                sign = 1
        else:
            if sign == 1 and p2 < 0:
                c += 1
            elif sign == -1 and p2 > 0:
                c += 1

            if p2 < 0:
                sign = -1
            else:
                sign = 1
    # Вывод полученных значений функций в таблицу
    if p2 == "-":
        print("|{:^20.7g}|{:^20.7g}|{:^20}|".format(z, p1, p2))
    else:
        print("|{:^20.7g}|{:^20.7g}|{:^20.7g}|".format(z, p1, p2))

print("-" * 64)
print(f"Количество перемен знака p2: {c}")

# Построение графика p1, ввод количества засечек
n = int(input("Введите количество засечек на оси ординат: "))
if not (4 <= n <= 8):
    print("Неверное количество засечек!")
    exit()
p = abs(max_value - min_value) / (n - 1)  # Шаг засечек
q = " " * int(p // (abs(max_value - min_value) / 80))  # Шаг в масштабе печати
print(" " * 11, end="")
# Вывод засечек
for i in range(n):
    temp = min_value + i * p
    print(f"{temp:.7g}" + q, end="")
print()

# Определение необходимости печати оси абсцисс
if max_value > 0 and min_value < 0:
    f = True
    t = int(abs(min_value) // (abs(max_value - min_value) / 80))
else:
    f = False
    t = None

# Построение графика
for i in range(k + 1):
    # Вычисление текущего значения z
    z = z0 + h * i
    # Вычисление z и его степеней
    z_2 = z * z
    z_3 = z_2 * z
    z_4 = z_3 * z
    # Вычисление значения функции p1
    p1 = z_4 - 3 * z_3 + 8 * z_2 - 5
    print(f"{z:<10.7g}|", end="")
    # Вычисление координаты точки в сетке печати
    l = int(abs(p1 - min_value) // (abs(max_value - min_value) / 80))
    if z == 0:
        q = "-" * l + "*" + "-" * (80 - l)
    else:
        if f:
            if l == t:
                q = " " * l + "*"
            elif p1 < 0:
                q = " " * l + "*" + " " * (t - l - 1) + "|"
            else:
                q = " " * t + "|" + (l - t) * " " + "*"
        else:
            q = " " * l + "*"
    print(q)
