nums = [10, 9, 2, 5, 3, 7, 101, 18]
n = len(nums)
arr = [0 for _ in range(n)]

for i in range(n):
    arr[i] = 1
    for j in range(i):
        if nums[i] > nums[j]:
            arr[i] = max(arr[i], arr[j] + 1)
