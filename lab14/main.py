from menu import cmd
from initialization import file_choose

filename = file_choose()
init = False
c = cmd(filename, init)
while c != 0:
    if type(c) is not int:
        filename = c
        init = False
    elif c == 2:
        init = True
    c = cmd(filename, init)
