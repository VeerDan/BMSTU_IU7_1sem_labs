"""
Автор: Андреев Игорь Николаевич
Группа: ИУ7-14Б
Метод левосторонних прямоугольников. Подсчёт площади пересечения графиков.
"""
# Импорт необходимых библиотек
from integrals import left_rectangle_integral
from math import sin, tan
from module import func_print, search, left_search


# Реализации функции f для анализа
def f(x):
    # return (x - 0.2) ** 0.5
    return x ** 2
    # return 1 / x


# Реализации функции g для анализа
def g(x):
    return x ** 2 - 2 * x + 3
    # return (x - 0.2) ** 0.5
    # return sin(x) + 10
    # return -(x) ** 2 + 3
    # return (x + 2.5) ** 0.5


# Печать анализируемых функций
print("Функции для анализа:")
func_print(f, name="f")
func_print(g, name="g")

# Нахождение отрезков, на которых есть корни
res = [(i - 2, i) for i in range(-20, 21, 2)]
t = None
res = []  # отрезки с корнями
for i in range(-20, 21, 2):
    try:
        t1 = f(i)
        t2 = g(i)
        if t is not None and t * (t1 - t2) <= 0:
            res.append((i - 4, i - 2))
            res.append((i - 2, i))
            res.append((i, i + 2))
        t = t1 - t2
        if type(t) not in [float, int]:
            raise TypeError
    except TypeError:
        t = None
    except ZeroDivisionError:
        t = None
# Нахождение точек пересечения
t = []  # точки пересечения
for i in res:
    l = i[0]
    r = i[1]
    temp1 = search(f, g, l, r)
    temp2 = left_search(f, g, l, r)
    if temp1 is not None:
        t.append(temp1)
    if temp2 is not None:
        t.append(temp2)
    try:
        if abs(f(l) - g(l)) < 1e-9:
            t.append(l)
    finally:
        pass
    try:
        if abs(f(r) - g(r)) < 1e-9:
            t.append(r)
    finally:
        pass
t.sort()
# Вычисление интеграла
length = len(t)
if length >= 2:
    try:
        e = float(input("\nВведите точность для вычисления интеграла: "))
    except ValueError:
        print("\nОшибка при вводе данных!")
    else:
        s = 0
        for i in range(len(t) - 1):
            a, b = t[i], t[i + 1]
            n = 1
            for_n = left_rectangle_integral(f, a, b, n)
            for_2n = left_rectangle_integral(f, a, b, 2 * n)
            while abs(for_n - for_2n) >= e:
                n += 1
                for_n = left_rectangle_integral(f, a, b, n)
                for_2n = left_rectangle_integral(f, a, b, 2 * n)
            res = for_n
            n = 1
            for_n = left_rectangle_integral(g, a, b, n)
            for_2n = left_rectangle_integral(g, a, b, 2 * n)
            while abs(for_n - for_2n) >= e:
                n += 1
                for_n = left_rectangle_integral(g, a, b, n)
                for_2n = left_rectangle_integral(g, a, b, 2 * n)
            res = res - for_n
            res = abs(res)
            s += res
        print(f"\nПлощадь фигуры, образованной пересечением графиков: {s:.7g}")
else:
    print("\nНевозможно посчитать интеграл! Недостаточно точек пересечения!")

# Построение графика
# Если было найдено пересечение - строитсся вычисляемая площадь
# Если нет - пользователь строит график на промежутке, который ему интересен для изучения
# Полчение начального и конечного значения по оси OX
if t:
    z0, zn = t[0], t[-1]
else:
    try:
        z0, zn = map(float, input("\nВведите начальное и конечное значения X для отображения графика: ").split())
        if zn <= z0:
            raise ValueError
    except ValueError:
        print("\nОшибка при вводе!")
        z0 = None

if z0 is not None:
    # Ввод количество засечек
    try:
        c = int(input("\nВведите количество засечек по оси X: "))
        if c <= 0:
            raise ValueError
    except ValueError:
        print("\nОшибка при вводе!")
    else:
        # Вычисление
        h = (zn - z0) / c
        n = 4
        k = int(round((zn - z0) / h, 0))  # количество шагов
        p1 = []
        p2 = []
        ts = []
        max_value = None
        min_value = None
        trace = False
        for i in range(k + 1):
            t = z0 + i * h
            ts.append(t)
            try:
                p = f(t)
                if type(p) in [float, int]:
                    p1.append(p)
                    if max_value is None or max_value < p:
                        max_value = p
                    if min_value is None or min_value > p:
                        min_value = p
                else:
                    raise ValueError
            except ValueError:
                p1.append(None)
            except ZeroDivisionError:
                p1.append(None)
            try:
                p = g(t)
                if type(p) in [float, int]:
                    p2.append(p)
                    if max_value is None or max_value < p:
                        max_value = p
                    if min_value is None or min_value > p:
                        min_value = p
                else:
                    raise ValueError
            except ValueError:
                p2.append(None)
            except ZeroDivisionError:
                p2.append(None)

        if max_value is None:
            print("\nФункции не определены на указанном отрезке!")
        else:
            print()
            p = abs(max_value - min_value) / (n - 1)  # Шаг засечек
            q = " " * int(p // (abs(max_value - min_value) / 120))  # Шаг в масштабе печати
            print(" " * 21, end="")
            for i in range(n - 1):
                temp = min_value + i * p
                print(f"{temp:.1f}" + q, end="")
            print(f"{min_value + (n - 1) * p:.1f}")
            for i in range(len(ts)):
                if p1[i] is None:
                    l1 = None
                else:
                    l1 = int(abs(p1[i] - min_value) // (abs(max_value - min_value) / 120))
                if p2[i] is None:
                    l2 = None
                else:
                    l2 = int(abs(p2[i] - min_value) // (abs(max_value - min_value) / 120))
                print(f"{ts[i]:<20.5g}|", end="")
                if ts[i] == 0:
                    if l1 is None and l2 is None:
                        q = "-" * 120
                    elif l1 is None:
                        q = "-" * l2 + "+" + "-" * (120 - l2 - 1)
                    elif l2 is None:
                        q = "-" * l1 + "*" + "-" * (120 - l1 - 1)
                    elif l1 < l2:
                        q = "-" * l1 + "*" + "-" * (l2 - l1 - 1) + "+" + "-" * (120 - l1 - l2 - 2)
                    elif l1 == l2:
                        q = "-" * l1 + "^" + "-" * (120 - l1 - 1)
                    else:
                        q = "-" * l2 + "+" + "-" * (l1 - l2 - 1) + "*" + "-" * (120 - l1 - l2 - 2)
                else:
                    if l1 is None and l2 is None:
                        q = " " * 120
                    elif l1 is None:
                        q = " " * l2 + "+" + " " * (120 - l2 - 1)
                    elif l2 is None:
                        q = " " * l1 + "*" + " " * (120 - l1 - 1)
                    elif l1 < l2:
                        if trace:
                            q = " " * l1 + "*" + "-" * (l2 - l1 - 1) + "+" + " " * (120 - l1 - l2 - 2)
                        else:
                            q = " " * l1 + "*" + " " * (l2 - l1 - 1) + "+" + " " * (120 - l1 - l2)
                    elif l1 == l2:
                        q = " " * l1 + "^" + " " * (120 - l1 - 1)
                    else:
                        if trace:
                            q = " " * l2 + "+" + "-" * (l1 - l2 - 1) + "*" + " " * (120 - l1 - l2 - 2)
                        else:
                            q = " " * l2 + "+" + " " * (l1 - l2 - 1) + "*" + " " * (120 - l1 - l2 - 2)
                if l1 is not None and l2 is not None and abs(l1 - l2) <= 1 and length >= 2:
                    trace = not trace
                print(q)
