# from collections import defaultdict, Counter, deque

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
#res = [2,2,2,1,4,3,3,9,6,7,19]
arr2 = [2,1,4,3,9,6]

# res = []
# for val in arr2:
#     for j in range(arr1.count(val)):
#         res.append(val)

# for el in sorted(set(arr1)):
#     if el not in res:
#         for j in range(arr1.count(el)):
#             res.append(el)

# print(res) 

hash_map = {}
for i in range(len(arr2)):
    hash_map[arr2[i]] = i


for i in range (len(arr1)):
    if arr1[i] not in hash_map:
        hash_map[arr1[i]] = 1000 + arr1[i]
# print(hash_map)
arr1.sort(key = lambda x: hash_map[x])
print(arr1)