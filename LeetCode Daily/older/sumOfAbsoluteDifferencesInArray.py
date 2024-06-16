nums = [2, 3,5]

memo = {}
res = []

for i in nums:
    temp = 0
    for j in nums:
        if (i, j) in memo.values():
            temp += memo[(i, j)]
        else:
            tmp = abs(i - j)
            memo[(i, j)] = tmp
            temp += tmp
    res.append(temp)
    
print(res)