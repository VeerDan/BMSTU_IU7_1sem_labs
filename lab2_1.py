'''
Автор: Андреев Игорь Николаевич
Группа: ИУ7-14Б
Вариант 5
'''
# Импорт необходимых библиотек
from math import log10, sqrt

# Ввод данных
x = input("Введите значение x: ").strip()

# Проверка введённых данных
al = "0123456789+-eE."
is_a_number = True
dot_count = 0
e_count = 0
for i in range(len(x)):
    if x[i] == ".":
        dot_count += 1
    if dot_count > 1:
        is_a_number = False
        break
    if x[i] in "eE":
        e_count += 1
        if i == 0 or i == len(x) - 1 or e_count > 1:
            is_a_number = False
            break
    if x[i] not in al:
        is_a_number = False
        break
    if x[i] in "+-" and (i > 0 and x[i - 1] != "e" or i == len(x) - 1):
        is_a_number = False
        break

if is_a_number:
    x = float(x)
    # Проверка значений за областью определения
    if x <= -5:
        print("Функция не определена!")
    else:
        # Решение
        if x <= -4:
            y = -log10(x + 5)
        elif x < 0:
            y = sqrt(4 - (x + 2) ** 2)
        elif x <= 4:
            y = sqrt(x)
        else:
            y = -x + 6
        # Вывод данных
        print(f"f(x) = {y:.7g}")
else:
    print("Введённые данные не являются числом!")
