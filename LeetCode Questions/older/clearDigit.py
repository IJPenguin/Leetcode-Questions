s = "gbysb5"
temp = [*s]
a = []

for c in s:
    if not c.isdigit():
        a.append(c)
    elif c.isdigit():
        temp.remove(c)
        a.pop()

print(''.join(a))