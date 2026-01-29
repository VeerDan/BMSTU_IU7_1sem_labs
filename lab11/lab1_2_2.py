from integrals import left_rectangle_integral


def search(left, right):
    while (right - left) >= 1e-9:
        m = (right + left) / 2
        tm = f(m) - g(m)
        tr = f(right) - g(right)
        tl = f(left) - g(left)
        if abs(tm) < 1e-9:
            return m
        elif tr * tm < 0:
            left = m
        else:
            right = m
    return right


def f(x):
    return x ** 2


def g(x):
    return -x ** 2 + 10


res = []
t = f(-20) - g(-20)
for i in range(-20, 21, 2):
    t1 = f(i)
    t2 = g(i)
    if t * (t1 - t2) <= 0:
        res.append((i - 2, i))
    t = t1 - t2
print(res)

t = []
for i in res:
    l = i[0]
    r = i[1]
    t.append(search(l, r))
    t.sort()
print(t)
c = len(t)
if t:
    try:
        e = float(input("Введите точность для вычисления интеграла: "))
    except ValueError:
        print("Ошибка при вводе данных!")
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
        print(f"Площадь фигуры, образованной пересечением графиков: {s:.7g}")
else:
    print("Графики не пересекаются на указанном отрезке!")


if t:
    z0, zn = t[0], t[-1]
else:
    z0, zn = 0, 1


if z0 is not None:
    try:
        c = int(input("Введите количество засечек по оси X: "))
        if c <= 0:
            raise ValueError
    except ValueError:
        print("Ошибка при вводе данных!")
    else:
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

        if max_value is None:
            print("Функции не определены на указанном отрезке!")
        else:
            p = abs(max_value - min_value) / (n - 1)  # Шаг засечек
            q = " " * int(p // (abs(max_value - min_value) / 120))  # Шаг в масштабе печати
            print(" " * 21, end="")
            # Вывод засечек
            for i in range(n):
                temp = min_value + i * p
                print(f"{temp:.3g}" + q, end="")
            print()
            if max_value > 0 and min_value < 0:
                f = True
                t = int(abs(min_value) // (abs(max_value - min_value) / 120))
            else:
                f = False
                t = None

            # Построение графика
            for i in range(len(ts)):
                # Вычисление координат точек в сетке печати
                if p1[i] is None:
                    l1 = None
                else:
                    l1 = int(abs(p1[i] - min_value) // (abs(max_value - min_value) / 120))
                if p2[i] is None:
                    l2 = None
                else:
                    l2 = int(abs(p2[i] - min_value) // (abs(max_value - min_value) / 120))
                print(f"{ts[i]:<20.7g}|", end="")
                if ts[i] == 0:
                    if l1 is None and l2 is None:
                        print("-" * 120)
                    elif l1 is None:
                        print("-" * l2 + "+" + "-" * (120 - l2 - 1))
                    elif l2 is None:
                        print("-" * l1 + "*" + "-" * (120 - l1 - 1))
                    elif l1 < l2:
                        q = "-" * l1 + "*" + "-" * (l2 - l1 - 1) + "+" + "-" * (120 - l1 - l2 - 2)
                    elif l1 == l2:
                        q = "-" * l1 + "^" + "-" * (120 - l1 - 1)
                    else:
                        q = "-" * l2 + "+" + "-" * (l1 - l2 - 1) + "*" + "-" * (120 - l1 - l2 - 2)
                else:
                    if l1 is None and l2 is None:
                        print(" " * 120)
                    elif l1 is None:
                        print(" " * l2 + "+" + " " * (120 - l2 - 1))
                    elif l2 is None:
                        print(" " * l1 + "*" + " " * (120 - l1 - 1))
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
                if l1 is not None and l2 is not None and abs(l1 - l2) <= 1:
                    trace = not trace
                print(q)
