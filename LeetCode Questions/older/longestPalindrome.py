s = "ccc"


count = {}
for c in set(s):
    count[c] = s.count(c)
length = 0
a = 0
for item in count.values():
    if item % 2 == 0:
        length += item
    elif item % 2 == 1 and a == 0:
        length += 1
        a += 1
    
print(length)