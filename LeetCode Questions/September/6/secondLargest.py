def secondLargest(arr):
    if len(arr) < 2:
        return -1
    m1 = arr[0]
    m2 = arr[1]

    for i in range(2, len(arr)):
        if arr[i] > m1:
            m2, m1 = m1, arr[i]
        elif arr[i] == m1:
            m2 = arr[i]
    return m2


arr = [1, 2, 3, 4, 5, 6, 7, 8, 8]
print(secondLargest(arr))
