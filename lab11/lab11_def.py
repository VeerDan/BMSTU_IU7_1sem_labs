N = 30
EPS = 1e-9


def f(t):
    return t ** 2 - t


def a(x):
    return x


def b(x):
    return x ** 2


def simpson(func, a, b, n) -> float:
    if b < a:
        neg = -1
        a, b = b, a
    else:
        neg = 1
    if abs(a - b) < EPS:
        s = 0
        p = 0
    else:
        s = 0
        p = abs(b - a) / n
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
    return neg * s * p / 3


try:
    start = float(input("Введите начало участка для построения графика: "))
    end = float(input("Введите конец участка для построения графика: "))
    n = int(input("Введите количество засечек по оси X: "))
except ValueError:
    print("Неверный ввод!")
else:
    ys = []
    h = (end - start) / n
    maxi = -1e10
    mini = 1e10
    xs = []
    for i in range(n):
        x = start + i * h
        y = simpson(f, a(x), b(x), N)
        mini = min(mini, y)
        maxi = max(maxi, y)
        ys.append(y)
        xs.append(x)
    print()
    p = abs(maxi - mini) / 6
    q = " " * int(p // (abs(maxi - mini) / 120))
    print(" " * 21, end="")
    for i in range(5):
        temp = mini + i * p
        print(f"{temp:.1f}" + q, end="")
    print(f"{mini + 5 * p:.3f}")
    for x, y in zip(xs, ys):
        print(f"{x:<20.5g}|", end="")
        if y is not None:
            l = int(abs(y - mini) // (abs(maxi - mini) / 120))
            print(" " * l + "*")
        else:
            print()
