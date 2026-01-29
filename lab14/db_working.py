import struct


def print_row(s):
    """
    Форматированная печать одной записи БД
    :param s: (tuple) - распакованная запись базы данных
    :return: None
    """
    for i in s:
        try:
            p = i.strip(b'\x00')
            print(f"|{p.decode('utf-8'):^15}", end="")
        except AttributeError:
            if type(i) is int:
                print(f"|{i:^15}", end="")
            else:
                print(f"|{i:^15.2f}", end="")
    print("|")


def print_db(filename):
    """
    Форматированная печать базу данных
    :param filename: (str) - имя файла с базой данных
    :return: None
    """
    count = 0
    with open(filename, "rb") as f:
        s = struct.unpack("=30s30s30s30s30s", f.read(150))
        print("-" * 82)
        print_row(s)
        while p := f.read(98):
            s = struct.unpack("=30s30s30sif", p)
            print("-" * 82)
            print_row(s)
            count += 1
        print("-" * 82)
        print(f"Affected rows: {count}")


if __name__ == "__main__":
    print_db("a.bin")
