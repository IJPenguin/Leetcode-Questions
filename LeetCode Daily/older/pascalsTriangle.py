n = 5
k = 1
res = [[] for _ in range(n)]

for i in range(n):
    for j in range(i+1):
        if j == 0 or j == i:
            res[i].append(1)
        else:
            res[i].append(res[i-1][j-1] + res[i-1][j])
print(res)
