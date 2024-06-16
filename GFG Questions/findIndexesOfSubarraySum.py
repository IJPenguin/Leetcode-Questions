# arr = [1,2,3,7,5]
# s = 12
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# s = 15
arr = [1, 1]
s = 0
n = len(arr)
if s == 0 and 0 in arr:
            i = arr.index(0)
            print([i + 1, i + 1])
elif s == 0:
    print(-1)
    exit()

l = 0
r = 0
res = arr[l]
add = False

while r < n:
    if add:
        res += arr[l]
        add = False
    else:
        r += 1
        res += arr[r]

    if r > s:
        res -= arr[l]
        l += 1
        add = True

    if res == s:
        print([l+ 1, r+1])
        break

# for i in range(n):
#     t = s
#     b = False
#     for j in range(i, n):
#         t -= arr[j]
#         if t == 0:
#             res = [i + 1, j + 1]
#             b = True
#             break
#     if b:
#         break

# print(res)
