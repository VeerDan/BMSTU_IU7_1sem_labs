import struct

FILE = "def.bin"

with open(FILE, "wb") as f:
    inp = list(map(int, input().split()))
    f.write(struct.pack(f"=i{'q' * (inp[0] * inp[0])}", *inp))

with open(FILE, "r+b") as f:
    n = struct.unpack("i", f.read(4))[0]
    pos = f.tell()
    i = 0
    j = -1
    f1 = False
    f2 = False
    while p := f.read(8):
        j += 1
        if i == j:
            el1 = p
            f1 = True
            p1 = pos
        if i + j == n - 1:
            el2 = p
            f2 = True
            p2 = pos
        if f1 and f2:
            f.seek(p1)
            f.write(el2)
            f.seek(p2)
            f.write(el1)
            f1 = False
            f2 = False
        if j + 1 == n:
            j = -1
            i += 1
        pos += 8
        f.seek(pos)

print("\nИзменённое содержимое:")
with open(FILE, "rb") as f:
    n = struct.unpack("i", f.read(4))[0]
    i = 0
    while p := f.read(8):
        t = struct.unpack("q", p)[0]
        print(t, end=" ")
        i += 1
        if i == n:
            print()
            i = 0
