# arr = [4, 3, 7, 8, 6, 2, 1]
arr = [1, 4, 3, 2]
# output = [3, 7, 4, 8, 2, 6, 1]
n = len(arr)

for i in range(n - 1):
    if i % 2 == 0:
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    else:
        if arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
