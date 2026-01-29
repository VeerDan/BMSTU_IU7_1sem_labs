from random import randint
from SelectionSort import selection_sort

try:
    a = list(map(int, input("Введите значения массива для сортировки через пробел: ").split()))
    a = selection_sort(a)[0]
    print("\nОтсортированный введённый массив:")
    print(*a)
except ValueError:
    print("\nНекоректный ввод! Завершение программы!")

try:
    n1, n2, n3 = map(int, input("\nВведите три различных размерности массивов для проверки "
                                "работы метода сортировки через пробел: ").split())
    if n1 == n2 or n2 == n3 or n1 == n3:
        raise ValueError
except ValueError:
    print("\nНекоректный ввод! Завершение программы!")
else:
    c = [0] * 9
    elapsed_time = [0] * 9

    t = 0
    for i in (n1, n2, n3):
        p = [randint(-2 * i, 2 * i) for _ in range(i)]
        p, c[t], elapsed_time[t] = selection_sort(p)
        p, c[t + 1], elapsed_time[t + 1] = selection_sort(p)
        p.reverse()
        p, c[t + 2], elapsed_time[t + 2] = selection_sort(p)
        t += 3
        del p

    print("\n")
    print("-" * 150)
    print("|" + " " * 28 + "|" + f"{'N1 = ' + str(n1):^39}" + "|" + f"{'N2 = ' + str(n2):^39}"
          + "|" + f"{'N3 = ' + str(n3):^39}" + "|")
    print("-" * 150)
    print("|" + " " * 28 + "|", end="")
    for i in range(3):
        print(f"{'время':^20}" + "|" + f"{'перестановки':^18}" + "|", end="")
    print("\n" + "-" * 150)

    print("|" + f"{'Упорядоченный':^28}" + "|", end="")
    for i in range(3):
        print(f"{elapsed_time[1 + i * 3]:^20.7g}" + "|" + f"{c[1 + i * 3]:^18}" + "|", end="")
    print("\n|" + f"{'список':^28}" + "|", end="")
    for i in range(3):
        print(f"{'':^20}" + "|" + f"{'':^18}" + "|", end="")
    print("\n" + "-" * 150)

    print("|" + f"{'Случайный':^28}" + "|", end="")
    for i in range(3):
        print(f"{elapsed_time[i * 3]:^20.7g}" + "|" + f"{c[i * 3]:^18}" + "|", end="")
    print("\n|" + f"{'список':^28}" + "|", end="")
    for i in range(3):
        print(f"{'':^20}" + "|" + f"{'':^18}" + "|", end="")
    print("\n" + "-" * 150)

    print("|" + f"{'Упорядоченный':^28}" + "|", end="")
    for i in range(3):
        print(f"{elapsed_time[2 + i * 3]:^20.7g}" + "|" + f"{c[2 + i * 3]:^18}" + "|", end="")
    print("\n|" + f"{'в обратном':^28}" + "|", end="")
    for i in range(3):
        print(f"{'':^20}" + "|" + f"{'':^18}" + "|", end="")
    print("\n|" + f"{'порядке':^28}" + "|", end="")
    for i in range(3):
        print(f"{'':^20}" + "|" + f"{'':^18}" + "|", end="")
    print("\n" + "-" * 150)
