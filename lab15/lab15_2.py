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
    while p := f.read(4):
        position += 4
        t = struct.unpack("i", p)[0]
        print(t)
        if t % 2 == 1:
            t *= 2
            t = struct.pack("i", t)
            f.seek(0, 2)
            f.write(t)
            start = f.tell() - 4
            while start != position:
                f.seek(-8, 1)
                t, p = f.read(4), f.read(4)
                f.seek(-8, 1)
                f.write(p)
                f.write(t)
                start -= 4
                f.seek(-4, 1)
            position += 4
        f.seek(position)

print("\nИзменённое содержимое:")
with open(FILE, "rb") as f:
    while p := f.read(4):
        t = struct.unpack("i", p)[0]
        print(t)
