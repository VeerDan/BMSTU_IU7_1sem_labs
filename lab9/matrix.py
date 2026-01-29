def int_check(s: str) -> bool:
    """
    Функция проверки входной строки на предмет того, что это целочисленное число
    :param s: входная строка
    :return: True, если строка является целым числом, иначе - False
    """
    f = True
    if s == '-':
        f = False
    else:
        for i in range(len(s)):
            if not ('0' <= s[i] <= '9' or s[i] == '-' and i == 0):
                f = False
    return f


def list_print(a: []) -> None:
    """
    Красивая печать списка
    :param a: Список для печати
    :return: None
    """
    matrix_print([a])


def matrix_print(matrix: [[]]) -> None:
    """
    Красивая печать целочисленной матрицы
    :param matrix: Матрица для печати
    :return: None
    """
    n, m = len(matrix), len(matrix[0])
    res = -1
    for i in range(n):
        for j in range(m):
            res = max(res, len("".format(matrix[i][j])))
    print("-" * (res * m + m + 1))
    for i in range(n):
        print("|", end="")
        for j in range(m):
            print(f"{matrix[i][j]:^{res}}|", end="")
        print()
        print("-" * (res * m + m + 1))


def str_matrix_print(matrix: [[]]) -> None:
    """
    Красивая печать матрицы строк
    :param matrix: матрциа строк для печати
    :return: None
    """
    n, m = len(matrix), len(matrix[0])
    res = -1
    for i in range(n):
        for j in range(m):
            res = max(res, len(matrix[i][j]))
    print("-" * (res * m + m + 1))
    for i in range(n):
        print("|", end="")
        for j in range(m):
            print(f"{matrix[i][j]:^{res}}|", end="")
        print()
        print("-" * (res * m + m + 1))


def list_input(name=None, max_el=None) -> []:
    """
    Функция ввода списка индексов
    :param name: имя списка
    :param max_el: максимальное значение индекса
    :return: массив индексов
    """
    if name is None:
        name = ""
    else:
        name = " " + name
    n = input("Введите длину массива" + name + ": ")
    t = params_check(n)
    if t:
        print(t)
        exit()
    n = int(n)
    a = [0] * n
    for i in range(n):
        t = input(f"Введите {i + 1} значение массива" + name + ": ")
        if not int_check(t):
            print("Введённое знаечние имеет неверный тип!")
            exit()
        t = int(t)
        if max_el is None:
            a[i] = t
        elif -max_el - 1 <= t <= max_el:
            a[i] = t
        else:
            print("Введённое значение недопустимо!")
            exit()
    return a


def str_matrix_input():
    """
    Ввод матрицы строк
    :return: матрица
    """
    rows = input("Введите количество строк матрицы: ")
    t = params_check(rows)
    if t:
        print(t)
        exit()
    rows = int(rows)
    columns = input("Введите количество столбцов матрицы: ")
    t = params_check(columns)
    if t:
        print(t)
        exit()
    columns = int(columns)
    a = [[""] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            t = input("Введите {}-й элемент {}-й строки матрицы: ".format(j + 1, i + 1))
            a[i][j] = t
    return a


def params_check(s: str) -> str:
    """
    Проверка вводимых параметров матрицы
    :param s: введённые параметры
    :return: True, если параметры допустимы, наче - False
    """
    f = ""
    if not int_check(s):
        f = "Введённое знаечние имеет неверный тип!"
    else:
        n = int(s)
        if n < 0:
            f = "Отрицательная длина массива!"
        elif n == 0:
            f = "Нулевая длина массива!"
    return f


def square_matrix(name=None, n=None) -> [[]]:
    """
    Ввод квадратной матрицы
    :param name: имя квадратной матрицы
    :param n: размерность квадратной матрицы
    :return: матрица
    """
    if name is None:
        name = ""
    else:
        name = " " + name
    if n is None:
        n = input("Введите размерность квадратной матрицы" + name + ": ")
        t = params_check(n)
        if t:
            print(t)
            exit()
        n = int(n)
    m = n
    a = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            t = input(("Введите {}-й элемент {}-й строки матрицы " + name + ": ").format(j + 1, i + 1))
            if not int_check(t):
                print("Введённое знаечние имеет неверный тип!")
                exit()
            a[i][j] = int(t)
    return a


def matrix_input(columns=None, rows=None, name=None) -> [[]]:
    """
    Ввод произвольной матрицы
    :param columns: количество столбцов матрицы
    :param rows: количество строк матрицы
    :param name: имя матрицы
    :return: матрциа
    """
    if name is None:
        name = ""
    else:
        name = " " + name
    if rows is None:
        rows = input("Введите количество строк матрицы " + name + ": ")
        t = params_check(rows)
        if t:
            print(t)
            exit()
        rows = int(rows)
    if columns is None:
        columns = input("Введите количество столбцов матрицы: ")
        t = params_check(columns)
        if t:
            print(t)
            exit()
        columns = int(columns)
    a = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            t = input(("Введите {}-й элемент {}-й строки матрицы " + name + ": ").format(j + 1, i + 1))
            if not int_check(t):
                print("Введённое знаечние имеет неверный тип!")
                exit()
            a[i][j] = int(t)
    return a


if __name__ == "__main__":
    q = matrix_input()
    matrix_print(q)
