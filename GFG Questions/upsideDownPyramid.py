rows = 11
pad = 0

for i in range(rows, -1, -2):
    print(f"{" " * pad}{"*" * i}{" " * pad}")
    pad += 1
