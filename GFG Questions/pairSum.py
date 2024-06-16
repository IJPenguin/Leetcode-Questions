# A = [1, 2, 4, 5, 7]
A = [-1, -2, 4, -6, 5, 7]
# B = [5, 6, 3, 4, 8]
B = [6, 3, 4, 0]
# X = 9
X = 8
res = []
A.sort()
for el in A:
    a = X - el
    if a in B:
        res.append([el, a])
print(res)
