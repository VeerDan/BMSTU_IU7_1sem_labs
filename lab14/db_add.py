import struct


def n(db):
    """
    Функция подсёта количества записей в БД
    :param db: (str) - имя файла с БД
    :return: (int) - количество записей в БД
    """
    with open(db, "rb") as f:
        f.read(150)
        i = 0
        while f.read(100):
            i += 1
    return i


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


def base_input():
    """
    Функция для записи данных в базу данных
    :return: (list) - значения столбцов новой записи в БД
    """
    c = []
    for i in ["фамилия", "имя", "отчество", "возраст", "средний балл"]:
        if i in ["фамилия", "имя", "отчество"]:
            t = str_input(i).strip()
        elif i == "возраст":
            t = age_input()
        else:
            t = float_input()
        c.append(t)
    return c


def add(filename, position):
    """
    Функция добавления в базу данных записи под номером position
    :param filename: (str) - имя файла с БД
    :param position: (int) - номер позиции для добавления
    :return: None
    """
    count = n(filename)
    if position <= 0 or count + 1 < position:
        raise IndexError
    c = base_input()
    t1, t2, t3, t4, t5 = [i for i in c]
    t1, t2, t3 = [i.encode('utf-8') for i in [t1, t2, t3]]
    t4 = int(t4)
    t5 = float(t5)
    s = struct.pack("=30s30s30sif", t1, t2, t3, t4, t5)
    with open(filename, "r+b") as f:
        f.read(150)
        i = 0
        found = False
        temp_position = 150
        temp = None
        while p := f.read(98):
            i += 1
            if i == position:
                found = True
                f.seek(temp_position)
                f.write(s)
                temp = p
            elif found:
                f.seek(temp_position)
                f.write(temp)
                temp = p
            temp_position += 98
        if temp is None:
            f.write(s)
        else:
            f.write(temp)


def delete(filename, position):
    """
    Функция удаляет запись из БД под номером position
    :param filename: (str) - имя файла с БД
    :param position: (int) - номер позиции для удаления
    :return: None
    """
    if position <= 0 or n(filename) < position:
        raise IndexError
    with open(filename, "r+b") as f:
        f.read(150)
        i = 0
        temp_position = 150
        found = False
        while f.read(98):
            i += 1
            if i == position:
                found = True
            if found:
                temp = f.read(98)
                f.seek(temp_position)
                f.write(temp)
            temp_position += 98
        f.seek(temp_position - 196)
        f.truncate()
