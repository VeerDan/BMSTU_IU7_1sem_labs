def parsing(text: list[str]) -> list[list[list[int]]]:
    """
    Функция реализует получение границ арифметических выражений в тексте
    :param text: list[str]
    :return: list[list[list[int]]] - спиок границ арифметических выражений.
                                     Левая и правая границы описываются парой чисел типа (номер строки, номер символа)
    """
    res = []
    l = -1
    t = ""
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] in "012345689-+*/() ":
                if not t:
                    l = (i, j)
                t += text[i][j]
            elif t != " " and t:
                r = (i, j - 1)
                res.append([t, l, r])
                t = ""
            else:
                t = ""
    return res


def expr_eval(s):
    s = str_to_list_expr(s)
    s = to_rpn(s)
    res = calc(s)
    return res


def str_to_list_expr(s: str):
    """
    Функция, представляющая выражение
    :param s:
    :return:
    """
    s = s.replace(" ", "")
    res = []
    temp = ""
    for i in s:
        if i not in "0123456789" and temp:
            res.append(temp)
            temp = ""
        if i not in "0123456789":
            res.append(i)
        else:
            temp += i
    if temp:
        res.append(temp)
    return res


def to_rpn(expression: list[str]):
    d = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '~': 3,
        '@': 3
    }
    res = []
    stack = []
    for i in range(len(expression)):
        if expression[i].isnumeric():
            res.append(int(expression[i]))
        elif expression[i] == '(':
            stack.append("(")
        elif expression[i] == ')':
            while len(stack) and stack[-1] != "(":
                res.append(stack.pop())
            if len(stack):
                stack.pop()
        elif expression[i] in d:
            if expression[i] == "-" and (i == 0 or i >= 1 and expression[i - 1] in d):
                expression[i] = "~"
            if expression[i] == "+" and (i == 0 or i >= 1 and expression[i - 1] in d):
                expression[i] = "@"
            while len(stack) and d[stack[-1]] > d[expression[i]]:
                res.append(stack.pop())
            stack.append(expression[i])
    while len(stack):
        res.append(stack.pop())
    return res


def calc(rpn_exp):
    stack = []
    for i in rpn_exp:
        if type(i) is int:
            stack.append(i)
        else:
            t = 0
            match i:
                case "*":
                    y, x = stack.pop(), stack.pop()
                    t = x * y
                case "-":
                    y, x = stack.pop(), stack.pop()
                    t = x - y
                case "+":
                    y, x = stack.pop(), stack.pop()
                    t = x + y
                case "/":
                    y, x = stack.pop(), stack.pop()
                    t = x / y
                case "~":
                    x = stack.pop()
                    t = -x
                case "@":
                    x = stack.pop()
                    t = x
            stack.append(t)
    return stack[0]


def expr_replace(text: list[str]) -> None:
    """
    Функция, реализующая замену арифметических выражений на их значения в рабочем тексте. Меняет исходный текст.
    :param text: list[str] - рабочий текст
    :return: None. Функция меняет изначальный текст.
    """
    temp = parsing(text)
    for e in temp:
        try:
            res = expr_eval(e[0])
        except ZeroDivisionError:
            pass
        except IndexError:
            pass
        except ValueError:
            pass
        else:
            l, r = e[1], e[2]
            if l[0] == r[0]:
                i = l[0]
                lj = l[1]
                rj = r[1]
                text[i] = text[i][:lj] + " " + str(res) + " " * (rj - lj - 1 - len(str(res))) + text[i][rj:]
            else:
                li = l[0]
                lj = l[1]
                ri = r[0]
                rj = r[1]
                text[li] = text[li][:lj + 1] + str(res)
                text[ri] = " " * rj + text[ri][rj:]
                if ri - li > 1:
                    for i in range(l[0] + 1, r[0]):
                        text[i] = text[i + 1]
                    for i in range(r[0], len(text) - 1):
                        text[i] = text[i + 1]
                    text = text[:-1]


if __name__ == "__main__":
    while True:
        try:
            a = input()
            result = expr_eval(a)
            print(result)
        except IndexError:
            print("Ошибка!")
