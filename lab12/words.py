def delete_word(text: list[str], word: str) -> None:
    """
    Функция, реализующая удаление всех вхождений слова в тексте. Изменяет исходный текст.
    :param text: (list[str]) - текст, разбитый по строкам
    :param word: слово , которое необходимо удалить
    :return: None - функция меняет исходный текст
    """
    t = ""
    start = -1
    c = 0
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j].isalpha():
                t += text[i][j]
                if start == -1:
                    start = j
            elif t == word:
                text[i] = text[i][:start] + " " * (j - start + 1) + text[i][j+1:]
                t = ""
                start = -1
                c += 1
            else:
                t = ""
                start = -1
        if t == word:
            text[i] = text[i][:start] + " "
            c += 1
    print(f"\nПроизведено {c} удалений!")


def replace_word(text: list[str], word: str, replacement_word: str) -> None:
    """
    Функция, реализующая замену всех вхождений слова в тексте на другое. Изменяет исходный текст.
    :param text: (list[str]) - текст, разбитый по строкам
    :param word: слово , которое необходимо заменить
    :param replacement_word: слово, на которое необходимо заменить
    :return: None - функция меняет исходный текст
    """
    t = ""
    start = -1
    c = 0
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j].isalpha():
                t += text[i][j]
                if start == -1:
                    start = j
            elif t == word or t == word[:1].upper() + word[1:]:
                text[i] = text[i][:start] + "@" * (j - start) + text[i][j:]
                t = ""
                start = -1
                c += 1
            else:
                t = ""
                start = -1
        if t == word or t == word[:1].upper() + word[1:]:
            text[i] = text[i][:start] + "@" * len(word)
            c += 1
    for i in range(len(text)):
        text[i] = text[i].replace("@" * len(word), replacement_word)
    print(f"\nПроизведено {c} замен!")
