def left_align(text: list[str]) -> None:
    """
    Функция, реализующая равнение текста по левому краю. Изменяет исходный текст
    :param text: (list[str]) - текст, разбитый по строкам
    :return: None - функция меняет исходный текст
    """
    for i in range(len(text)):
        while "  " in text[i]:
            text[i] = text[i].replace("  ", " ")
        text[i] = text[i].lstrip(" ")


def right_align(text: list[str]) -> None:
    """
    Функция, реализующая выравнивание текста по правому карю. Ориентируется на строку с максимальной длиной.
    Изменяет исходный текст.
    :param text: (list[str]) - текст, разбитый по строкам
    :return: None - функция меняет исходный текст
    """
    for i in range(len(text)):
        while "  " in text[i]:
            text[i] = text[i].replace("  ", " ")
    # определение максимальной длины строки
    try:
        max_value = len(max(text, key=len))
    except ValueError:
        print("Ошибка! Пустой текст!")
    else:
        # форматирование текста
        for i in range(len(text)):
            text[i] = " " * (max_value - len(text[i])) + text[i]


def justify(text: list[str]) -> None:
    """
    Функция, реализующая выравнивание текста по ширине. Ориентируется на строку с максимальной длиной.
    Изменяет исходный текст.
    :param text: (list[str]) - текст, разбитый по строкам
    :return: None - функция меняет исходный текст
    """
    for i in range(len(text)):
        while "  " in text[i]:
            text[i] = text[i].replace("  ", " ")
        text[i] = text[i].strip(" ")
    # определение максимальной длины строки
    try:
        max_value = len(max(text, key=len))
    except ValueError:
        print("Ошибка! Пустой текст!")
    else:
        # форматирование текста
        for i in range(len(text)):
            t = max_value - len(text[i])
            q = text[i].count(" ")
            try:
                p = t // q
                rest = t % q
                j = 0
                while j < len(text[i]):
                    if text[i][j] == " " and text[i].rfind(" ") == j:
                        text[i] = text[i][:j + 1] + " " * (p + rest) + text[i][j + 1:]
                        j += p + rest
                    elif text[i][j] == " ":
                        text[i] = text[i][:j + 1] + " " * p + text[i][j + 1:]
                        j += p
                    j += 1
            except ZeroDivisionError:
                pass
