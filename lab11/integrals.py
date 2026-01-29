EPS = 1e-9


class ParamError(Exception):
    pass


class BorderError(Exception):
    pass


def left_rectangle_integral(func, a, b, n) -> float:
    """
    Функция, реализующая подсчёт определённого интеграла методом левых прямоугольников
    :param func: (function) - интегрируемая функция
    :param a: (float) - начало отрезка дифференцирования
    :param b: (float) - конец отрезка дифференцирования
    :param n: (int) - количество участков разбиения
    :raise: BorderError - ошибка соотношения границ отрезка интегрирования
    :return: (float) - приближённое значение определённого интеграла
    """
    if a > b:
        raise BorderError("Ошибка! Начало отрезка больше конца отрезка!")
    elif abs(a - b) < EPS:
        s = 0
    else:
        s = 0
        p = (b - a) / n
        t = a
        while abs(t - b) >= EPS:
            s += func(t) * p
            t += p
    return s


def parabola_integral(func, a, b, n) -> float:
    """
     Функция, реализующая подсчёт определённого интеграла методом левых прямоугольников
     :param func: (function) - интегрируемая функция
     :param a: (float) - начало отрезка дифференцирования
     :param b: (float) - конец отрезка дифференцирования
     :param n: (int) - количество участков разбиения
     :raise: BorderError - ошибка соотношения границ отрезка интегрирования
             ParamError - ошибка значения количество участков для разбиения
     :return: (float) - приближённое значение определённого интеграла
     """
    if a > b:
        raise BorderError("Ошибка! Начало отрезка больше конца отрезка!")
    elif n % 2 != 0:
        raise ParamError("Ошибка! Для использования метода")
    elif abs(a - b) < EPS:
        s = 0
    else:
        s = 0
        p = (b - a) / n
        s += func(a)
        s += func(b)
        t = a + p
        i = 1
        while abs(t - b - p) >= EPS:
            if i % 2 == 1:
                s += 4 * func(t)
            else:
                s += 2 * func(t)
            t += p
            i += 1
    return s * p / 3


def calc(method_func, func, a, b, n):
    return method_func(func, a, b, n)


if __name__ == "__main__":
    f = lambda x: x ** 2
    res = left_rectangle_integral(f, -1, 1, 20)
    print(res)
