arr = [1, 3, 5, 2, 2]
arr = [8, 8, 3, 7, 8, 2, 7, 2]
l_sum = [0 for _ in range(len(arr) + 1)]
r_sum = [0 for _ in range(len(arr) + 1)]
ls , rs = 0,0

for i, l in enumerate(arr):
    ls += l
    l_sum[i + 1] = ls
l_sum.remove(l_sum[-1])
print(l_sum)

for i, r in enumerate(arr[::-1]):
    rs += r

    r_sum[len(arr) - i- 1] = rs
r_sum.remove(r_sum[0])
print(r_sum)

a = list(zip(l_sum, r_sum))
for index, vals in enumerate(a):
    i, j = vals
    if i == j:
        print(index+ 1)
        break
A = [1, 3, 5, 2, 2]
# A = [8 ,8 ,3, 7, 8, 2 ,7 ,2]
l = []
r = []
prev = 0
for el in A:
    l.append(prev)
    prev += el
prev = 0
for i in range(len(A) - 1, -1, -1):
    r.append(prev)
    prev += A[i]
r = r[::-1]
a = list(zip(l, r))
for ind, val in enumerate(a):
    i, j = val
    if i == j:
        print(ind+1)
        break
