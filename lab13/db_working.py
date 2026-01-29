def print_db(db: str):
    """
    Функция печати базы данных в stdin
    :param db: (str) - название имени файла бащы данных
    :return:
    """
    maximum = [-1, -1, -1, -1, -1, -1]
    count = 0
    with open(db, "r") as f:
        while t := f.readline():
            c = 0
            for i in t.split("\t"):
                maximum[c] = max(maximum[c], len(i))
                c += 1
            count += 1
    with open(db, "r") as f:
        print("\n")
        while t := f.readline().strip():
            print("-" * (sum(maximum) + 7))
            c = 0
            print("|", end="")
            for i in t.split("\t"):
                print(f"{i:^{maximum[c]}}" + "|", end="")
                c += 1
            print()
        print("-" * (sum(maximum) + 7))
    print(f"Affected rows: {count - 1}")


def str_input(name):
    """
    Ввод строковой переменной с возращением ошибки
    :param name: (str) - имя переменной
    :return: (str) - введённая переменная
    """
    f = True
    t = ""
    while f:
        try:
            t = input(f"Введите значение для поля {name}: ").strip()
            if not t.isalpha():
                raise TypeError
        except TypeError:
            print("Неверный тип данных! Повторите ввод!")
        else:
            f = False
    return t


def age_input():
    """
    Ввод возраста
    :return: (int) - возраст
    """
    f = True
    t = ""
    while f:
        try:
            t = input(f"Введите значение для поля возраст: ")
            t = int(t)
            if t < 0:
                raise ValueError
        except ValueError:
            print("Неверный тип данных! Повторите ввод!")
        else:
            f = False
    return t


def float_input():
    """
    Ввод float
    :return: (float) - значение float
    """
    f = True
    t = ""
    while f:
        try:
            t = input(f"Введите значение для поля средний балл: ")
            t = float(t)
            if t < 0 or t > 100:
                raise ValueError
        except ValueError:
            print("Неверный тип данных! Повторите ввод!")
        else:
            f = False
    return t


def n_max(db):
    """
    Функция поиска максимального id
    :param db: (str) - имя файла с базой данных
    :return: (int) - макимальный id
    """
    res = 0
    with open(db, "r") as f:
        f.readline()
        for i in f:
            t = int(i.strip().split("\t")[0])
            res = max(res, t)
    return res


def add(db):
    """
    Функция добавления записи в конец базы данных
    :param db: (str) - имя файла с базой данных
    :return: (None)
    """
    with open(db, "r") as f:
        a = f.readline().strip().split("\t")
    n = n_max(db)
    c = [str(n + 1)]
    for i in a[1:]:
        t = ""
        if i in ["фамилия", "имя", "отчество"]:
            t = str_input(i)
        elif i == "возраст":
            t = age_input()
        else:
            t = float_input()
        c.append(str(t))
    with open(db, "a") as f:
        for i in range(len(c)):
            f.write(c[i])
            if i != 5:
                f.write("\t")
        f.write("\n")


if __name__ == "__main__":
    print_db("base.txt")
    add("base.txt")
    print_db("base.txt")
