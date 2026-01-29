def get_sentences(text):
    """

    :param text:
    :return:
    """
    res = []
    start = [0, 0]
    for i in range(len(text)):
        end = [i, 0]
        for j in range(len(text[i])):
            if text[i][j] in ".?!":
                res.append([start, end])
                start = [end[0], end[1] + 1]
                end = [end[0], end[1] + 1]
            else:
                end[-1] += 1
    return res


def search(text):
    """
    Предложение с самым коротким словом
    :param text:
    :return:
    """
    temp = get_sentences(text)
    minimum = []
    for t in temp:
        i_start = t[0][0]
        j_start = t[0][1]
        i_end = t[1][0]
        j_end = t[1][1]
        i = i_start
        j = j_start
        res = ""
        while i < i_end or j <= j_end and i == i_end:
            if text[i][j].isalpha():
                res += text[i][j]
            else:
                if minimum and len(res) and len(res) < minimum[0]:
                    minimum = [len(res), t]
                elif not minimum:
                    minimum = [len(res), t]
                res = ""
            if j + 1 == len(text[i]):
                i += 1
                j = 0
            else:
                j += 1
    return minimum


def print_sentence(text, formatting=None):
    try:
        borders = search(text)
        i = borders[1][0][0]
        j = borders[1][0][1]
        i_end = borders[1][1][0]
        j_end = borders[1][1][1]
    except IndexError:
        print("Ошибка! Пустой текст!")
    else:
        while i < i_end or j <= j_end and i == i_end:
            if formatting is None:
                print(text[i][j], end="")
            else:
                print(f"{formatting}{text[i][j]}", end="")
            text[i] = text[i][:j] + " " + text[i][j + 1:]
            if j + 1 == len(text[i]):
                i += 1
                j = 0
                print()
            else:
                j += 1
        print()
        i = borders[1][0][0]
        i_end = borders[1][1][0]
        while i < i_end:
            while "  " in text[i]:
                text[i] = text[i].replace("  ", " ")
            i += 1
        if text:
            delete_empty_lines(text)


def delete_empty_lines(text):
    for i in range(len(text) - 1):
        if text[i].strip():
            continue
        text[i], text[i + 1] = text[i + 1], text[i]
    while not text[-1].strip():
        del text[-1]
        if not text:
            break


if __name__ == "__main__":
    with open("text.txt", "r") as f:
        a = [i.strip() for i in f]
    print_sentence(a, "\033[32m")
    print_sentence(a, "\033[32m")
