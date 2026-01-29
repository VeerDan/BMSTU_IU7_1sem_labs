from align import left_align, right_align, justify
from words import delete_word, replace_word
from calc import expr_replace
from search import print_sentence


def word_input():
    input_valid = False
    word = ""
    while not input_valid:
        try:
            word = input("Введите слово для обработки: ")
            if len(word.split()) != 1:
                raise ValueError
            for i in word:
                if not i.isalpha():
                    raise TypeError
            input_valid = True
        except ValueError:
            print("Введите только одно слово без суфиксных и префиксных пробелов! Повторите ввод!")
        except TypeError:
            print("Введите слово!")
    return word


def cmd_input():
    input_valid = False
    c = -1
    while not input_valid:
        try:
            c = int(input("Введите номер команды для работы с текстом: "))
            if c not in range(8):
                raise ValueError
            input_valid = True
        except ValueError:
            print("Введена недопустимая команда! Повторите ввод!")
    return c


def text_output(text):
    print("\n\033[30;43mТекущее состояние текста:\033[0m")
    for i in text:
        print(f"\033[32m{i}\033[0m")


def menu():
    print("\n\033[46;30mКоманды для работы с текстом:\033[0m\n"
          "\033[46;30m0. Завершение работы программы\033[0m\n"
          "\033[46;30m1. Выровнять текст по левому краю.\033[0m\n"
          "\033[46;30m2. Выровнять текст по правому краю.\033[0m\n"
          "\033[46;30m3. Выровнять текст по ширине.\033[0m\n"
          "\033[46;30m4. Удаление всех вхождений заданного слова.\033[0m\n"
          "\033[46;30m5. Замена одного слова другим во всём тексте.\033[0m\n"
          "\033[46;30m6. Вычисление арифметических выражений над целыми числами внутри текста.\033[0m\n"
          "\033[46;30m7. Найти и затем удалить предложение с самым коротким словом.\033[0m\n")
    c = cmd_input()
    word = ""
    word_replace = ""
    if c == 4:
        print("Ввод слова для удаления:")
        word = word_input()
    elif c == 5:
        print("Ввод слова, которое требуется заменить:")
        word = word_input()
        word_replace = input("Ввод слова, на которое будет изменено данное: ")
    return c, word, word_replace


def cmd(text, command):
    match command[0]:
        case 0:
            return 0
        case 1:
            left_align(text)
        case 2:
            right_align(text)
        case 3:
            justify(text)
        case 4:
            delete_word(text, command[1])
        case 5:
            replace_word(text, command[1], command[2])
        case 6:
            try:
                expr_replace(text)
            except IndexError:
                print("Текст пустой!")
        case 7:
            print("\n\033[30;43mПредложение с самым коротким словом:\033[0m")
            print_sentence(text, "\033[32m")
    text_output(text)
