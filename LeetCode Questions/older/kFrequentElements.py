nums = [1, 1, 1, 2, 2, 3]
k = 2
n = []

for num in set(nums):
    n.append([num, nums.count(num)])

n.sort(key=lambda x: x[1], reverse=True)
res = [k for k, v in n[:k]]
print(res)
