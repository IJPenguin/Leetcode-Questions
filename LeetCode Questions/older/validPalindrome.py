# s = "race a car"
# s = "A man, a plan, a canal: Panama"
# s = "0P"
s = "a"
r = ""

for c in s:
    if ord(c) <= 122 and ord(c) >= 97:
        r += c
        continue
    elif ord(c) <= 90 and ord(c) >= 65:
        c = chr(ord(c) + 32)
        r += c
        continue
    elif ord(c) <= 57 and ord(c) >= 48:
        r += c
        continue
    else:
        continue

left = 0
right = len(r) - 1

while left <= right:
    if r[left] != r[right]:
        print(False)
        exit()
    left += 1
    right -= 1

print(True)
