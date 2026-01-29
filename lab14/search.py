import struct
from db_working import print_row, print_db


def field_input():
    """
    Ввод поля для поиска
    :return: (str) - имя поля для поиска
    """
    f = True
    c = 0
    while f:
        try:
            c = int(input("Введите цифру, под которой идёт нужный критерий: "))
            if not (0 <= c <= 4):
                raise ValueError
        except ValueError:
            print("Неверный тип входных данных! Повторите ввод!")
        else:
            f = False
    return c


def field_menu():
    """
    Печать меню полей
    :return: (None)
    """
    print("\nВыберете поле для поиска:\n"
          "0. Фамилия\n"
          "1. Имя\n"
          "2. Отчество\n"
          "3. Возраст\n"
          "4. Средний балл")


def age_input():
    """
    Ввод возраста
    :return: (int)
    """
    f = True
    t = ""
    while f:
        try:
            t = input(f"Введите значение для поиска: ")
            t = int(t)
            if t < 0:
                raise ValueError
        except ValueError:
            print("Неверный тип данных! Повторите ввод!")
        else:
            f = False
    return t


def str_input():
    """
    Ввод строковой переменной
    :return: (str)
    """
    f = True
    t = ""
    while f:
        try:
            t = input(f"Введите значение для поиска: ").strip()
            if not t.isalpha():
                raise TypeError
        except TypeError:
            print("Неверный тип данных! Повторите ввод!")
        else:
            f = False
    return t


def float_input():
    """
    Ввод float
    :return: (float)
    """
    f = True
    t = ""
    while f:
        try:
            t = input(f"Введите значение для поиска: ")
            t = float(t)
            if t < 0 or t > 100:
                raise ValueError
        except ValueError:
            print("Неверный тип данных! Повторите ввод!")
        else:
            f = False
    return t


def one_field_search_input():
    """
    Ввод аргументов для поиска по одному полю
    :return: (int, any) - номер поля и значения поиска
    """
    field_menu()
    c = field_input()
    searching_for = ""
    match c:
        case 0 | 1 | 2:
            searching_for = str_input()
        case 3:
            searching_for = age_input()
        case 4:
            searching_for = float_input()
    return c, searching_for


def one_field_search(filename):
    """
    Функция поиска по одному полю
    :param filename: (str) - имя файла с БД
    :return: (None) - результат печатается на экран
    """
    c, s = one_field_search_input()
    found = False
    count = 0
    with open(filename, "rb") as f:
        temp = struct.unpack("30s30s30s30s30s", f.read(150))
        print("-" * 82)
        print_row(temp)
        while p := f.read(100):
            temp = struct.unpack("30s30s30sif", p)
            flag = False
            if 0 <= c <= 2 and temp[c].strip(b"\x00").decode("utf-8") == s:
                flag = True
            elif temp[c] == s:
                flag = True
            if flag:
                print("-" * 82)
                print_row(temp)
                found = True
                count += 1
        print("-" * 82)
        print(f"Affected rows: {count}")


def two_fields_search_input():
    """
    Ввод аргументов для поиска по двум полям
    :return: (int, anyб, int, any) - номер полей и значения поиска
    """
    print("Сначала выберете первое поле для поиска и значение для поиска, потом второе!")
    c1, s1 = one_field_search_input()
    c2, s2 = one_field_search_input()
    return c1, s1, c2, s2


def two_field_search(filename):
    """
    Функция поиска по двум полям
    :param filename: (str) - имя файла с БД
    :return: (None) - результат печатается на экран
    """
    c1, s1, c2, s2 = two_fields_search_input()
    found = False
    count = 0
    with open(filename, "rb") as f:
        temp = struct.unpack("30s30s30s30s30s", f.read(150))
        print("-" * 82)
        print_row(temp)
        while p := f.read(100):
            temp = struct.unpack("30s30s30sif", p)
            f1 = False
            f2 = False
            if 0 <= c1 <= 2 and temp[c1].strip(b"\x00").decode("utf-8") == s1:
                f1 = True
            elif temp[c1] == s1:
                f1 = True
            if 0 <= c2 <= 2 and temp[c2].strip(b"\x00").decode("utf-8") == s2:
                f2 = True
            elif temp[c2] == s2:
                f2 = True
            if f1 and f2:
                found = True
                count += 1
                print("-" * 82)
                print_row(temp)
        print("-" * 82)
        print(f"Affected rows: {count}")


if __name__ == "__main__":
    two_field_search("a.bin")
    print_db("a.bin")
