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
        cur = struct.unpack("i", p)[-1]
        position += 4
        start = position - 8
        if start >= 0:
            f.seek(-8, 1)
            flag = True
            while start >= 0 and flag:
                temp = struct.unpack("i", q := f.read(4))[-1]
                if temp > cur:
                    f.seek(-4, 1)
                    f.write(p)
                    f.write(q)
                else:
                    flag = False
                start -= 4
                if start >= 0:
                    f.seek(start)
        f.seek(position)

print("\nИзменённое содержимое:")
with open(FILE, "rb") as f:
    while p := f.read(4):
        t = struct.unpack("i", p)[0]
        print(t)
