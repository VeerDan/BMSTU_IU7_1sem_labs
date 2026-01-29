from input_check import int_check, float_check


def matrix_print(matrix: [[]]) -> None:
    n, m = len(matrix), len(matrix[0])
    res = -1
    for i in range(n):
        for j in range(m):
            res = max(res, len("{:.7g}".format(matrix[i][j])))
    print("-" * (res * m + m + 1))
    for i in range(n):
        print("|", end="")
        for j in range(m):
            print(f"{matrix[i][j]:^{res}.7g}|", end="")
        print()
        print("-" * (res * m + m + 1))


def matrix_input(square=False) -> [[]]:
    if square:
        n = input("Введите размерность квадратной матрицы: ")
        if not int_check(n):
            print("Введённое знаечние имеет неверный тип!")
            exit()
        n = int(n)
        if n < 0:
            print("Отрицательная размерность матрицы недопустима!")
            exit()
        elif n == 0:
            print("Нулевая размерность матрицы недопустима!")
            exit()
        m = n
    else:
        n = input("Введите количество строк матрицы: ")
        if not int_check(n):
            print("Введённое знаечние имеет неверный тип!")
            exit()
        n = int(n)
        if n < 0:
            print("Отрицательное количество строк матрицы недопустимо!")
            exit()
        elif n == 0:
            print("Нулевое количество строк матрицы недопустимо!")
            exit()
        m = input("Введите количество столбцов матрицы: ")
        if not int_check(m):
            print("Введённое знаечние имеет неверный тип!")
            exit()
        m = int(m)
    if m < 0:
        print("Отрицательное количество элементов в строке матрицы недопустимо!")
        exit()
    elif m == 0:
        print("Нулевое количество элементов в строке матрицы недопустимо!")
        exit()
    a = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            t = input("Введите {}-й элемент {}-й строки: ".format(j + 1, i + 1))
            if not float_check(t):
                print("Введённое знаечние имеет неверный тип!")
                exit()
            a[i][j] = float(t)
    return a


if __name__ == "__main__":
    q = matrix_input()
    matrix_print(q)
