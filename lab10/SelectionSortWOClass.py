from time import time


def time_wrapper(func):
    """
    Декоратор, который засекает время выполнения функции сортировки
    :param func: функция сортировки
    :return: функция, засекающая время исполнения функции
    """
    def time_note(a: list) -> (list, int, float):
        """
        Функция, засекающая время исполнения функции сортировки
        :param a: список для сортировки
        :return: a - отсортированный список
                 c - количество перестановок
                 elapsed_time - время исполнения функции
        """
        time_start = time()
        a, c = func(a)
        time_end = time()
        elapsed_time = time_end - time_start
        return a, c, elapsed_time
    return time_note


@time_wrapper
def selection_sort(a: list) -> (list, int):
    """
    Функция реализует сортировку заданного массива методом простого выбора
    :param a: массив, который требуется отсортировать
    :return: list[int] - отсортированный массив
             int - количество перестановок в массиве во время сортировки
    """
    c = 0
    n = len(a)
    for i in range(1, n):
        cur = a[i]
        j = i - 1
        while j >= 0 and cur < a[j]:
            a[j + 1] = a[j]
            c += 1
            j -= 1
        a[j + 1] = cur
    return a, c
