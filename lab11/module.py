from inspect import getsourcelines


def func_print(func, name="f"):
    """
    Форматированная печать математической функции
    :param func: (function) - математическая функция
    :param name: (str) - имя функции
    :return: (None)
    """
    code, _ = getsourcelines(func)
    func = ""
    for i in code:
        t = i.strip().split()
        if t[0] == "return":
            func = " ".join(t[1:])
        elif "lambda" in t:
            func = " ".join(t[t.index("lambda") + 2:])
    print(f"{name}: y = {func}")


def search(f, g, a, b):
    """
    Функция находит точки пересечения графиков f и g методом пловинного деления на заданном отрезке справа
    :param f: функция f
    :param g: функция g
    :param a: (float) - левый конец отрезка
    :param b: (float) - правый конец отрезка
    :return: (float) - если найдено пересечение, в ином случае - (None)
    """
    m = (b + a) / 2
    n = 1e3
    c = 0
    while c != n:
        try:
            temp = f(m) - g(m)
            if abs(temp) < 1e-9:
                break
            elif temp * (f(b) - g(b)) < 0:
                a = m
            else:
                b = m
        except:
            a = m
        c += 1
        m = (b + a) / 2
    try:
        temp = f(m) - g(m)
    except:
        temp = None
    if temp is not None and abs(temp) < 1e-9:
        return m
    return None


def left_search(f, g, a, b):
    """
    Функция находит точки пересечения графиков f и g методом пловинного деления на заданном отрезке слева
    :param f: функция f
    :param g: функция g
    :param a: (float) - левый конец отрезка
    :param b: (float) - правый конец отрезка
    :return: (float) - если найдено пересечение, в ином случае - (None)
    """
    m = (b + a) / 2
    n = 1e3
    c = 0
    while c != n:
        try:
            temp = f(m) - g(m)
            if abs(temp) < 1e-9:
                break
            elif temp * (f(a) - g(a)) < 0:
                b = m
            else:
                a = m
        except:
            b = m
        c += 1
        m = (b + a) / 2
    try:
        temp = f(m) - g(m)
    except:
        temp = None
    if temp is not None and abs(temp) < 1e-9:
        return m
    return None