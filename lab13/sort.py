from os import remove


def field_input():
    """
   Ввод поля для сортировки
   :return: (str) - имя поля для сортировки
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
    print("\nВыберете поле для сортировки:\n"
          "0. Фамилия\n"
          "1. Имя\n"
          "2. Отчество\n"
          "3. Возраст\n"
          "4. Средний балл")


def one_filed_sort(db, desc=False):
    """
    Сортировка по одному полю
    :param db: имя файла с базой данных
    :param desc: (bool) - по возрастанию или по убыванию
    :return: None
    """
    field_menu()
    c = field_input()
    res = []
    with open(db, "r") as f:
        f.readline()
        for i in f:
            t = i.strip().split("\t")
            if t[c + 1].isalpha():
                res.append((t[0], t[c + 1]))
            else:
                try:
                    res.append((t[0], int(t[c + 1])))
                except ValueError:
                    res.append((t[0], float(t[c + 1])))
    res.sort(key=lambda x: x[1], reverse=desc)
    with open("temp.txt", "w") as temp:
        with open(db, "r") as f:
            temp.write(f.readline())
        for i in res:
            with open(db, "r") as f:
                for j in f:
                    if j.strip().split("\t")[0] == i[0]:
                        temp.write(j.strip())
                        temp.write("\n")
    with open("temp.txt", "r") as temp:
        with open(db, "w") as f:
            for i in temp:
                f.write(i)
    remove("temp.txt")
    print("Упорядочивание завершено успешно!")


def two_fields_sort(db, desc=False):
    """
    Сортировка по двум полям
    :param db: имя файла с базой данных
    :param desc: (bool) - по возрастанию или по убыванию
    :return: None
    """
    print("Выберете сначала один параметр для сортировки, потом другой!")
    field_menu()
    c1 = field_input()
    field_menu()
    c2 = field_input()
    res = []
    with open(db, "r") as f:
        f.readline()
        for i in f:
            t = i.strip().split("\t")
            res.append((t[0], []))
            for c in [c1, c2]:
                if t[c + 1].isalpha():
                    res[-1][-1].append(t[c + 1])
                else:
                    try:
                        res[-1][-1].append(int(t[c + 1]))
                    except ValueError:
                        res[-1][-1].append(float(t[c + 1]))
    res.sort(key=lambda x: x[1], reverse=desc)
    with open("temp.txt", "w") as temp:
        with open(db, "r") as f:
            temp.write(f.readline())
        for i in res:
            with open(db, "r") as f:
                for j in f:
                    t = j.strip().split("\t")
                    if t[0] == i[0]:
                        temp.write(j.strip())
                        temp.write("\n")
    with open("temp.txt", "r") as temp:
        with open(db, "w") as f:
            for i in temp:
                f.write(i)
    remove("temp.txt")
    print("Упорядочивание завершено успешно!")
