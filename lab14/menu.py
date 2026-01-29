from initialization import file_choose, init
from db_working import print_db
from search import one_field_search, two_field_search
from db_add import add, delete


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
            if not (0 <= c <= 7):
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
          "4. Добавить запись по индексу.\n"
          "5. Удалить запись из базы данных по индексу.\n"
          "6. Поиск по выбранному полю.\n"
          "7. Поиск по двум выбранным полям.\n")


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
                ind = int(input("Введите индекс для вставки записи: "))
                try:
                    add(filename, ind)
                except IndexError:
                    print("Введён недопустимый индекс!")
            else:
                print("База данных не инициализирована!")
        case 5:
            if initial:
                ind = int(input("Введите индекс для удаления записи: "))
                try:
                    delete(filename, ind)
                except IndexError:
                    print("Введён недопустимый индекс!")
            else:
                print("База данных не инициализирована!")
        case 6:
            if initial:
                one_field_search(filename)
            else:
                print("База данных не инициализирована!")
        case 7:
            if initial:
                two_field_search(filename)
            else:
                print("База данных не инициализирована!")
    return c
