from menu import menu, cmd


text = []
with open("text.txt", "r") as f:
    while t := f.readline():
        text.append(t.strip())

c = menu()
p = cmd(text, c)
while p is None:
    c = menu()
    p = cmd(text, c)
