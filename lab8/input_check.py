def int_check(s: str) -> bool:
    if s == '-':
        return False
    for i in range(len(s)):
        if '0' <= s[i] <= '9' or s[i] == '-' and i == 0:
            continue
        return False
    return True


def int_check(s: str) -> bool:
    for i in range(len(s)):
        if s[i] == '-' and i != 0:
            return False
        if '0' <= s[i] <= '9' or s[i] == '-' and i == 0:
            continue
        return False
    return True


def float_check(s: str) -> bool:
    # Проверка введённых данных
    al = "0123456789+-eE."
    dot_count = 0
    e_count = 0
    for i in range(len(s)):
        if s[i] == ".":
            dot_count += 1
            if e_count > 0:
                return False
        if dot_count > 1:
            return False
        if s[i] in "eE":
            e_count += 1
            if i == 0 or i == len(s) - 1 or e_count > 1:
                return False
        if s[i] not in al:
            return False
        if s[i] in "+-" and (i > 0 and s[i - 1] != "e" or i == len(s) - 1):
            return False
    return True


if __name__ == '__main__':
    while p := input():
        if float_check(p):
            print(float(p))
        else:
            print(False)
