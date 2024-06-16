# a = [3, 1, 1]
a = [6, 1, 9, 5, 4]
# b = [6, 5, 4]
b = [3, 4, 8, 2, 4]
a.sort()
b.sort()
b = list(reversed(b))
res = 0
for i in range(len(a)):
    res += a[i] * b[i]
print(res)
