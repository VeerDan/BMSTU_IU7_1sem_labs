from initialization import file_choose, init
from db_working import add, print_db
from search import one_field_search, two_fields_search
from sort import one_filed_sort, two_fields_sort


def cmd_input():
    """
    Ввод команды для взаимодействия
    :return: (int) - номер команды
    """
    f = True
    c = 0
    while f:
        try:
            c = int(input("Введите номер команды для работы с базами данных: "))
            if not (0 <= c <= 8):
                raise ValueError
        except ValueError:
            print("Неверный тип входных данных! Повторите ввод!")
        else:
            f = False
    return c


def menu():
    """
    Печать меню для работы с базыми данных
    :return: (None)
    """
    print("\nКоманды для работы с базами данных:\n"
          "0. Завершение работы программы\n"
          "1. Выбрать файл для работы.\n"
          "2. Инициализировать базу данных.\n"
          "3. Вывести содержимое базы данных.\n"
          "4. Добавить запись в конец базы данных.\n"
          "5. Поиск по выбранному полю.\n"
          "6. Поиск по двум выбранным полям.\n"
          "7. Упорядочить базу данных по выбранному полю.\n"
          "8. Упорядочить базу данных по двум выбранным полям.\n")


def dec_input():
    """
    Ввод по возрастанию или убыванию
    :return: (bool)
    """
    f = True
    res = 0
    while f:
        try:
            res = int(input("Введите 0, если хотите упорядочить в порядке неубывания, "
                            "1 - в порядке невозрастания: ").strip())
            if res != 0 and res != 1:
                raise ValueError
        except ValueError:
            print("Неверные входные данные! Повторите ввод!")
        else:
            f = False
    return bool(res)


def cmd(filename, initial):
    """
    Функция взаимдействия с баззой данных по командам
    :param filename: (str) - имя файла с базой данных
    :param initial: (bool) - инициализирована ли база данных
    :return: int | str
    """
    menu()
    c = cmd_input()
    match c:
        case 0:
            pass
        case 1:
            return file_choose()
        case 2:
            init(filename)
        case 3:
            if initial:
                print_db(filename)
            else:
                print("База данных не инициализирована!")
        case 4:
            if initial:
                add(filename)
            else:
                print("База данных не инициализирована!")
        case 5:
            if initial:
                one_field_search(filename)
            else:
                print("База данных не инициализирована!")
        case 6:
            if initial:
                two_fields_search(filename)
            else:
                print("База данных не инициализирована!")
        case 7:
            if initial:
                d = dec_input()
                one_filed_sort(filename, desc=d)
            else:
                print("База данных не инициализирована!")
        case 8:
            if initial:
                d = dec_input()
                two_fields_sort(filename, desc=d)
            else:
                print("База данных не инициализирована!")
    return c
