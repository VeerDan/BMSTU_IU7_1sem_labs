from matrix import matrix_input

m = matrix_input(square=True)
n = len(m)
# n = 10
# m = [[n * j + i for i in range(n)] for j in range(n)]
# print(m[-5][9])
# m[-5][9] = 10

t = None
for i in range(n):
    for j in range(n):
        i_t, j_t = int(abs(m[i][j]) // n) % n, int(abs(m[i][j]) % n)
        if m[i_t][j_t] < 0:
            t = m[i][j]
        else:
            m[i_t][j_t] *= (-1)

t0 = None
for i in range(n):
    for j in range(n):
        if m[i][j] > 0:
            t0 = n * i + j

print(f"Повторяющийся элемент: {abs(int(t))}")
print(f"Недостоющий элемент: {t0 if t0 else n ** 2}")
