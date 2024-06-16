s = "aba*"
s = [*s]
# s = "abca*"
big = []

for i, char in enumerate(s):
    if char == "*":
        big.sort(key=lambda x: x[1])
        s.pop(big[-1][0])
        big.pop()
    else:
        big.append([i, ord(char)])

s = ''.join(s)
print(s)
