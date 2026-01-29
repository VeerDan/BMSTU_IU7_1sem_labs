import os.path

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
    elif filename in ["input.txt", "temp.txt", "database.txt"]:
        f = False
    elif ".txt" not in filename:
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
    with open(filename, "w"):
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
    with open(filename, "w") as f:
        with open(input_file, "r") as inp:
            while s := inp.readline():
                f.write(s)
    print("База данных инициализирована успешно!")


if __name__ == "__main__":
    file = file_choose()
    init(file)
