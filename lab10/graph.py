# Импорт необходимых библиотек
from random import randint
from SelectionSort import selection_sort

# Решение
try:
    # Ввод данных
    n1, n2 = map(int, input("Введите минимальную и максимальную размерности массивов через пробел: ").split())
    # Проверка корректности ввода (минимальное меньше максимального)
    if n1 >= n2:
        raise ValueError
    p = (n2 - n1) // 9  # Шаг
    if p == 0:
        raise ValueError
except ValueError:
    # обработка исключения
    print("\nНекоректный ввод! Завершение программы!")
else:
    max_value = None  # Максимальное значение времени
    # Вывод оси N
    print("\n")
    print(" " * 20 + "N")
    print(" " * 20 + "^")
    print(" " * 20 + "|")
    # поитерационный вывод строк графика
    for i in range(n2, n1 - 1, -p):
        elapsed_time = [0] * 3  # вычисленное время работы
        # Случайный массив и тесты сортировок
        p = [randint(-2 * i, 2 * i) for _ in range(i)]
        p, _, elapsed_time[0] = selection_sort(p)
        p, _, elapsed_time[1] = selection_sort(p)
        p = p[::-1]
        p, _, elapsed_time[2] = selection_sort(p)
        if max_value is None:
            max_value = max(elapsed_time)
        # вывод строки графика
        l = [int(j // (abs(max_value) / 100)) for j in sorted(elapsed_time)]
        print(f"{i:^20}|", end="")
        if l[1] - l[0] == 0 and l[2] - l[1] == 0:
            print(" " * l[0] + "^")
        elif l[1] - l[0] == 0:
            print(" " * l[0] + "<" + " " * (l[2] - l[1]) + "+")
        elif l[2] - l[1] == 0:
            print(" " * l[0] + "*" + " " * (l[1] - l[0]) + ">")
        else:
            print(" " * l[0] + "*" + " " * (l[1] - l[0]) + "&" + " " * (l[2] - l[1]) + "+")
    # Вывод оси t и засечек
    print("-" * 160 + "-> t")
    k = max_value / 6
    l = int(k // (abs(max_value) / 100))
    print(" " * 20 + "0", end="")
    for i in range(1, 6):
        t = k * i
        print(" " * l + f"{t:.7g}", end="")
    # Вывод пояснений к обозначениям
    print("\nПояснение к обозначениям:")
    print("* - время сортировки упорядоченного массива")
    print("& - время сортировки случайного массива")
    print("+ - время сортировки обратноупорядоченного массива")
    print("< - совпадение времени работы сортировок на упорядоченном и случайном массивах")
    print("> - совпадение времени работы сортировок на случайном и обратноупорядоченном массивах")
    print("^ - совпадение времени работы сортировок на всех тестовых массивах")
