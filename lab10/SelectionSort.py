from time import time


class SortResult:
    """
    Класс предоставляет результат работы функции сортировки с расширением

    Атрибуты:
        a (list): отсортированный массив
        c (int): количество перестановок во время сортировки
        elapsed_time (float): время работы сортировки
    """
    def __init__(self, a=None, c=None, elapsed_time=None):
        """
        Инициализирует объект класса
        :param a: (list) отсортированный список
        :param c: (int) количество перестановок во время сортировки
        :param elapsed_time: (float) время работы сортировки
        """
        self.a = a
        self.c = c
        self.elapsed_time = elapsed_time

    def __getitem__(self, item):
        """
        Обращение к атрибутам объекта по индексу
            self.a имеет индекс 0
            self.c имеет индекс 1
            self.elapsed_time индекс 2
        :param item: индекс элемента
        :return: элемент по item
        """
        t = [self.a, self.c, self.elapsed_time]
        return t[item]

    def __iter__(self):
        """
        возвращает генератор атрибутов объекта класса
        :return: generator
        """
        for i in [self.a, self.c, self.elapsed_time]:
            yield i


def time_wrapper(func):
    """
    Декоратор, который засекает время выполнения функции сортировки
    :param func: функция сортировки
    :return: функция, засекающая время исполнения функции
    """
    def time_note(a: list) -> SortResult:
        """
        Функция, засекающая время исполнения функции сортировки
        :param a: список для сортировки
        :return: a - отсортированный список
                 c - количество перестановок
                 elapsed_time - время исполнения функции
        """
        time_start = time()
        res = func(a)
        time_end = time()
        elapsed_time = time_end - time_start
        res.elapsed_time = elapsed_time
        return res
    return time_note


@time_wrapper
def selection_sort(a: list) -> SortResult:
    """
    Функция реализует сортировку заданного массива методом простого выбора
    :param a: массив, который требуется отсортировать
    :return: a - отсортированный массив
             c - количество перестановок в массиве во время сортировки
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
    return SortResult(a=a, c=c)
