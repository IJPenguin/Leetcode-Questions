arr = [1, 1, 2, 3, 4, 4, 5, 2]
arr = [1, 2, -1, 1, 3, 1]


def findRepeating(arr):

    hash = {}
    for i in range(len(arr)):
        if arr[i] in hash:
            hash[arr[i]] += 1
        else:
            hash[arr[i]] = 1

    return [x for x in hash.keys() if hash[x] >= 2]


def findNonRepeating(arr):

    hash = {}
    for i in range(len(arr)):
        if arr[i] in hash:
            hash[arr[i]] += 1
        else:
            hash[arr[i]] = 1

    return [x for x in hash.keys() if hash[x] == 1]

    ...


print(findRepeating(arr))
print(findNonRepeating(arr))
