import struct

FILE = "ints.bin"

with open(FILE, "wb") as f:
    inp = True
    print("Если хотите завершить ввод нажмите Enter!")
    while inp:
        try:
            s = input("Введите число для добавления в файл: ")
            if not s:
                raise StopIteration
            s = int(s)
        except ValueError:
            print("Неверный типа данных! Повторите ввод!")
        except StopIteration:
            inp = False
        else:
            temp = struct.pack("i", s)
            f.write(temp)

with open(FILE, "r+b") as f:
    position = 0
    i = 0
    while p := f.read(4):
        position += 4
        t = struct.unpack("i", p)[0]
        if t == 0:
            i += 1
            while q := f.read(4):
                f.seek(-8, 1)
                f.write(q)
                f.write(p)
        f.seek(position)
    size = f.seek(0, 2)
    size -= i // 2 * 4
    f.truncate(size)

print("\nИзменённое содержимое:")
with open(FILE, "rb") as f:
    while p := f.read(4):
        t = struct.unpack("i", p)[0]
        print(t)
