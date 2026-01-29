import os.path
import struct

INPUT_FILE = "input.txt"


# Функция проверки корректность имени файла
def filename_check(filename: str) -> bool:
    """
    Проверяет введённое имя файла на правильность. input.txt, temp.txt, database.txt - зарезервированы
    :param filename: (имя файла)
    :return: (bool)
    """
    if any(i in filename for i in r"\/:?*"):
        f = False
    elif ".bin" not in filename:
        f = False
    else:
        f = True
    return f


# Функция ввода имени файла
def filename_input() -> str:
    """
    Ввод имени файла с проверкой
    :raise: TypeError - не соответсвие имени файла
    :return: (str) - имя файла
    """
    filename = input("Введите имя файла для работы: ").strip()
    if not filename_check(filename):
        raise TypeError
    return filename


# Функция выбора файла
def file_choose():
    """
    Ввод имени файла с проверкой. Ввод продолжается пока не будет введено корректное имя файла.
    :return: (str) - имя файла
    """
    f = True
    filename = ""
    while f:
        try:
            filename = filename_input()
        except TypeError:
            print("Недопустимое имя файла! Пвторите ввод!")
        else:
            if not os.path.exists(filename):
                f = False
            else:
                c = input("Файл уже существует! "
                          "Введите 1, если хотите перезаписать его, или любой другой символ, "
                          "если хотите выбрать другой файл: ")
                c = c.strip()
                if c == "1":
                    f = False
                else:
                    print("Выберет другой файл для работы!")
    with open(filename, "wb"):
        pass
    print(f"Успешно выбран файл: {filename}!")
    return filename


# Инициализация БД
def init(filename, input_file=INPUT_FILE):
    """
    Функция инициализации базы данных
    :param filename: (str) - имя файла
    :param input_file: (str) - имя файла с входными данными
    :return: (None)
    """
    with open(filename, "wb") as f:
        with open(input_file, "r") as inp:
            i = 0
            while s := inp.readline().strip():
                if i == 0:
                    t1, t2, t3, t4, t5 = [i.encode('utf-8') for i in s.split("\t")]
                    f.write(struct.pack("=30s30s30s30s30s", t1, t2, t3, t4, t5))
                else:
                    t1, t2, t3, t4, t5 = [i for i in s.split("\t")]
                    t1, t2, t3 = [i.encode('utf-8') for i in [t1, t2, t3]]
                    t4 = int(t4)
                    t5 = float(t5)
                    f.write(struct.pack("=30s30s30sif", t1, t2, t3, t4, t5))
                i += 1
    print("База данных инициализирована успешно!")


if __name__ == "__main__":
    file = file_choose()
    init(file)
