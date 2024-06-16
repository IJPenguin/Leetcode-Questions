A = [10, 4, 2, 4, 1]
m = A[-1]
res = []
for i in range(len(A)-1, -1, -1):
    if A[i] >= m:
        m = A[i]
        res.append(m)
print(list(reversed(res)))
