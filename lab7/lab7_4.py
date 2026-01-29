'''
Автор: Андреев Игорь Николаевич
Группа: ИУ7-14Б
Задание 4. Вариант: 3.
'''
# Ввод данных
n = int(input("Введите размер массива: "))
# Проверка на корректность ввода длины массива
if n < 0:
    print("\nОтрицательная длина массива!")
    exit()
elif n == 0:
    print("\nПустой массив!")
    exit()
# Создание массива и ввод значений в него
a = [""] * n
for i in range(n):
    a[i] = input("Введите {}-й элемент: ".format(i+1))

# Решение
for i in range(len(a)):
    res = ""
    for j in range(len(a[i])):
        tmp = a[i][j].lower()
        if 'a' <= tmp <= 'z' and tmp not in "aeuio":
            res += tmp  # chr(ord(a[i][j]) + 32)
        else:
            res += a[i][j]
    a[i] = res

# Вывод данных
print("\nОтредактированный массив:")
for (i, el) in enumerate(a):
    print("{}-й элемент массива: {}".format(i + 1, el))
