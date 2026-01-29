from random import randint


def quicksort(arr: list[int]) -> None:
    """
    Функция, реализующая quicksort без использования рекурсии.
    Сортирует и изменяет изначальный массив.
    :param arr: list[int] - список для сортировки
    :return: None
    """
    stack = list()
    stack.append((0, len(arr) - 1))
    while stack:
        start, end = stack.pop()
        if start < end:
            pivot = arr[end]
            i = start - 1  # последний элемент, меньший pivot
            for j in range(start, end):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[end] = arr[end], arr[i + 1]
            stack.append((start, i))
            stack.append((i + 2, end))


p = [randint(-2, 2) for i in range(20)]
print(*p)
quicksort(p)
print(*p)
