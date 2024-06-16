arr = [
    6,
    19,
    23,
    3,
    8,
    6,
    23,
    2,
    23,
    1,
    15,
    19,
    22,
    21,
    0,
    19,
    28,
    23,
    25,
    18,
    12,
    27,
    16,
    18,
    20,
    2,
    3,
    27,
    29,
    14,
]
print(len(arr))

res = 0
l = r = 0
while r < len(arr) - 1:
    old = r
    farthest = 0
    for i in range(l, r + 1):
        farthest = max(farthest, i + arr[i])
    l = r + 1
    r = farthest
    
    if r == old:
        print("-1")
        break
    res += 1

print(res)
