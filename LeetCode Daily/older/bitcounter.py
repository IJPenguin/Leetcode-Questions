n = 5
ans = []
for i in range(n+1):
    x = bin(i)
    m = x.count('1')
    ans.append(m)

print(ans)