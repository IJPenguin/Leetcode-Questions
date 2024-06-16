from itertools import groupby
nums = [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]


def diagonalTraverse(nums):
    arr = []
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            tup = (i + j, i, nums[i][j])
            arr.append(tup)
    res = []
    arr = sorted(arr, key=lambda x: x[0])

    arr = [list(group) for key, group in groupby(arr, key=lambda x: x[0])]
    for i, a in enumerate(arr):
        a = sorted(a, key=lambda x: x[1], reverse=True)
        arr[i] = a
    for a in arr:
        for j in a:
            res.append(j[2])
    return res


print(diagonalTraverse(nums))
