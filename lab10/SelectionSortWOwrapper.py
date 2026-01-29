from time import time


def selection_sort(a: list) -> (list, int, float):
    """
    Функция реализует сортировку заданного массива методом простого выбора
    :param a: массив, который требуется отсортировать
    :return: a - отсортированный массив
             c - количество перестановок в массиве во время сортировки
             elapsed_time - время работки сортировки
    """
    c = 0
    n = len(a)
    start_time = time()
    for i in range(1, n):
        cur = a[i]
        j = i - 1
        while j >= 0 and cur < a[j]:
            a[j + 1] = a[j]
            c += 1
            j -= 1
        a[j + 1] = cur
    end_time = time()
    elapsed_time = end_time - start_time
    return a, c, elapsed_time
