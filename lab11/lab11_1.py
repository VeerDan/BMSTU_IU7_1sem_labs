"""
Автор: Андреев Игорь Николаевич
Группа: ИУ7-14Б
Вычисление приближенного значения определённого интеграла
Метод левых прямоугольников и метод парабол
"""
from integrals import left_rectangle_integral, parabola_integral, ParamError, BorderError


# интегрируемая функция
def func(x):
    return x ** 2


# первообразная функция
def int_func(x):
    return x ** 3 / 3


# подсчёт неопределённого интеграла
def int_calc(a, b):
    return int_func(b) - int_func(a)


try:
    a, b = map(float, input("Введите начало и конец отрезка через пробел: ").split())
    if b < a:
        raise BorderError("Ошибка! Начало отрезка больше конца отрезка!")
    t = func(a)
    if type(t) not in [float, int]:
        raise TypeError
    t = func(b)
    if type(t) not in [float, int]:
        raise TypeError
except TypeError:
    print("Функция неопределена на отрезке!")
except ZeroDivisionError:
    print("Деление на ноль!")
else:
    try:
        n1, n2 = map(int, input("Введите два значения количества участков разбиения через пробел: ").split())
    except ValueError:
        print("Ошибка при вводе входных данных!")
    except BorderError as e:
        print(e)
    else:
        s = []
        f = ""
        for method in [left_rectangle_integral, parabola_integral]:
            for n in [n1, n2]:
                try:
                    t = method(func, a, b, n)
                except ParamError as e:
                    t = "-"
                except TypeError:
                    t = ""
                s.append(t)
        print("\n")
        print("-" * 114)
        print("|" + f"{'Метод':^30}" + "|" + f"{'N1 = ' + str(n1):^40}" + "|" + f"{'N2 = ' + str(n2):^40}|")
        print("-" * 114)
        for i in range(len(s)):
            if i == 0:
                print(f"|{'Левых прямоугольников':^30}|", end="")
                try:
                    print(f"{s[i]:^40.7g}|", end="")
                except ValueError:
                    print(f"{s[i]:^40}|", end="")
            elif i == 2:
                print(f"|{'Парабол':^30}|", end="")
                try:
                    print(f"{s[i]:^40.7g}|", end="")
                except ValueError:
                    print(f"{s[i]:^40}|", end="")
            else:
                try:
                    print(f"{s[i]:^40.7g}|")
                except ValueError:
                    print(f"{s[i]:^40}|")
                print("-" * 114)

        deltas = []
        epsilons = []
        for i in range(len(s)):
            try:
                delta = abs(int_calc(a, b) - s[i])
            except TypeError:
                delta = None
            if delta is not None:
                epsilon = delta / abs(s[i])
            else:
                epsilon = None
            deltas.append(delta)
            epsilons.append(epsilon)

        c = 0
        q = ["левых прямоугольников", "парабол"]
        n = [n1, n2]
        for i, j in zip(deltas, epsilons):
            if deltas[c] is None:
                print(f"\nПри {n[c % 2]} делениях интеграл методом {q[c // 2]} вычислен не был! Погрешности не посчитаны!")
            else:
                print(f"\nАбсолютная и относительная погрешности для метода {q[c // 2]} при {n[c % 2]} делениях:")
                print(f"\tdelta = {deltas[c]}")
                print(f"\tepsilon = {epsilons[c]}")
            c += 1

        if deltas[2] is None and deltas[3] is None:
            print("\nДля заданных n функция методом парабол не проинтегрирована! Считаем метод левых прямоугольников более "
                  "точным!")
            optimized, not_optimized = left_rectangle_integral, parabola_integral
        elif deltas[2] is not None and deltas[0] < deltas[2] or deltas[3] is not None and deltas[1] < deltas[3]:
            optimized, not_optimized = left_rectangle_integral, parabola_integral
            print("\nМетод левых прямоугольников более точный!")
        else:
            optimized, not_optimized = parabola_integral, left_rectangle_integral
            print("\nМетод парабол более точный!")
        e = float(input("\nВведите значение точности для вычисления интеграла: "))
        n = 1
        for_n = optimized(func, a, b, n)
        for_2n = optimized(func, a, b, 2 * n)
        while abs(for_n - for_2n) >= e:
            n += 1
            for_n = optimized(func, a, b, n)
            for_2n = optimized(func, a, b, 2 * n)
        print(f"\nДля достижения указанной точности необходимо {n} операций!")
        print(f"Вычесленное значение интеграла: {for_n}")
