from db_working import print_db
from os import remove


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
    :return: (int, str) - номер поля и значения поиска
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
    return c, str(searching_for)


def two_fields_search_input():
    print("Сначала выберете первое поле для поиска и значение для поиска, потом второе!")
    c1, s1 = one_field_search_input()
    c2, s2 = one_field_search_input()
    return c1, s1, c2, s2


def one_field_search(db):
    c, s = one_field_search_input()
    with open(db, "r") as f:
        with open("temp.txt", "w") as res:
            res.write(f.readline())
            for i in f:
                if i.strip().split("\t")[c + 1] == s:
                    res.write(i)
    print_db("temp.txt")
    remove("temp.txt")


def two_fields_search(db):
    c1, s1, c2, s2 = two_fields_search_input()
    with open(db, "r") as f:
        with open("temp.txt", "w") as res:
            res.write(f.readline())
            for i in f:
                t = i.strip().split("\t")
                if t[c1 + 1] == s1 and t[c2 + 1] == s2:
                    res.write(i)
    print_db("temp.txt")
    remove("temp.txt")


if __name__ == "__main__":
    # one_field_search("input.txt")
    two_fields_search("input.txt")
