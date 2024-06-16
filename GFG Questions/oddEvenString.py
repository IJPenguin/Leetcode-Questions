from collections import Counter
s = "fj"
c = Counter(s)
cache = []
x = 0
y = 0
for i, el in enumerate(s):
    if el not in cache:
        cache.append(el)
        if (ord(el)%2 == 1) and c[el]%2 == 1:
            y += 1
        elif (ord(el)%2 == 0) and c[el]% 2== 0:
            x += 1

if (x + y) % 2 == 0:
    print("EVEN")
else:
    print("ODD")
