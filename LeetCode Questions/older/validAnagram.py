s = "anagram"
t = "nagaram"

if set(s) != set(t):
    print(False)

for c in s:
    if c in t:
        t = t.replace(c, '', 1)
        print(t)
    else:
        print(False)

if not t:
    print(True)
else:
    print(False)