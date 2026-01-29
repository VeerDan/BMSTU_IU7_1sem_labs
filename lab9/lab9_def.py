from matrix import matrix_input, matrix_print

a = matrix_input()
n, m = len(a), len(a[0])

c = 0

if n == 1:
    for j in range(m - 1):
        i = -1
        t1, t3 = a[i][j], a[i][j + 1]
        if t1 < 0 and t3 < 0:
            a[i][j] *= -1
            a[i][j + 1] *= -1
            c += 1
        elif t1 < 0:
            if abs(t1) > t3:
                a[i][j] *= -1
                a[i][j + 1] *= -1
                c += 1
    if a[-1][-1] < 0:
        t1 = a[-1][-1]
        t2 = a[-1][-2]
        if t2 < 0:
            a[-1][-1] *= -1
            a[-1][-2] *= -1
            c += 1
        elif t1 < 0:
            if abs(t1) > t2:
                a[-1][-1] *= -1
                a[-1][-2] *= -1
                c += 1
elif m == 1:
    for i in range(n - 1):
        j = -1
        t1, t2 = a[i][j], a[i + 1][j]
        if t1 < 0 and t2 < 0:
            a[i][j] *= -1
            a[i + 1][j] *= -1
            c += 1
        elif t1 < 0:
            if abs(t1) > t2:
                a[i][j] *= -1
                a[i + 1][j] *= -1
                c += 1
    if a[-1][-1] < 0:
        t1 = a[-1][-1]
        t3 = a[-2][-1]
        if t3 < 0:
            a[-1][-1] *= -1
            a[-2][-1] *= -1
            c += 1
        elif t1 < 0:
            if abs(t1) > t3:
                a[-1][-1] *= -1
                a[-2][-1] *= -1
                c += 1
else:
    for i in range(n - 1):
        for j in range(m - 1):
            t1, t2, t3 = a[i][j], a[i + 1][j], a[i][j + 1]
            if t1 < 0 and t2 < 0:
                a[i][j] *= -1
                a[i + 1][j] *= -1
                c += 1
            elif t1 < 0 and t3 < 0:
                a[i][j] *= -1
                a[i][j + 1] *= -1
                c += 1
            elif t1 < 0:
                if abs(t1) > t2:
                    a[i][j] *= -1
                    a[i + 1][j] *= -1
                    c += 1
                elif abs(t1) > t3:
                    a[i][j] *= -1
                    a[i][j + 1] *= -1
                    c += 1

    for i in range(n - 1):
        j = -1
        t1, t2 = a[i][j], a[i + 1][j]
        if t1 < 0 and t2 < 0:
            a[i][j] *= -1
            a[i + 1][j] *= -1
            c += 1
        elif t1 < 0:
            if abs(t1) > t2:
                a[i][j] *= -1
                a[i + 1][j] *= -1
                c += 1

    for j in range(m - 1):
        i = -1
        t1, t3 = a[i][j], a[i][j + 1]
        if t1 < 0 and t3 < 0:
            a[i][j] *= -1
            a[i][j + 1] *= -1
            c += 1
        elif t1 < 0:
            if abs(t1) > t3:
                a[i][j] *= -1
                a[i][j + 1] *= -1
                c += 1

    if a[-1][-1] < 0:
        t1 = a[-1][-1]
        t2 = a[-1][-2]
        t3 = a[-2][-1]
        if t2 < 0:
            a[-1][-1] *= -1
            a[-1][-2] *= -1
            c += 1
        elif t3 < 0:
            a[-1][-1] *= -1
            a[-2][-1] *= -1
            c += 1
        elif t1 < 0:
            if abs(t1) > t2:
                a[-1][-1] *= -1
                a[-1][-2] *= -1
                c += 1
            elif abs(t1) > t3:
                a[-1][-1] *= -1
                a[-2][-1] *= -1
                c += 1

s = 0
for i in range(n):
    for j in range(m):
        s += a[i][j]

print(c, s)
